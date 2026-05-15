# Book Distiller

**Stop summarizing books. Start arguing with them.**

## The Problem

Every commercial book-summary tool — Blinkist, Shortform, Headway, ChatGPT free-form — preserves everything proportionally. The result is a shorter version of the same book, which is exactly the wrong artifact for triage. Reviewers comparing recent Blinkist summaries to ChatGPT find them "surprisingly similar." Users report 15-minute summaries "can't capture nuance, case studies, or detailed arguments — you get the 'what' but miss the 'why.'"

There's a deeper problem the commercial tools can't fix: their business model depends on validating your interest in the book. None of them will tell you "skip this, read X instead." Goodreads reviews validate. Blinks validate. The whole ecosystem is structurally incapable of triage.

The people who do book criticism well — NYRB review-essays, Tyler Cowen's interview prep, Replicability-Index's chapter-by-chapter audit of *Thinking, Fast and Slow*, Derek Sivers' book notes — all do the same five moves: state what the book is trying to do, judge whether it does it, locate it in a longer conversation, name who should engage with it, and end with what it doesn't address. None of the tools do any of this. This skill does.

## What It Does

You give it a book title (and ideally an author). It produces an opinionated distillation:

1. **Core thesis** — 2 sentences about what the book is *trying to do*, not what it summarizes
2. **3-5 genuinely new ideas** — the parts that justify reading
3. **What's recycled** — specific prior work the book builds on, with citations
4. **Who should read it** — 2-4 specific reader profiles
5. **Who should skip it** — and what to read instead
6. **3 questions the book doesn't answer** — the open conversation it leaves behind

Reads in 5 minutes regardless of how long the book is. Compression is the feature.

## How to Use It

### In Claude.ai

1. Start a new conversation
2. Open the skill: say "Use the book-distiller skill" (if added to your Project) or paste the contents of `SKILL.md` as your first message
3. Tell Claude the book — title and author work best ("Distill *Thinking, Fast and Slow* by Daniel Kahneman")
4. If you have notes, highlights, or the table of contents, paste them — the distillation gets sharper
5. Receive the distillation. Ask follow-ups on any section.

### In Claude Code

1. Add the skill to your Claude Code configuration:
   - Copy `SKILL.md` to `~/.claude/skills/book-distiller/SKILL.md`
   - Or reference it in your `.claude/CLAUDE.md`: `When distilling a book, read path/to/book-distiller/SKILL.md`
2. Tell Claude Code: "Distill [book] by [author]"
3. Save the output as a `.md` file in your reading-notes directory if you want to keep it

### Tips for Better Results

- **Provide the author.** Title + author beats title alone — disambiguates editions and avoids confusion with similarly-named books.
- **Paste material if you have it.** Table of contents, your highlights, a passage from the introduction — all of it makes the distillation sharper. The skill treats user-pasted material as ground truth.
- **For recent or niche books, expect the skill to ask for input** rather than fake competence. That's intentional. Refusing to confabulate is the feature.
- **Push back on the verdict if you disagree.** The skill is designed to take positions, which means some of them will be wrong. Engage with the disagreement and the output gets better.

## What You Get

Tier A example output for a book Claude has deep training data on:

```markdown
# Book Distillation: Thinking, Fast and Slow
**Author:** Daniel Kahneman | **Published:** 2011 | **Knowledge depth: deep**

## Core Thesis
[2 sentences about what the book is trying to do, not what it covers]

## Genuinely New Ideas
1. [The new framing, with one line on why it counts as new]
2. ...

## What's Recycled
- [Specific prior work + author + year]
- ...

## Who Should Read It
- [Specific reader profile]
- ...

## Who Should Skip It
- [Specific reader profile + what to read instead]
- ...

## 3 Questions the Book Doesn't Answer
1. [Open question the book raises but doesn't address]
2. ...
3. ...
```

For mid-list and recent books (Tier B), you get the same template with a thin-data banner and a more conservative recycled-ideas section. For niche or very recent books (Tier C), the skill refuses to fake it and asks you to paste material first. That refusal is the design.

## The Research Behind It

Four findings shaped the design:

**Strong reviewers argue, they don't summarize.** Across NYRB review-essays, academic critical reviews, and Tyler Cowen's interview prep, the structural pattern converges: state a position about the book, bound the summary to ~1/3 of the review (this skill targets ~1/20), evaluate against the book's own goals, locate it in a longer conversation, end with a directional verdict. Summary-first collapses into Blinkist. Argument-first is the differentiator.

**Claude can do intellectual genealogy — for canonical books, with confidence tiers.** For *Thinking, Fast and Slow*, Claude can reliably trace the heuristics-and-biases framework to the 1974 Tversky/Kahneman *Science* paper and surface the documented Chapter 4 replication concerns Kahneman publicly conceded in 2017. For *Good to Great*, the Rosenzweig halo-effect critique and Levitt's portfolio-underperformance analysis are well-documented and surfaceable. For niche or very recent books, this fails — confidently. The skill handles this with a three-tier system: deep / partial / thin training data, with explicit refusal at the thin tier.

**The commercial tools all share one gap.** None of Blinkist, Shortform, Headway, or Goodreads reviews will tell you to skip the book. Their business model depends on validating your interest. The "Who Should Skip It" section — with specific reader profiles and "what to read instead" pointers — is the move no commercial tool can make. It's also the most useful section for actual triage.

**Compression is the feature, not the constraint.** Academic guides cap summary at 1/3 of a critical review. This skill targets ~1/20. The output replaces (or triages) the reading; it doesn't duplicate it. A Tier A distillation runs 400-600 words. If it's longer, it's padded.

## Design Decisions

| Decision | Choice | Why |
|----------|--------|-----|
| Argument-first vs. summary-first | Argument-first — open with a thesis *about the book*, not *of the book* | Every strong review tradition leads with a position. |
| Compression ratio | Aggressive — ~5-minute read regardless of book length | Output replaces or triages the reading; doesn't duplicate it. |
| Genealogy as hero or supporting feature | Supporting, with confidence tiers | Claude does this well for canonical books, fails confidently on niche ones. Tiering keeps the feature without the hallucination risk. |
| Tiered outputs | Single template, content tiers based on training-data depth | Tier A full distillation; Tier B with thin-data banner; Tier C refuses to fake it. |
| Star ratings vs. directional verdicts | Directional verdicts only | Stars validate; directional verdicts triage. Triage is the job. |
| Recycled ideas: include or skip | Include, with strict citation rules | Every bullet names specific prior work + year. Empty sections are acceptable; invented ones are catastrophic. |
| 3 unanswered questions: useful or filler | Useful — keep them | The most shareable part of the output. Turns a review into the start of a conversation. |

## When NOT to Use It

- **Fiction or narrative-driven memoir** — the framework doesn't fit story. Use a different tool.
- **Academic citation purposes** — the genealogy section is for orientation, not for citing in a paper. Verify primary sources.
- **Books the skill has no training data on AND you have no material for** — the skill will refuse and that's correct. Read enough to give it 3 passages and a table of contents, then come back.

## Pairs With

- **[mental-models](/mental-models/)** — After distilling the book, work through which of its frameworks actually apply to your problem.
- **[devils-advocate](/devils-advocate/)** — Test the book's central thesis before adopting it.
- **[self-interview](/self-interview/)** — Surface what you already think before reading the book; compare your priors to the book's claims.
- **[ask-me-the-questions](/ask-me-the-questions/)** — If you're trying to figure out *which* book to read on a topic, start there.
