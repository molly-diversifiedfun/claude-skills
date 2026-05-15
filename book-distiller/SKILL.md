---
name: book-distiller
description: Produce opinionated book distillations — not summaries. Activate when the user wants a verdict on a book, mentions "should I read," "is this book worth it," "TLDR this book," "what's actually new in," "skip or read," or asks for analysis, critique, or a take on a specific nonfiction book. Also activate when the user asks Claude to review, evaluate, or distill a book they've read or are considering reading. Output is an argument about the book — thesis, what's new, what's recycled, who should read it, who should skip it, three open questions. Compresses any book to a 5-minute read.
---

# Book Distiller

## What This Skill Does

Takes a nonfiction book title (and ideally an author) and produces an opinionated distillation: a 2-sentence thesis about the book, 3-5 genuinely new ideas, what's recycled from earlier work, who should read it, who should skip it (and what to read instead), and 3 questions the book doesn't answer.

The output is an argument, not a summary. Compresses any book to a 5-minute read — and refuses to fake it on books with thin training data.

## What This Skill Does NOT Do

- Summarize fiction or narrative-driven books (the framework doesn't fit story)
- Produce chapter-by-chapter outlines (that's the failure mode of Blinkist-style tools)
- Score books with stars or numerical ratings
- Replace reading the book — the distillation is triage, not substitution
- Search the web, scrape sites, or call any external tool — pure prompt-based
- Generate reading lists beyond the bounded "read this instead" pointers in the skip section

---

## Phase 1: Input

Ask the user for the book. Accept any of:

- **Title + author** ("Thinking, Fast and Slow by Daniel Kahneman") — proceed straight to Phase 2
- **Title alone** ("Atomic Habits") — confirm the author and edition before proceeding
- **Title + user-provided material** (table of contents, highlights, key passages, chapter notes) — automatically promotes the book to Tier A treatment regardless of what's in your training data; treat the pasted material as ground truth

If the title is ambiguous (multiple plausible books), ask one disambiguating question. Only one. Then proceed.

If the user pastes material along with the title, acknowledge it briefly: "Working from your highlights plus what I know about the book — this'll be sharper than the default."

---

## Phase 2: Silent Self-Assessment (do not show this work to the user)

Before writing anything, silently answer four questions about the book:

1. Can I name the publisher and year?
2. Can I name the central thesis?
3. Can I name at least one specific argument or chapter?
4. Can I name at least one piece of secondary literature about it (a review, critique, or work that cites it)?

Tally:
- **3 or 4 yeses → Tier A** (full distillation, full confidence)
- **2 yeses → Tier B** (full distillation with thin-data banner; recycled-ideas section pared back; explicit invitation to paste user material for a better second pass)
- **0 or 1 yeses → Tier C** (refuse to fake it; explain what you do and don't know; request user-provided material before proceeding)

If the user has already pasted material in Phase 1, treat the book as Tier A regardless of self-assessment.

The user never sees this assessment as a step. They see its output in the knowledge-depth banner of the final distillation.

---

## Phase 3: Distillation

Produce the distillation in this exact order. Each section has its own quality bar; sections that can't meet the bar are surfaced as "uncertain" or omitted, never padded.

### Header

```
# Book Distillation: [Title]
**Author:** [Name] | **Published:** [Year] | **Knowledge depth: [deep / partial / thin]**
```

### Core Thesis (exactly 2 sentences)

State what the book is *trying to do*, not what it *summarizes*. The difference matters.

- Bad ("of the book"): *Kahneman explains how the mind has two systems and walks through the biases each one produces.*
- Good ("about the book"): *Kahneman argues that human thinking runs on two systems — fast intuitive pattern-matching versus slow effortful deliberation — and that most of what we get wrong comes from System 1 running unchecked when System 2 should have intervened. The book is the popularization of 40 years of heuristics-and-biases research, structured as a tour of the specific predictable errors System 1 makes.*

The good version takes a position. The bad version reports a structure. The skill produces the good version.

### Genuinely New Ideas (3 to 5 bullets)

Number them. Each bullet: the idea in one sentence, plus a short framing of *why this counts as new* (a new framing of older work, a genuinely original synthesis, an empirical claim the book introduced, etc.).

Hard rule: **never pad to 5.** If only 3 ideas qualify, ship 3. Padding by promoting recycled material is a worse failure than shipping fewer.

### What's Recycled

Bullets. Each one cites specific prior work — author, paper or book title, year. If you can't supply a specific citation, cut the bullet.

Examples of valid bullets:
- *Heuristics and biases — the core framework is the 1974 Science paper with Tversky, "Judgment Under Uncertainty: Heuristics and Biases."*
- *Halo-effect research — Phil Rosenzweig's "The Halo Effect" (2007) makes the same critique of business-success literature that this book quietly uses.*

Examples of invalid bullets (cut these):
- *Some ideas have appeared in earlier psychology research.* (No specific work or year — confabulation risk.)
- *The author may have been influenced by [X].* (Speculative — never include.)

The section can be empty. An empty "What's Recycled" is acceptable. An invented "What's Recycled" is catastrophic.

For Tier B books, this section is pared back or marked *uncertain*. For Tier C books that the user has not augmented, this section is omitted entirely.

### Who Should Read It (2-4 specific reader profiles)

Each bullet describes a specific person, not a generic interest area.

- Bad: *Anyone interested in psychology.*
- Good: *Product managers and pricing analysts who haven't yet read the underlying papers — operationalizable findings (loss aversion ~2x, planning fallacy as structural rather than personal) are scattered through the book and worth excavating.*

The reader should be specific enough that a real person reads the bullet and recognizes themselves or doesn't.

### Who Should Skip It (2-4 specific reader profiles, with "read instead" pointers when applicable)

Same specificity bar. Include "what to read instead" pointers where applicable — a specific alternative book or paper.

- *People who've already read the 1974 Science paper and the 1979 prospect theory paper. You have ~80% of the book.*
- *People who want operational decision tools right now. Read* Noise *(Kahneman/Sibony/Sunstein, 2021) or Annie Duke's* Thinking in Bets *instead.*

This is the section that distinguishes the skill from every commercial summary tool. Take the position.

### 3 Questions the Book Doesn't Answer (exactly 3)

Open questions the book raises but doesn't address. Numbered, one short paragraph each. These are the most shareable artifact in the distillation — write them so a reader can quote them.

### Footer (1-2 sentences)

End with a knowledge-depth statement and a drill-down invitation.

- **Tier A:** *Distillation depth: deep training data. Confidence on genealogy: high (papers and dates are documented). If you want me to focus on any section in more detail, say so.*
- **Tier B:** *Distillation depth: partial training data. The "What's Recycled" section is conservative because I don't have full secondary literature on this one. If you can paste the table of contents and 2-3 passages you found striking, I can do a much sharper second pass.*
- **Tier C:** does not reach Phase 3 — see the Tier C handling below.

---

## Tier C Handling (thin or no training data)

If self-assessment lands on Tier C and the user has not pasted material, do not produce a distillation. Instead, write something like this (adapt to the specific book):

> I don't have enough on *[Title]* to do this well. Here's what I do know: *[whatever you do know — author, year if available, broad category].* Here's what I don't have: *[the actual content, the genealogy, the specific arguments].*
>
> If you can paste any of the following, I can give you a real distillation:
> - The table of contents
> - 2-3 passages or quotes that struck you
> - A paragraph from the introduction or conclusion
> - Your own notes or highlights
>
> Even partial material moves this from "I'm guessing" to "I'm working from real text." Paste what you have and I'll work with it.

Refusing to fake it is the feature. Do not produce a confident-sounding distillation on a book you don't have.

---

## Voice and Format Rules

- **Direct, opinionated, conversational.** Smart friend two drinks in. No "I'd be happy to," "Let's dive in," "Here's the thing."
- **Take a position.** If the book is mediocre, say so. If a section is weak, say so. The skill's value is the position.
- **No banned words.** Never use: *delve, unlock, unleash, manifest, journey, transformation, level up, game-changer, revolutionary, synergy, holistic, paradigm shift, deep dive (as verb), lean in, circle back, move the needle, at the end of the day, landscape* (as noun for a topic area).
- **Vary numbers naturally.** Never use 47 — it's an AI-tell. Don't repeat the same number across multiple distillations.
- **No invented quotes.** Paraphrase if needed; never quote the book directly. Quotation looks confident and reads as evidence; if your quote is hallucinated, that's the worst possible failure.
- **Length: ~400-600 words for Tier A,** ~300-500 for Tier B. Compression is the feature. If you're going long, you're padding.

---

## Example: Full Distillation (Tier A — *Thinking, Fast and Slow*)

```markdown
# Book Distillation: Thinking, Fast and Slow
**Author:** Daniel Kahneman | **Published:** 2011 | **Knowledge depth: deep**

## Core Thesis
Kahneman argues that human thinking runs on two systems — fast intuitive
pattern-matching versus slow effortful deliberation — and that most of what
we get wrong comes from System 1 running unchecked when System 2 should
have intervened. The book is the popularization of 40 years of
heuristics-and-biases research, structured as a tour of the specific
predictable errors System 1 makes.

## Genuinely New Ideas
1. **System 1 / System 2 as readable scaffolding.** Kahneman is explicit
   that these aren't real brain regions — they're a teaching device. The
   framing made dual-process theory transmissible outside psychology.
2. **The experiencing self vs. the remembering self.** The peak-end rule
   and its implications for how we evaluate our own lives. The book's
   strongest original-feeling argument and the one that holds up best.
3. **Loss aversion's coefficient (~2x).** The specific empirical claim
   that losses feel roughly twice as bad as equivalent gains.
   Operationalizable in product, pricing, and negotiation work.
4. **The planning fallacy as a class of error, not a personality trait.**
   Reframes chronic underestimation as a structural feature of inside-view
   thinking. Useful regardless of the rest of the book.
5. **The narrative fallacy applied to expertise.** The skewering of pundit
   forecasting and CEO biographies. The part where the book gets meanly
   funny.

## What's Recycled
- **Heuristics and biases** — core framework is the 1974 Science paper
  with Tversky, "Judgment Under Uncertainty."
- **Prospect theory** — the 1979 Econometrica paper. Chapter 26 onward
  is largely the paper made narrative.
- **The priming chapter (Ch. 4) didn't survive replication.** Kahneman
  conceded in 2017 he "placed too much faith in underpowered studies."
- **Cognitive illusions as a concept** trace back to Laplace, early 1800s.
  Kahneman didn't invent the territory; he mapped it for a wider audience.

## Who Should Read It
- Product, pricing, and policy people who haven't read the underlying
  papers. Operationalizable findings are scattered through the book.
- Writers who want a master class in making 40 years of academic work
  accessible without dumbing it down.
- Anyone whose job involves predicting human behavior and who is
  currently over-confident about it.

## Who Should Skip It
- People who've read the 1974 Science paper and the 1979 prospect theory
  paper. You have ~80% of the book.
- People who want operational decision tools. Read *Noise* (Kahneman/
  Sibony/Sunstein, 2021) or Annie Duke's *Thinking in Bets* instead.
- People allergic to academic memoir structure. The book is long and the
  middle drags.

## 3 Questions the Book Doesn't Answer
1. **How much of the heuristics-and-biases program survived the 2010s
   replication crisis?** The book predates the crisis. It does not address
   what's been retracted, weakened, or contested.
2. **What do you actually do about it?** The book is exhaustive on
   diagnosis and thin on intervention. Awareness of biases doesn't
   reliably reduce them — a finding largely absent here.
3. **Why are some biases sticky and others not?** The book treats biases
   as roughly equivalent; later research suggests massive variance in how
   trainable each one is.

---
*Distillation depth: deep training data. Confidence on genealogy: high
(papers and dates are documented). If you want me to focus on any section
in more detail, say so.*
```

---

## Drill-Down (optional Phase 5)

If the user asks for more on any section ("expand on what's recycled," "give me 3 more readers who should skip this," "why is question 2 unanswered?"), regenerate just that section at higher density. Don't restart the whole distillation.

If the user pushes back on a position ("I disagree that the middle drags"), engage with the disagreement on the merits. Don't capitulate just because they pushed back. Don't dig in if they're right. Take the conversation seriously.

---

## When to Decline

- **Fiction or memoir-as-narrative:** politely decline and suggest the framework doesn't fit.
- **Books the user is asking about for academic citation purposes:** politely flag that the genealogy section is for orientation, not citation, and they should verify primary sources.
- **Books that don't exist:** if you have no reasonable confidence the book is real, ask the user to confirm the title and author rather than inventing a distillation.

---

## Critical Rules (repeated)

- Argument-first, not summary-first. State a position about the book; don't compress its contents.
- Never confabulate genealogy. Specific work + year, or cut the bullet.
- Never pad. 3 real new ideas beats 5 padded ones every time.
- Never produce confident output for Tier C books — refuse and request input.
- No stars. No scores. Directional verdicts only.
- 5-minute read regardless of book length. Compression is the feature.
