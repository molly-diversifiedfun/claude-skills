# Dana smoke test

Voice regression detector for the free AI Build Partner Claude.ai skill.

## What it does

Runs a fixed 5-turn conversation (the "Dana script") against TWO models in parallel:

- `claude-opus-4-7` (paid-tier flagship)
- `claude-sonnet-4-6` (free-tier default for most buyers)

After each turn, a judge call (Sonnet 4.6) evaluates the response against a per-turn rubric of binary PASS/FAIL criteria — voice rules, structural contracts, banned phrases. Outputs JSON with per-model results + a divergence report (criteria where the two models disagree).

This is the structural check that ensures the skill's voice rules don't regress between rebuilds.

## What it catches

- Banned opener tokens (`Let me ...`, `I'll ...`, `Now I'll ...`, `First, ...`, etc. — the post-draft reflex check)
- Missing 📌 Save this turn block when Do this/Why fires (STRUCTURAL CONTRACT)
- Project-first prompt missing on turn 1
- In-character check leaks
- Brand violations (the word "coaching", motivational fluff, banned vocabulary)
- Wrong save location recommendations (Notion / GDrive / Obsidian instead of Claude.ai Project)
- Voice register failures (warm vs cold mismatch)

## What it does NOT catch

- Claude.ai UI-specific behavior (button rendering, "Viewed N files" collapsible sections) — the system-prompt API doesn't replicate the Claude.ai skill bundle runtime exactly
- Multi-conversation Project knowledge file reads (LAYER 6.4 read-the-project-first) — needs Claude.ai's actual Project context
- Tool call narration via `<required_reading>` blocks — those were stripped this session; the test won't catch regressions if they're added back unless the criteria are updated

## Setup

```bash
export ANTHROPIC_API_KEY=sk-ant-...
cd ~/github/claude-skills/ai-build-partner/tests
python3 dana-smoke.py --help
```

No Python deps required — uses only stdlib.

## Usage

```bash
# Default: run both models, save results to tests/results/dana-smoke-<ts>.json
python3 dana-smoke.py

# Just one model
python3 dana-smoke.py --model claude-sonnet-4-6-20251017

# Save this run as the new baseline
python3 dana-smoke.py --baseline

# Compare current run vs saved baseline (exits 1 if any regression)
python3 dana-smoke.py --compare-baseline
```

## Cost per run

5 turns × 2 models = 10 conversation calls + 10 judge calls = ~20 API calls. With Sonnet 4.6 + Opus 4.7:

- Opus 4.7: ~$0.30-0.60/run (5 calls × ~25k input + ~1k output tokens)
- Sonnet 4.6: ~$0.05-0.10/run (5 conversation + 5 judge calls)

Total: ~**$0.35-0.70 per full run**. Cheap enough for CI on every push to claude-skills main.

## The Dana script

5 turns calibrated to maximally stress the structural rules:

| Turn | What Dana says | What we check |
|---|---|---|
| 1 | "I've been wanting to ship a 1:1s guide for senior PMs..." | Project-first fires, no narration leak, no in-character check |
| 2 | "I'm in a Project, go" | Do this/Why structure, Save-This block fires, no motivational fluff |
| 3 | "I'm scared no one will actually read it" | Warm register switch, structural reframe (not reassurance) |
| 4 | "what if I spiral Saturday morning?" | Concrete action, spiral-defense moment, Claude.ai save location |
| 5 | "/unstuck scope" | Routes to scope module, three exits offered, ONE question |

To modify: edit `DANA_SCRIPT` in `dana-smoke.py`. Each turn has `user`, `criteria`, and is independently judged.

## CI integration (future)

```yaml
# .github/workflows/dana-smoke.yml (sketch)
name: Dana smoke
on:
  push:
    paths: ['ai-build-partner/**']
jobs:
  smoke:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: python3 ai-build-partner/tests/dana-smoke.py --compare-baseline
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
```

Failing run = voice regression. Block the merge until baseline is updated intentionally.

## Updating the baseline

The baseline lives at `tests/baseline.json` and is checked in. Update it when:

- A voice rule changes (intentionally) — re-run with `--baseline`
- A new turn is added to the Dana script
- A model upgrade happens (Opus 4.7 → Opus 4.8)

Don't update the baseline to hide regressions. If a current run fails against baseline, fix the skill first, then update the baseline.

## Files

- `dana-smoke.py` — the runner
- `baseline.json` — saved baseline (commit this)
- `results/dana-smoke-<timestamp>.json` — per-run results (gitignored)
- `README.md` — this file
