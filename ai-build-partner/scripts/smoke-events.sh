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
for f in install_id email version last_session_at; do
  [[ -f "$ABP_DIR/$f" ]] && cp "$ABP_DIR/$f" "$BACKUP_DIR/$f"
done

# Restore on exit
trap '
  for f in install_id email version last_session_at; do
    if [[ -f "$BACKUP_DIR/$f" ]]; then
      cp "$BACKUP_DIR/$f" "$ABP_DIR/$f"
    else
      rm -f "$ABP_DIR/$f"
    fi
  done
  rm -rf "$BACKUP_DIR"
  rm -f /tmp/abp-session-$$
  rm -f /tmp/abp-save-$$-*
  echo "Restored install state."
' EXIT

# Set up synthetic install
SYNTHETIC_INSTALL_ID="smoke-$(uuidgen 2>/dev/null || date +%s%N)"
printf '%s\n' "$SYNTHETIC_INSTALL_ID" > "$ABP_DIR/install_id"
printf 'smoke@unstuckwithmolly.com\n' > "$ABP_DIR/email"
printf '1.0.0-smoke\n' > "$ABP_DIR/version"

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

# 1. ai_build_partner_installed (paid:kit variant — free already fired by install.sh)
fire ai_build_partner_installed '"os":"Darwin","arch":"arm64"' paid:kit

# 2. build_partner_invoked
fire build_partner_invoked '' claude-skill

# 3. session_started (also writes last_session_at)
fire session_started '"entry_context":"fresh"' claude-skill

# Force last_session_at to be ≥1 day old so session_resumed has data to report
date -u -v-2d +"%Y-%m-%dT%H:%M:%SZ" > "$ABP_DIR/last_session_at" 2>/dev/null || \
  date -u -d "2 days ago" +"%Y-%m-%dT%H:%M:%SZ" > "$ABP_DIR/last_session_at" 2>/dev/null || \
  date -u +"%Y-%m-%dT%H:%M:%SZ" > "$ABP_DIR/last_session_at"

# 8. session_resumed
DAYS_SINCE_LAST=$(source "$HELPER" && abp_days_since_last)
echo "      days_since_last computed: $DAYS_SINCE_LAST"
fire session_resumed "\"days_since_last\":$DAYS_SINCE_LAST" claude-skill

# 4. project_first_response
fire project_first_response '"outcome":"accepted","turn_index":2' claude-skill

# 5. command_fired
fire command_fired '"command":"scope"' claude-skill

# 6. command_completed
fire command_completed '"command":"scope","artifact_kind":"scope"' claude-skill

# 7. save_block_fired (deduped — second call should no-op, but we test the first)
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
