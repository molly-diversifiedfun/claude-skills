---
name: ai-tell-killer
description: Detect and surgically remove AI writing patterns from text. Use when user wants to make AI-generated text sound human, remove AI tells, humanize AI writing, fix robotic prose, or beat AI detection through better writing. Trigger on phrases like "this sounds like AI," "make this more human," "remove AI tells," "humanize this," "this reads like ChatGPT," "AI fingerprint," "sounds robotic," or any request to edit AI-generated text to read as human-written. NOT for rewriting from scratch — that destroys voice. NOT for editing human-written text — use precision-editor for that.
---

# AI Tell Killer

## What This Skill Does

Takes AI-generated or AI-assisted text, identifies specific AI patterns using a categorized taxonomy with confidence ratings, and surgically fixes only the flagged patterns. Everything else stays untouched. Two-pass architecture: first pass catches known tells, second pass audits for anything the first pass missed.

This is not a rewriter. Rewriters make text worse 74% of the time (Masrour et al., ACL 2025). This is a pattern detector and surgical editor.

**Goal:** Remove the machine fingerprint. Not fool AI detectors (they're unreliable). Make the text stop *feeling* AI-generated to human readers.

**Core principle:** Change fewer than 20% of sentences. If you're changing more, something is wrong.

## Before You Start

Read the full taxonomy at `references/tell-taxonomy.md` in this skill's directory. That file contains every detection rule, genre threshold, and fix strategy. This file defines the interaction flow and operating rules.

---

## Step 1: Input + Preset Selection

When the user provides text, ask:

> **What's the genre?**
> (a) Blog post
> (b) Business / email / report
> (c) Academic
> (d) Creative fiction
> (e) Social media
>
> This adjusts what gets flagged. Academic writing tolerates more hedging. Creative writing has a lower threshold for AI vocabulary. Pick the closest match.

If the user specifies genre in their initial message, skip the question and proceed.

**Store the genre preset.** It controls every threshold in the taxonomy.

---

## Step 2: First Pass — Pattern Detection + Annotation

Scan the user's text against the full taxonomy (references/tell-taxonomy.md). Work through each category systematically:

### Scan Order (structural and rhythm first — these matter most)

1. **Rhythm** — Calculate sentence-length variation. Check for sterile perfection.
2. **Structure** — Summary paragraphs, heading inflation, list overuse, tricolon, parallel construction.
3. **Vocabulary** — Cluster detection (3+ co-occurring words), hedging phrases, elegant variation.
4. **Transitions** — Stacked formal transitions, "Let's explore" patterns, mechanical intervals.
5. **Punctuation** — Em dash density, absence patterns.
6. **Semantic** — False balance, signposting, cliche openers. Only flag these if Tier 1/2 tells already present.

### Apply genre thresholds

Use the threshold tables in the taxonomy for every detection rule. A blog post and an academic paper have different tolerances.

### Output the Annotated Report

Present findings in this exact format:

```
## AI Tell Report

**Overall AI Signature: [None / Low / Medium / High]**
([N] patterns detected across [N] categories)

### Flagged Patterns

1. **[CATEGORY]** Lines [X-Y]: [What was detected and why].
   Confidence: [High / Medium].
   → Suggested fix: [Specific replacement text or structural change.
   Show the exact before and after.]

2. **[CATEGORY]** Lines [X-Y]: [Description].
   Confidence: [High / Medium].
   → Suggested fix: [Specific fix.]

[Continue for all flagged patterns]

### Passed (not flagged)
- [Category]: [Brief reason it passed]
- [Category]: [Brief reason it passed]
```

**Rules for the report:**
- Number every flagged pattern.
- Always state the category in brackets: VOCABULARY CLUSTER, RHYTHM, STRUCTURE, TRANSITION, PUNCTUATION, SEMANTIC, OPENING.
- Always include confidence level.
- Every flag MUST have a specific suggested fix — not "consider revising" but the actual replacement text.
- The "Passed" section builds trust. Show the user what you checked and found acceptable.
- If zero patterns found, say so: "No AI tells detected at [genre] thresholds. This text reads as human-written."

### Severity Scale

- **High (3+ categories flagged):** "This text has a strong AI signature. Multiple pattern types co-occur."
- **Medium (2 categories flagged):** "Moderate AI signature. A few patterns stand out."
- **Low (1 category flagged):** "Mild AI signature. One pattern type detected."
- **None:** "No AI tells detected at these thresholds."

---

## Step 3: User Review

After presenting the report, ask:

> **How do you want to proceed?**
> (a) Apply all fixes
> (b) Review each fix individually — I'll show them one at a time and you approve or reject
> (c) Apply all except [list numbers to skip]

Wait for the user's response. Do not apply any fixes until instructed.

If the user chooses (b), present each fix as:

> **Fix [N]: [CATEGORY]**
> Before: "[exact original text]"
> After: "[exact proposed replacement]"
> Apply this fix? (y/n)

---

## Step 4: Second Pass — Residual Audit

After applying the approved fixes from Step 3, re-read the complete edited text as a whole. Do not re-check against the taxonomy mechanically — instead, read it as a skeptical human reader who regularly encounters AI output.

Ask yourself: **"What still feels AI-generated about this text?"**

The second pass catches:
- Structural patterns that only become visible after vocabulary fixes (the "uncanny valley" where individual sentences are fine but the overall flow is mechanical)
- Rhythm problems created by the first-pass edits themselves
- Patterns the taxonomy doesn't cover but a perceptive reader would notice

If the second pass finds issues, present them the same way as Step 2 — numbered, categorized, with specific fixes. Ask the user to approve before applying.

If the second pass finds nothing: "Second pass complete. No remaining AI signature detected."

---

## Step 5: Output

Deliver the final edited text. Then offer:

> **Want a diff view?** I can show exactly what changed, line by line.

If the user says yes, show a before/after comparison with changes marked. Use strikethrough for removed text and bold for added text, or a side-by-side format — whatever is clearest for the amount of changes.

---

## Hard Rules — Never Violate These

### Surgical editing, not rewriting
- If more than 30% of sentences change, stop and reassess. You are overcorrecting.
- Preserve the author's sentence structure, argument order, and examples unless they are themselves AI tells.
- The user should recognize the output as their own text with targeted fixes.

### Co-occurrence, not word bans
- Never flag a single vocabulary word in isolation. The signal is clustering — 3+ AI-associated words in proximity.
- "Robust" in an engineering paper is fine. "Robust, nuanced, and multifaceted" in a blog post is a tell.
- ESL writers, academic writers, and formal prose all share features with AI output. Single-word flags produce unacceptable false positives.

### Structure and rhythm over vocabulary
- Prioritize fixing sentence-length uniformity and structural patterns over swapping individual words.
- Synonym swapping alone does not change the statistical fingerprint. Rhythm and structure do.

### Never add deliberate errors
- Do not introduce typos, grammatical mistakes, or awkward phrasing to seem "more human."
- This is the Undetectable.ai failure mode. It degrades quality without fooling anyone.

### Never strip all structure
- Well-organized writing is not an AI tell. Formulaic organization is.
- A blog post with three clear sections is fine. A blog post where every section has exactly three bullet points with bold lead-ins is a tell.

### Never remove human signals
- Contractions, first-person pronouns, personal anecdotes, sentence fragments, and informal punctuation are HUMAN signals.
- If these are present in the input, preserve them. If they're absent, consider adding them as fixes.

### Em dashes are not the enemy
- 1-2 em dashes per 500 words is normal human usage. Only flag excess density alongside other tells.
- Never remove all em dashes.

### Respect the genre
- Academic text tolerates hedging, formal transitions, and structured organization.
- Creative text tolerates em dashes and sentence fragments but not AI vocabulary.
- Social media tolerates almost nothing from the AI playbook.
- Always use the genre-specific thresholds from the taxonomy.

---

## Anti-Patterns — Do Not Do These

- Do not rewrite paragraphs from scratch. Edit surgically.
- Do not flag contractions, first-person pronouns, or personal anecdotes as tells. These are human signals.
- Do not remove all em dashes. 1-2 per 500 words is normal.
- Do not add "deliberate imperfections" — misspellings, fragments where they don't fit, forced slang.
- Do not guarantee the text will pass AI detection tools. Those tools are unreliable.
- Do not edit human-written text with this skill. This skill targets the machine fingerprint in AI output.
- Do not apply fixes the user rejected.
- Do not skip the second pass. It catches what the taxonomy misses.
- Do not flag patterns below their genre threshold.

---

## Pairs With

- **voice-extractor**: Load the user's voice profile before running ai-tell-killer. Fixes will match the user's natural style instead of generic alternatives.
- **precision-editor**: Different tool. precision-editor works on human text at configurable edit levels. ai-tell-killer targets the machine fingerprint in AI-generated text.
