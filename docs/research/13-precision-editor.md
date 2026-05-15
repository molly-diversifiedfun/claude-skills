# Precision Editor — Research Results

The strongest signal from this research is a structural one: **AI editing tools fail not because they edit badly, but because they don't know which level they're operating at.** Professional editors don't have this problem. A copyeditor who restructured an author's chapter would get fired. An LLM does it on the first prompt. The publishing industry solved the level problem 80 years ago with named tiers (developmental, line, copy, proof) and explicit scope boundaries for each. Every successful AI editing prompt I could find smuggles those tiers in informally. The skill's job is to make that explicit — pick a level first, then enforce its scope.

What follows is the dimension-by-dimension breakdown.

---

## Q1: Four levels, defined by what they DON'T touch

The Editorial Freelancers Association and the Chicago Manual of Style converge on the same four-tier hierarchy. The terminology has minor variations across publishers but the scope boundaries are stable.

**Developmental editing (substantive, structural, content editing).** Operates on the whole manuscript. Deals with content, organization, and genre. The deliverable is usually a revision letter, not a marked-up text. Plot holes, pacing, structural reordering, character arcs, missing sections, thematic coherence. The editor proposes changes; the author rewrites. EFA defines this as "content, organization, and genre considerations." On a chapter level, the developmental editor will say "this section is in the wrong place" or "this argument is missing evidence" — they do not fix the prose itself.

**Line editing (sometimes called stylistic editing).** Operates at sentence and paragraph level. Focuses on style, rhythm, voice, clarity, transitions, and flow. The editor reworks awkward sentences, smooths transitions, tightens repetition, asks the author to reconsider word choices that fight the intended tone. Critically: the line editor preserves voice while clarifying it. Jane Friedman's framing: "tightening sentences and smoothing dialogue while keeping core mechanics intact." This is where the "edit vs. rewrite" line is most contested, because the line editor's job IS to touch sentences — but the rule is "improve the line the author wrote," not "write a better line."

**Copy editing.** Operates at the mechanical level. Spelling, grammar, punctuation, capitalization, treatment of numbers, formatting consistency, style-guide compliance (Chicago, AP, MLA), citation format, basic fact-checks. The Chicago Manual of Style calls this "mechanical editing." The copyeditor follows a style sheet and fixes violations. They do NOT restructure sentences, change word choices for style reasons, or rewrite for clarity unless something is genuinely ambiguous. ACES (the American Copy Editors Society) explicitly trains copyeditors that "if the only reason you can muster for revising text is 'I would never write it like that,' leave the sentence alone."

**Proofreading.** Operates on the typeset/final-format text. Catches typos, formatting errors, broken layouts, last-mile mistakes. By the time a manuscript reaches a proofreader, structural and stylistic decisions are locked. Proofreaders don't query the author's word choices. They flag typos, missing punctuation, layout breaks, and inconsistencies that survived the copy edit. EFA: "a final, super-meticulous check for surface-level errors."

**Pricing as a scope signal.** EFA's 2026 rate chart shows developmental editing at the highest hourly bands ($60-$90+), line editing in the middle ($50-$70), basic copyediting at $30-$40, and proofreading at $30-$45. The pay gradient mirrors the depth of intervention. Authors who pay for a copy edit and receive a developmental rewrite are entitled to refunds — the levels are contractually distinct.

**The "preserve author voice" rule.** Across every editorial style guide reviewed (ACES, Chicago, EFA, Cell Press, Indie Author Magazine), the same principle appears: editors are not permitted to substitute their preferences for the author's. The Cell Press editorial guide phrases it as "the author's voice is not a problem to be solved." ACES's three-step protection protocol: (1) read the whole piece before changing anything, (2) distinguish error from style choice, (3) when in doubt, query rather than change. Subtle word choices ("may" vs. "might," "until" vs. "till") are explicitly off-limits — these are voice fingerprints, not errors.

**Sources:** [EFA Editorial Service Definitions](https://www.the-efa.org/editorial-services-definitions/), [EFA 2026 Rate Chart](https://www.the-efa.org/rates/), [Chicago Manual of Style 18th edition](https://www.chicagomanualofstyle.org/), [Jane Friedman on editing levels](https://janefriedman.com/the-differences-between-line-editing-copy-editing-and-proofreading/), [ACES "Three Steps to Protecting the Author's Voice"](https://aceseditors.org/news/2019/three-steps-to-protecting-the-authors-voice), [Cell Press: Preserving Author Voice During Copyediting](https://crosstalk.cell.com/blog/preserving-author-voice-during-copyediting).

**Confidence: High.** The four-tier hierarchy is industry-standard, taught by every editorial association, and stable across decades. The voice-preservation rule is universal across professional editing literature.

---

## Q2: AI editing breaks because LLMs are trained to generate, not preserve

This is the skill's central design problem. The 2026 arXiv paper "Voice Under Revision" (Atari et al.) ran controlled experiments: even with explicit "preserve voice" prompts, frontier models pushed function words and first-person pronouns in the same direction (down), increased vocabulary diversity, and increased word length. Voice-preserving prompts reduced the magnitude of these shifts by 32% — but the direction persisted. The model knows how to soften the request but not how to refuse it.

The Junia.ai analysis crystallizes the failure mode: "LLMs are trained to generate, not preserve. They don't know which sentences are intentional, which phrasing carries personality, or what rhythm represents voice. To the model, everything is editable because nothing is sacred." When you say "improve this," the model interprets it as: "rewrite this in the safest, smoothest, most statistically common style possible."

Empirically: a 2026 Berkeley study cited in bookmoth's analysis found that LLMs made **3x the lexical changes humans made**, and even when prompted for "minimal grammar edits," the models replaced personal anecdotes with abstract phrasing and swapped first-person constructions ("I feel") for impersonal ones ("It is observed"). The Niche cognitive-debt research found heavy LLM editing produced a **70% increase in neutral argumentative stances** and significant loss of personal voice.

**What works (from the prompt-engineering literature):**

1. **Specify what to change AND what not to change.** Generic "improve this" loses every time. "Edit for clarity. Do not change word choices that don't have a grammatical error. Do not restructure sentences. Flag anything you'd want to change but couldn't" — this works because it gives the model a refusal channel.

2. **Make the model surface what it wanted to change but didn't.** Writing tools researcher Louis Bouchard's "editor cleanup system" uses a separate "editor" model whose only job is to find and label issues, never rewrite. The Anchorchange Substack approach: "review, don't rewrite. Paste the draft. Get a list. Decide what to fix yourself."

3. **Constrain with named scope.** Marketingaid.io's interview with editorial AI users found the most reliable pattern was naming the editorial level explicitly — "act as a copy editor working only at the level of grammar and punctuation" beat "edit lightly" by a wide margin. The named level imports the scope rules with it.

4. **Show before/after with a delta.** When the model has to itemize what it changed and why, it changes less. The accountability structure is the constraint. This is the redline/track-changes pattern from publishing — the editor's marks are visible and the author can reject each one.

5. **Repeat the constraint at the end.** Liu et al.'s "Lost in the Middle" attention-decay finding (referenced in the voice-extractor research) applies here too. Critical instructions like "do not rewrite" need front-loading AND end-loading; otherwise the model loses them by the time it generates output.

**The "improvement reflex" failure.** The most insidious AI editing failure isn't bad edits — it's polishing things that were already fine. The model encounters a sentence that's slightly idiosyncratic ("She bought eggs and was furious about it.") and rewrites it to be slightly less interesting ("Frustrated, she purchased the eggs."). The original survived professional copy editing; the AI version would be flagged as voice-killing in a real edit. The fix is explicit: "if a sentence has no grammatical error and no ambiguity, leave it alone, even if you'd write it differently."

**Sources:** ["Voice Under Revision" (Atari et al., arXiv 2026)](https://arxiv.org/html/2604.22142), [Junia.ai: LLM Default Voice](https://www.junia.ai/blog/llm-default-voice-ai-writing), [Louis Bouchard: How to Clean Up AI Drafts](https://www.louisbouchard.ai/ai-editing/), [Anchorchange: How to Edit Without Losing Your Voice](https://anchorchange.substack.com/p/how-to-edit-without-losing-your-voice), [Marketingaid.io: AI as Writing Partner](https://www.marketingaid.io/most-writers-are-using-ai-wrong-heres-the-workflow-that-fixes-it/), [Niche: AI Writing and Cognitive Debt](https://niche.org.uk/ai-writing-authenticity-cognitive-debt), [Hacker News thread: We're losing our voice to LLMs](https://news.ycombinator.com/item?id=46069771).

**Confidence: High.** Multiple peer-reviewed sources, strong community signal, and consistent practitioner experience.

---

## Q3: Output formats — match the level

Each editing level has a publishing-standard output format. The skill should match those, not invent new ones.

**Level 1 (flag only)** maps to the proofreader's marked-up margin or the developmental editor's reader's report. Best format: **numbered issue list with quoted excerpts**. Each entry has a location reference (paragraph 3, sentence 2), the quoted text, and the issue category (grammar, clarity, voice, fact, structure). No suggested fix. The author decides whether to act on it.

**Level 2 (suggest as comments)** maps to Microsoft Word track-changes with comments enabled. Best format in chat: **original text reproduced, with bracketed suggestions inline** like `[suggest: change "utilize" to "use" — corporate jargon]`. Or, for longer pieces, a numbered-comment system where superscript numbers in the text reference numbered suggestions below. The original is intact. The author can copy-paste their version with surgical changes.

**Level 3 (light copy edit)** maps to the copyeditor's clean copy + redline. Best format: **two artifacts** — the edited text (clean) and a change log (what changed and why, grouped by category). The change log is the accountability mechanism. Without it, the author can't audit whether the edit stayed in scope. With it, the author can reject any change and preserve the original.

**Level 4 (developmental edit)** maps to the editorial revision letter + suggested restructuring. Best format: **editorial memo first, then optional rewrite**. The memo names the structural issues, suggests the reorganization, and lets the author decide whether to do the rewrite themselves or accept the AI's draft. Crucially: at level 4, the rewrite is explicitly allowed — but the author opted into it.

**Chat interface vs. artifact tradeoffs.** In a chat interface, levels 1-2 work inline. Levels 3-4 should produce a downloadable or copyable artifact (markdown file) because the change log + clean copy combination doesn't render well as conversational output.

**Sources:** [Microsoft Word track changes documentation](https://support.microsoft.com/en-us/office/track-changes-in-word-197ba630-0f5f-4a8e-9a77-3712475e806a), [Debbie Emmitt: Tracked changes pro tips for authors](https://www.debbie-emmitt.com/tracked-changes-and-comments-in-word-pro-tips-for-authors-with-videos/), [PaperCheck: Track Changes guide](https://www.papercheck.com/resources/microsoft-word-track-changes), [University of Illinois Law Library: Track Changes for legal writing](https://libguides.law.illinois.edu/c.php?g=1272613&p=9336248).

**Confidence: Medium-High.** Output format conventions are well-established in publishing. The translation to chat interface is a design judgment, not a researched best practice.

---

## Q4: Existing AI editing tools — all operate at one level, none let the user pick

**Grammarly** operates at copy-edit + proofread level. Grammar, spelling, tone suggestions, occasional clarity nudges. Voice preservation is decent because the scope is narrow — Grammarly mostly leaves your sentences alone. Failure mode: tone suggestions sometimes drift into voice rewriting ("Make this more confident" rewrites the sentence).

**Hemingway Editor** operates at line-edit level (readability, sentence length, passive voice flags). It flags but doesn't rewrite — the user fixes things themselves. This is the cleanest "level 1 (flag only)" implementation in the wild. It works because it doesn't try to do more than its scope.

**ProWritingAid** operates across multiple levels (copy through line) with separate "reports" for grammar, style, readability, repetition, etc. The user picks which report to run. This is the closest existing tool to the level-picker model — but the "levels" are feature axes, not scope tiers.

**Sudowrite** is a fiction-specific tool with a "Muse" model trained for voice preservation and a "Style" box for sample-based prompting. Despite the dedicated architecture, the 2026 Berkeley study found Sudowrite's voice preservation degrades over long-form output. Sudowrite operates closer to a developmental + line-edit hybrid — it's designed to extend and rewrite, not to preserve.

**Claude and ChatGPT (general use)** have no editing-level convention. Users invent their own through prompts. The langgptai/awesome-claude-prompts repo includes several "editor mode" prompts that smuggle in level definitions ("act as a copy editor, only fix grammar and punctuation"). These work — they just require the user to be a prompt engineer.

**The gap the skill fills.** No tool surveyed lets the user pick a named editing level before the AI touches the text and then enforces that level's scope. Hemingway is closest but is locked to one level. ProWritingAid is closest in structure but uses feature-axes instead of editorial-tier names. The skill's contribution is the named-tier-with-scope-enforcement pattern, applied to general-purpose AI editing.

**Sources:** [ProWritingAid: Hemingway vs Grammarly comparison](https://prowritingaid.com/hemingway-vs-grammarly), [Tools for Writing: Grammarly vs Hemingway vs ProWritingAid](https://toolsforwriting.com/blog/grammarly-vs-hemingway-vs-prowritingaid), [Sudowrite product page](https://sudowrite.com/), [Bookmoth: AI Writing Tools That Preserve Voice (Berkeley study)](https://bookmoth.app/blog/ai-writing-tool-that-preserves-voice/), [langgptai/awesome-claude-prompts](https://github.com/langgptai/awesome-claude-prompts).

**Confidence: High** on tool capabilities, **Medium** on the gap claim — there may be specialized professional tools the consumer-facing search missed.

---

## Key Design Decisions

| Decision | Choice | Why |
|----------|--------|-----|
| Level selection — when | **Before the skill touches a single sentence** | The biggest failure mode in AI editing is the model deciding the level for you. Forcing the user to pick first imports the scope rules with the choice. |
| Number of levels | **Four, mapped 1:1 to publishing tiers** (flag / suggest / copy edit / developmental) | Industry-standard names import scope conventions for free. Inventing "level 1.5" or "moderate edit" loses that signal. |
| Default level if user is unsure | **Level 2 (suggest)** | Suggest is the safest non-trivial level. Author's text is preserved; AI's input is visible; author decides what to apply. Default at a level that can't damage the original. |
| Change-log requirement | **Mandatory at levels 2-4, optional at level 1** | The change log is the accountability mechanism. Without it, scope creep is invisible. With it, the author can audit whether the AI stayed in its lane. |
| Refusal channel for the model | **Required at every level** | Models that can't say "I'd want to change this but it's out of scope" will silently rewrite instead. A "wanted to change but didn't" section traps the rewrite reflex. |
| Voice preservation guardrails at levels 1-3 | **Block list of changes the model is forbidden from making** — no word swaps for style ("utilize" → "use"), no sentence restructuring, no idiom replacement, no tone shifts | Generic "preserve voice" doesn't work (Atari et al. showed it's a 32% softener at best). Specific prohibitions work. |
| Show before/after | **Always, redline-style** | Track-changes is the publishing standard. Hidden edits are unauditable. The clean copy is offered separately, not instead. |

---

## Editing Level Spec

### Level 1 — Flag Only

**Touches:** Nothing in the original text.

**Outputs:** Numbered list of issues. Each entry has location, quoted excerpt, issue type. No suggested fix.

**Scope:** Grammar errors, spelling errors, factual claims worth checking, ambiguous sentences, voice inconsistencies, structural concerns. The model says "here's what I noticed." The author decides what to do.

**Forbidden:** Any rewriting. Any "and here's how to fix it" content. Any unsolicited improvement suggestions.

**Before/After example:**

> *Original:* "The team utilized agile methodologies to ship the feature in a timely manner."
>
> *Level 1 output:* "1. Paragraph 1, sentence 1: 'utilized' and 'in a timely manner' are corporate jargon — flag for review. 2. Paragraph 1, sentence 1: 'agile methodologies' is plural; check whether singular ('agile methodology') is intended. No grammatical errors found."

### Level 2 — Suggest as Comments

**Touches:** Nothing in the original text.

**Outputs:** Original text reproduced verbatim, with bracketed suggestions inline. Each suggestion includes the proposed change and a one-line reason.

**Scope:** Same as Level 1, plus optional alternative phrasings for clarity issues. The author copy-pastes the original, accepts or rejects each bracketed suggestion manually.

**Forbidden:** Replacing sentences. Producing an "edited version." Any output where the original isn't preserved verbatim alongside the suggestions.

**Before/After example:**

> *Original:* "The team utilized agile methodologies to ship the feature in a timely manner."
>
> *Level 2 output:* "The team utilized [suggest: 'used' — 'utilized' is corporate jargon] agile methodologies to ship the feature in a timely manner [suggest: 'on time' or 'fast' — 'in a timely manner' is filler]."

### Level 3 — Light Copy Edit

**Touches:** Grammar errors, spelling errors, punctuation, capitalization, formatting consistency, style-guide violations. May tighten obvious redundancies (double words, "in order to" → "to") but only when the change is mechanical, not stylistic.

**Outputs:** Two artifacts: clean edited text + change log. Change log groups changes by category and quotes original → revised for each.

**Scope:** What a professional copyeditor would do, scoped tight. Mechanical fixes only. Preserves the author's sentences as-written if they're not broken.

**Forbidden:** Rewriting sentences for style. Replacing word choices that aren't errors ("until" → "till," "may" → "might"). Restructuring paragraphs. Smoothing transitions. Changing tone. Adding or removing content. ACES rule: "If your only reason is 'I would never write it like that,' leave it alone."

**Before/After example:**

> *Original:* "The team utilized agile methodologies to ship the feature in a timely manner. They're proud of how it turned out, despite the rough start they had."
>
> *Level 3 output:* "The team utilized agile methodologies to ship the feature in a timely manner. They're proud of how it turned out despite the rough start they had."
>
> *Change log:* "Removed comma before 'despite' — restrictive clause, no comma needed. No other changes."

(Note: "utilized" and "in a timely manner" survive the copy edit. They're not errors. A copyeditor would query them, not change them.)

### Level 4 — Heavy Developmental Edit

**Touches:** Anything, with the author's permission.

**Outputs:** Editorial memo first (structural issues, suggested reordering, gaps in argument). Optional rewrite second, only if requested. Memo lists each proposed structural change with reasoning.

**Scope:** Full developmental editor's toolkit. Restructuring, expansion, condensation, gap-filling, tone shifts, voice tightening. The author has explicitly opted into having their text reworked.

**Forbidden:** Surprising the author. Skipping the editorial memo. Producing a rewrite without the memo first. Treating opting into level 4 as opting into a single specific style of rewrite — the model still asks before substituting voice.

**Before/After example:**

> *Original:* "The team utilized agile methodologies to ship the feature in a timely manner. They're proud of how it turned out, despite the rough start they had."
>
> *Level 4 memo:* "Two sentences doing four jobs (process, outcome, emotion, history). Suggest splitting into a process sentence + a result sentence + a brief story callback. The corporate-jargon vocabulary fights the personal pride beat — recommend reaching for plainer verbs to let the emotion land. Want me to draft the rewrite?"
