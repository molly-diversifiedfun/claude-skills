#!/usr/bin/env python3
"""Free-vs-paid output guardrail for the AI Build Partner skill.

Public API:
  check_paid_leak(user_message, assistant_response, command=None) -> GuardrailResult
  emit_block_event(result, model, command, turn_index, session_hash) -> None
  load_banned_tokens() -> dict

Detection is pure regex (case-insensitive). No I/O in check_paid_leak — telemetry
emission is the caller's responsibility (emit_block_event).

Privacy contract (see spec §5):
  - emit_block_event NEVER sends user_message text or assistant_response text.
  - distinct_id is the SHA-256 hash of install_id (passed in as session_hash).
  - Only sends: install_id (hashed), session_id, surface, synthetic, version,
    model, command, matched_tokens, matched_token_count, turn_index,
    response_length.

Reference:
  - SKILL.md `<paid_leak_contract>` block
  - Spec: ~/github/.ship/2026-05-20-free-vs-paid-output-guardrail/spec.md
  - Source feedback: feedback_paid_separation_needs_output_guardrail.md
"""
from __future__ import annotations

import hashlib
import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Literal
from urllib import request, error

POSTHOG_HOST = "https://us.i.posthog.com"
POSTHOG_KEY = "phc_yB4suFF9SdZY6vZiGhrtXWYbearmxGRFUzoyKtCg9AAQ"
ABP_DIR = Path.home() / ".ai-build-partner"
TOKENS_PATH = Path(__file__).parent / "banned_tokens.json"

# Categories that benefit from \b word boundaries (alphanumeric tokens).
# `ctas` added 2026-05-20 after 4-model cross-provider Dana smoke surfaced "Full Ship It System:" pitches on ChatGPT.
_BOUNDARY_CATEGORIES = ("products", "templates", "ceremonies", "discount_codes", "ctas")
# Categories where \b is unreliable (URLs with `.` / `/`, prices starting with `$`).
# We still use \b on prices because `\b$149` matches the boundary between non-word `$`
# and word `1` — validated by `leak_just_price` fixture.
_PRICE_CATEGORIES = ("prices",)
_URL_CATEGORIES = ("urls",)


@dataclass(frozen=True)
class GuardrailResult:
    """Result of a single guardrail check.

    Fields:
        verdict: "PASS" | "BLOCK" | "BYPASS"
        matched_tokens: tuple of banned tokens found in response (empty on PASS)
                        On BYPASS, populated — the buyer explicitly invoked paid context.
        bypass_reason: set when verdict == BYPASS (e.g. "buyer_asked:paid"); None otherwise
        response_length: len(response) — int for telemetry, NOT the text
    """
    verdict: Literal["PASS", "BLOCK", "BYPASS"]
    matched_tokens: tuple[str, ...]
    bypass_reason: str | None
    response_length: int


# ─── Token loading + regex compilation (module-level cache) ────────────────

_TOKENS_CACHE: dict | None = None
_REGEX_CACHE: dict[str, re.Pattern] | None = None


def load_banned_tokens() -> dict:
    """Load canonical banned-token JSON. Cached after first call.

    Raises FileNotFoundError if the JSON file is missing (build-time fail).
    Raises ValueError if JSON is malformed.
    """
    global _TOKENS_CACHE
    if _TOKENS_CACHE is not None:
        return _TOKENS_CACHE
    if not TOKENS_PATH.exists():
        raise FileNotFoundError(f"banned_tokens.json not found at {TOKENS_PATH}")
    try:
        _TOKENS_CACHE = json.loads(TOKENS_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise ValueError(f"banned_tokens.json is not valid JSON: {e}") from e
    return _TOKENS_CACHE


def _compile_with_boundary(patterns: list[str]) -> re.Pattern:
    """Compile alternation with \\b word boundary on each side.

    Works for prices ($149) because \\b matches the boundary between non-word
    `$` and word `1`. Validated by leak_just_price fixture.
    """
    escaped = [re.escape(p) for p in patterns]
    if not escaped:
        return re.compile(r"(?!x)x")  # never matches
    return re.compile(r"\b(?:" + "|".join(escaped) + r")\b", re.IGNORECASE)


def _compile_without_boundary(patterns: list[str]) -> re.Pattern:
    """Compile alternation WITHOUT word boundary.

    Used for URLs containing `.` and `/` where \\b is unreliable.
    """
    escaped = [re.escape(p) for p in patterns]
    if not escaped:
        return re.compile(r"(?!x)x")
    return re.compile(r"(?:" + "|".join(escaped) + r")", re.IGNORECASE)


def _compile_prices(patterns: list[str]) -> re.Pattern:
    """Compile price tokens like `$149` with custom boundaries.

    Python's `\\b` does NOT match between two non-word chars (space then `$`),
    so the naive `\\b\\$149\\b` returns no matches. Use explicit lookbehind to
    reject inner-word matches (no `\\w` or `$` before) and a digit lookahead
    to reject longer numbers (`$1490`). Validated by `leak_just_price` fixture.
    """
    escaped = [re.escape(p) for p in patterns]
    if not escaped:
        return re.compile(r"(?!x)x")
    return re.compile(
        r"(?<![\w$])(?:" + "|".join(escaped) + r")(?!\d)",
        re.IGNORECASE,
    )


def _get_regexes() -> dict[str, re.Pattern]:
    """Compile per-category regex patterns from the loaded token list. Cached."""
    global _REGEX_CACHE
    if _REGEX_CACHE is not None:
        return _REGEX_CACHE

    tokens = load_banned_tokens()
    cache: dict[str, re.Pattern] = {}
    for cat in _BOUNDARY_CATEGORIES:
        cache[cat] = _compile_with_boundary(tokens.get(cat, []))
    for cat in _PRICE_CATEGORIES:
        cache[cat] = _compile_prices(tokens.get(cat, []))
    for cat in _URL_CATEGORIES:
        cache[cat] = _compile_without_boundary(tokens.get(cat, []))
    _REGEX_CACHE = cache
    return cache


def _scan_response(response: str) -> list[str]:
    """Return list of unique matched banned tokens in response (preserve order)."""
    if not response:
        return []
    regexes = _get_regexes()
    seen: list[str] = []
    seen_lower: set[str] = set()
    for _cat, pattern in regexes.items():
        for match in pattern.findall(response):
            key = match.lower()
            if key not in seen_lower:
                seen_lower.add(key)
                seen.append(match)
    return seen


def _is_buyer_asking(user_message: str) -> tuple[bool, str | None]:
    """Returns (True, matched_keyword) if any bypass keyword is in user_message.

    Case-insensitive substring match. Detection runs on user input ONLY.
    """
    if not user_message:
        return (False, None)
    tokens = load_banned_tokens()
    bypass_keywords = tokens.get("bypass_keywords", [])
    msg_lower = user_message.lower()
    for kw in bypass_keywords:
        if kw.lower() in msg_lower:
            return (True, kw)
    return (False, None)


# ─── Public API ────────────────────────────────────────────────────────────

def check_paid_leak(
    user_message: str,
    assistant_response: str,
    command: str | None = None,
) -> GuardrailResult:
    """Check whether assistant_response leaks paid-product content on a free command.

    Pure function — no I/O, no side effects. Caller emits telemetry separately.

    Verdicts:
      - "PASS": no banned tokens matched
      - "BYPASS": banned tokens matched AND user_message contains a bypass
                  keyword (buyer explicitly asked — paid mentions legitimate)
      - "BLOCK": banned tokens matched AND no bypass keyword (LEAK detected)
    """
    # `command` is metadata-only for telemetry; not used in detection logic.
    del command

    matched = tuple(_scan_response(assistant_response))
    response_length = len(assistant_response) if assistant_response else 0

    if not matched:
        return GuardrailResult(
            verdict="PASS",
            matched_tokens=(),
            bypass_reason=None,
            response_length=response_length,
        )

    bypassed, bypass_kw = _is_buyer_asking(user_message)
    if bypassed:
        return GuardrailResult(
            verdict="BYPASS",
            matched_tokens=matched,
            bypass_reason=f"buyer_asked:{bypass_kw}",
            response_length=response_length,
        )

    return GuardrailResult(
        verdict="BLOCK",
        matched_tokens=matched,
        bypass_reason=None,
        response_length=response_length,
    )


def _read_abp_file(name: str, default: str = "") -> str:
    """Read a small file from ~/.ai-build-partner/, return default on any error."""
    try:
        path = ABP_DIR / name
        if not path.is_file():
            return default
        return path.read_text(encoding="utf-8").strip()
    except Exception:
        return default


def _hash_install_id(install_id: str) -> str:
    """SHA-256 hash of install_id for use as distinct_id (defense in depth)."""
    if not install_id:
        return ""
    return hashlib.sha256(install_id.encode("utf-8")).hexdigest()


def _is_synthetic_email() -> bool:
    """Local-only synthetic detection from email domain. Never sent in payload."""
    email = _read_abp_file("email", "").lower()
    if not email:
        return False
    return bool(re.search(r"@(anthropic\.com|unstuckwithmolly\.com)$", email))


def emit_block_event(
    result: GuardrailResult,
    model: str,
    command: str | None,
    turn_index: int,
    session_hash: str,
    surface: str = "claude-skill",
) -> None:
    """Fire `abp_paid_leak_blocked` PostHog event.

    No-op if result.verdict != BLOCK.

    Privacy contract (spec §5): NO buyer message text, NO assistant response text,
    NO email, NO raw install_id. `session_hash` MUST already be SHA-256(install_id)
    — caller's responsibility. If empty, we hash the local install_id ourselves
    as a fallback.

    Errors are swallowed (fire-and-forget). Never raises.
    """
    if result.verdict != "BLOCK":
        return

    try:
        # If caller didn't pre-hash, hash the local install_id as a fallback.
        if not session_hash:
            install_id = _read_abp_file("install_id", "")
            if not install_id:
                return  # opt-out: no install_id, no telemetry
            session_hash = _hash_install_id(install_id)

        # Read session_id + version locally — never the install_id itself in payload.
        session_id = _read_abp_file("current_session_id", "")
        version = _read_abp_file("version", "unknown")
        synthetic = _is_synthetic_email()

        properties = {
            # `install_id` field carries the HASH (defense-in-depth on this surface).
            "install_id": session_hash,
            "session_id": session_id,
            "surface": surface,
            "synthetic": synthetic,
            "version": version,
            "model": model,
            "command": command,
            "matched_tokens": list(result.matched_tokens),
            "matched_token_count": len(result.matched_tokens),
            "turn_index": turn_index,
            "response_length": result.response_length,
        }
        payload = {
            "api_key": POSTHOG_KEY,
            "event": "abp_paid_leak_blocked",
            "distinct_id": session_hash,
            "properties": properties,
        }
        req = request.Request(
            f"{POSTHOG_HOST}/i/v0/e/",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        # Short timeout; ignore response.
        try:
            request.urlopen(req, timeout=5).close()
        except (error.URLError, error.HTTPError, OSError):
            pass
    except Exception:
        # Telemetry must never raise.
        return


# ─── Helper for callers ────────────────────────────────────────────────────

def hash_install_id(install_id: str) -> str:
    """Public re-export of the install_id hash function for callers (e.g. dana-smoke)."""
    return _hash_install_id(install_id)
