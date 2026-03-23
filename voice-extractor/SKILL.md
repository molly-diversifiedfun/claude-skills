---
name: voice-extractor
description: Extract a reusable voice profile from writing samples. Activate when user wants to capture their writing voice, create a voice profile, make AI sound like them, stop AI from sounding generic, or mentions "voice profile," "brand voice," "writing style," or "sound like me." Also activate when user says output doesn't sound like them, complains about AI voice, or wants consistent voice across conversations.
---

# Voice Extractor

## What This Skill Does

Takes 3-5 writing samples and produces a reusable voice profile (.md file). The user pastes this profile into any Claude conversation and gets output that sounds like them. Sample-based extraction, not self-reported adjectives. Directives, not descriptions.

Two artifacts: a detailed extraction report (reference document) and a 1,000-1,500 word operational voice profile (the file they actually use).

## What This Skill Does NOT Do

- Real-time voice matching during conversation (it produces a profile; other conversations consume it)
- Fine-tuning or model training
- Voice matching for fiction characters (this is for the user's voice, not a character's voice)
- Voice matching from audio or video (text samples only)
- Copywriting or content generation (it builds the voice spec; writing happens after)

---

## Phase 1: Sample Collection

Ask the user to paste 3-5 writing samples. Say this:

> Paste 3-5 writing samples — 500 to 1,000 words each. Aim for 5,000+ words total.
>
> Your best samples are ones you wrote fast without overthinking. Same-format samples (all blog posts, all newsletters) produce the cleanest signal. If you want me to capture range, add 1-2 samples in a different format.
>
> Paste each sample with a label (e.g., "Sample 1: Newsletter edition from March") so I can reference them later. Samples should be from the last 1-2 years — voice drifts over time.

After the user pastes samples:

1. Count total words across all samples.
2. If under 2,000 words total: warn that profile quality will be limited and ask for more. Say: "I have [X] words total. Profiles built on under 2,000 words will miss patterns. Can you add another sample or two?"
3. If 2,000-5,000 words: proceed but note that more samples would improve accuracy.
4. If 5,000+ words: confirm receipt and move to Phase 2.
5. If fewer than 3 samples: ask for at least one more regardless of word count.

Confirm receipt with a brief summary: number of samples, total word count, format(s) detected.

---

## Phase 2: Extraction (automatic — no user input needed)

Analyze all samples silently. Do not show this work to the user yet. Extract these dimensions:

### Tier 1 — High-confidence dimensions (build the profile around these)

**Sentence length distribution:**
- Mean words per sentence
- Approximate range (shortest to longest typical sentence)
- Short:long ratio (sentences under 10 words vs. over 30 words)
- Sentence length variation pattern (consistent, rhythmic alternation, or erratic)

**Pronoun patterns:**
- I/we/you ratios
- Direct-address frequency ("you" aimed at the reader)
- First-person stance (heavy "I" = personal authority; heavy "we" = inclusive; absent = removed)

**Punctuation habits:**
- Em dash density (frequent, occasional, absent)
- Semicolon usage (yes/no — many writers never use them)
- Parenthetical frequency (asides in parentheses or em dashes)
- Exclamation mark rate (never, rare, frequent)
- Ellipsis usage
- Any unusual punctuation patterns

**Active/passive voice ratio:**
- Approximate percentage of active voice constructions

**Vocabulary register:**
- Anglo-Saxon monosyllable preference vs. Latinate polysyllable preference
- Rare/unusual word frequency
- Contractions (always, sometimes, never)
- Profanity or colloquialism level

### Tier 2 — Medium-confidence dimensions (include but note approximation)

**Paragraph structure:**
- Typical paragraph length (sentences per paragraph)
- Topic-sentence placement (lead with the point, build to it, or mixed)
- One-sentence paragraph frequency (a distinctive stylistic choice when present)

**Transition mechanics:**
- Connective density (heavy use of "but," "so," "however" vs. juxtaposition without connectives)
- Favorite transition words or phrases
- Section-to-section flow style

**Opening and closing patterns:**
- How do samples begin? (anecdote, question, bold claim, scene-setting, data point)
- How do samples end? (callback, CTA, open question, summary, kicker line)

### Emergent Patterns

Scan for distinctive patterns not covered above:
- Signature phrases or constructions the author uses repeatedly
- Unusual structural moves (e.g., mid-paragraph single-word sentences, lists inside prose, direct reader commands)
- Tonal shifts within pieces (e.g., serious setup to funny punchline)
- Formatting preferences (headers, bold, italics usage patterns)
- Anything that makes this voice different from generic good writing

### Anti-Pattern Detection

Identify what the author does NOT do:
- Words that never appear despite being common in their genre
- Structures they avoid (e.g., never uses passive voice, never opens with a definition, never uses rhetorical questions)
- AI-default behaviors they'd reject (e.g., list-heavy formatting, "Let's dive in," hedge phrases)
- Places where an AI would "correct" an intentional stylistic choice (e.g., sentence fragments, starting sentences with "And" or "But," one-word paragraphs)

---

## Phase 3: Targeted Questions

After extraction, ask 3-5 questions. Ask them all at once in a numbered list — do not drip them one by one.

Always ask these three:

1. "What writing makes you cringe? Give me a specific example of a sentence or style you'd never write."
2. "How do you use humor — frequently, rarely, never? If you use it, what kind: sarcasm, dry wit, self-deprecation, absurdist, something else?"
3. "Who is your typical reader? How do you want them to feel after reading your work?"

Add 1-2 more based on what the samples revealed:

4. (If samples span formats): "Is your voice different in [format A] vs. [format B], or is it the same voice in different containers?"
5. (If samples show ambiguous patterns): Ask one specific clarifying question about the ambiguity. Example: "Your samples alternate between very short punchy paragraphs and longer analytical ones. Is that intentional rhythm, or does it depend on the topic?"

### Weighting Rule

When the user's self-reported preferences conflict with what the samples show, weight the sample evidence. Samples capture unconscious patterns — the most authentic markers of voice. Self-reports capture the writer they wish they were, not the writer they are. Note the conflict in the extraction report but build the profile from sample evidence.

Exception: anti-patterns and cringe responses. If the user says "I never want to sound like X," honor that even if X occasionally appears in samples. People evolve past patterns they now reject.

---

## Phase 4: Profile Generation

After receiving answers to Phase 3 questions, produce two artifacts.

### Artifact 1: Voice Extraction Report

Full analysis document. Approximately 3,000 words. This is a reference — not for pasting into conversations.

Structure:

```
# Voice Extraction Report: [User's Name or Label]

## Sample Summary
[Number of samples, total word count, formats analyzed, date range if known]

## Tier 1 Dimensions
### Sentence Architecture
[Metrics + 2-3 example sentences from samples showing the pattern]

### Pronoun Patterns
[Ratios + examples + what this reveals about stance]

### Punctuation Profile
[Frequencies + examples of distinctive punctuation use]

### Voice Ratio
[Active/passive split + examples]

### Vocabulary Register
[Register analysis + example word choices that define the voice]

## Tier 2 Dimensions
### Paragraph Structure
[Analysis + representative paragraph from samples]

### Transition Mechanics
[Connective patterns + favorite transitions]

### Opening/Closing Patterns
[Pattern analysis across all samples]

## Distinctive Patterns
[Anything unique that emerged — the patterns that make this voice THIS voice]

## Anti-Patterns
[What the author avoids, what AI would get wrong, intentional "rule-breaking"]

## Interview Findings
[Summary of Phase 3 answers, any conflicts with sample evidence noted]

## Calibration Anchors
[3-5 paragraphs pulled directly from samples that best represent the voice at its most distinctive — annotated with what makes each one exemplary]
```

### Artifact 2: Operational Voice Profile

The .md file the user actually pastes into conversations. 1,000-1,500 words. Never shorter than 800 words. Never longer than 2,000 words.

Critical rules go at the top AND are repeated at the bottom (counters the "lost in the middle" effect where models lose attention to instructions in the middle of long context).

Every line must be a directive. No analysis. No "the author tends to..." — only "Use...", "Never...", "Always...", "Write...", "Avoid..."

Structure:

```
# Voice Profile: [Name]

## Identity
[2-3 sentences: who you are, who you write for, what you sound like at your best. Written as instructions to the AI.]

## Critical Rules
[The 3-5 most important rules. These are the ones that, if violated, make the output sound wrong. Front-loaded for maximum attention.]

## Structural Rules
[Sentence length targets as ranges, not exact numbers. Paragraph style. Formatting preferences. All as directives.]

## Vocabulary
### Use These
[Specific words, transition phrases, industry terms the author actually uses — with example sentences from their samples showing usage in context]

### Never Use
[Banned words with replacements. AI-isms to block. Corporate filler to avoid. Format: "Never write [X] — write [Y] instead."]

## Anti-Patterns
[Specific structures to avoid. Tonal moves that are off-brand. AI defaults that must be overridden. This section should be ~60% of the profile's instructional weight.]

## Tone Dimensions
[Measurable dimensions, not adjectives. Use scales.
Example: "Formality: 3/10 — Use contractions freely. Address the reader as 'you.' Swear if it lands."
Example: "Humor: 6/10 — Dry wit and self-deprecation. Never slapstick. Never explain the joke."
Cover: formality, humor, confidence, warmth, pace]

## Calibration Samples
[2-3 paragraphs pulled directly from the user's writing. These are few-shot examples for Claude to match. Choose paragraphs that are the most distinctively "them."]

## Critical Rules (repeated)
[Same 3-5 rules from the top. Verbatim repeat. This is intentional — it counters attention decay in long context windows.]
```

### Profile Quality Checks

Before delivering, verify:
- [ ] Every line is a directive (no analysis, no "tends to")
- [ ] Anti-patterns section is at least as long as positive-pattern sections combined
- [ ] Calibration samples are actual excerpts from the user's writing, not generated examples
- [ ] No unsupported adjectives ("engaging," "warm," "professional" — unless anchored to specific behaviors)
- [ ] Tone dimensions use numeric scales with behavioral anchors
- [ ] Profile is between 800 and 2,000 words
- [ ] Critical rules appear at top and bottom
- [ ] Vocabulary section includes concrete examples, not just word lists

---

## Phase 5: Validation (offer this, don't force it)

After delivering both artifacts, say:

> Want me to test it? Give me a topic and I'll write a short paragraph using your voice profile. You tell me what sounds right and what's off, and I'll adjust.

If the user accepts:
1. Write a 100-150 word paragraph on the topic, following the operational profile strictly.
2. Ask: "Does this sound like you? What's off?"
3. If corrections needed: update both artifacts and regenerate the operational profile.
4. Offer one more round if the first had significant corrections.

If the user declines: deliver the artifacts and suggest they test it in a new conversation by pasting the operational profile as instructions.

---

## Hardcoded Rules

- Never describe voice with unsupported adjectives. "Engaging" means nothing without "because she opens with data points, not definitions."
- Never produce an operational profile shorter than 800 words. Too thin to constrain output.
- Never produce an operational profile longer than 2,000 words. Lost-in-the-middle effect kills mid-document rules.
- Never include analysis language in the operational profile. "The author tends to use short sentences" is an error. "Keep sentences under 15 words in openings" is correct.
- Never weight self-reported preferences over sample evidence when they conflict (except for anti-patterns — honor stated rejections).
- Never extract jargon density as a voice dimension. It overfits to topic, not style (Stamatatos, 2009).
- Never fabricate calibration samples. Use only actual excerpts from the user's writing.
- The operational profile must work when pasted into a blank Claude conversation with zero other context. It must be self-contained.
- The 60/40 rule: anti-patterns and prohibitions should comprise roughly 60% of the profile's instructional content. What you reject is more instructable than what you do. AI has strong defaults — overriding them requires explicit prohibitions.
- Tone dimensions must be behavioral, not adjectival. "Warm" is useless. "Address the reader directly. Use second person. Share personal failures before giving advice." is useful.

---

## Edge Cases

**User provides only 1-2 samples:** Do not proceed to extraction. Ask for at least one more sample. Explain that patterns need at least 3 data points to distinguish signal from noise.

**User provides 10+ samples:** Accept them all. More data improves accuracy. Note in the extraction report which samples contributed most to each dimension.

**Samples are in wildly different voices:** Ask if they're for different audiences/contexts. If yes, offer to build separate profiles or a single profile with context-specific sections. If no, use the most recent samples as the primary signal.

**User asks for a fiction character voice:** Decline. This skill extracts the user's own voice. Fiction character voices require different methodology (scene context, dialogue patterns, narrative distance). Say: "This skill is built for your voice — the one you use in nonfiction, emails, posts. Character voices need a different approach."

**User provides audio/video transcripts:** Accept with a caveat: spoken voice differs from written voice. Note in the extraction report that the profile captures the user's spoken register, which may need adjustment for written contexts.

**User wants to combine multiple people's voices:** Decline. Voice profiles work because they capture one person's patterns. Combining voices produces mush. Suggest building separate profiles and specifying which to use per context.
