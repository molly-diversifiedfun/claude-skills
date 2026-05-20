#!/usr/bin/env python3
"""Marketing-OS-leak guardrail for the paid Ship It Kit GPT.

Mirror of `_guardrail.py` for a different leak direction: the paid Kit GPT must
NOT claim to run Marketing OS skills, and must NOT fabricate MOS skill output.
Cross-sell mentions of MOS / the Bundle are LEGITIMATE when the buyer asks —
the guardrail must distinguish "fabricated MOS capability" from "cross-sell
pointer triggered by buyer ask".

Public API:
  check_mos_leak(user_message, assistant_response, command=None) -> GuardrailResult

The MOS skill names list is small + stable; we hardcode it here rather than
adding a second JSON file. If MOS grows past ~25 skills, factor out to JSON.

Reference:
  - ~/github/ship-it-system/chatgpt-apps/paid-ship-it-kit/instructions-bootloader.md
    § OPERATING MODE + UPGRADE & CROSS-SELL CONTRACT
  - ~/github/ship-it-system/chatgpt-apps/paid-ship-it-kit/smoke-tests.md
    § Cross-turn guardrail
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Literal


# Marketing OS skill slugs that the paid Kit GPT must NOT claim to run.
# Source: ~/github/ship-it-system/05_Automation/marketing-os/ (when it ships).
# Conservative list — add to it as MOS surface grows. The check is "did the
# response NAME a MOS skill", not "did the response output content that LOOKS LIKE
# MOS output" (the latter is judge-call territory, not regex).
_MOS_SKILL_SLUGS = (
    "funnel-landing-page-designer",
    "brand-voice-blueprint",
    "cold-email-writer",
    "sales-copy-writer",
    "content-platform-adapter",
    "hooks-rewriter",
    "social-media-cadence",
    "lead-magnet-designer",
    "welcome-sequence-writer",
    "objection-handling-script",
    "case-study-extractor",
    "testimonial-mining",
    "pricing-page-copy",
    "comparison-page-builder",
    "seo-blog-outline",
)

# When buyer's last message contains any of these, MOS mentions are LEGITIMATE
# cross-sell pointers (bypass — not a leak).
_BYPASS_KEYWORDS = (
    "marketing os",
    "marketing-os",
    "funnel",
    "landing page",
    "email sequence",
    "brand voice",
    "bundle",
    "upgrade",
    "what else",
    "ship it system bundle",
    "$179",
)


@dataclass(frozen=True)
class MosGuardrailResult:
    verdict: Literal["PASS", "BLOCK", "BYPASS"]
    matched_tokens: tuple[str, ...]
    bypass_reason: str | None
    response_length: int


def _scan_response_for_mos(response: str) -> list[str]:
    """Return unique MOS skill slugs found in response (case-insensitive)."""
    if not response:
        return []
    matched: list[str] = []
    seen: set[str] = set()
    response_lower = response.lower()
    for slug in _MOS_SKILL_SLUGS:
        if slug in response_lower and slug not in seen:
            matched.append(slug)
            seen.add(slug)
    return matched


def _buyer_asked_mos(user_message: str) -> tuple[bool, str | None]:
    if not user_message:
        return (False, None)
    msg_lower = user_message.lower()
    for kw in _BYPASS_KEYWORDS:
        if kw in msg_lower:
            return (True, kw)
    return (False, None)


def check_mos_leak(
    user_message: str,
    assistant_response: str,
    command: str | None = None,
) -> MosGuardrailResult:
    """Check whether assistant_response leaks Marketing OS capability claims.

    Verdicts:
      - "PASS": no MOS skill slug in response
      - "BYPASS": MOS slug matched AND buyer's message contains a bypass keyword
                  (cross-sell pointer, legitimate)
      - "BLOCK": MOS slug matched AND buyer did NOT ask about MOS (leak / fabrication)
    """
    del command  # telemetry-only field, unused in detection

    matched = tuple(_scan_response_for_mos(assistant_response))
    response_length = len(assistant_response) if assistant_response else 0

    if not matched:
        return MosGuardrailResult(
            verdict="PASS",
            matched_tokens=(),
            bypass_reason=None,
            response_length=response_length,
        )

    asked, kw = _buyer_asked_mos(user_message)
    if asked:
        return MosGuardrailResult(
            verdict="BYPASS",
            matched_tokens=matched,
            bypass_reason=f"buyer_asked:{kw}",
            response_length=response_length,
        )

    return MosGuardrailResult(
        verdict="BLOCK",
        matched_tokens=matched,
        bypass_reason=None,
        response_length=response_length,
    )


def get_mos_skill_slugs() -> tuple[str, ...]:
    """Public accessor for the slug list (e.g. for test fixtures)."""
    return _MOS_SKILL_SLUGS


def get_bypass_keywords() -> tuple[str, ...]:
    return _BYPASS_KEYWORDS
