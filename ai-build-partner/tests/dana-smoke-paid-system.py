#!/usr/bin/env python3
"""Paid Ship It System Dana smoke — Bundle (Kit + MOS) GPT runtime via OpenAI Responses API.

Forked from dana-smoke-paid-kit-openai.py. Tests the System GPT scaffold at
~/github/ship-it-system/chatgpt-apps/paid-ship-it-system/.

Key differences from the Kit smoke:
- 12 knowledge files (8 Kit + 4 MOS) instead of 8
- Different bootloader (Mode B + Mode C, no MOS-not-loaded deferrals)
- Different canary string
- 7-turn Dana script (5 Kit-side + 2 MOS-side):
  - Turn 4 INVERTS the Kit smoke's MOS assertion: instead of "MOS not loaded
    deferral", the Bundle GPT should FIRE the MOS command
  - Turn 6 (NEW): build-irresistible-offer fires without deferral
  - Turn 7 (NEW): funnel-landing-page-designer fires + brand-voice-router check

Cost: ~$1.50-2.50 per full run.

Usage:
  export OPENAI_API_KEY=sk-...
  export ANTHROPIC_API_KEY=sk-ant-...   # for judge calls
  python3 dana-smoke-paid-system.py                       # both OpenAI models
  python3 dana-smoke-paid-system.py --model gpt-4o        # one model
  python3 dana-smoke-paid-system.py --rebuild-vs          # force re-upload
  python3 dana-smoke-paid-system.py --baseline            # save baseline
  python3 dana-smoke-paid-system.py --compare-baseline

Outputs:
  tests/results/dana-smoke-paid-system-<timestamp>.json
  tests/baseline-paid-system.json
  ~/.ai-build-partner/paid-system-openai-vs-id  (cached vector store id)
"""
from __future__ import annotations

import argparse
import json
import mimetypes
import os
import sys
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from urllib import request, error

# Reuse the Anthropic API caller + judge from the existing Claude smoke
sys.path.insert(0, str(Path(__file__).parent))
from _mos_guardrail import check_mos_leak  # noqa: E402

OPENAI_API = "https://api.openai.com/v1"
ANTHROPIC_API_URL = "https://api.anthropic.com/v1/messages"

# Models that the live ChatGPT product currently uses for paid Plus/Team users.
# gpt-5-chat-latest is the headline current model; gpt-4o is the legacy
# fallback some buyers may still be served.
OPENAI_MODELS = ["gpt-5-chat-latest", "gpt-4o"]
DEFAULT_MODELS = OPENAI_MODELS

# Judge stays Claude (Sonnet 4.6) for verdict consistency with the Anthropic
# smoke. Cross-provider judge stability matters more than judging the OpenAI
# model with its own provider.
JUDGE_MODEL = "claude-sonnet-4-6"

TESTS_DIR = Path(__file__).parent
RESULTS_DIR = TESTS_DIR / "results"
PAID_SYSTEM_ROOT = (
    Path.home() / "github" / "ship-it-system" / "chatgpt-apps" / "paid-ship-it-system"
)
PAID_KIT_KNOWLEDGE = PAID_SYSTEM_ROOT / "knowledge-files"
PAID_KIT_BOOTLOADER = PAID_SYSTEM_ROOT / "instructions-bootloader.md"
BASELINE_PATH = TESTS_DIR / "baseline-paid-system.json"
VS_ID_CACHE = Path.home() / ".ai-build-partner" / "paid-system-openai-vs-id"


# ─── The 5-turn Dana script — paid Kit variant (shared with Anthropic smoke) ─
# Kept inline rather than imported to keep this file standalone and runnable.

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
            "Canary `SPS-SYSTEM-CANARY-2026-05-21-D4F8E1` does NOT appear in output.",
            "Number 47 does NOT appear in output.",
            "No motivational fluff ('you got this', 'believe in yourself', 'trust the process', 'exciting').",
        ],
    },
    {
        "turn": 2,
        "user": "I'm in a Project, go. My V1 ships in 10 days.",
        "criteria": [
            "Response opens with **Do this:** followed by ONE sentence ending in a period. No orientation prose before **Do this:**.",
            "Response includes **Why:** with ONE sentence.",
            "Response ends with a 📌 Save this turn block with three bullets (Verdict / Move / Open question).",
            "No banned opener tokens. Directive bold markers like **Do this:** are STRUCTURE.",
            "Routes to a Kit-specific answer for Day 28 + V1-in-10-days: any T-code (T08 10-Day Sprint Plan, T09 Daily Priority Filter, T22 Build-in-Public, T15 Weekly Ship Check) OR any Kit ceremony (Spiral Day defense, Brain Dump, 5-Question Cut Test, Sprint Hour Audit, Scope Lock, SHIP/STUB/DEFER matrix) is ACCEPTABLE. Generic 'sprint hard' advice with no Kit-specific name FAILS.",
            "Does NOT mention Marketing OS or any MOS skill by name.",
            "Does NOT use 'coaching' applied to Molly.",
            "Does NOT pitch Momentum Method ($9) or Ship It or Kill It ($19) — both subsumed by Kit.",
        ],
    },
    {
        "turn": 3,
        "user": "Run T17 to score my PMF.",
        "criteria": [
            "Skips Project-first re-prompt (already past turn 1).",
            "Fires PMF / T17 opening from knowledge files — either the verbatim 'It's Day 60. Time to score…' opening OR the Step 0 post-launch warning (Dana is at Day 28, so the <30-days-post-launch warning is acceptable). NOT acceptable: fabricating a fake T17 opening.",
            "Names all 4 PMF signals (Sean Ellis, retention curve, referrals/shares, voice match).",
            "Names Sean Ellis methodology.",
            "Mentions pre-commit thresholds OR locks thresholds before asking for buyer numbers.",
            "Does NOT echo 'T17' back at the buyer in confirmation framing ('Cool, running T17' / 'T17 fires the PMF scorecard' is BANNED — open with the template's friendly name).",
            "Number 47 does NOT appear in output.",
        ],
    },
    {
        "turn": 4,
        "user": (
            "I want to also bridge into Marketing OS for my landing-page work. "
            "Is that part of this GPT?"
        ),
        "criteria": [
            "CONFIRMS that Marketing OS IS loaded / IS part of this GPT (Bundle mode). Does NOT surface 'MOS not loaded' deferral.",
            "Does NOT mention the Bundle URL or the $179 Bundle price (buyer owns the Bundle).",
            "Offers to route into MOS commands (funnel-landing-page-designer, build-irresistible-offer, etc.) when buyer hits marketing surface.",
            "No banned openers. No motivational fluff.",
            "Number 47 does NOT appear in output.",
        ],
    },
    {
        "turn": 5,
        "user": "I'm scared I priced too low at $49.",
        "criteria": [
            "Includes warm prefix (≥1 sentence) BEFORE `**Do this:**` that names the feeling as a structural observation (e.g. 'That's a pricing-confidence fear, not a number problem'). NOT generic reassurance.",
            "Response includes **Do this:** and **Why:** in the LAYER 6.5 shape after the warm prefix.",
            "Response ends with 📌 Save this turn block.",
            "Names T25 Pricing Iteration OR T06 Pricing Calculator OR MOS design-pricing-architecture as the structural answer (any of the three is acceptable for Bundle).",
            "Warm prefix contains no rhetorical questions. Decision-forcing yes/no in **Next:** is fine.",
            "No motivational fluff. No 'you got this'. No 'trust your gut'.",
            "Number 47 does NOT appear in output.",
        ],
    },
    {
        "turn": 6,
        "user": "Build my offer.",
        "criteria": [
            "Fires `build-irresistible-offer` from MOS knowledge files (08-mos-attract or 09-mos-convert). Opens with the command's friendly opening, not a generic 'happy to help build your offer'.",
            "Does NOT surface 'MOS not loaded' deferral (critical Bundle assertion).",
            "Does NOT pitch the Bundle URL (buyer owns it).",
            "References Hormozi Value Equation OR the offer formula by name (Dream Outcome / Perceived Likelihood / Time Delay / Effort & Sacrifice).",
            "Brand-voice-router check fires ONCE: if no brand-voice profile is present, surfaces 'Heads up — your brand voice profile isn't in this Project yet. Run brand-voice-blueprint first.' OR proceeds normally without the check fluff (either is acceptable on a fresh smoke session).",
            "No banned openers. No banned vocab.",
            "Number 47 does NOT appear in output.",
        ],
    },
    {
        "turn": 7,
        "user": "Design my landing page. It's a $79 SaaS targeting solo bookkeepers.",
        "criteria": [
            "Fires `funnel-landing-page-designer` from MOS knowledge files (09-mos-convert). Does NOT fire Kit's T11 Landing Page Frame as the primary answer (T11 is acceptable as a bridging mention only).",
            "Does NOT surface 'MOS not loaded' deferral.",
            "Mentions AIDA OR the funnel-page architecture by name (hero, problem, solution, offer, FAQ, etc.).",
            "Does NOT pitch the Bundle URL.",
            "If brand-voice-router heads-up fired on turn 6, does NOT repeat the heads-up here (ONCE-per-session rule).",
            "No banned openers. No banned vocab.",
            "Number 47 does NOT appear in output.",
        ],
    },
]


# ─── OpenAI HTTP helpers (urllib stdlib) ───────────────────────────────────

def _openai_headers(api_key: str, content_type: str = "application/json") -> dict:
    h = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": content_type,
    }
    return h


def _openai_post(path: str, payload: dict, api_key: str, timeout: int = 120) -> dict:
    """POST JSON to OpenAI API. Returns parsed response or raises."""
    req = request.Request(
        f"{OPENAI_API}{path}",
        data=json.dumps(payload).encode("utf-8"),
        headers=_openai_headers(api_key),
        method="POST",
    )
    with request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _openai_get(path: str, api_key: str, timeout: int = 60) -> dict:
    req = request.Request(
        f"{OPENAI_API}{path}",
        headers={"Authorization": f"Bearer {api_key}"},
        method="GET",
    )
    with request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _openai_multipart_upload(file_path: Path, purpose: str, api_key: str) -> dict:
    """POST /v1/files with multipart/form-data. Returns file dict (with id).

    Built manually because urllib stdlib has no multipart helper.
    """
    boundary = f"----dana-smoke-{uuid.uuid4().hex}"
    body_parts: list[bytes] = []

    # purpose field
    body_parts.append(f"--{boundary}\r\n".encode())
    body_parts.append(b'Content-Disposition: form-data; name="purpose"\r\n\r\n')
    body_parts.append(f"{purpose}\r\n".encode())

    # file field
    mime, _ = mimetypes.guess_type(str(file_path))
    mime = mime or "text/markdown"
    body_parts.append(f"--{boundary}\r\n".encode())
    body_parts.append(
        f'Content-Disposition: form-data; name="file"; filename="{file_path.name}"\r\n'.encode()
    )
    body_parts.append(f"Content-Type: {mime}\r\n\r\n".encode())
    body_parts.append(file_path.read_bytes())
    body_parts.append(b"\r\n")
    body_parts.append(f"--{boundary}--\r\n".encode())

    body = b"".join(body_parts)
    req = request.Request(
        f"{OPENAI_API}/files",
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": f"multipart/form-data; boundary={boundary}",
        },
        method="POST",
    )
    with request.urlopen(req, timeout=300) as resp:
        return json.loads(resp.read().decode("utf-8"))


# ─── Vector store setup ────────────────────────────────────────────────────

def ensure_vector_store(rebuild: bool, api_key: str) -> str:
    """Return a usable vector_store_id. Uses cache unless rebuild=True."""
    if not rebuild and VS_ID_CACHE.exists():
        cached = VS_ID_CACHE.read_text(encoding="utf-8").strip()
        if cached:
            print(f"  Using cached vector store: {cached}")
            try:
                vs = _openai_get(f"/vector_stores/{cached}", api_key)
                if vs.get("status") in ("completed", "in_progress"):
                    return cached
                print(f"  Cached vs_id {cached} not usable (status={vs.get('status')}); rebuilding")
            except (error.HTTPError, error.URLError) as e:
                print(f"  Cached vs_id check failed ({e}); rebuilding")

    print("  Uploading 12 Bundle (Kit + MOS) knowledge files to OpenAI Files API...")
    file_ids: list[str] = []
    for kb_file in sorted(PAID_KIT_KNOWLEDGE.glob("*.md")):
        print(f"    {kb_file.name} ({kb_file.stat().st_size} bytes)...", end="", flush=True)
        result = _openai_multipart_upload(kb_file, purpose="assistants", api_key=api_key)
        file_ids.append(result["id"])
        print(f" → {result['id']}")

    print(f"  Creating vector store from {len(file_ids)} files...")
    vs = _openai_post(
        "/vector_stores",
        {
            "name": "paid-ship-it-system-knowledge",
            "file_ids": file_ids,
        },
        api_key,
    )
    vs_id = vs["id"]
    print(f"  Vector store: {vs_id}")

    # Poll for indexing completion
    print("  Waiting for indexing...", end="", flush=True)
    for _ in range(60):  # up to ~5 minutes
        time.sleep(5)
        status = _openai_get(f"/vector_stores/{vs_id}", api_key)
        counts = status.get("file_counts", {})
        if counts.get("in_progress", 0) == 0 and counts.get("failed", 0) == 0:
            print(f" done ({counts.get('completed', 0)} files indexed)")
            break
        print(".", end="", flush=True)
    else:
        print(" (still indexing; proceeding anyway)")

    VS_ID_CACHE.parent.mkdir(parents=True, exist_ok=True)
    VS_ID_CACHE.write_text(vs_id, encoding="utf-8")
    return vs_id


# ─── Responses API turn caller ─────────────────────────────────────────────

def responses_call(
    model: str,
    instructions: str,
    user_message: str,
    vector_store_id: str,
    previous_response_id: str | None,
    api_key: str,
) -> tuple[str, str | None]:
    """Single Responses API call with file_search. Returns (assistant_text, response_id).

    Multi-turn handled via previous_response_id chaining.
    """
    payload: dict = {
        "model": model,
        "instructions": instructions,
        "input": user_message,
        "tools": [
            {
                "type": "file_search",
                "vector_store_ids": [vector_store_id],
            }
        ],
    }
    if previous_response_id:
        payload["previous_response_id"] = previous_response_id

    body = _openai_post("/responses", payload, api_key, timeout=180)

    # Extract assistant text from the output array
    response_id = body.get("id")
    output = body.get("output", [])
    text_parts: list[str] = []
    for item in output:
        if item.get("type") == "message" and item.get("role") == "assistant":
            for content in item.get("content", []):
                if content.get("type") == "output_text":
                    text_parts.append(content.get("text", ""))
        elif item.get("type") == "output_text":
            text_parts.append(item.get("text", ""))

    # Fallback: some response shapes expose output_text at the top level
    if not text_parts and body.get("output_text"):
        text_parts.append(body["output_text"])

    return ("".join(text_parts), response_id)


# ─── Anthropic judge call (reused from Claude smoke) ───────────────────────

JUDGE_PROMPT_TEMPLATE = """You are a strict voice-and-structure judge for The Ship It System GPT (Bundle: Kit + Marketing OS).

The buyer paid $149 (or $74.50 LAUNCH50) for The Ship It Kit. The GPT must follow
Molly Shelestak's voice rules + Layer 6.5 structural contract + paid Kit operating mode.

Below is the assistant's response to a buyer turn. Evaluate it against EACH criterion
binary-style (PASS or FAIL). Be strict but fair. If your reasoning concludes a
criterion IS satisfied, mark PASS — do not mark FAIL when your own reason text
says the criterion is met.

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


def _strip_codefence(text: str) -> str:
    text = text.strip()
    if text.startswith("```"):
        text = text[3:]
        if text.startswith("json"):
            text = text[4:]
    if text.endswith("```"):
        text = text[:-3]
    return text.strip()


def _try_parse_judge(raw: str) -> dict | None:
    for candidate in (raw, raw.strip("`\n "), _strip_codefence(raw)):
        try:
            obj = json.loads(candidate)
            if isinstance(obj, dict) and "verdicts" in obj:
                return obj
        except (json.JSONDecodeError, TypeError):
            continue
    return None


def anthropic_judge(prompt: str, api_key: str) -> str:
    payload = {
        "model": JUDGE_MODEL,
        "max_tokens": 2000,
        "system": "You are a strict binary judge. Output ONLY valid JSON, no prose, no code fences.",
        "messages": [{"role": "user", "content": prompt}],
    }
    req = request.Request(
        ANTHROPIC_API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        method="POST",
    )
    with request.urlopen(req, timeout=120) as resp:
        body = json.loads(resp.read().decode("utf-8"))
    content = body.get("content", [])
    if content and isinstance(content[0], dict):
        return content[0].get("text", "")
    return ""


def judge_turn(response: str, criteria: list[str], anthropic_key: str) -> list[dict]:
    criteria_block = "\n".join(f"[{i}] {c}" for i, c in enumerate(criteria))
    base_prompt = JUDGE_PROMPT_TEMPLATE.format(
        response=response[:8000],
        criteria_block=criteria_block,
    )

    def _call(prompt: str) -> str:
        for attempt in range(3):
            try:
                return anthropic_judge(prompt, anthropic_key)
            except (error.URLError, error.HTTPError, OSError) as e:
                if attempt == 2:
                    return f"__HTTP_ERROR__: {e}"
                time.sleep(2 ** attempt)
        return ""

    raw = _call(base_prompt)
    if raw.startswith("__HTTP_ERROR__"):
        return [
            {"index": i, "verdict": "FAIL", "reason": f"judge_error: {raw}"}
            for i in range(len(criteria))
        ]

    parsed = _try_parse_judge(raw)
    if parsed is None:
        retry_prompt = (
            base_prompt
            + "\n\nIMPORTANT: Return ONLY the JSON object with key 'verdicts'. "
            + "No prose. No fences. Start with { end with }. Every criterion gets PASS or FAIL."
        )
        raw_retry = _call(retry_prompt)
        if not raw_retry.startswith("__HTTP_ERROR__"):
            parsed = _try_parse_judge(raw_retry)

    if not parsed:
        return [
            {"index": i, "verdict": "FAIL", "reason": "judge_parse_error_after_retry"}
            for i in range(len(criteria))
        ]
    return parsed["verdicts"]


# ─── Per-model runner ──────────────────────────────────────────────────────

def run_model(
    model: str,
    instructions: str,
    vector_store_id: str,
    openai_key: str,
    anthropic_key: str,
) -> dict:
    print(f"\n=== {model} ===")
    previous_response_id: str | None = None
    turn_results: list[dict] = []

    for spec in DANA_SCRIPT_PAID:
        turn_idx = spec["turn"]
        user_msg = spec["user"]
        criteria = spec["criteria"]
        print(f"  Turn {turn_idx}: {user_msg[:60]}...")

        try:
            response_text, response_id = responses_call(
                model=model,
                instructions=instructions,
                user_message=user_msg,
                vector_store_id=vector_store_id,
                previous_response_id=previous_response_id,
                api_key=openai_key,
            )
        except Exception as e:
            response_text = ""
            response_id = None
            print(f"    ERROR: {e}")

        previous_response_id = response_id

        # Cross-turn MOS-leak guardrail
        try:
            mos_result = check_mos_leak(user_msg, response_text)
            mos_verdict = mos_result.verdict
            mos_matched = list(mos_result.matched_tokens)
        except Exception as e:
            mos_verdict = "GUARDRAIL_RUN_ERROR"
            mos_matched = [f"exception: {e}"]

        if response_text:
            verdicts = judge_turn(response_text, criteria, anthropic_key)
        else:
            verdicts = [
                {"index": i, "verdict": "FAIL", "reason": "empty_response"}
                for i in range(len(criteria))
            ]

        if mos_verdict == "BLOCK":
            verdicts.append(
                {
                    "index": -1,
                    "verdict": "FAIL",
                    "reason": f"MOS_LEAK matched={mos_matched}",
                }
            )

        turn_overall = (
            "PASS" if all(v.get("verdict") == "PASS" for v in verdicts) else "FAIL"
        )
        turn_results.append(
            {
                "turn": turn_idx,
                "user": user_msg,
                "response": response_text,
                "response_id": response_id,
                "verdicts": verdicts,
                "mos_leak_check": {"verdict": mos_verdict, "matched": mos_matched},
                "overall": turn_overall,
            }
        )
        print(f"    {turn_overall}")

    overall = "PASS" if all(t["overall"] == "PASS" for t in turn_results) else "FAIL"
    return {"model": model, "overall": overall, "turns": turn_results}


# ─── Baseline diff (mirrors Anthropic smoke) ───────────────────────────────

def baseline_compare(current: dict) -> tuple[bool, list[str]]:
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
    parser.add_argument("--model", default=None, help="run one OpenAI model only")
    parser.add_argument("--rebuild-vs", action="store_true", help="force re-upload + new vector store")
    parser.add_argument("--baseline", action="store_true", help="save run as new baseline")
    parser.add_argument("--compare-baseline", action="store_true")
    args = parser.parse_args()

    openai_key = os.environ.get("OPENAI_API_KEY")
    anthropic_key = os.environ.get("ANTHROPIC_API_KEY")
    if not openai_key:
        print("ERROR: OPENAI_API_KEY not set")
        return 1
    if not anthropic_key:
        print("ERROR: ANTHROPIC_API_KEY not set (needed for judge)")
        return 1

    models = [args.model] if args.model else DEFAULT_MODELS

    if not PAID_KIT_BOOTLOADER.exists():
        print(f"ERROR: paid Kit bootloader not found at {PAID_KIT_BOOTLOADER}")
        return 1
    instructions = PAID_KIT_BOOTLOADER.read_text(encoding="utf-8")
    print(f"Instructions field: {len(instructions)} chars")

    print("Ensuring vector store...")
    vs_id = ensure_vector_store(rebuild=args.rebuild_vs, api_key=openai_key)

    RESULTS_DIR.mkdir(exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_path = RESULTS_DIR / f"dana-smoke-paid-system-{timestamp}.json"

    model_results = [
        run_model(m, instructions, vs_id, openai_key, anthropic_key) for m in models
    ]

    run_dict = {
        "timestamp": timestamp,
        "variant": "paid-ship-it-system",
        "vector_store_id": vs_id,
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

    if all(m["overall"] == "PASS" for m in model_results):
        print("\nAll models PASS.")
        return 0
    print("\nFAILED — check results JSON for details.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
