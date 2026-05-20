#!/usr/bin/env bash
# ABP_TELEMETRY_SENTINEL_v1
#
# Shared event-fire snippet for the ABP buyer-signal analytics taxonomy.
# Canonical copy: ~/github/claude-skills/ai-build-partner/scripts/abp-fire-event.sh
# Duplicated (per separation contract) into each paid skill's scripts/ dir.
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
# Properties NEVER sent: prompt text, file paths, message bodies, project names.

POSTHOG_HOST="https://us.i.posthog.com"
POSTHOG_KEY="phc_yB4suFF9SdZY6vZiGhrtXWYbearmxGRFUzoyKtCg9AAQ"
ABP_DIR="$HOME/.ai-build-partner"

abp_fire_event() {
  local event_name="$1"
  local extra_props="${2:-}"

  # Opt-out check: silent no-op if no install_id
  [[ -s "$ABP_DIR/install_id" ]] || return 0
  command -v curl >/dev/null 2>&1 || return 0

  local install_id email version surface session_id synthetic distinct_id session_file
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

  # Session id — persisted per shell process; new shell = new session
  session_file="/tmp/abp-session-$$"
  if [[ -s "$session_file" ]]; then
    session_id="$(cat "$session_file")"
  else
    session_id="$(uuidgen 2>/dev/null || cat /proc/sys/kernel/random/uuid 2>/dev/null || \
                  date +%s%N)-$$"
    printf '%s\n' "$session_id" > "$session_file"
  fi

  distinct_id="${email:-$install_id}"

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

# If invoked directly (not sourced), dispatch
if [[ "${BASH_SOURCE[0]:-$0}" == "${0}" ]]; then
  abp_fire_event "$@"
fi
