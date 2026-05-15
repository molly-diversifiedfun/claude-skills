# PRD: book-distiller

## Problem

Book summary tools — Blinkist, Shortform, Headway, ChatGPT free-form summaries — preserve everything proportionally. The result is a shorter version of the same book, which is exactly the wrong artifact for triage. Users get the "what" and miss the "why" (makeheadway.com Blinkist review). Recent Blinkist summaries show "telltale signs of AI-generated content" with mechanical voice; reviewers comparing Blinkist to ChatGPT find them "surprisingly similar." Goodreads reviews validate the user's interest in the book — that's their business model — and so the entire commercial summary ecosystem is structurally incapable of saying "skip this, read X instead."

What's missing is the move every strong reviewer makes: a position on the book. NYRB review-essays, Tyler Cowen's interview prep, Replicability-Index's chapter-by-chapter audit of *Thinking, Fast and Slow*, and Derek Sivers' book notes all do the same thing — state what the book is trying to do, judge whether it does it, locate it in a longer conversation, and tell you whether to engage. None of the commercial tools do any of this.

## Solution

A skill that produces opinionated book distillations, not summaries. Given a book title, output: a 2-sentence thesis about the book (not of the book), 5 genuinely new ideas, what's recycled from earlier work, who should read it, who should skip it (and what to read instead), and 3 questions the book doesn't answer. Confidence-tiered on intellectual genealogy. Refuses to fake competence on books with thin training data.

The output reads in 5 minutes regardless of book length. It's the artifact you'd want before deciding whether to buy a $30 hardcover and spend 10 hours with it.

## Design Decisions (from research)

| Decision | Choice | Why |
|----------|--------|-----|
| Argument-first vs. summary-first | **Argument-first** — open with a 2-sentence thesis *about the book*, not *of the book* | Every strong review tradition (NYRB, academic, Cowen-style) leads with a position. Summary-first collapses into Blinkist. |
| Compression ratio | **Aggressive** — output reads in ~5 minutes regardless of book length | Academic guides cap summary at 1/3 of a critical review. This skill targets ~1/20. The output replaces or triages the reading; it doesn't duplicate it. |
| Genealogy: hero feature or supporting feature | **Supporting, with confidence tiers** | Q2 finding: Claude can reliably trace genealogy for canonical books with secondary literature (*Thinking, Fast and Slow* → 1974 *Science* paper; *Good to Great* → Rosenzweig halo-effect critique). Fails confidently on niche/recent books. Tiered confidence (documented / plausible / uncertain) keeps the feature without the hallucination risk. |
| One output template or tiered outputs | **Single template, tiered content** based on training-data depth | Tier A (bestsellers, canon): full distillation. Tier B (recent/mid-list, partial coverage): full distillation + thin-data warning + offer to accept user notes. Tier C (niche/indie/very recent): refuse to fake it; ask for user input first. |
| Star rating vs. directional verdict | **Directional verdict only** — *who this is for, who should skip, what to read instead* | Stars validate; directional verdicts triage. Triage is the job. |
| Recycled-ideas section: include or skip | **Include, with strict citation rules** — name a specific work and year or downgrade to "uncertain" | Forces specificity. Empty section is acceptable; confabulated section is not. |
| 3 unanswered questions: useful or filler | **Useful — keep them** | Cowen's prep, NYRB essays, Sivers' notes all end with "what this book doesn't address." It's the move that turns a review into the start of a conversation. |

## Interaction Model

**Phase 1: Input** (10 seconds)

User provides one of:
- A book title and author ("Thinking, Fast and Slow by Daniel Kahneman")
- A title alone ("Atomic Habits") — skill confirms author/edition before proceeding
- A title plus user-pasted material (table of contents, highlights, chapter notes, key passages) — auto-promotes the book to Tier A treatment regardless of training-data depth

If the user provides only a title with no author and there are multiple plausible books with that title, the skill asks one disambiguating question and proceeds.

**Phase 2: Silent Self-Assessment** (automatic, user never sees this)

Before writing anything, the skill checks four things:
1. Can I name the publisher and year?
2. Can I name the central thesis?
3. Can I name at least one specific argument or chapter?
4. Can I name at least one piece of secondary literature about it (review, critique, citing work)?

- 4/4 or 3/4 → Tier A (full distillation)
- 2/4 → Tier B (full distillation, thin-data banner, recycled-ideas section pared back)
- 1/4 or 0/4 → Tier C (refuse to fake it; ask for user-provided material first)

**Phase 3: Distillation** (automatic, no further user input)

Produce the distillation in the order below. Each section has its own quality bar; sections that can't meet the bar are surfaced as "uncertain" rather than padded.

1. **Header** — title, author, year, knowledge-depth indicator
2. **Core Thesis** — exactly 2 sentences, about what the book is trying to do, not what it summarizes
3. **5 Genuinely New Ideas** — numbered, each with a one-line "why this is the new part" framing. If fewer than 5 ideas qualify as new, ship 3 or 4; never pad to 5.
4. **What's Recycled** — bullets, each citing specific prior work (author, title or paper, year). If no specific citation is possible, the bullet is omitted. The section can be empty.
5. **Who Should Read It** — 2-4 specific reader profiles, not generic ones ("anyone interested in productivity" is a fail mode)
6. **Who Should Skip It** — 2-4 specific reader profiles, including "what to read instead" pointers when applicable
7. **3 Questions the Book Doesn't Answer** — open questions the book raises but doesn't address; these are the most shareable artifact

**Phase 4: Calibration footer**

End with a one-line confidence statement: knowledge depth, genealogy confidence, and an invitation to drill in on any section. Example:

> *Distillation depth: deep training data. Confidence on genealogy: high (papers and dates are documented). If you want me to focus on any section in more detail, say so.*

For Tier B/C books, the footer reads differently and explicitly invites user input:

> *Distillation depth: thin training data. I'm working from the publisher copy and a few reviews. If you can paste the table of contents and 2-3 passages you found striking, I can do a much sharper second pass.*

**Phase 5 (optional): Drill-down**

If the user asks for more on any section ("expand on what's recycled," "give me 3 more readers who should skip this"), regenerate just that section at higher density without restarting the whole distillation.

## Anti-Patterns to Avoid in Implementation

- **Never summarize chapter-by-chapter.** That is the failure mode of every commercial tool. The skill's job is judgment, not compression.
- **Never confabulate intellectual genealogy.** If a specific prior work and year cannot be named, the bullet is cut. Empty "What's Recycled" sections are acceptable; invented ones are catastrophic.
- **Never use star ratings, scores, or "X/10."** Directional verdicts only.
- **Never write "Who Should Read It" bullets that could fit any book.** "Anyone interested in [topic]" is a fail. Reader profiles should be specific enough that a real person reads it and recognizes themselves or doesn't.
- **Never pad the "5 new ideas" section.** If only 3 ideas qualify as genuinely new, ship 3. Padding to 5 by promoting recycled material is a worse failure than shipping 3.
- **Never refuse to take a position.** If the book is mediocre, say so. If the genealogy is weak, say so. The skill's value is the position; without it, the user could have used Blinkist.
- **Never produce output longer than ~600 words for a Tier A book.** The compression target is the feature.
- **Never invent quotes from the book.** Paraphrase if needed; never quote.
- **Never claim to have read sections that don't appear in Claude's training corpus.** Tier C exists for exactly this reason.

## Output Spec

| Element | Spec |
|---------|------|
| Total length (Tier A) | 400-600 words |
| Total length (Tier B) | 300-500 words + thin-data banner |
| Total length (Tier C) | ~100 words declining to proceed + request for user input |
| Core thesis | Exactly 2 sentences |
| New ideas | 3-5 bullets, never padded |
| Recycled ideas | 0-5 bullets, every one citing specific prior work + year |
| Who should read / skip | 2-4 specific reader profiles each |
| Unanswered questions | Exactly 3 |
| Footer | 1-2 sentences on knowledge depth + drill-down invitation |
| Voice | Direct, opinionated, no corporate filler. No "47" or other AI-tell numbers. No phrases like "delve," "landscape," "I'd be happy to," "let's dive in." |

## Success Criteria

- A reader who has not read the book can decide in 5 minutes whether to read it, skip it, or read a specific chapter.
- A reader who has read the book recognizes the distillation as accurate and surprising — they got something they didn't have from reading the book themselves.
- For Tier A books, the genealogy section is verifiable: every cited prior work exists and is correctly attributed.
- For Tier C books, the skill refuses to fake competence — failure mode is requesting input, not generating confident slop.
- The output sounds like a smart friend two drinks in, not a Goodreads reviewer or a Blinkist editor.

## What This Skill Does NOT Do

- It does not summarize fiction. The framework (5 new ideas, what's recycled, who should skip) doesn't fit narrative work. Fiction recommendations need a different skill.
- It does not produce reading lists or "if you liked X, read Y" recommendations beyond the bounded "read this instead" pointers in the skip section.
- It does not score books numerically.
- It does not replace reading the book. For most Tier A books, the distillation is a triage tool; for the books that pass triage, the user still reads them.
- It does not generate the distillation from scratch in real-time scraping mode — it works from training data plus user-provided material. No web fetch, no API key.

## Technical Notes

- Pure prompt-based; works in Claude.ai (no tools required) and Claude Code.
- No external dependencies — no web search, no MCP servers, no file I/O beyond what the user pastes.
- For books where the user wants to inject current material (recent reviews, the actual table of contents, their own highlights), they paste it inline. The skill treats user-pasted material as ground truth.
- Tier-detection happens silently in Phase 2; the user only sees the final tier reflected in the depth banner.
