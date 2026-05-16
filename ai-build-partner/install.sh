#!/usr/bin/env bash
# AI Build Partner — installer with optional install telemetry.
#
# Run from inside the cloned/unzipped ai-build-partner directory:
#   ./install.sh
#   ./install.sh --email=you@example.com
#   ./install.sh --no-telemetry
#
# What gets installed:
#   - Skill files copied to ~/.claude/skills/ai-build-partner/
#   - Local registration written to ~/.ai-build-partner/
#
# What gets sent (unless --no-telemetry):
#   Event:  ai_build_partner_installed
#   To:     PostHog (theshipitsystem project, 426369), US region
#   Data:   install_id (UUID), email (lowercased), version, OS, utm_source, utm_campaign
#   Why:    so Molly can see which ads/channels drive installs, and measure how
#           many installs actually get used (no per-keystroke tracking — just
#           install + invocation events).

set -euo pipefail

VERSION="2.2.0"
POSTHOG_HOST="https://us.i.posthog.com"
POSTHOG_KEY="phc_yB4suFF9SdZY6vZiGhrtXWYbearmxGRFUzoyKtCg9AAQ"
SKILL_NAME="ai-build-partner"

EMAIL=""
INSTALL_ID=""
TELEMETRY="ask"
UTM_SOURCE="${UTM_SOURCE:-direct}"
UTM_CAMPAIGN="${UTM_CAMPAIGN:-}"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --email=*) EMAIL="${1#*=}"; shift ;;
    --email) EMAIL="${2:-}"; shift 2 ;;
    --install-id=*) INSTALL_ID="${1#*=}"; shift ;;
    --install-id) INSTALL_ID="${2:-}"; shift 2 ;;
    --no-telemetry) TELEMETRY="no"; shift ;;
    --yes-telemetry) TELEMETRY="yes"; shift ;;
    --utm-source=*) UTM_SOURCE="${1#*=}"; shift ;;
    --utm-campaign=*) UTM_CAMPAIGN="${1#*=}"; shift ;;
    -h|--help)
      grep -E '^# ' "$0" | sed 's/^# //'
      exit 0
      ;;
    *) printf 'Unknown option: %s\n' "$1" >&2; exit 1 ;;
  esac
done

printf '\n  AI Build Partner v%s\n  by Unstuck with Molly\n\n' "$VERSION"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"
if [[ ! -f "$SCRIPT_DIR/SKILL.md" ]]; then
  printf 'error: SKILL.md not found in %s\n' "$SCRIPT_DIR" >&2
  printf 'Run this script from inside the ai-build-partner directory.\n' >&2
  exit 1
fi

if [[ "$TELEMETRY" == "ask" ]]; then
  cat <<EOF
Quick consent check before install:

  Send a one-time install event to PostHog so Molly can see how ads → installs
  perform? You'll get the skill either way.

  What gets sent: install_id (random UUID), your email, version, OS, UTM tags.
  Where: PostHog (us.i.posthog.com), Molly's account only.
  Frequency: once at install + once per Claude session when you USE the skill
             (the per-session ping asks for Bash permission separately, you can
             deny it any time).

  [y] yes, send install event
  [n] no, install without telemetry

EOF
  printf 'Your choice [y/n]: '
  read -r telemetry_choice
  case "$telemetry_choice" in
    y|Y|yes|YES) TELEMETRY="yes" ;;
    *) TELEMETRY="no" ;;
  esac
fi

if [[ "$TELEMETRY" == "yes" && -z "$EMAIL" ]]; then
  printf '\nYour email (links install to ad attribution; press enter to skip): '
  read -r EMAIL
fi

if [[ -z "$INSTALL_ID" ]]; then
  if command -v uuidgen >/dev/null 2>&1; then
    INSTALL_ID="$(uuidgen | tr '[:upper:]' '[:lower:]')"
  else
    INSTALL_ID="abp-$(date +%s)-${RANDOM}${RANDOM}"
  fi
fi

EMAIL_LC="$(printf '%s' "$EMAIL" | tr '[:upper:]' '[:lower:]')"
LOCAL_DIR="$HOME/.ai-build-partner"
mkdir -p "$LOCAL_DIR"
printf '%s\n' "$INSTALL_ID" > "$LOCAL_DIR/install_id"
printf '%s\n' "$EMAIL_LC" > "$LOCAL_DIR/email"
printf '%s\n' "$VERSION" > "$LOCAL_DIR/version"
printf '%s\n' "$TELEMETRY" > "$LOCAL_DIR/telemetry"

SKILL_DEST="$HOME/.claude/skills/$SKILL_NAME"
mkdir -p "$SKILL_DEST"
rm -rf "$SKILL_DEST"/* 2>/dev/null || true
cp -R "$SCRIPT_DIR/." "$SKILL_DEST/"
rm -f "$SKILL_DEST/install.sh"

printf '\n  installed to %s\n' "$SKILL_DEST"
printf '  install_id  %s\n' "$INSTALL_ID"
printf '  telemetry   %s\n' "$TELEMETRY"

if [[ "$TELEMETRY" == "yes" ]] && command -v curl >/dev/null 2>&1; then
  OS_NAME="$(uname -s)"
  ARCH="$(uname -m)"
  TIMESTAMP="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  DISTINCT_ID="${EMAIL_LC:-$INSTALL_ID}"

  INSTALL_PAYLOAD=$(cat <<JSON
{
  "api_key": "$POSTHOG_KEY",
  "event": "ai_build_partner_installed",
  "distinct_id": "$DISTINCT_ID",
  "properties": {
    "install_id": "$INSTALL_ID",
    "email": "$EMAIL_LC",
    "version": "$VERSION",
    "os": "$OS_NAME",
    "arch": "$ARCH",
    "utm_source": "$UTM_SOURCE",
    "utm_campaign": "$UTM_CAMPAIGN",
    "\$set": {
      "email": "$EMAIL_LC",
      "ai_build_partner_version": "$VERSION",
      "ai_build_partner_installed_at": "$TIMESTAMP"
    },
    "\$set_once": {
      "ai_build_partner_first_seen_at": "$TIMESTAMP",
      "ai_build_partner_first_utm_source": "$UTM_SOURCE",
      "ai_build_partner_first_utm_campaign": "$UTM_CAMPAIGN"
    }
  },
  "timestamp": "$TIMESTAMP"
}
JSON
)

  if curl -fsS -m 5 -X POST "$POSTHOG_HOST/i/v0/e/" \
       -H "Content-Type: application/json" \
       -d "$INSTALL_PAYLOAD" >/dev/null 2>&1; then
    printf '  install ping sent\n'
  else
    printf '  install ping failed (offline?) — skill still works\n'
  fi

  if [[ -n "$EMAIL_LC" ]]; then
    IDENTIFY_PAYLOAD=$(cat <<JSON
{
  "api_key": "$POSTHOG_KEY",
  "event": "\$identify",
  "distinct_id": "$EMAIL_LC",
  "properties": {
    "\$anon_distinct_id": "$INSTALL_ID",
    "\$set": {
      "email": "$EMAIL_LC"
    }
  },
  "timestamp": "$TIMESTAMP"
}
JSON
)
    curl -fsS -m 5 -X POST "$POSTHOG_HOST/i/v0/e/" \
      -H "Content-Type: application/json" \
      -d "$IDENTIFY_PAYLOAD" >/dev/null 2>&1 || true
  fi
fi

cat <<NEXT

Next:
  1. Open Claude Code (or claude.ai with a Project + SKILL.md uploaded).
  2. Say: "Use the ai-build-partner skill" — or just describe what you're stuck on.
  3. Answer the in-character check, then pick a module.

5-minute first session: try /unstuck diagnose with one paragraph about your project.

To opt out of session telemetry later: rm $LOCAL_DIR/install_id
NEXT
