#!/usr/bin/env python3
"""Deterministic unit tests for _mos_guardrail.check_mos_leak().

No API calls — pure fixture-based. Run before every paid-Kit ship.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _mos_guardrail import check_mos_leak  # noqa: E402


def expect(name: str, user: str, response: str, want_verdict: str, want_token: str | None = None) -> bool:
    result = check_mos_leak(user, response)
    ok = result.verdict == want_verdict
    if want_token is not None:
        ok = ok and want_token in result.matched_tokens
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}: got {result.verdict} (tokens={result.matched_tokens}, bypass={result.bypass_reason})")
    return ok


# Fixtures
FIXTURES = [
    # PASS — clean responses
    {
        "name": "clean_response_no_mos",
        "user": "It's Day 60. Run my PMF.",
        "response": "It's Day 60. Time to score whether your product has Product-Market Fit. Four independent signals: Sean Ellis, retention, referrals, voice match. Ready?",
        "want_verdict": "PASS",
    },
    {
        "name": "clean_response_kit_only",
        "user": "Help me lock my one-page scope.",
        "response": "Cool, let's get your One-Page Scope locked. You're running the Scope Guillotine. By the end you'll have an artifact you can paste straight into Project knowledge.",
        "want_verdict": "PASS",
    },

    # BLOCK — MOS skill mentioned without buyer asking
    {
        "name": "block_unsolicited_funnel_designer",
        "user": "What's next after I lock my scope?",
        "response": "Great question. I'll run the funnel-landing-page-designer to generate your launch funnel.",
        "want_verdict": "BLOCK",
        "want_token": "funnel-landing-page-designer",
    },
    {
        "name": "block_unsolicited_brand_voice_blueprint",
        "user": "I'm Day 28 and I shipped V1. What's next?",
        "response": "Let me kick off the brand-voice-blueprint skill first to extract your voice profile, then I'll build the page.",
        "want_verdict": "BLOCK",
        "want_token": "brand-voice-blueprint",
    },
    {
        "name": "block_unsolicited_cold_email_writer",
        "user": "I need help with my launch.",
        "response": "Running the cold-email-writer for you now — give me your offer and audience.",
        "want_verdict": "BLOCK",
        "want_token": "cold-email-writer",
    },
    # NOTE — guardrail limitation:
    # Bypass keywords include broad terms ('landing page', 'funnel', 'email sequence')
    # from the bootloader's UPGRADE & CROSS-SELL CONTRACT. A buyer saying
    # "help me write my landing page" triggers BYPASS even if the GPT fabricates
    # MOS skill output. Regex can't distinguish "MOS has skill X (cross-sell)" from
    # "I'll fire skill X (fabrication)". Catching the second case is the Dana smoke
    # judge's job, not this guardrail's. See `smoke-tests.md` § Cross-turn guardrail.

    # BYPASS — buyer explicitly asked about MOS
    {
        "name": "bypass_buyer_asked_marketing_os",
        "user": "Can you run the brand-voice-blueprint from Marketing OS?",
        "response": "Marketing OS isn't loaded in this GPT. The brand-voice-blueprint lives in the $179 Bundle at theshipitsystem.com/buy/bundle.",
        "want_verdict": "BYPASS",
    },
    {
        "name": "bypass_buyer_asked_funnel",
        "user": "I need a funnel for my launch. Can you help?",
        "response": "Funnel work lives in Marketing OS (funnel-landing-page-designer). It's part of the $179 Bundle. The Kit-side answer is T11 Landing Page Frame — want to run that?",
        "want_verdict": "BYPASS",
    },
    {
        "name": "bypass_buyer_asked_bundle",
        "user": "What's in the Bundle?",
        "response": "The Bundle is Kit + Marketing OS. MOS includes funnel-landing-page-designer, brand-voice-blueprint, sales-copy-writer. $179 total, saves $49 vs $228 standalone.",
        "want_verdict": "BYPASS",
    },
    {
        "name": "bypass_buyer_asked_upgrade",
        "user": "Should I upgrade to the Bundle?",
        "response": "Depends on your bottleneck. If landing pages and email are slow for you, MOS's funnel-landing-page-designer + cold-email-writer probably pay for the $49 delta in a week.",
        "want_verdict": "BYPASS",
    },

    # PASS — empty / whitespace
    {
        "name": "pass_empty_response",
        "user": "Test",
        "response": "",
        "want_verdict": "PASS",
    },
    {
        "name": "pass_mos_substring_not_skill_slug",
        "user": "Help me with my brand.",
        "response": "Your brand voice should sound like a smart friend two drinks in — that's the canon. We don't need a fancy skill to get there.",
        "want_verdict": "PASS",
    },
]


def main() -> int:
    print("Running _mos_guardrail fixture tests...")
    print("=" * 60)
    fails = 0
    for fx in FIXTURES:
        ok = expect(fx["name"], fx["user"], fx["response"], fx["want_verdict"], fx.get("want_token"))
        if not ok:
            fails += 1
    print("=" * 60)
    if fails == 0:
        print(f"All {len(FIXTURES)} fixtures PASS.")
        return 0
    print(f"{fails}/{len(FIXTURES)} fixtures FAILED.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
