#!/usr/bin/env python3
"""
Dana smoke test — voice regression detector for the free AI Build Partner skill.

Runs a fixed 5-message conversation against TWO models in parallel:
- claude-opus-4-7  (1M context flagship; expected default for paid buyers)
- claude-sonnet-4-6 (cheaper / tighter; expected for most free buyers)

After each model turn, a judge call (Claude Sonnet 4.6) evaluates the
response against a per-turn rubric. Output is JSON with per-model
pass/fail per criterion, plus a divergence report (where one model passes
and the other fails).

Usage:
  export ANTHROPIC_API_KEY=sk-ant-...
  python3 dana-smoke.py                                # both models, full run
  python3 dana-smoke.py --model claude-sonnet-4-6      # one model
  python3 dana-smoke.py --baseline                     # save as new baseline
  python3 dana-smoke.py --compare-baseline             # diff vs saved baseline

Outputs:
  tests/results/dana-smoke-<timestamp>.json   # full transcript + verdicts
  tests/baseline.json                          # most recent saved baseline
"""

from __future__ import annotations
import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib import request, error

API_URL = "https://api.anthropic.com/v1/messages"
DEFAULT_MODELS = ["claude-opus-4-7", "claude-sonnet-4-6"]
JUDGE_MODEL = "claude-sonnet-4-6"
TESTS_DIR = Path(__file__).parent
SKILL_ROOT = TESTS_DIR.parent
RESULTS_DIR = TESTS_DIR / "results"

# ─── The 5-turn Dana script ────────────────────────────────────────────────
# Each turn has the user message + a list of binary pass/fail criteria.
# Criteria are written so a judge model can answer YES/NO with confidence.

DANA_SCRIPT = [
    {
        "turn": 1,
        "user": (
            "I've been wanting to ship a 1:1s guide for senior PMs. I have like "
            "4 years of notes. Where do I start?"
        ),
        "criteria": [
            "Project-first prompt fires verbatim or near-verbatim (mentions Claude.ai Project + 30 seconds to set up + sidebar/Projects path).",
            "Response ends after the Project-first prompt — does NOT continue into substantive build advice on the same turn.",
            "No 'Let me' / 'I'll' / 'Now I'll' / 'First,' / 'Read' / 'Reading' / 'Heading into' / 'Diving into' opening tokens in the first sentence.",
            "No in-character check leak (e.g. 'Build Partner active in Standalone mode' / 'Framework: ...' / 'Banned word avoided: ...').",
            "No motivational fluff ('you've got this', 'believe in yourself', etc.).",
        ],
    },
    {
        "turn": 2,
        "user": "I'm in a Project, go",
        "criteria": [
            "Response opens with **Do this:** followed by a one-sentence action.",
            "Response includes **Why:** with ONE sentence (not a paragraph).",
            "Response ends with a 📌 Save this turn block with three bullets (Verdict / Move / Open question).",
            "No banned opener tokens (Let me / I'll / Now / First / Read). NOTE: directive bold markers like **Do this:** and **Why:** are REQUIRED structure per LAYER 6.5 and DO NOT count as banned openers. Banned openers are conversational prefixes only ('Let me', 'I'll', 'Now I'll', 'First,', 'Read', 'Reading', 'Heading into', 'Diving into', 'Sure,', 'Great,').",
            "Does NOT preach motivation — reframe is structural, not 'you can do this'.",
            "Does NOT use the word 'coaching' anywhere (brand rule: it's a 'build partnership').",
        ],
    },
    {
        "turn": 3,
        "user": "I'm scared no one will actually read it",
        "criteria": [
            "Response uses warm register (second-person, present-tense, bodily detail OK) since this is an emotional moment.",
            "Response includes **Do this:** and **Why:** in the LAYER 6.5 short shape.",
            "Response ends with 📌 Save this turn block.",
            "Reframes the fear structurally (not 'don't worry' / 'most people feel that way'). The reframe should translate a personal flaw into a system observation.",
            "No banned opener tokens in the first sentence. NOTE: directive bold markers like **Do this:** and **Why:** are REQUIRED structure per LAYER 6.5 and DO NOT count as banned openers. Banned openers are conversational prefixes only ('Let me', 'I'll', 'Now I'll', 'First,', 'Read', 'Reading', 'Heading into', 'Diving into').",
            "Does NOT use rhetorical questions. A rhetorical question is one phrased as a question but not literally expecting an answer in context — e.g. 'How can you expect to ship if...?', 'Which one is louder right now?', 'What does your gut tell you?', 'Wouldn't you rather have it done than perfect?'. Direct decision-forcing questions ('Pick one.', 'Which feature are you cutting first?', 'Distribution or validation — which fear?') are NOT rhetorical and PASS. EXCLUSION: the template line 'Want the full breakdown?' (and 'Want me to go deeper?') is a REQUIRED LAYER 6.5 meta-prompt that explicitly tells the user how to answer — it is NOT a rhetorical question for the purposes of this criterion. Same for the final 'Anything else?' offer.",
        ],
    },
    {
        "turn": 4,
        "user": "what if I spiral Saturday morning?",
        "criteria": [
            "Response includes **Do this:** with a concrete action (not abstract advice).",
            "Response includes a 'spiral has a tell' or 'spiral defense' moment — something tactical the buyer can recognize.",
            "Response ends with 📌 Save this turn block.",
            "No banned opener tokens. NOTE: directive bold markers like **Do this:** and **Why:** are REQUIRED structure per LAYER 6.5 and DO NOT count as banned openers. Banned openers are conversational prefixes only ('Let me', 'I'll', 'Now I'll', 'First,', 'Read', 'Reading', 'Heading into', 'Diving into').",
            "Does NOT name Notion, Google Drive, Dropbox, Obsidian, OneNote, Evernote, or Coda by name as a save location. Saving as a `.md` file (e.g. `1on1s-guide-notes.md`) in Claude.ai Project knowledge is the CORRECT pattern and PASSES this check — Claude.ai Project knowledge is the assumed default save location.",
        ],
    },
    {
        "turn": 5,
        "user": "/unstuck scope",
        "criteria": [
            # B3: accept either (a) Scope module open (any opening that fires scope work — Guillotine naming OR JTBD framing OR Step-1-of-scope question OR brain-dump prompt — all map to the scope module's documented Step-1 patterns) OR (b) coherent redirect to a prerequisite module (validate, discovery, decide) that names the specific missing input.
            "Routes the turn coherently for the /unstuck scope command: EITHER (a) opens the scope module flow (any of: mentions Scope Guillotine; opens JTBD-framing question 'When [situation], reader wants to [motivation], so they can [outcome]'; asks a Step-1-of-scope question like 'what's the one job'; opens a brain-dump prompt to cut features), OR (b) redirects to a prerequisite module (/unstuck validate, /unstuck discovery, /unstuck decide) AND names the specific missing input (e.g. 'no validation scorecard', 'no decided shape', 'project not picked yet'). A generic 'do something else first' redirect without naming what's missing FAILS.",
            "If branch (a): explicitly names scope, in/out, the Guillotine, JTBD, or 'the one job' — any opener that signals scope-cutting is the work right now. If branch (b): explicitly names the missing input by name (validation scorecard, decided shape, locked format, T04, project shape, etc.) rather than vague 'we should validate first' / 'we should discover first'.",
            "If branch (a): offers the three exits (hint / guide me / draft it) OR equivalent labels (e.g. 'Draft it' / 'I have one' / 'Guide me through it' — semantic equivalents pass). If branch (b): offers a clear next step with at least one explicit option AND an override path. A redirect with no override path is acceptable if the missing input is hard-blocking; ambiguous or no-next-step FAILS.",
            "Asks ONE primary question (Step 1 of scope for branch a, or 'run the prerequisite or override?' for branch b), not three+ simultaneous questions on different axes. Sub-questions clarifying the SAME single decision are OK. Stacking unrelated questions (e.g. 'which spiral trigger?' + 'which format?' + 'run free scope?') FAILS.",
            "No banned opener tokens. NOTE: directive bold markers like **Do this:** and **Why:** are REQUIRED structure per LAYER 6.5 and DO NOT count as banned openers. Banned openers are conversational prefixes only ('Let me', 'I'll', 'Now I'll', 'First,', 'Read', 'Reading', 'Heading into', 'Diving into').",
        ],
    },
]


# ─── Build system prompt from skill bundle ─────────────────────────────────

def build_system_prompt() -> str:
    """Concatenate SKILL.md + kit-files/* + references/* into the system prompt
    Claude.ai would construct from the installed skill bundle.
    """
    parts = []

    skill_md = SKILL_ROOT / "SKILL.md"
    parts.append(f"<!-- SKILL.md -->\n{skill_md.read_text()}\n")

    kit_files = sorted((SKILL_ROOT / "kit-files").glob("*.md"))
    for f in kit_files:
        parts.append(f"<!-- kit-files/{f.name} -->\n{f.read_text()}\n")

    refs_dir = SKILL_ROOT / "references"
    if refs_dir.exists():
        for f in sorted(refs_dir.glob("*.md")):
            parts.append(f"<!-- references/{f.name} -->\n{f.read_text()}\n")

    return "\n".join(parts)


# ─── API call ───────────────────────────────────────────────────────────────

def call_anthropic(model: str, system: str, messages: list[dict], max_tokens: int = 2048) -> str:
    """Call Anthropic Messages API. Returns assistant text."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise SystemExit("ANTHROPIC_API_KEY not set in env. Export it before running.")

    payload = {
        "model": model,
        "max_tokens": max_tokens,
        "system": system,
        "messages": messages,
    }
    req = request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
        },
        method="POST",
    )
    try:
        with request.urlopen(req, timeout=90) as resp:
            body = json.loads(resp.read().decode("utf-8"))
    except error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        raise SystemExit(f"Anthropic API HTTP {e.code}: {err_body}")
    except error.URLError as e:
        raise SystemExit(f"Anthropic API network error: {e.reason}")

    if "content" not in body or not body["content"]:
        raise SystemExit(f"Anthropic API returned no content: {json.dumps(body)[:500]}")
    return "".join(block.get("text", "") for block in body["content"] if block.get("type") == "text")


# ─── Judge ──────────────────────────────────────────────────────────────────

JUDGE_SYSTEM = (
    "You are a rigorous binary judge evaluating AI Build Partner responses against "
    "voice/structural rules. For each criterion you answer ONLY 'PASS' or 'FAIL', "
    "followed by a one-sentence reason citing the specific text. Be strict — if a "
    "criterion is partially satisfied or ambiguous, FAIL it. Output ONLY valid JSON, "
    "no prose around it, in this exact shape:\n"
    '{"verdicts": [{"criterion": "...", "verdict": "PASS|FAIL", "reason": "..."}, ...]}'
)

JUDGE_SYSTEM_STRICT = (
    "RETURN ONLY VALID JSON. NO PROSE BEFORE OR AFTER. NO CODE FENCES. JUST THE JSON OBJECT.\n\n"
    + JUDGE_SYSTEM
)


def _strip_fences_and_parse(raw: str) -> list[dict] | None:
    """Strip ```json fences, extract first {...} substring, attempt parse.
    Returns verdicts list on success, None on failure (including valid JSON
    that lacks a non-empty `verdicts` list — triggers retry instead of
    silently scoring the turn as zero criteria).
    Reference pattern: feedback_haiku_drift_strip_fences.md.
    """
    s = raw.strip()
    if s.startswith("```"):
        s = s.split("```", 2)[1]
        if s.startswith("json"):
            s = s[4:]
        s = s.strip()
    if s.endswith("```"):
        s = s[:-3].strip()

    def _extract(obj: Any) -> list[dict] | None:
        if not isinstance(obj, dict):
            return None
        v = obj.get("verdicts")
        if isinstance(v, list) and len(v) > 0:
            return v
        return None

    # Try direct parse
    try:
        result = _extract(json.loads(s))
        if result is not None:
            return result
    except json.JSONDecodeError:
        pass

    # Fallback: extract first '{' to last '}' substring
    first = s.find("{")
    last = s.rfind("}")
    if first >= 0 and last > first:
        try:
            result = _extract(json.loads(s[first:last + 1]))
            if result is not None:
                return result
        except json.JSONDecodeError:
            pass

    return None


def judge_response(user_msg: str, assistant_response: str, criteria: list[str]) -> list[dict]:
    """Call the judge model to evaluate the response against criteria.

    On JSONDecodeError: retry ONCE with a stricter system prompt prepending
    'RETURN ONLY VALID JSON…' (per A3 in spec; pattern from
    feedback_haiku_drift_strip_fences.md). On second failure, return the
    existing FAIL fallback so the run does not abort.
    """
    criteria_block = "\n".join(f"{i+1}. {c}" for i, c in enumerate(criteria))
    user_prompt = (
        f"# User message\n{user_msg}\n\n"
        f"# Assistant response\n{assistant_response}\n\n"
        f"# Criteria (evaluate each in order)\n{criteria_block}\n\n"
        "Return JSON with one verdict object per criterion, in the same order."
    )

    # First attempt: default system prompt
    raw = call_anthropic(
        model=JUDGE_MODEL,
        system=JUDGE_SYSTEM,
        messages=[{"role": "user", "content": user_prompt}],
        max_tokens=2048,
    )
    verdicts = _strip_fences_and_parse(raw)
    if verdicts is not None:
        return verdicts

    # Retry once with stricter system prompt
    print(f"      [judge JSON parse failed — retrying with stricter prompt]")
    raw2 = call_anthropic(
        model=JUDGE_MODEL,
        system=JUDGE_SYSTEM_STRICT,
        messages=[{"role": "user", "content": user_prompt}],
        max_tokens=2048,
    )
    verdicts = _strip_fences_and_parse(raw2)
    if verdicts is not None:
        return verdicts

    # Both attempts failed — surface FAIL fallback with both raw responses
    return [{
        "criterion": "JUDGE_PARSE_ERROR",
        "verdict": "FAIL",
        "reason": f"Judge returned unparseable JSON twice. first={raw[:150]} | retry={raw2[:150]}",
    }]


# ─── Run the 5-turn script against one model ───────────────────────────────

def run_model(model: str, system_prompt: str) -> dict:
    """Run the full 5-turn Dana script against one model. Return structured result."""
    print(f"\n{'='*60}\n  Model: {model}\n{'='*60}")
    messages = []
    turns = []
    for spec in DANA_SCRIPT:
        print(f"\n--- Turn {spec['turn']}: Dana says '{spec['user'][:60]}{'…' if len(spec['user'])>60 else ''}'")
        messages.append({"role": "user", "content": spec["user"]})
        t0 = time.time()
        response = call_anthropic(model=model, system=system_prompt, messages=messages)
        elapsed = time.time() - t0
        messages.append({"role": "assistant", "content": response})

        print(f"    [{elapsed:.1f}s, {len(response)} chars] Judging…")
        verdicts = judge_response(spec["user"], response, spec["criteria"])
        passes = sum(1 for v in verdicts if v.get("verdict") == "PASS")
        fails = sum(1 for v in verdicts if v.get("verdict") == "FAIL")
        print(f"    {passes}✓ {fails}✗ / {len(spec['criteria'])} criteria")
        for v in verdicts:
            sym = "✓" if v.get("verdict") == "PASS" else "✗"
            print(f"      {sym} {v.get('criterion', '')[:80]}")
            if v.get("verdict") == "FAIL":
                print(f"          → {v.get('reason', '')[:100]}")

        turns.append({
            "turn": spec["turn"],
            "user": spec["user"],
            "response": response,
            "elapsed_seconds": round(elapsed, 1),
            "criteria": spec["criteria"],
            "verdicts": verdicts,
            "passes": passes,
            "fails": fails,
        })
        time.sleep(0.5)

    total_pass = sum(t["passes"] for t in turns)
    total_fail = sum(t["fails"] for t in turns)
    return {
        "model": model,
        "turns": turns,
        "total_pass": total_pass,
        "total_fail": total_fail,
        "verdict": "PASS" if total_fail == 0 else "FAIL",
    }


# ─── Divergence report ──────────────────────────────────────────────────────

def divergence(results: list[dict]) -> list[dict]:
    """Where do models disagree on the same criterion?"""
    out = []
    if len(results) < 2:
        return out
    for ti, _ in enumerate(DANA_SCRIPT):
        per_model = [r["turns"][ti]["verdicts"] for r in results]
        criteria = DANA_SCRIPT[ti]["criteria"]
        for ci, criterion in enumerate(criteria):
            verdicts = []
            for vlist in per_model:
                verdicts.append(vlist[ci].get("verdict") if ci < len(vlist) else "MISSING")
            if len(set(verdicts)) > 1:
                out.append({
                    "turn": DANA_SCRIPT[ti]["turn"],
                    "criterion": criterion,
                    "per_model": {results[i]["model"]: verdicts[i] for i in range(len(results))},
                })
    return out


# ─── Main ───────────────────────────────────────────────────────────────────

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", action="append", help="Model to test (repeat for multiple). Defaults to both.")
    ap.add_argument("--baseline", action="store_true", help="Save this run as the new baseline.")
    ap.add_argument("--compare-baseline", action="store_true", help="Diff this run vs the saved baseline.")
    args = ap.parse_args()

    models = args.model or DEFAULT_MODELS
    system_prompt = build_system_prompt()
    print(f"System prompt size: {len(system_prompt):,} chars")

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    results = [run_model(m, system_prompt) for m in models]

    div = divergence(results)
    report = {
        "timestamp": timestamp,
        "system_prompt_size": len(system_prompt),
        "models": models,
        "results": results,
        "divergence": div,
        "overall_verdict": "PASS" if all(r["verdict"] == "PASS" for r in results) else "FAIL",
    }

    out_file = RESULTS_DIR / f"dana-smoke-{timestamp}.json"
    out_file.write_text(json.dumps(report, indent=2))
    print(f"\n{'='*60}\n  Results written: {out_file}\n{'='*60}")
    for r in results:
        print(f"  {r['model']:<40} {r['total_pass']:>3}✓ {r['total_fail']:>3}✗   {r['verdict']}")
    if div:
        print(f"\nDivergence: {len(div)} criteria where models disagreed")
        for d in div[:5]:
            print(f"  Turn {d['turn']}: {d['criterion'][:60]}")
            for m, v in d["per_model"].items():
                print(f"    {m}: {v}")

    if args.baseline:
        (TESTS_DIR / "baseline.json").write_text(json.dumps(report, indent=2))
        print(f"\nBaseline saved to {TESTS_DIR / 'baseline.json'}")

    if args.compare_baseline:
        baseline_file = TESTS_DIR / "baseline.json"
        if not baseline_file.exists():
            print("No baseline to compare against. Run with --baseline first.")
            return 1
        baseline = json.loads(baseline_file.read_text())
        regressions = []
        for ri, r in enumerate(results):
            if ri >= len(baseline.get("results", [])):
                continue
            b = baseline["results"][ri]
            if r["total_fail"] > b["total_fail"]:
                regressions.append(f"{r['model']}: {b['total_fail']}✗ → {r['total_fail']}✗ (regression)")
        if regressions:
            print("\nREGRESSIONS vs baseline:")
            for line in regressions:
                print(f"  {line}")
            return 1
        print("\nNo regressions vs baseline. ✓")

    return 0 if report["overall_verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
