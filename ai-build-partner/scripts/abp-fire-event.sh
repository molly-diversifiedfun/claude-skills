#!/usr/bin/env bash
# ABP_TELEMETRY_SENTINEL_v1
#
# Shared event-fire snippet for the ABP buyer-signal analytics taxonomy.
# Canonical copy: ~/github/claude-skills/ai-build-partner/scripts/abp-fire-event.sh
# Duplicated (per separation contract) into each paid skill's scripts/ dir.
# All 4 copies MUST be byte-identical — drift is enforced by check-event-drift.sh.
#
# Usage (sourced or invoked):
#   SURFACE=claude-skill abp_fire_event <event_name> [json_props]
#
# Example:
#   SURFACE=claude-skill abp_fire_event session_started '"entry_context":"fresh","turn_index":1'
#
# All events:
#   - silent no-op if ~/.ai-build-partner/install_id missing (opt-out)
#   - background curl, errors suppressed
#   - $? always 0 (never blocks calling skill)
#
# Properties sent automatically:
#   install_id, session_id, surface, synthetic, version
#
# Properties NEVER sent: prompt text, file paths, message bodies, project names,
#   email address (used locally only for synthetic-traffic derivation, spec §5).
#
# Design note (DO NOT "FIX"): this script intentionally does NOT use
#   `set -euo pipefail`. Every read is guarded with `[[ -s ... ]] || return 0`,
#   every external call has `2>/dev/null`, and the function always returns 0.
#   Adding `set -e` would propagate transient failures (offline curl, missing
#   uuidgen on minimal containers, locale issues) up into the model's Bash
#   output and break the calling skill. Failure must be silent.

POSTHOG_HOST="https://us.i.posthog.com"
POSTHOG_KEY="phc_yB4suFF9SdZY6vZiGhrtXWYbearmxGRFUzoyKtCg9AAQ"
ABP_DIR="$HOME/.ai-build-partner"
SESSION_TTL_SECS=1800  # 30 min idle → new session_id

abp_fire_event() {
  local event_name="$1"
  local extra_props="${2:-}"

  # Opt-out check: silent no-op if no install_id
  [[ -s "$ABP_DIR/install_id" ]] || return 0
  command -v curl >/dev/null 2>&1 || return 0

  local install_id email version surface session_id synthetic distinct_id
  local session_id_file session_at_file last_at now_ts age
  install_id="$(cat "$ABP_DIR/install_id" 2>/dev/null)"
  email="$(cat "$ABP_DIR/email" 2>/dev/null || echo "")"
  version="$(cat "$ABP_DIR/version" 2>/dev/null || echo "unknown")"
  surface="${SURFACE:-claude-skill}"

  # Synthetic = internal Anthropic or Unstuck traffic
  if printf '%s' "$email" | tr '[:upper:]' '[:lower:]' \
       | grep -qE '@(anthropic\.com|unstuckwithmolly\.com)$'; then
    synthetic="true"
  else
    synthetic="false"
  fi

  # Session id — persisted in ~/.ai-build-partner/current_session_id with a
  # sliding TTL stamp. Claude.ai spawns a fresh `bash -c` per tool call so
  # `/tmp/$$` collapses funnels (every event gets a new session_id). The
  # file-based approach survives across Bash invocations within the same
  # conversation; TTL expires it after 30 min idle so unrelated sessions
  # later in the day don't get stitched together.
  mkdir -p "$ABP_DIR" 2>/dev/null
  session_id_file="$ABP_DIR/current_session_id"
  session_at_file="$ABP_DIR/current_session_at"
  now_ts="$(date -u +%s 2>/dev/null || echo 0)"
  last_at="$(cat "$session_at_file" 2>/dev/null || echo 0)"
  [[ "$last_at" =~ ^[0-9]+$ ]] || last_at=0
  age=$(( now_ts - last_at ))
  if [[ -s "$session_id_file" && "$age" -lt "$SESSION_TTL_SECS" && "$age" -ge 0 ]]; then
    session_id="$(cat "$session_id_file" 2>/dev/null)"
  else
    session_id="$(uuidgen 2>/dev/null || cat /proc/sys/kernel/random/uuid 2>/dev/null || \
                  echo "abp-$(date +%s 2>/dev/null)-$RANDOM$RANDOM")"
    printf '%s\n' "$session_id" > "$session_id_file" 2>/dev/null || true
  fi
  # Sliding TTL: every fire bumps the stamp forward
  printf '%s\n' "$now_ts" > "$session_at_file" 2>/dev/null || true

  # distinct_id is ALWAYS install_id — email never leaves the machine (spec §5).
  distinct_id="$install_id"

  # Side-effect: bump last_session_at on session_started so session_resumed can compute
  if [[ "$event_name" == "session_started" ]]; then
    date -u +"%Y-%m-%dT%H:%M:%SZ" > "$ABP_DIR/last_session_at" 2>/dev/null || true
  fi

  local props
  props="\"install_id\":\"$install_id\",\"session_id\":\"$session_id\",\"surface\":\"$surface\",\"synthetic\":$synthetic,\"version\":\"$version\""
  [[ -n "$extra_props" ]] && props="$props,$extra_props"

  # Fire-and-forget. Background, errors silenced.
  ( curl -fsS -m 5 -X POST "$POSTHOG_HOST/i/v0/e/" \
      -H "Content-Type: application/json" \
      -d "{\"api_key\":\"$POSTHOG_KEY\",\"event\":\"$event_name\",\"distinct_id\":\"$distinct_id\",\"properties\":{$props}}" \
      >/dev/null 2>&1 ) &

  return 0
}

# Compute days since last session — used by session_resumed
abp_days_since_last() {
  local last_file="$ABP_DIR/last_session_at"
  [[ -s "$last_file" ]] || { echo "0"; return 0; }
  local last_ts now_ts diff
  last_ts="$(date -u -j -f "%Y-%m-%dT%H:%M:%SZ" "$(cat "$last_file")" "+%s" 2>/dev/null || \
             date -u -d "$(cat "$last_file")" "+%s" 2>/dev/null || echo "0")"
  now_ts="$(date -u +%s)"
  [[ "$last_ts" == "0" ]] && { echo "0"; return 0; }
  diff=$(( (now_ts - last_ts) / 86400 ))
  echo "$diff"
}

# If invoked directly (not sourced), dispatch — but guard against an empty $1
# which would fire `event:""` (the bug fixed in Stage 6.1).
if [[ "${BASH_SOURCE[0]:-$0}" == "${0}" ]]; then
  [[ -z "${1:-}" ]] && exit 0
  abp_fire_event "$@"
fi
