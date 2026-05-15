# PRD: research-brief

## Problem

People treat LLM output as research and get burned. By 2026, over 700 court cases involve AI-fabricated citations — average penalty $4,713, with public reprimands and bar referrals. Stanford found general-purpose models hallucinate in 58–88% of legal-question answers. The same failure mode shows up in journalism, consulting, medical decisions, and product strategy: the model produces fluent prose with confident-sounding citations that don't exist, and the reader has no way to tell which claims are solid versus which were generated to fit the shape of an answer.

The 2025 LLM calibration literature confirms why: out-of-the-box, models are at chance (AUROC 0.43–0.53) at estimating their own uncertainty in instruction-following tasks. They can't reliably tell *you* what they don't know because they can't reliably tell *themselves*.

The fix is structural, not statistical. Force the model to separate knowledge from inference from speculation, force it to tag every substantive claim with an evidence type, and ban fabricated citations entirely in favor of search-handles the user can verify in 30 seconds.

## Solution

A skill that takes a research question and produces a structured brief. Every claim carries a confidence rating (GRADE-style four-rung scale) and an inline tag for source type. Citations are search-handles, not fake references. The brief always includes a "What's contested" section (positions in genuine disagreement), a "What's unknown" section (where the model is speculating), and a "What to verify" section (the actual reading list).

The output is a single markdown file the user can paste into a doc, share with a team, or use as a scoping artifact for deeper research.

## Design Decisions (from research)

| Decision | Choice | Why |
|----------|--------|-----|
| Confidence scale | **GRADE four-rung: High / Moderate / Low / Very Low** | WEP's 7-point ladder (Sherman Kent / ICD 203) is more precise but cognitively heavier. GRADE is the global medical standard — four bins is what humans hold in working memory. We lose probability granularity, gain readability and faster pattern-recognition. |
| Source type taxonomy | **Three primitives: trained-knowledge / inference / speculation, plus an optional source-type tag (peer-reviewed / industry data / trade press / anecdotal)** | 2025 calibration research (ICLR, JMIR) shows that prompting models to *name the source type* before rating confidence is what actually moves calibration. It's also the specific countermeasure to the lawyer-fabrication problem — naming "speculation" prevents it from masquerading as fact. |
| Citations | **Search-handles only, never fabricated references** | Stanford 2024: 58–88% hallucination rate on legal citations. The pattern that works in retrieval-grounded tools (Perplexity, Elicit, Wikipedia "citation needed") is to tell the user *what to search* and *what type of source it should be*. The user verifies in seconds; the model can't fabricate something that's structurally not a citation. |
| Likelihood vs. evidence quality | **Single combined Confidence rating** (collapse ICD 203's two-axis WEP × LCA system) | The IC's two-dimensional system ("likely, with low confidence") is more rigorous but confuses non-analyst readers. Collapse to one axis at the cost of rigor. Power users can request the split via follow-up. |
| Brief structure | **Fixed sections: TL;DR → What we know → What's contested → What's inference → What's unknown → What to read next** | Could be more freeform. But "what's contested" and "what's unknown" are the highest-leverage sections (where most LLM output fails) — dropping them defeats the purpose. The structure is the product. |
| Iteration model | **Single-pass with explicit "ask me to dig deeper on section X" suggestion at the end** | Multi-turn-by-default balloons context and most uses are scoping. One-shot output, optional follow-up, user controls the depth. |
| Domain coverage | **General-purpose, not domain-specialized** | Medical/legal/financial briefs would benefit from domain-specific quality scales (GRADE for medicine, evidence pyramids for law). But the three-source taxonomy travels across domains. Specialize later if user data supports it. |

## Interaction Model

**Phase 1: Question intake** (immediate)

User provides a research question. The skill checks two things before producing anything:

1. **Is this in scope?** If the question requires real-time data (current stock prices, breaking news, anything from the last few weeks), the skill says so explicitly and recommends Perplexity, Elicit, or a browse-enabled tool instead. It doesn't pretend to answer.
2. **Is this a brief-shaped question?** Single-fact lookups ("population of Estonia") get a one-line answer with a "this doesn't need a brief" note. Brief format is reserved for synthesis, scoping, contested-evidence, and decision-support questions.

If the question is too vague to brief well, the skill asks one targeted clarifier — not five. ("Are you asking about [scope A] or [scope B]? I'll brief whichever.")

**Phase 2: Internal source-type pass** (no user input, happens before generation)

Before producing the brief, the model walks through the question and explicitly categorizes what it's about to claim:
- What do I know from training data with high certainty?
- What am I inferring from combining trained facts?
- Where would I be speculating?
- What's contested in the field — and what are the actual contested positions?

This pass is what separates the brief from "Claude's first instinct." It's the calibration step the literature shows actually works.

**Phase 3: Brief generation** (single output)

Produce one markdown brief following the template (see Output Spec below). Every substantive claim carries an inline confidence tag. Citations are search-handles. The "What's contested" section names actual positions, not vague gestures at "some experts argue." The "What to read next" section gives 3–5 search-handles tagged by source type.

**Phase 4: Optional deepening** (user-initiated)

The brief ends with: "Want me to dig deeper on [contested section] or [unknown section]? Or generate a longer brief on a sub-question?" The user drives any follow-up. The skill doesn't multi-turn by default.

## Output Spec

```markdown
# Research Brief: [Question]

## TL;DR
[2-3 sentences. The single most important thing.]
**Overall confidence: [High / Moderate / Low / Very Low]**

## What We Know (well-supported)
- **[Claim].** [1-2 sentence elaboration.]
  - *Confidence: High | Source type: [peer-reviewed research / industry data / etc.]*
  - *Verify: search "[specific handle]"*

## What's Contested
- **[Position A]:** [Who holds it, what they argue, why]
  - *Source type: [type] | Verify: search "[handle]"*
- **[Position B]:** [Who holds it, what they argue, why]
  - *Source type: [type] | Verify: search "[handle]"*

## What's Inference (my synthesis, not direct knowledge)
- **[Claim].** [Why I'm inferring this — what facts I'm combining.]
  - *Confidence: Moderate | Tag: inference from [A] + [B]*
  - *Verify: [what to check that would confirm or break it]*

## What's Unknown / Speculation
- **[Open question].** [What we'd need to know.]
  - *Confidence: Very Low — speculation only*

## What to Read Next
- For the strongest "yes" case: search "[handle]" — type: [source type]
- For the strongest "no" case: search "[handle]" — type: [source type]
- For methodology debates: search "[handle]" — type: [source type]
- For a recent overview: search "[handle]" — type: [source type]

## Confidence Scale (reference)
- **High** — multiple independent well-documented sources, low ambiguity, recent
- **Moderate** — supported but limited sources, or older, or some ambiguity
- **Low** — partial evidence, indirect inference, significant unknowns
- **Very Low / Speculation** — extrapolation beyond evidence; treat as hypothesis

---
*Want me to dig deeper on a section? Or brief a sub-question? Just ask.*
```

## Success Criteria

- The user can hand the brief to someone else and that person can verify every substantive claim within 30 minutes (search-handles work).
- "What's contested" surfaces actual disagreements the user didn't already know about, not strawmen.
- The user trusts the High-confidence claims enough to act on them and treats Low / Very Low claims as hypotheses to investigate.
- Zero fabricated citations across 100 briefs (the binary success metric).
- Brief takes under 10 minutes to read; produces in a single pass.

## What This Skill Does NOT Do

- Real-time research (no web access — use Perplexity, Elicit, or browse-enabled tools)
- Original research (no interviews, no fieldwork, no primary data collection)
- Definitive answers on high-stakes legal/medical/financial questions (always scoping, never final word)
- Single-fact lookups (overkill — just answer the question directly)
- Continuous research-assistant mode (one brief per request; user drives any follow-up)
- Citation generation in formal academic style (search-handles only, by design)

## Anti-Patterns to Avoid in Implementation

- **Never fabricate a citation in the form `Author (Year), Journal, page`.** This is the single failure mode the skill exists to prevent. If you don't know the specific source, write the search-handle and the source type — never the fake reference.
- **Never bury uncertainty in hedge words.** "Some studies suggest" without a confidence tag is the failure mode. Every claim gets an explicit rating.
- **Never present inference as fact.** If you combined two trained facts to reach a conclusion, tag it as inference. The reader needs to know which conclusions came from your synthesis vs. which came from the source material.
- **Never skip "What's contested."** If you can't name two positions in genuine disagreement, the question may be settled (say so) or you may not have enough source material (say so). Don't manufacture a fake debate, but don't skip the section either.
- **Never produce a brief without "What to read next."** The brief is a scoping artifact. Without next-steps it becomes a final answer, which is the wrong frame.
- **Never use ICD 203 probability words ("almost certain," "likely") and the GRADE confidence words ("High," "Moderate") interchangeably.** Pick one (we picked GRADE). Mixing is what produces "almost certainly likely" garbage.
- **Never claim confidence in time-sensitive claims without flagging the training cutoff.** Markets, current events, recent research, anything that drifts — auto-downgrade and note it.
- **Never default to "balanced both sides" on questions where the evidence isn't balanced.** If 90% of the evidence supports one position, the brief should reflect that with a confidence rating, not artificial both-sides framing.

## Technical Notes

- The skill works in Claude.ai (no tools required) — pure prompt-based extraction from training data.
- Works identically in Claude Code (no file I/O required, output is markdown to chat).
- No external dependencies, no API keys, no MCPs.
- Brief length target: 600–1,200 words. Longer for genuinely complex multi-position topics; shorter for narrower questions.
- Confidence calibration is ordinal, not absolute (per 2025 LLM calibration research) — users should trust *relative* ratings (this claim is more confident than that one) more than absolute percentages.
