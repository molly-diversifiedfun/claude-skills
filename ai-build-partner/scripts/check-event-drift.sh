#!/usr/bin/env bash
# ABP buyer-signal v1 drift check
#
# Greps the ABP_TELEMETRY_SENTINEL_v1 marker across all 4 SKILL.md files
# (free ABP + 3 paid skills). Fails non-zero if any file is missing it.
#
# Stage 6.1 added: extract every fenced ```bash block from each SKILL.md and
# run `bash -n` on it. Catches the `& ; }` syntax class of bug that the review
# caught — the snippets are meant to be executed by the model in Claude.ai,
# so a parse error means the event never fires.
#
# Run:
#   bash scripts/check-event-drift.sh
#
# Exit codes:
#   0 = all 4 SKILL.md files have the sentinel + helper present + every
#       embedded ```bash snippet parses clean
#   1 = drift detected (missing sentinel, missing helper, or unparseable snippet)

set -uo pipefail

SENTINEL="ABP_TELEMETRY_SENTINEL_v1"

declare -a TARGETS=(
  "$HOME/github/claude-skills/ai-build-partner/SKILL.md"
  "$HOME/github/ship-it-system/skills/ship-it-kit-skill/SKILL.md"
  "$HOME/github/ship-it-system/skills/marketing-os-skill/SKILL.md"
  "$HOME/github/ship-it-system/skills/momentum-method-skill/SKILL.md"
)

declare -a HELPERS=(
  "$HOME/github/claude-skills/ai-build-partner/scripts/abp-fire-event.sh"
  "$HOME/github/ship-it-system/skills/ship-it-kit-skill/scripts/abp-fire-event.sh"
  "$HOME/github/ship-it-system/skills/marketing-os-skill/scripts/abp-fire-event.sh"
  "$HOME/github/ship-it-system/skills/momentum-method-skill/scripts/abp-fire-event.sh"
)

echo "=== ABP telemetry drift check ==="
echo "Sentinel: $SENTINEL"
echo

FAILED=0

echo "-- SKILL.md sentinel presence --"
for f in "${TARGETS[@]}"; do
  if [[ ! -f "$f" ]]; then
    printf "  MISSING FILE: %s\n" "$f"
    FAILED=1
    continue
  fi
  COUNT=$(grep -c "$SENTINEL" "$f" || true)
  if [[ "$COUNT" -lt 1 ]]; then
    printf "  FAIL: 0 hits in %s\n" "$f"
    FAILED=1
  else
    printf "  OK:   %d hit(s) in %s\n" "$COUNT" "$f"
  fi
done

echo
echo "-- abp-fire-event.sh helper presence --"
for h in "${HELPERS[@]}"; do
  if [[ -x "$h" ]]; then
    printf "  OK:   %s\n" "$h"
  elif [[ -f "$h" ]]; then
    printf "  WARN: %s exists but not executable\n" "$h"
  else
    printf "  FAIL: missing %s\n" "$h"
    FAILED=1
  fi
done

echo
echo "-- Helper sentinel presence --"
for h in "${HELPERS[@]}"; do
  [[ -f "$h" ]] || continue
  COUNT=$(grep -c "$SENTINEL" "$h" || true)
  if [[ "$COUNT" -lt 1 ]]; then
    printf "  FAIL: 0 hits in %s\n" "$h"
    FAILED=1
  else
    printf "  OK:   %d hit(s) in %s\n" "$COUNT" "$h"
  fi
done

echo
echo '-- Embedded fenced-bash snippet parse check (bash -n) --'
# Extract every fenced-bash block from each SKILL.md and pipe through bash -n.
# Snippets that reference $CMD/$DAYS/$ENTRY etc. are fine: bash -n is parse-only,
# not runtime. It would have caught the trailing-semicolon-after-ampersand bug.
for f in "${TARGETS[@]}"; do
  [[ -f "$f" ]] || continue
  snippets="$(awk '/^[[:space:]]*```bash[[:space:]]*$/{flag=1;next} /^[[:space:]]*```[[:space:]]*$/{flag=0} flag' "$f")"
  if [[ -z "$snippets" ]]; then
    printf '  SKIP: no fenced-bash blocks in %s\n' "$f"
    continue
  fi
  if printf '%s\n' "$snippets" | bash -n 2>/tmp/abp-drift-parse.$$; then
    snippet_count=$(awk '/^[[:space:]]*```bash[[:space:]]*$/{c++} END{print c+0}' "$f")
    printf '  OK:   %d fenced-bash block(s) parse clean in %s\n' "$snippet_count" "$f"
  else
    printf '  FAIL: parse error in %s:\n' "$f"
    sed 's/^/        /' /tmp/abp-drift-parse.$$
    FAILED=1
  fi
  rm -f /tmp/abp-drift-parse.$$
done

echo
if [[ "$FAILED" -eq 0 ]]; then
  echo "=== PASS: sentinel + helper + embedded snippets clean across all 4 surfaces ==="
  exit 0
else
  echo "=== FAIL: drift detected ==="
  exit 1
fi
