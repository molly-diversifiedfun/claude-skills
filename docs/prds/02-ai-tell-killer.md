# PRD: ai-tell-killer

## Problem

AI-generated text has a statistical fingerprint that readers increasingly recognize — and existing "humanizer" tools make text worse 74% of the time (DAMAGE paper, Masrour et al., ACL 2025). The problem isn't individual words like "delve." It's sentence-length uniformity, structural repetition, and vocabulary clustering. Current tools do full rewrites that strip the author's voice. Users need surgical editing that fixes only the tells.

## Solution

An analyzer skill that takes AI-generated or AI-assisted text, identifies specific AI patterns with confidence ratings, and fixes only the flagged patterns — leaving everything else untouched. The user can diff before and after to see exactly what changed.

## Design Decisions (from research)

| Decision | Choice | Why |
|----------|--------|-----|
| Detection scope | **Human perception, not detector evasion** | Detector evasion chases a moving target. Removing patterns that make text *feel* AI-generated produces durably better writing. |
| Edit granularity | **Sub-sentence surgical editing** | Sentence-level replacement changes too much voice. Surgical swaps preserve surrounding text. Accept occasional awkward seams as the tradeoff. |
| Single-pass vs. two-pass | **Two-pass** — fix known tells, then audit for remaining AI feel | blader/humanizer (10.5k stars) validates this architecture. Second pass catches structural patterns the first pass misses. |
| Default aggression | **Conservative** — flag only co-occurring clusters and high-confidence structural patterns | ESL writers, academic writers, and formal prose all share features with AI output. Single-word flags produce unacceptable false positives. Co-occurrence is the key signal. |
| Explanation model | **Annotated editing** — show each flagged tell with category and confidence before applying | Builds user trust, enables learning, lets user override bad calls. The friction is worth it for a tool whose #1 risk is overcorrection. |
| Context gating | **Genre presets** (academic, blog, business, creative) with different thresholds | More predictable and debuggable than dynamic inference. User picks the preset; skill adjusts what's flagged. |
| Structural vs. lexical priority | **Structural and rhythm first** | Research is unambiguous: synonym swapping doesn't change the statistical fingerprint. Sentence-length variation and structural variety produce more fundamental improvement. |

## The AI Tell Taxonomy

The skill's core IP — the categorized detection system:

### Tier 1: Always Flag (high confidence, high severity)

**Vocabulary Clusters** (flag when 3+ co-occur in proximity)
- delves, underscores, showcasing, commendable, meticulous, intricate, multifaceted, pivotal, realm, tapestry, landscape, foster, harness, nuanced, seamless, groundbreaking, transformative, robust
- Context gate: domain-appropriate usage passes (archaeology for "delve," engineering for "robust")

**Structural Patterns**
- Summary paragraphs that restate everything (opens with "Overall," "In summary," "In conclusion" + contains no new information)
- Heading inflation (excessive subheadings with identical sub-structure)
- List overuse as RLHF artifact (Zhang et al., 2024)

**Rhythm**
- Sentence-length SD < 4 words across 5+ sentences (AI uniformity signal)
- Zero sentence fragments in 500+ words of informal text (sterile perfection)

### Tier 2: Flag If Excessive (medium confidence)

**Vocabulary**
- Hedging phrases: "It's important to note," "It bears mentioning," "It's worth considering" — flag if 2+ appear in 500 words
- Elegant variation: unnatural synonym cycling for the same referent within a paragraph

**Punctuation**
- Em dash density > 3-4 per 500 words (weak individual signal, strengthen with other markers)
- Zero semicolons, zero parenthetical asides, zero contractions in informal text

**Transitions**
- "Furthermore," "Moreover," "Additionally" opening consecutive paragraphs
- "Let's explore," "Let's unpack," "Now let's turn to," "With that in mind"
- Formulaic transitions at fixed intervals

**Structure**
- Reflexive tricolon ("keynote sessions, panel discussions, and networking opportunities") used mechanically
- Parallel construction overuse ("not only X but also Y" + "whether X or Y" in same passage)

### Tier 3: Flag Only With Context (low confidence individually)

**Semantic**
- False balance ("While X, it's also true that Y" when Y is unwarranted)
- Excessive signposting ("In this section, we will discuss...")
- The "Challenges + Future Prospects" formula

**Punctuation**
- Perfect Oxford comma consistency (humans are inconsistent)
- American English spelling defaults when author uses British English

**Openings**
- "In today's fast-paced world," "In the ever-evolving landscape of"
- Filler affirmations in conversational output ("Great question!", "Absolutely!")

## Interaction Model

**Step 1: Input + Preset Selection** (30 sec)
- User pastes text
- Skill asks: "What's the context? (a) blog post (b) business/email (c) academic (d) creative fiction (e) social media"
- Preset adjusts thresholds (e.g., academic tolerates more hedging phrases; creative tolerates more em dashes)

**Step 2: First Pass — Pattern Detection + Annotation** (automatic)
- Scan text against the taxonomy
- Produce annotated report:

```
## AI Tell Report

**Overall AI Signature: Medium** (4 patterns detected across 2 categories)

### Flagged Patterns

1. **[VOCABULARY CLUSTER]** Lines 3-5: "multifaceted," "nuanced," and
   "robust" within 2 sentences. Confidence: High.
   → Suggested fix: [specific replacement preserving meaning]

2. **[RHYTHM]** Lines 1-12: Sentence length SD = 2.8 words (12 sentences).
   Human writing typically varies more. Confidence: High.
   → Suggested fix: Break sentence on line 4 into two. Combine sentences
   on lines 7-8 into one. Add a fragment on line 10.

3. **[TRANSITION]** Lines 8, 14, 20: Three consecutive paragraphs open
   with "Furthermore," "Moreover," "Additionally." Confidence: Medium.
   → Suggested fix: [specific rewrites for each opening]

4. **[STRUCTURE]** Lines 22-25: Summary paragraph restates all prior
   points with no new information. Confidence: High.
   → Suggested fix: Cut entirely, or replace with a forward-looking
   statement.

### Passed (not flagged)
- Vocabulary register: appropriate for context
- Punctuation: em dash usage within normal range
- Paragraph structure: varied lengths
```

**Step 3: User Review** (1 min)
- "Apply all fixes? Or review individually?"
- If individual: user approves/rejects each flagged pattern
- User can override any call

**Step 4: Second Pass — Residual Audit** (automatic)
- After fixes applied, re-read the complete text
- Ask: "What still feels AI-generated about this?"
- Flag any remaining patterns the first pass missed (often structural patterns that only become visible after vocabulary fixes)
- Apply or present for review

**Step 5: Output**
- Clean text with only flagged patterns changed
- Optional: diff view showing exactly what was modified

## Success Criteria

- A human reader who regularly reads AI output cannot identify the edited text as AI-generated
- The author recognizes the output as their own voice (if voice-extractor profile was loaded)
- Fewer than 5% of edits are overcorrections (things that were fine and got made worse)
- The skill changes fewer than 20% of sentences in typical AI output (surgical, not rewrite)

## What This Skill Does NOT Do

- Guarantee passing AI detection tools (those are unreliable and chase a moving target)
- Rewrite text from scratch (that's what every competing tool does, and they break 74% of the time)
- Add voice or personality (that's voice-extractor's job — this skill removes AI fingerprint)
- Edit human-written text (not designed for this; precision-editor handles human text editing)

## Anti-Patterns to Avoid in Implementation

- Never do a full rewrite — if more than 30% of sentences change, something is wrong
- Never ban individual words without co-occurrence context (false positive trap for ESL writers)
- Never remove all em dashes — 1-2 per 500 words is normal human usage
- Never add deliberate errors to seem more human (the Undetectable.ai failure mode)
- Never strip all structure — well-organized writing isn't an AI tell; *formulaic* organization is
- Never flag contractions, first-person pronouns, or personal anecdotes as tells (these are human signals)

## Pairs With

- **voice-extractor**: Load the user's voice profile before running ai-tell-killer. The skill then fixes AI tells while preserving the specific voice directives.
- **precision-editor**: Different tool. precision-editor works on human text at configurable levels. ai-tell-killer works on AI text to remove machine fingerprint.
