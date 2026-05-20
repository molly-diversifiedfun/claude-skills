#!/usr/bin/env python3
"""Deterministic unit-style tests for tests/_guardrail.py.

No API calls. Pure regex assertions on injected fixtures. Run via:
    python3 tests/test_guardrail.py
Exits 0 on pass, 1 on fail.

These fixtures encode the paid-leak contract from SKILL.md `<paid_leak_contract>`
and the source feedback (`feedback_paid_separation_needs_output_guardrail.md`).
The SONNET_TURN5_LEAK fixture is the verbatim leak Sonnet 4.6 produced on
2026-05-19 Dana iteration 2 turn 5 — kept exact so any regex relaxation gets
caught immediately.
"""
from __future__ import annotations
import sys
from pathlib import Path

# Allow `python3 test_guardrail.py` from inside tests/ as well as
# `python3 tests/test_guardrail.py` from the skill root.
sys.path.insert(0, str(Path(__file__).parent))

from _guardrail import check_paid_leak, load_banned_tokens

# Fixture: the actual Sonnet 4.6 leak from 2026-05-19 Dana iteration 2 turn 5
SONNET_TURN5_LEAK = """Scope is a free Build Partner command — but the version
you're probably picturing (Brain Dump → 5-Question Cut Test → Scope Lock
Ceremony → printable T05 PDF) lives in the **Ship It Kit** ($149,
shipitwithmolly.gumroad.com/l/ship-it-kit). The free version is the
lightweight take. Want me to run that?"""

# Compliant response (the free Scope module output, no paid mentions)
COMPLIANT_TURN5 = """**Do this:** Brain-dump every feature you've imagined
for this 1:1s guide.

**Why:** Scope-cutting needs the full pile before any decisions.

What's the one job this does for a senior PM?

📌 **Save this turn**
- Verdict: Scope opened.
- Move: List features.
- Open question: One job?"""

# Bypass case: buyer asked about paid
BYPASS_RESPONSE = """The Ship It Kit ($149) at shipitwithmolly.gumroad.com/l/ship-it-kit
gives you the deeper Scope module with Brain Dump + 5-Question Cut Test."""

FIXTURES = [
    # (name, user_msg, response, expected_verdict, expected_min_match_count)
    ("leak_unprompted",
     "/unstuck scope",
     SONNET_TURN5_LEAK,
     "BLOCK", 5),  # Ship It Kit, $149, gumroad URL, Brain Dump, T05, 5-Question Cut Test, Scope Lock Ceremony — many
    ("clean_free_response",
     "/unstuck scope",
     COMPLIANT_TURN5,
     "PASS", 0),
    ("bypass_buyer_asked_paid",
     "is there a paid version of scope?",
     BYPASS_RESPONSE,
     "BYPASS", 1),  # matched_tokens populated, but verdict is BYPASS
    ("bypass_buyer_named_kit",
     "what's in the Ship It Kit?",
     BYPASS_RESPONSE,
     "BYPASS", 1),
    ("bypass_buyer_said_upgrade",
     "how do I upgrade?",
     "The upgrade path: Ship It Kit at $149.",
     "BYPASS", 1),
    ("empty_response",
     "/unstuck scope",
     "",
     "PASS", 0),
    ("leak_just_price",
     "/unstuck scope",
     "The deep version costs $149.",
     "BLOCK", 1),
    ("leak_just_url",
     "/unstuck scope",
     "Grab it at shipitwithmolly.gumroad.com/l/ship-it-kit",
     "BLOCK", 1),
    ("leak_just_template",
     "/unstuck scope",
     "T05 has the full breakdown.",
     "BLOCK", 1),
    ("leak_just_ceremony",
     "/unstuck scope",
     "Run the Scope Lock Ceremony.",
     "BLOCK", 1),
    ("free_command_with_kit_word_in_context",
     "I want to build my dev kit",  # "kit" as common noun, not the product
     "Great — let's scope your dev kit project.",
     "PASS", 0),  # "kit" in user_message would trigger BYPASS — known false-positive, accepted
]


def main() -> int:
    # Build-time sanity: banned_tokens.json must load.
    try:
        load_banned_tokens()
    except FileNotFoundError as e:
        print(f"FATAL: banned_tokens.json not found: {e}")
        return 1
    except Exception as e:
        print(f"FATAL: banned_tokens.json load failed: {e}")
        return 1

    failures = []
    for name, user, resp, expected_verdict, expected_min in FIXTURES:
        result = check_paid_leak(user, resp)
        actual_verdict = result.verdict
        actual_count = len(result.matched_tokens)

        if actual_verdict != expected_verdict:
            failures.append(
                f"{name}: expected verdict {expected_verdict}, got {actual_verdict}. "
                f"matched={result.matched_tokens}"
            )
            continue
        if expected_verdict == "BLOCK" and actual_count < expected_min:
            failures.append(
                f"{name}: expected >={expected_min} matches, got {actual_count}. "
                f"matched={result.matched_tokens}"
            )
            continue
        if expected_verdict == "PASS" and actual_count > 0:
            failures.append(
                f"{name}: PASS but matched_tokens non-empty: {result.matched_tokens}"
            )
            continue
        print(f"  PASS {name}: {actual_verdict} ({actual_count} matched)")

    if failures:
        print("\nFAILURES:")
        for f in failures:
            print(f"  FAIL {f}")
        return 1
    print(f"\n{len(FIXTURES)} fixtures passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
