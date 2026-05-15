# Research Brief

**Stop treating LLM output as research. Start producing briefs you can actually verify.**

## The Problem

By 2026, over 700 court cases involve AI-fabricated citations. Average penalty: $4,713. Public reprimands, dismissed cases, bar referrals. Stanford found general-purpose models hallucinate in 58–88% of legal-question answers — they invent case names, court rulings, and page numbers that don't exist, packaged in fluent legal-sounding prose.

It's not just lawyers. The same failure shows up in journalism, consulting, medical decisions, and product strategy. The model produces confident-sounding output, the reader trusts it because it sounds right, and nobody catches the fabrication until it's already in the deliverable.

The 2025 calibration literature explains why: out of the box, LLMs are at chance (AUROC 0.43–0.53) at estimating their own uncertainty. They can't reliably tell you what they don't know because they can't reliably tell themselves.

## What It Does

You ask a research question. The skill produces a structured brief with five sections:

- **TL;DR** — the single most important thing, with an overall confidence rating
- **What We Know** — well-supported claims, each with a confidence tag and a source-type tag
- **What's Contested** — actual positions in disagreement, named with the people or institutions that hold them
- **What's Inference** — the synthesis the model is doing, explicitly flagged
- **What's Unknown / Speculation** — open questions and where the model would be guessing
- **What to Read Next** — 3-5 search-handles tagged by source type

Every substantive claim carries a confidence rating: **High / Moderate / Low / Very Low** (the GRADE medical-evidence scale). Every source reference is a search-handle (the phrase to paste into Google) — never a fabricated citation. The skill explicitly separates trained-knowledge from inference from speculation, in-line, on every claim.

Output is a single markdown file. Paste it into a doc, share it with a team, or use it as a scoping artifact before deeper research.

## How to Use It

### In Claude.ai

1. Start a new conversation
2. Paste the contents of `SKILL.md` as your first message (or add it to a Project)
3. Ask your research question
4. Get the brief
5. Optionally: ask for a deeper dive on a specific section

### In Claude Code

1. Drop the `research-brief/` directory into `~/.claude/skills/`
2. The skill auto-activates on phrases like "research brief," "what does the research say," "give me the lay of the land," or any scoping question
3. Or invoke explicitly: `/skill research-brief`

## When to Use It

The brief format pays off when **structure and uncertainty matter more than freshness**:

- **Strategy and decision support** — "Should we adopt X?" The brief surfaces strongest cases for and against.
- **Pre-research scoping** — Before a deep dive (consultant work, journalism, product spec), the brief tells you what's known, what's contested, and what to actually go read.
- **Technical / medical / legal questions where users tend to over-trust LLM output** — explicit confidence tags act as a circuit breaker. Every "Low confidence" line is a "go verify" prompt.
- **Synthesis of contested topics** — "What does the evidence say about intermittent fasting?" Brief format surfaces conflicting studies instead of picking a winner.

## When NOT to Use It

- **Real-time / current events** — no web access, training cutoff is the ceiling. Use Perplexity, Elicit, or browse-enabled tools.
- **Single-fact lookup** — "Population of Estonia." A brief for that is overkill.
- **Original research** — the skill summarizes; it doesn't replace primary research, fieldwork, or interviews.
- **High-stakes legal / medical / financial decisions** — useful as scoping, never as the final word.

## What Makes This Different

Most "AI research" output is fluent prose with confident-sounding citations and no way to tell what's real. This skill is built around the inverse:

- **Citations are search-handles, not fabrications.** You can verify every claim in 30 seconds, or the skill tells you it can't be verified.
- **Confidence is on the claim, not the brief.** A "High confidence" overall rating means nothing. Per-claim ratings give you a map of what to trust and what to investigate.
- **Inference is tagged separately from knowledge.** When the model synthesizes, it tells you. You decide whether to trust the synthesis.
- **"What's contested" is mandatory.** If the model can't name two positions in disagreement, it says the question is settled (or that it doesn't have enough sources). It doesn't invent a fake debate.
- **"What to read next" is mandatory.** The brief is a scoping artifact, not a final answer.

## The Research Behind the Skill

Built on:

- **ICD 203** (US Intelligence Community Analytic Standards) — the Words of Estimative Probability and Levels of Confidence framework. We borrowed the principle of separating likelihood from evidence quality.
- **GRADE** (medicine) — the four-rung quality scale (High / Moderate / Low / Very Low) used by 100+ orgs including WHO and Cochrane. We use it for per-claim confidence.
- **Cochrane Summary of Findings tables** — one row, one claim, one rating. No bundling.
- **2025 LLM calibration research** (ICLR, JMIR, MICCAI) — out of the box LLMs are bad at self-confidence (AUROC ≈ 0.5), but *prompting them to name source type before rating* meaningfully improves calibration. That's the Phase 2 source-type pass.
- **Stanford's "Large Legal Fictions" study** and the 700+ documented cases of AI-fabricated citations in court — the failure mode this skill exists to prevent.

Full research synthesis at [`docs/research/11-research-brief.md`](../docs/research/11-research-brief.md). Design tradeoffs at [`docs/prds/11-research-brief.md`](../docs/prds/11-research-brief.md).

## Plays Well With

- **decision-maker** — the brief scopes the evidence; decision-maker structures the actual choice.
- **devils-advocate** — once you have a brief, stress-test the conclusion you're drawn to.
- **mental-models** — the brief tells you what's known; mental-models helps you think through implications.
- **self-interview** — when you want to clarify what *you* think, not gather external evidence.

## License

MIT. Use it, fork it, adapt it. If it saves you from a fabricated citation, that's the win.
