# Book Distiller — Research Results

The strongest signal across this research is a contradiction worth naming up front: **the people who do the best book analysis don't summarize at all — they argue.** NYRB review-essays, Tyler Cowen's interview prep, and the better Goodreads-killer reviewers all converge on the same posture: state what the book is trying to do, judge whether it does it, and locate it in a longer conversation. The summary is a means, not the product. That's the design target. The harder question is whether Claude can do the *locating in a longer conversation* part — the intellectual genealogy — without confabulating. Q2 finding: partially. The genealogy feature survives, but with strong guardrails and a confidence ladder, not as a hero feature.

---

## Q1: What makes book criticism useful vs. just shorter

Four traditions of useful book analysis kept showing up: the long review-essay (NYRB, LRB), the academic critical review, the prepared interview (Cowen, Ferriss), and the contrarian operator review (Sattersten on *Good to Great*, Replicability-Index on *Thinking, Fast and Slow*). They share five structural moves and almost nothing else.

**Move 1: The argument, stated early.** A review makes an argument; it's a commentary, not a summary (UNC Writing Center, USC Libraries). When NYRB founders Silvers and Epstein launched in 1963, the brief was three thousand words in three weeks — long enough to make a real claim, fast enough that the claim still mattered. The shortest reviews "have a structure of necessity to get in and out fast"; review-essays have an argument structure that earns the length. Actionable for the skill: lead with a 2-sentence thesis about the book, not a 2-sentence summary of the book. Different objects.

**Move 2: Summary is bounded.** Across academic guides, the summary is "about a third of the critical review" (USC, UNC, U-Toronto). Anything more and the review collapses into Blinkist. The skill's compression target should sit well under that — closer to 1/10 — because the user reads the skill output *instead of* the book or as triage *for* the book.

**Move 3: Evaluation against the book's own goals.** Strong reviews "integrate a summary with constructive insight and critique regarding the extent to which the work succeeds in achieving its goals" (USC). This is the move Blinkist cannot make because Blinkist refuses to have a position. It's also what Replicability-Index did to *Thinking, Fast and Slow* — graded each chapter against the book's empirical claims, found Chapter 4 had an R-Index of 19, and Kahneman publicly agreed (Retraction Watch, 2017). That's the upper bound of useful: a review that the author concedes.

**Move 4: Locate the book in a conversation.** The "contribution to the conversation" frame is the one move Blinkist, Shortform, and most podcast hosts skip. The Foucault-genealogy review tradition (Notre Dame Philosophical Reviews) treats this as the central job: a book is a move in an ongoing argument with prior moves. For the skill, this becomes the "What's actually new" and "What's recycled" sections — the parts that justify reading or skipping.

**Move 5: A directional recommendation, not a star rating.** Cowen's interview prep ("read everything they wrote, then look for what hasn't been explored enough") and Ferriss's stated approach ("if I find it interesting, I have a guaranteed audience of one") both produce directional verdicts: who should engage with this, on what terms, and what to skip. The skill should output the same shape — *who this is for, who should skip it, and what to read instead* — never a 4.2/5.

**One more finding worth flagging.** Cowen now uses LLMs as part of his prep — for the Donald Lopez Buddhism episode, GPT queries replaced "a few hundred dollars" of book purchases. He still read 30 books, but the LLM did the second-tier reading. That's the actual job-to-be-done for this skill: triage what's worth your full attention, surface the ideas worth taking seriously, and tell you what to skip — not replace the reading you'd actually do.

**Sources:** [UNC Writing Center on Book Reviews](https://writingcenter.unc.edu/tips-and-tools/book-reviews/), [USC Libraries Writing Guide](https://libguides.usc.edu/writingguide/assignments/bookreview), [University of Toronto Writing Advice](https://advice.writing.utoronto.ca/types-of-writing/book-review/), [The Scholarly Kitchen on review craft](https://scholarlykitchen.sspnet.org/2017/01/09/the-art-and-craft-of-review/), [Conversations with Tyler retrospectives](https://conversationswithtyler.com/), [Notre Dame Philosophical Reviews](https://ndpr.nd.edu/reviews/genealogy-as-critique-foucault-and-the-problems-of-modernity/). Read yourself: a few NYRB long-form reviews of books you know well — the structural pattern is more visible than any meta-guide describes.

**Confidence: High** on the structural moves (academic and editorial guides converge). **Medium** on the claim that this transfers cleanly to LLM output — none of the source material is about machine-generated criticism.

---

## Q2: Can Claude reliably identify original vs. recycled ideas?

Mostly no, but better than expected on books with strong public criticism, and the failure modes are predictable enough to design around. This is the single most important finding for the skill's scope.

**What works.** For canonical books with extensive secondary literature, the genealogy is well-documented and Claude has it. *Thinking, Fast and Slow* is the test case: there is a public, well-known critical apparatus around it — the Kahneman/Tversky 1974 *Science* paper "Judgment Under Uncertainty" predates the book by 37 years and contains the core heuristics-and-biases framework; the priming-research concerns and 2017 partial retraction are documented; even the deeper genealogy (cognitive illusions formulated by Laplace in the early 1800s) appears in the academic conversation. Claude can reliably surface "this chapter is the 1974 paper made readable; this chapter is the part that didn't replicate." That's real value.

Same for *Good to Great*: the critical literature (Phil Rosenzweig's halo-effect critique, Steven Levitt on portfolio underperformance, Todd Sattersten's "Might and Myth" essay) provides the genealogy. Many findings Collins reports "are supported by other peer-reviewed research, something Collins fails to use." A skill that surfaces this is doing the job.

**What breaks.** Three failure modes, in order of severity:

*False attribution.* Claude will confidently claim Idea X comes from Author Y when it's a closer-but-wrong neighbor. The Bibliotechnism paper (arxiv 2401.04854) frames this well: even novel LLM sentences derive their meaningfulness from inputs, which makes them prone to "derivative meaning" errors — the claim *sounds* right because the connections are statistically near, not because they're documented. Mitigation: never attribute without naming a specific work and year, and downgrade confidence when both can't be supplied.

*Missed borrowing.* Recent or niche books (post-2024, indie publishers, small academic presses) sit outside Claude's training apparatus. The skill will pattern-match to nearby better-known books and miss the actual lineage. Mitigation: a thin-data warning, surfaced before the genealogy section runs, plus an offer to accept user-pasted notes/highlights.

*Hallucinated lineage.* The most dangerous failure: confident, well-formed claims about influence that are simply invented. Survey work on hallucinations (Lilian Weng, Lakera 2026 guide, Frontiers 2025 survey) consistently finds that fluent fabrication is the hardest mode to detect because the output looks well-structured. Mitigation: the genealogy section must be confidence-tiered — *documented* (named source + year), *plausible* (consistent with the literature but not explicitly cited), *likely-original-or-uncertain* — and the skill must default to the lowest defensible tier.

**Verdict for the feature.** Intellectual genealogy survives, but reframed. Not "trace every idea to its source" — that overpromises. Instead: "flag the 3-5 ideas where I'm confident about lineage, and call out where I think the book is reusing well-known prior work." Books with thin training-data coverage get a warning and a pared-back genealogy section. This is the design that ships.

**Sources:** [Replicability-Index meta-scientific perspective on Thinking Fast and Slow](https://replicationindex.com/2020/12/30/a-meta-scientific-perspective-on-thinking-fast-and-slow/), [Retraction Watch on Kahneman's admission](https://retractionwatch.com/2017/02/20/placed-much-faith-underpowered-studies-nobel-prize-winner-admits-mistakes/), [Rosenzweig and Sattersten critiques of Good to Great](https://toddsattersten.com/2011/06/13/the-might-and-myth-of-good-to-great/), [N2Growth's "Rethinking Good to Great"](https://www.n2growth.com/rethinking-good-to-great/), [Bibliotechnism paper on LLMs and derivative meaning](https://arxiv.org/html/2401.04854v1), [Lilian Weng on extrinsic hallucinations](https://lilianweng.github.io/posts/2024-07-07-hallucination/), [Lakera 2026 hallucination guide](https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models). Read yourself: the Replicability-Index post — it's the model for how confident, well-cited critique should look.

**Confidence: Medium-High** on the failure modes (well-documented in the LLM hallucination literature). **Medium** on the specific feasibility threshold — would harden to High after a structured eval across 20 books with known genealogies.

---

## Q3: Books with thin training data

Three tiers, three behaviors. The skill needs to handle all three without faking competence on the bottom tier.

**Tier A — Bestsellers and canon (deep coverage).** Pre-2024 bestsellers, anything with Wikipedia entries longer than two paragraphs, anything cited in academic literature. Claude can produce the full distillation cleanly. No special handling needed.

**Tier B — Mid-list and recent (partial coverage).** Books published 2024-2026, mid-list nonfiction, books with a few reviews but no academic apparatus. Claude has the publisher copy, some review snippets, possibly the table of contents. The skill should: name what it actually knows (book exists, published year, broad category), warn that the genealogy section will be thin, and offer to accept user-provided highlights, the table of contents, or a few key passages as input. With those, Tier B becomes Tier A for the duration of the conversation.

**Tier C — Niche, indie, recent academic, foreign-language.** Claude may have the title and not much else. The skill should refuse to fake it: "I don't have enough on this one to do the analysis well. If you can paste the table of contents and 2-3 passages you found striking, I can work from those." This is the inverse of the failure mode that wrecks Blinkist — produce confident output regardless of underlying knowledge. Refusing is the feature.

**Detection heuristic.** Before generating the distillation, the skill should silently self-assess: can I name the publisher, year, central thesis, and at least one specific argument or chapter? If three of four come back yes, Tier A. If two, Tier B. If one or zero, Tier C. This is a calibration step the user never sees, but it gates which version of the output runs.

**Sources:** [Hallucination survey from arxiv 2311.05232](https://arxiv.org/pdf/2311.05232), [Frontiers survey on hallucination prompting strategies](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1622292/full).

**Confidence: Medium-High.** The tiered approach is supported by hallucination-mitigation literature. The specific 4-question heuristic is judgment, not from a paper.

---

## Q4: What existing tools exist and what they get wrong

Blinkist, Shortform, Headway, ChatGPT free-form summaries, Goodreads reviews, the long tail of "book summary" sites. Three structural complaints recur and one of them is the gap this skill targets.

**Complaint 1: Surface-level oversimplification.** "15-minute summaries can't capture nuance, case studies, or detailed arguments — users get the 'what' but often miss the 'why'" (makeheadway.com review of Blinkist). Reviewers compare Blinkist outputs to ChatGPT and find them "surprisingly similar" — Blinkist's editorial moat is gone. Shortform is judged better but still, per reviewers, "miss[es] much of the nuance and practical advice." The shared failure: they all preserve everything proportionally, which makes them all about as useful as the table of contents.

**Complaint 2: Mechanical voice and AI tells.** Recent Blinkist summaries show "telltale signs of AI-generated content," with "language [that] feels mechanical and lacks the nuanced interpretation expected from expert human curators." Quality varies by summary. The market has the tooling; what it lacks is point of view.

**Complaint 3 — the gap.** None of these tools say "skip this." Every Blink, every Shortform guide, every Goodreads review is built to validate the user's interest in the book. There is no commercial product whose business model survives telling 30% of users "this isn't for you, read X instead." That's the opening. An opinionated distillation that names the audience, names the skip-list, and names the better book if there is one — that's the differentiated output. It also explains why this is a skill rather than a product: skills can afford to be useful in ways products can't monetize.

Honorable mention: Tyler Cowen's *Conversations with Tyler* prep notes (the part that gets published as the episode itself) and Derek Sivers' [book notes](https://sive.rs/book) are the closest existing analogues to what this skill should produce. Both are short, opinionated, and skip-the-book-if-X friendly.

**Sources:** [makeheadway Blinkist review](https://makeheadway.com/blog/is-blinkist-worth-it/), [makeheadway Shortform vs Blinkist](https://makeheadway.com/blog/shortform-vs-blinkist/), [Nate Shivar's Blinkist pros/cons](https://www.nateshivar.com/27734/blinkist-book-summaries-review/), [Keith Lang on book-summary apps](https://keithjlang.com/book-summary-apps/), [Derek Sivers' book notes](https://sive.rs/book). Read yourself: 3-4 Sivers notes on books you've read — the format is closer to the target than anything else public.

**Confidence: High.** User complaints across multiple review sites converge. The "no tool says skip" gap is observable directly.

---

## Key Design Decisions

| Decision | Choice | Why |
|----------|--------|-----|
| **Argument-first vs. summary-first** | Argument-first — open with a 2-sentence thesis *about the book*, not *of the book* | Every strong review tradition (NYRB, academic, Cowen-style) leads with a position. Summary-first collapses into Blinkist. |
| **Compression ratio** | Aggressive — output reads in 5 minutes regardless of book length | Academic guides cap summary at 1/3 of a review; this skill is reaching for ~1/20. The skill replaces (or triages) the reading; it doesn't duplicate it. |
| **Genealogy as hero feature vs. supporting feature** | Supporting, with confidence tiers | Q2 finding: Claude can do this for well-documented books, fails confidently on niche ones. Tiered confidence (documented / plausible / uncertain) keeps the feature without the hallucination risk. |
| **One output or tiered outputs** | Single output, but the *content* tiers based on training-data depth | Tier A (bestsellers): full distillation. Tier B (recent/mid-list): distillation + thin-data warning + offer to accept user notes. Tier C (niche): refuse to fake it; ask for user input first. |
| **Star rating vs. directional verdict** | Directional verdict only — *who this is for, who should skip, what to read instead* | Stars validate; directional verdicts triage. The skill's job is triage. |
| **Recycled-ideas section: include or skip** | Include, with strict citation rules | Forces specificity ("Idea X appears earlier in Y, 1974"). Empty section is acceptable — better than confabulation. |
| **3 unanswered questions: useful or filler** | Useful — they're the most-cited shareable artifact in actual reviews | Cowen's prep, NYRB essays, and the better Substack reviewers all end with "what this book doesn't address." It's the move that makes a review feel like the start of a conversation, not the end. |

---

## Book Distillation Template v1

The output the skill produces. Example content uses *Thinking, Fast and Slow* by Daniel Kahneman (Tier A — extensive training data, well-documented genealogy).

```markdown
# Book Distillation: Thinking, Fast and Slow
**Author:** Daniel Kahneman | **Published:** 2011 | **Knowledge depth: deep**

## Core Thesis (2 sentences)
Kahneman argues that human thinking runs on two systems — fast, intuitive,
and pattern-matching versus slow, deliberate, and effortful — and that most
of what we get wrong comes from System 1 running unchecked when System 2
should have intervened. The book is the popularization of 40 years of
heuristics-and-biases research, structured as a tour of the specific
predictable errors System 1 makes.

## 5 Genuinely New Ideas (or new framings of older ideas)
1. **The two-systems metaphor as readable scaffolding.** Kahneman is explicit
   that System 1 / System 2 are not real brain regions; they're a teaching
   device. The framing made dual-process theory transmissible outside
   psychology. (Original contribution: the framing, not the underlying theory.)
2. **The experiencing self vs. remembering self.** The peak-end rule and its
   implications for how we evaluate our own lives. This is the book's
   strongest original-feeling argument and the one that holds up best.
3. **Loss aversion's coefficient (~2x).** The specific empirical claim that
   losses feel roughly twice as bad as equivalent gains. Operationalizable in
   product, pricing, and negotiation work.
4. **The planning fallacy as a class of error, not a personality trait.**
   Reframing chronic underestimation as a structural feature of inside-view
   thinking. Useful for project planning regardless of the rest of the book.
5. **The narrative fallacy applied to expertise.** The skewering of pundit
   forecasting and CEO biographies — the part where the book gets meanly
   funny.

## What's Recycled
- **Heuristics and biases.** The core framework is the 1974 *Science* paper
  with Tversky, "Judgment Under Uncertainty: Heuristics and Biases." If
  you've read the original, the first third of the book is review.
- **Prospect theory.** The 1979 *Econometrica* paper. Chapter 26 onward
  is largely the paper made narrative.
- **The priming chapter (Ch. 4) didn't survive replication.** Kahneman
  publicly conceded in 2017 that he "placed too much faith in underpowered
  studies" — Replicability-Index gave Ch. 4 an R-Index of 19. Read it
  knowing the empirical scaffolding is shaky.
- **Cognitive illusions as a concept** trace back to Laplace in the early
  1800s. Kahneman didn't invent the territory; he mapped it for a wider
  audience.

## Who Should Read It
- Anyone making product, pricing, or policy decisions who has not yet read
  the underlying papers.
- Writers who want a master class in making 40 years of academic work
  accessible without dumbing it down.
- Anyone whose job involves predicting human behavior and who is currently
  over-confident about it.

## Who Should Skip It
- People who've read the 1974 *Science* paper and the 1979 prospect theory
  paper. You have ~80% of the book.
- People who want operational decision tools right now. Read *Noise*
  (Kahneman/Sibony/Sunstein) or Annie Duke's *Thinking in Bets* instead.
- People allergic to academic memoir structure. The book is long and the
  middle drags.

## 3 Questions the Book Doesn't Answer
1. **How much of the heuristics-and-biases program survived the 2010s
   replication crisis?** The book was published before the crisis broke.
   It does not address what's been retracted, weakened, or contested.
2. **What do you actually do about it?** The book is exhaustive on
   diagnosis and thin on intervention. Awareness of biases doesn't reliably
   reduce them — a finding largely absent here.
3. **Why are some biases sticky and others not?** The book treats biases
   as roughly equivalent; later research suggests massive variance in how
   trainable each one is. Worth reading [name a recent overview] alongside.

---
*Distillation depth: deep training data. Confidence on genealogy: high
(papers and dates are documented). If you want me to focus on any
section in more detail, say so.*
```

For Tier B and Tier C books, the same template runs but with these adjustments: a thin-data banner at the top, the "What's recycled" section either pared back or marked *uncertain*, and an offer near the bottom inviting the user to paste highlights or chapter titles for a second pass.
