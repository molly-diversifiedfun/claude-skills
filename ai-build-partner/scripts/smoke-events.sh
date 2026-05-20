#!/usr/bin/env bash
# ABP buyer-signal v1 smoke test
#
# Fires each of the 8 v1 events with a synthetic install (@unstuckwithmolly.com).
# All events get synthetic=true so they're filtered from prod dashboards.
#
# Run:
#   bash scripts/smoke-events.sh
#
# Expected: 8 events visible in PostHog 426369 within 5-10 min (Cloud query lag).
#
# HogQL verification query (run ≥10 min after smoke):
#
#   SELECT event, properties.surface, properties.synthetic, count()
#   FROM events
#   WHERE event IN ('ai_build_partner_installed','build_partner_invoked',
#                   'session_started','project_first_response','command_fired',
#                   'command_completed','save_block_fired','session_resumed')
#     AND properties.synthetic = true
#     AND timestamp > now() - INTERVAL 1 HOUR
#   GROUP BY event, properties.surface, properties.synthetic
#   ORDER BY event
#
# Expected: 8 rows, each count >= 1, all synthetic = true.
#
# Cleanup: this script DOES NOT touch ~/.ai-build-partner/install_id permanently —
# it backs it up to /tmp/install_id.bak.$$ and restores on exit.
#
# Design note: `set -uo pipefail` (no `-e`) is intentional. The helper itself
# never returns non-zero (every read is guarded, every external call is silenced).
# Smoke should never abort mid-test because a single curl timed out; we want to
# fire all 8 events and surface any failures via the PostHog verification query.

set -uo pipefail

ABP_DIR="$HOME/.ai-build-partner"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HELPER="$SCRIPT_DIR/abp-fire-event.sh"

if [[ ! -x "$HELPER" ]]; then
  echo "FAIL: helper not found at $HELPER"
  exit 1
fi

# Back up real install state if present
mkdir -p "$ABP_DIR"
BACKUP_DIR="/tmp/abp-smoke-backup-$$"
mkdir -p "$BACKUP_DIR"
for f in install_id email version last_session_at current_session_id current_session_at; do
  [[ -f "$ABP_DIR/$f" ]] && cp "$ABP_DIR/$f" "$BACKUP_DIR/$f"
done
# Save-marks dir
[[ -d "$ABP_DIR/save-marks" ]] && cp -R "$ABP_DIR/save-marks" "$BACKUP_DIR/save-marks"

# Restore on exit
trap '
  for f in install_id email version last_session_at current_session_id current_session_at; do
    if [[ -f "$BACKUP_DIR/$f" ]]; then
      cp "$BACKUP_DIR/$f" "$ABP_DIR/$f"
    else
      rm -f "$ABP_DIR/$f"
    fi
  done
  if [[ -d "$BACKUP_DIR/save-marks" ]]; then
    rm -rf "$ABP_DIR/save-marks"
    cp -R "$BACKUP_DIR/save-marks" "$ABP_DIR/save-marks"
  else
    rm -rf "$ABP_DIR/save-marks"
  fi
  rm -rf "$BACKUP_DIR"
  echo "Restored install state."
' EXIT

# Set up synthetic install
SYNTHETIC_INSTALL_ID="smoke-$(uuidgen 2>/dev/null || date +%s%N)"
printf '%s\n' "$SYNTHETIC_INSTALL_ID" > "$ABP_DIR/install_id"
printf 'smoke@unstuckwithmolly.com\n' > "$ABP_DIR/email"
printf '1.0.0-smoke\n' > "$ABP_DIR/version"
# Start each smoke run with a fresh session_id (clear TTL state + save-marks)
rm -f "$ABP_DIR/current_session_id" "$ABP_DIR/current_session_at"
rm -rf "$ABP_DIR/save-marks"

# Pre-seed last_session_at to ≥1 day old BEFORE firing session_started, so the
# precheck (which mirrors SKILL.md ordering) sees a real gap. session_started
# will overwrite it to NOW; that's the bug Stage 6.1 fixed (Critical #3).
date -u -v-2d +"%Y-%m-%dT%H:%M:%SZ" > "$ABP_DIR/last_session_at" 2>/dev/null || \
  date -u -d "2 days ago" +"%Y-%m-%dT%H:%M:%SZ" > "$ABP_DIR/last_session_at" 2>/dev/null || \
  date -u +"%Y-%m-%dT%H:%M:%SZ" > "$ABP_DIR/last_session_at"

echo "=== ABP v1 smoke test ==="
echo "install_id: $SYNTHETIC_INSTALL_ID"
echo "email:      smoke@unstuckwithmolly.com (synthetic=true expected)"
echo

fire() {
  local name="$1"
  local props="$2"
  local surface="${3:-claude-skill}"
  echo "FIRE  $name  (surface=$surface)"
  SURFACE="$surface" bash "$HELPER" "$name" "$props"
  sleep 0.2
}

# Order mirrors spec §3 funnel walk:
# install → invoked → session_started → session_resumed → project_first → cmd_fired → cmd_completed → save_block

# 1. ai_build_partner_installed (paid:kit variant — free already fired by install.sh)
fire ai_build_partner_installed '"os":"Darwin","arch":"arm64"' paid:kit

# 2. build_partner_invoked
fire build_partner_invoked '' claude-skill

# 3-4. Compute DAYS BEFORE session_started (Critical #3 fix).
#      Sourcing the helper does NOT fire an event (High #1 fix).
DAYS_SINCE_LAST=$(source "$HELPER" && abp_days_since_last)
echo "      days_since_last computed BEFORE session_started: $DAYS_SINCE_LAST"
ENTRY_CTX=$([ "$DAYS_SINCE_LAST" -ge 1 ] && echo "resumed" || echo "fresh")
fire session_started "\"entry_context\":\"$ENTRY_CTX\"" claude-skill

# 4. session_resumed — only if DAYS >= 1
if [ "$DAYS_SINCE_LAST" -ge 1 ]; then
  fire session_resumed "\"days_since_last\":$DAYS_SINCE_LAST" claude-skill
else
  echo "SKIP  session_resumed (days_since_last=0)"
fi

# 5. project_first_response
fire project_first_response '"outcome":"accepted","turn_index":2' claude-skill

# 6. command_fired
fire command_fired '"command":"scope"' claude-skill

# 7. command_completed
fire command_completed '"command":"scope","artifact_kind":"scope"' claude-skill

# 8. save_block_fired (deduped via ~/.ai-build-partner/save-marks/<cmd>)
fire save_block_fired '"command":"scope"' claude-skill

# Wait for background curls to flush
echo
echo "Waiting 3s for background curls to drain..."
wait 2>/dev/null
sleep 3

echo
echo "=== Smoke complete. 8 events fired with synthetic=true. ==="
echo
echo "Verify in PostHog 426369 (wait 5-10 min for Cloud query lag):"
echo
echo "  SELECT event, properties.surface, count() FROM events"
echo "  WHERE event IN ('ai_build_partner_installed','build_partner_invoked',"
echo "                  'session_started','session_resumed','project_first_response',"
echo "                  'command_fired','command_completed','save_block_fired')"
echo "    AND properties.synthetic = true"
echo "    AND properties.install_id = '$SYNTHETIC_INSTALL_ID'"
echo "  GROUP BY event, properties.surface"
echo
echo "Expected: 8 rows. All synthetic=true. surface column shows claude-skill or paid:kit."
