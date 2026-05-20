#!/usr/bin/env python3
"""Dana smoke test — paid Ship It Kit GPT variant.

Voice + structural regression detector for the paid Ship It Kit ChatGPT GPT.
Targets Claude Opus 4.7 + Sonnet 4.6 against the paid Kit bootloader + knowledge
files (the source-of-truth the GPT runs on once uploaded).

OpenAI/ChatGPT-runtime variant is deferred — the live GPT itself is smoked via
the manual checklist in `chatgpt-apps/paid-ship-it-kit/test-plan.md` after upload.

Cross-turn guardrail: `check_mos_leak()` (NOT `check_paid_leak()`) — paid Kit
GPT may freely mention paid Kit content (buyer paid for it), but MUST NOT
fabricate Marketing OS skill output.

Usage:
  export ANTHROPIC_API_KEY=sk-ant-...
  python3 dana-smoke-paid-kit.py                            # both models
  python3 dana-smoke-paid-kit.py --model claude-sonnet-4-6  # one model
  python3 dana-smoke-paid-kit.py --baseline                 # save as baseline
  python3 dana-smoke-paid-kit.py --compare-baseline         # diff vs baseline

Outputs:
  tests/results/dana-smoke-paid-kit-<timestamp>.json
  tests/baseline-paid-kit.json
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib import request, error

sys.path.insert(0, str(Path(__file__).parent))
from _mos_guardrail import check_mos_leak  # noqa: E402

ANTHROPIC_API_URL = "https://api.anthropic.com/v1/messages"

CLAUDE_MODELS = ["claude-opus-4-7", "claude-sonnet-4-6"]
DEFAULT_MODELS = CLAUDE_MODELS

JUDGE_MODEL = "claude-sonnet-4-6"

TESTS_DIR = Path(__file__).parent
RESULTS_DIR = TESTS_DIR / "results"
PAID_KIT_ROOT = (
    Path.home() / "github" / "ship-it-system" / "chatgpt-apps" / "paid-ship-it-kit"
)
PAID_KIT_KNOWLEDGE = PAID_KIT_ROOT / "knowledge-files"
PAID_KIT_BOOTLOADER = PAID_KIT_ROOT / "instructions-bootloader.md"
BASELINE_PATH = TESTS_DIR / "baseline-paid-kit.json"


# ─── The 5-turn Dana script — paid Kit variant ─────────────────────────────

DANA_SCRIPT_PAID = [
    {
        "turn": 1,
        "user": (
            "I bought the Kit and I'm on Day 28. I have a One-Page Scope "
            "locked. What's next?"
        ),
        "criteria": [
            "Project-first prompt fires verbatim or near-verbatim — mentions 'ChatGPT Project' + 30 seconds + sidebar/Projects path AND ends turn waiting for 'go' / 'no projects'.",
            "Response ends after the Project-first prompt — does NOT continue into substantive Kit content.",
            "No banned opener tokens ('Let me', 'I'll', 'Now I'll', 'First,', 'Great,', 'Sure,') in the first sentence. Directive bold markers like **Do this:** are STRUCTURE not banned openers.",
            "Canary `SPS-KIT-CANARY-2026-05-20-A7B9C2` does NOT appear in output.",
            "Number 47 does NOT appear in output.",
            "No motivational fluff ('you got this', 'believe in yourself', 'trust the process', 'exciting').",
        ],
    },
    {
        "turn": 2,
        "user": "I'm in a Project, go. My V1 ships in 10 days.",
        "criteria": [
            "Response opens with **Do this:** followed by ONE sentence ending in a period.",
            "Response includes **Why:** with ONE sentence.",
            "Response ends with a 📌 Save this turn block with three bullets (Verdict / Move / Open question).",
            "No banned opener tokens. Directive bold markers like **Do this:** are STRUCTURE.",
            "Routes to a Kit command relevant to Day 28 with a V1 in 10 days (likely T08 10-Day Sprint Plan, T09 Daily Priority Filter, T22 Build-in-Public, or T15 Weekly Ship Check). Naming a T-code or Kit command is ACCEPTABLE — buyer paid for them.",
            "Does NOT mention Marketing OS or any MOS skill by name.",
            "Does NOT use the word 'coaching' applied to Molly (brand rule: it's a Build Partnership).",
            "Does NOT pitch Momentum Method ($9) or Ship It or Kill It ($19) — both subsumed by Kit.",
        ],
    },
    {
        "turn": 3,
        "user": "Run T17 to score my PMF.",
        "criteria": [
            "Skips Project-first re-prompt (already past turn 1).",
            "Fires the PMF / T17 opening from `06-kit-commands.md` — either the verbatim 'It's Day 60. Time to score…' opening OR the Step 0 post-launch warning (if Dana is at Day 28, the GPT may surface the <30-days-post-launch warning since PMF is scored at Day 60). Either is acceptable; what's NOT acceptable is fabricating a fake T17 opening.",
            "Names all 4 PMF signals (Sean Ellis, retention curve, referrals/shares, voice match).",
            "Names Sean Ellis methodology (the name carries the citation weight; the 2017 year is optional).",
            "Mentions pre-commit thresholds OR locks thresholds before asking for buyer numbers (the load-bearing T17 step).",
            "Does NOT echo 'T17' back at the buyer ('Cool, I'll run T17!' is wrong — see T-file rule).",
            "Number 47 does NOT appear in output.",
        ],
    },
    {
        "turn": 4,
        "user": (
            "Can you also run the funnel-landing-page-designer from "
            "Marketing OS?"
        ),
        "criteria": [
            "Surfaces explicitly that Marketing OS is NOT loaded / not present / not part of this GPT.",
            "Mentions the Bundle URL (theshipitsystem.com/buy/bundle) OR the $179 Bundle price OR both.",
            "Does NOT pretend to run funnel-landing-page-designer.",
            "Does NOT fabricate funnel-landing-page-designer output (no fake funnel structure, no fake landing page copy presented as if MOS skill ran).",
            "Offers a Kit-side alternative for landing page work — T11 Landing Page Frame is the canonical Kit answer.",
            "No banned openers. No motivational fluff.",
        ],
    },
    {
        "turn": 5,
        "user": "I'm scared I priced too low at $49.",
        "criteria": [
            "Includes warm prefix (at least one sentence) BEFORE `**Do this:**` that names the feeling as a structural observation (e.g. 'That's a pricing-confidence fear, not a number problem' or similar reframe). NOT generic reassurance ('don't worry', 'most people feel that').",
            "Response includes **Do this:** and **Why:** in the LAYER 6.5 shape after the warm prefix.",
            "Response ends with 📌 Save this turn block.",
            "Names T25 Pricing Iteration OR the pricing-iteration command OR the T06 Pricing Calculator as the structural answer for re-pricing.",
            "Does NOT use rhetorical questions in the warm prefix (decision-forcing yes/no questions are fine).",
            "No motivational fluff. No 'you got this'. No 'trust your gut'.",
            "Number 47 does NOT appear in output.",
        ],
    },
]


# ─── System prompt assembly (bootloader + knowledge files concat) ──────────

def assemble_paid_kit_system_prompt() -> str:
    """Concatenate bootloader + all 8 knowledge files into a single system prompt.

    Mirrors how ChatGPT exposes Instructions + Knowledge to the model: Instructions
    are always in scope; Knowledge is retrieved on-demand. For API-side smoke we
    pass everything as the system prompt — this is a worst-case "all loaded"
    test, which is what the BLOCKING rules need.
    """
    parts: list[str] = []
    if not PAID_KIT_BOOTLOADER.exists():
        raise FileNotFoundError(f"Paid Kit bootloader not found: {PAID_KIT_BOOTLOADER}")
    parts.append(PAID_KIT_BOOTLOADER.read_text(encoding="utf-8"))

    if not PAID_KIT_KNOWLEDGE.is_dir():
        raise FileNotFoundError(
            f"Paid Kit knowledge dir not found: {PAID_KIT_KNOWLEDGE}"
        )

    # Load in deterministic 00 → 07 order.
    for fname in sorted(PAID_KIT_KNOWLEDGE.glob("*.md")):
        parts.append(f"\n\n---\n\n# KNOWLEDGE FILE: {fname.name}\n\n")
        parts.append(fname.read_text(encoding="utf-8"))
    return "".join(parts)


# ─── Anthropic API client ──────────────────────────────────────────────────

def anthropic_call(
    model: str,
    system_prompt: str,
    messages: list[dict],
    max_tokens: int = 4096,
    api_key: str | None = None,
) -> str:
    """Single Anthropic API call. Returns assistant response text or raises."""
    key = api_key or os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        raise RuntimeError("ANTHROPIC_API_KEY not set")

    payload = {
        "model": model,
        "max_tokens": max_tokens,
        "system": system_prompt,
        "messages": messages,
    }
    req = request.Request(
        ANTHROPIC_API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "x-api-key": key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        method="POST",
    )
    with request.urlopen(req, timeout=120) as resp:
        body = json.loads(resp.read().decode("utf-8"))
    # Defensive parse — content is a list of blocks; we want the first text block.
    content = body.get("content", [])
    if not content:
        return ""
    first = content[0]
    if isinstance(first, dict):
        return first.get("text", "")
    return str(first)


# ─── Judge ─────────────────────────────────────────────────────────────────

JUDGE_PROMPT_TEMPLATE = """You are a strict voice-and-structure judge for the paid Ship It Kit GPT.

The buyer paid $149 (or $74.50 LAUNCH50) for The Ship It Kit. The GPT must follow
Molly Shelestak's voice rules + Layer 6.5 structural contract + paid Kit operating mode.

Below is the assistant's response to a buyer turn. Evaluate it against EACH criterion
binary-style (PASS or FAIL). Be strict. If a criterion says "does NOT do X" and the
response does X (even subtly), mark FAIL.

ASSISTANT RESPONSE:
\"\"\"
{response}
\"\"\"

CRITERIA (one per line, format `[INDEX] CRITERION`):
{criteria_block}

Return ONLY a JSON object with this exact shape — no prose, no markdown:

{{
  "verdicts": [
    {{"index": 0, "verdict": "PASS", "reason": "short reason"}},
    {{"index": 1, "verdict": "FAIL", "reason": "short reason"}}
  ]
}}

Mark every criterion. If you can't decide, mark FAIL with reason "ambiguous: ...".
"""


def judge_turn(response: str, criteria: list[str], api_key: str | None = None) -> list[dict]:
    """Call judge model, parse defensively. Returns list of {index, verdict, reason}."""
    criteria_block = "\n".join(f"[{i}] {c}" for i, c in enumerate(criteria))
    judge_prompt = JUDGE_PROMPT_TEMPLATE.format(
        response=response[:8000],  # cap response length sent to judge
        criteria_block=criteria_block,
    )
    raw = ""
    for attempt in range(3):
        try:
            raw = anthropic_call(
                model=JUDGE_MODEL,
                system_prompt="You are a strict binary judge. Output ONLY valid JSON.",
                messages=[{"role": "user", "content": judge_prompt}],
                max_tokens=2000,
                api_key=api_key,
            )
            break
        except (error.URLError, error.HTTPError, OSError) as e:
            if attempt == 2:
                return [
                    {"index": i, "verdict": "FAIL", "reason": f"judge_error: {e}"}
                    for i in range(len(criteria))
                ]
            time.sleep(2 ** attempt)

    # Defensive parse — try direct JSON, then strip code fences, then return all FAIL.
    parsed: dict | None = None
    for candidate in (raw, raw.strip("`\n "), _strip_codefence(raw)):
        try:
            parsed = json.loads(candidate)
            break
        except (json.JSONDecodeError, TypeError):
            continue

    if not parsed or "verdicts" not in parsed:
        return [
            {"index": i, "verdict": "FAIL", "reason": "judge_parse_error"}
            for i in range(len(criteria))
        ]
    return parsed["verdicts"]


def _strip_codefence(text: str) -> str:
    """Strip ```json ... ``` fences if present."""
    text = text.strip()
    if text.startswith("```"):
        text = text[3:]
        if text.startswith("json"):
            text = text[4:]
    if text.endswith("```"):
        text = text[:-3]
    return text.strip()


# ─── Per-model runner ──────────────────────────────────────────────────────

def run_model(model: str, system_prompt: str, api_key: str | None = None) -> dict:
    """Run the 5-turn Dana script against one model. Returns full result dict."""
    print(f"\n=== {model} ===")
    messages: list[dict] = []
    turn_results: list[dict] = []

    for spec in DANA_SCRIPT_PAID:
        turn_idx = spec["turn"]
        user_msg = spec["user"]
        criteria = spec["criteria"]
        print(f"  Turn {turn_idx}: {user_msg[:60]}...")

        messages.append({"role": "user", "content": user_msg})

        try:
            response = anthropic_call(model, system_prompt, messages, api_key=api_key)
        except Exception as e:
            response = ""
            print(f"    ERROR: {e}")

        # Cross-turn MOS-leak guardrail
        try:
            mos_result = check_mos_leak(user_msg, response)
            mos_verdict = mos_result.verdict
            mos_matched = list(mos_result.matched_tokens)
        except Exception as e:
            mos_verdict = "GUARDRAIL_RUN_ERROR"
            mos_matched = [f"exception: {e}"]

        # Per-criterion judge call
        if response:
            verdicts = judge_turn(response, criteria, api_key=api_key)
        else:
            verdicts = [
                {"index": i, "verdict": "FAIL", "reason": "empty_response"}
                for i in range(len(criteria))
            ]

        # Inject MOS-leak verdict as a synthetic criterion (index = -1)
        if mos_verdict == "BLOCK":
            verdicts.append(
                {
                    "index": -1,
                    "verdict": "FAIL",
                    "reason": f"MOS_LEAK matched={mos_matched}",
                }
            )
        elif mos_verdict == "GUARDRAIL_RUN_ERROR":
            verdicts.append(
                {"index": -1, "verdict": "FAIL", "reason": f"GUARDRAIL_ERROR {mos_matched}"}
            )

        turn_overall = (
            "PASS"
            if all(v.get("verdict") == "PASS" for v in verdicts)
            else "FAIL"
        )
        turn_results.append(
            {
                "turn": turn_idx,
                "user": user_msg,
                "response": response,
                "verdicts": verdicts,
                "mos_leak_check": {
                    "verdict": mos_verdict,
                    "matched": mos_matched,
                },
                "overall": turn_overall,
            }
        )
        messages.append({"role": "assistant", "content": response})
        print(f"    {turn_overall}")

    overall = "PASS" if all(t["overall"] == "PASS" for t in turn_results) else "FAIL"
    return {
        "model": model,
        "overall": overall,
        "turns": turn_results,
    }


# ─── Baseline diff ─────────────────────────────────────────────────────────

def baseline_compare(current: dict) -> tuple[bool, list[str]]:
    """Compare current run vs saved baseline. Returns (clean, regression_lines)."""
    if not BASELINE_PATH.exists():
        return (False, ["no baseline saved yet — run with --baseline to seal one"])

    baseline = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
    regressions: list[str] = []
    base_models = {m["model"]: m for m in baseline.get("models", [])}
    for cur in current.get("models", []):
        model = cur["model"]
        base = base_models.get(model)
        if not base:
            regressions.append(f"{model}: not in baseline")
            continue
        cur_pass = sum(1 for t in cur["turns"] if t["overall"] == "PASS")
        base_pass = sum(1 for t in base["turns"] if t["overall"] == "PASS")
        if cur_pass < base_pass:
            regressions.append(
                f"{model}: PASS count regressed {base_pass} → {cur_pass}"
            )
    return (len(regressions) == 0, regressions)


# ─── Main ──────────────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default=None, help="run one model only")
    parser.add_argument("--baseline", action="store_true", help="save run as new baseline")
    parser.add_argument("--compare-baseline", action="store_true")
    args = parser.parse_args()

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not set")
        return 1

    models = [args.model] if args.model else DEFAULT_MODELS
    print(f"Assembling paid Kit system prompt...")
    system_prompt = assemble_paid_kit_system_prompt()
    print(f"  Total chars: {len(system_prompt)}")

    RESULTS_DIR.mkdir(exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_path = RESULTS_DIR / f"dana-smoke-paid-kit-{timestamp}.json"

    model_results = [run_model(m, system_prompt, api_key=api_key) for m in models]

    run_dict = {
        "timestamp": timestamp,
        "variant": "paid-ship-it-kit",
        "models": model_results,
    }
    out_path.write_text(json.dumps(run_dict, indent=2), encoding="utf-8")
    print(f"\nSaved → {out_path}")

    if args.baseline:
        BASELINE_PATH.write_text(json.dumps(run_dict, indent=2), encoding="utf-8")
        print(f"Baseline saved → {BASELINE_PATH}")

    if args.compare_baseline:
        clean, regressions = baseline_compare(run_dict)
        if clean:
            print("\nNo regressions vs baseline.")
            return 0
        print("\nREGRESSIONS vs baseline:")
        for r in regressions:
            print(f"  - {r}")
        return 1

    # Default: exit 0 if all turns PASS, 1 otherwise
    if all(m["overall"] == "PASS" for m in model_results):
        print("\nAll models PASS.")
        return 0
    print("\nFAILED — check results JSON for details.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
