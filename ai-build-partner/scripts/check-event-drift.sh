#!/usr/bin/env bash
# ABP buyer-signal v1 drift check
#
# Greps the ABP_TELEMETRY_SENTINEL_v1 marker across all 4 SKILL.md files
# (free ABP + 3 paid skills). Fails non-zero if any file is missing it.
#
# Run:
#   bash scripts/check-event-drift.sh
#
# Exit codes:
#   0 = all 4 SKILL.md files have the sentinel + shared abp-fire-event.sh present
#   1 = at least one file missing the sentinel or helper script

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
if [[ "$FAILED" -eq 0 ]]; then
  echo "=== PASS: sentinel + helper present in all 4 surfaces ==="
  exit 0
else
  echo "=== FAIL: drift detected ==="
  exit 1
fi
