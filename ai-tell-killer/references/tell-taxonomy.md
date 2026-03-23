# AI Tell Taxonomy — Full Reference

This is the detection catalog used by the ai-tell-killer skill. Each tell has a tier, category, detection criteria, and genre-specific thresholds.

---

## Tier 1: Always Flag (High Confidence, High Severity)

### 1A. Vocabulary Clusters

**Detection rule:** Flag when 3+ of these words co-occur within 200 words of each other.

**Never flag a single instance.** One "robust" is not a tell. Three of these words in proximity is.

**The words:** delves, underscores, showcasing, commendable, meticulous, intricate, multifaceted, pivotal, realm, tapestry, landscape, foster, harness, nuanced, seamless, groundbreaking, transformative, robust

**Context gate — pass these through:**
- Domain-appropriate usage: "delve" in archaeology, "robust" in engineering, "landscape" in geography, "seamless" in textile/UX, "intricate" in jewelry/watchmaking
- Direct quotations from other sources
- Deliberate stylistic choice the author has confirmed

**Genre thresholds:**
| Genre | Cluster size to flag | Notes |
|-------|---------------------|-------|
| Academic | 4+ | Academic writing legitimately uses "robust," "nuanced," "multifaceted" |
| Blog | 3+ | Standard threshold |
| Business | 3+ | Standard threshold |
| Creative | 2+ | These words almost never appear in natural fiction |
| Social media | 2+ | Extremely unnatural in casual posts |

### 1B. Structural: Summary Paragraphs

**Detection rule:** Flag paragraphs that meet ALL of these criteria:
1. Opens with "Overall," "In summary," "In conclusion," "To summarize," "In short," or "All in all"
2. Contains no new information, arguments, examples, or forward-looking statements
3. Merely restates points already made in prior paragraphs

**Do not flag:**
- Conclusions that add a new insight, recommendation, or call to action
- Academic paper conclusions (these follow genre convention)
- Executive summaries at the TOP of a document

### 1C. Structural: Heading Inflation

**Detection rule:** Flag when:
- More than 1 subheading per 150 words in non-reference content
- Every section follows identical sub-structure (e.g., every section has exactly 3 bullet points)
- Title Case applied to all headings regardless of level

**Genre thresholds:**
| Genre | Threshold | Notes |
|-------|-----------|-------|
| Academic | Do not flag | Heading-heavy structure is convention |
| Blog | 1 per 200 words | Blog posts use subheadings, but not every paragraph |
| Business | 1 per 150 words | Reports legitimately have many headings |
| Creative | Almost never | Subheadings in fiction are a strong tell |
| Social media | Do not flag | Too short to evaluate |

### 1D. Structural: List Overuse (RLHF Artifact)

**Detection rule:** Flag when:
- 3+ bulleted/numbered lists in 500 words of prose-expected content
- Lists used where a paragraph would be more natural
- Bold lead-in on every list item (the "**Bold:** explanation" pattern)

**Do not flag:**
- Reference material, documentation, or how-to guides (lists are appropriate)
- A single list used to organize genuinely parallel items

### 1E. Rhythm: Sentence-Length Uniformity

**Detection rule:** Calculate standard deviation of word count across sentences in each paragraph or passage of 5+ sentences.

- SD < 4 words across 5+ sentences = flag (AI uniformity signal)
- SD 4-6 = note but do not flag unless other tells co-occur
- SD > 6 = pass

**How to fix (not just what to flag):**
- Break one long sentence into two short ones
- Combine two medium sentences into one long one with a conjunction or semicolon
- Add a fragment (1-4 words) somewhere in the passage
- Vary paragraph openings: start one with a prepositional phrase, one with a subject, one with a conjunction

### 1F. Rhythm: Sterile Perfection

**Detection rule:** Flag when ALL of the following are true in 500+ words of informal text:
- Zero sentence fragments
- Zero sentences starting with "And," "But," or "So"
- Zero contractions
- Zero parenthetical asides

**Genre thresholds:**
| Genre | Apply? | Notes |
|-------|--------|-------|
| Academic | No | Formal perfection is appropriate |
| Blog | Yes | Informal writing should have texture |
| Business | Partial | Flag only if zero contractions AND zero fragments |
| Creative | Yes | Fiction without fragments is deeply unnatural |
| Social media | Yes | Casual content demands imperfection |

---

## Tier 2: Flag If Excessive (Medium Confidence)

### 2A. Hedging Phrases

**The phrases:** "It's important to note," "It bears mentioning," "It's worth considering," "It's worth noting," "It should be noted," "One might argue"

**Detection rule:** Flag if 2+ appear in 500 words.

**Genre thresholds:**
| Genre | Threshold | Notes |
|-------|-----------|-------|
| Academic | 3+ per 500 words | Academic writing hedges legitimately |
| Blog | 2+ per 500 words | Standard |
| Business | 2+ per 500 words | Standard |
| Creative | 1+ per 500 words | These almost never appear in fiction |
| Social media | 1+ per 500 words | Completely unnatural |

### 2B. Elegant Variation (Unnatural Synonym Cycling)

**Detection rule:** Flag when the same referent gets 3+ different labels within a single paragraph without rhetorical purpose.

**Examples:**
- "the CEO" → "the executive" → "the business leader" → "the corporate head" in one paragraph
- "the study" → "the research" → "the investigation" → "the inquiry"
- A character's name → "the protagonist" → "the young woman" → "the aspiring artist"

**Do not flag:**
- Deliberate variation for rhetorical effect (building from specific to general)
- Using a pronoun alongside a proper noun (normal reference)

### 2C. Transition Stacking

**The patterns:**
- "Furthermore," "Moreover," "Additionally" opening consecutive paragraphs
- "Let's explore," "Let's unpack," "Now let's turn to," "With that in mind"
- "It is also worth noting" or "Another key aspect"
- Formulaic transitions at fixed intervals (every 2-3 paragraphs)

**Detection rule:** Flag when:
- 2+ consecutive paragraphs open with formal additive transitions
- 3+ instances of "Let's [verb]" in one piece
- Transitions appear at mechanically regular intervals

### 2D. Punctuation: Em Dash Overuse

**Detection rule:** Flag when em dash count exceeds threshold AND other tells co-occur.

**Em dash alone is a weak signal.** Only flag alongside other markers.

| Genre | Threshold | Notes |
|-------|-----------|-------|
| Academic | 4+ per 500 words | Academics rarely use em dashes |
| Blog | 5+ per 500 words | Blog writers use them; higher threshold |
| Business | 4+ per 500 words | Standard |
| Creative | 6+ per 500 words | Literary writers use them heavily; very high threshold |
| Social media | 3+ per 500 words | Unusual in casual posts |

### 2E. Punctuation: Absence Patterns

**Detection rule:** In informal text (blog, social media), flag when ALL of:
- Zero semicolons
- Zero parenthetical asides
- Zero contractions

This absence of variety is the tell, not any single missing element.

### 2F. Structural: Reflexive Tricolon

**Detection rule:** Flag when tricolon (three-part list) appears 2+ times in 500 words AND the items follow a mechanical pattern (same part of speech, similar length, no surprise in the third element).

**Examples of mechanical tricolon (flag):**
- "keynote sessions, panel discussions, and networking opportunities"
- "innovation, collaboration, and growth"
- "strategic, impactful, and transformative"

**Examples of rhetorical tricolon (pass):**
- "I came, I saw, I conquered" (escalation)
- "Life, liberty, and the pursuit of happiness" (culturally established)
- Any three-part list where the third element subverts or surprises

### 2G. Structural: Parallel Construction Overuse

**Detection rule:** Flag when 2+ of these patterns co-occur in one passage:
- "not only X but also Y"
- "whether X or Y"
- "from X to Y"
- Repeated participial phrases ("leveraging X, driving Y, fostering Z")

Any one of these alone is fine. The cluster is the tell.

---

## Tier 3: Flag Only With Context (Low Confidence Individually)

These are NEVER flagged alone. They strengthen a case when Tier 1 or Tier 2 tells are already present.

### 3A. Semantic: False Balance

**Pattern:** "While X, it's also true that Y" — where Y is unwarranted hedging that weakens a clear point.

**Only flag when:** The balancing clause adds no substance and the topic doesn't warrant equivocation.

### 3B. Semantic: Excessive Signposting

**Pattern:** "In this section, we will discuss..." / "As mentioned earlier..." / "As we'll see below..."

**Only flag when:** 3+ signposts in 500 words, or signposting in informal text where it reads as robotic.

### 3C. Semantic: The "Challenges + Future Prospects" Formula

**Pattern:** Any section that mechanically pairs "challenges" with "future prospects" or "opportunities" — the default LLM structure for discussing any topic.

### 3D. Openings: Cliche Openers

**The patterns:**
- "In today's fast-paced world,"
- "In the ever-evolving landscape of [X],"
- "In an era of [X],"
- "As [technology/field] continues to [evolve/advance/transform],"
- "[Topic] has become increasingly important in recent years"

**Always flag these.** They are high-confidence tells that happen to be Tier 3 only because they appear in opening lines rather than throughout the text.

### 3E. Openings: Filler Affirmations

**Pattern:** "Great question!", "Absolutely!", "That's a fascinating point!", "What a great observation!"

**Only flag in:** Polished/published text. These are normal in live conversation but tells in written content.

### 3F. Punctuation: Perfect Consistency

**Patterns:**
- Perfect Oxford comma consistency throughout (humans are inconsistent)
- American English spelling when the author uses British English
- Zero typos or formatting inconsistencies in casual content

**Never flag these alone.** They only matter as corroborating evidence.

---

## Fix Strategies by Category

### Vocabulary Cluster Fixes
- Replace with plainer, more specific alternatives
- Use the word the author would actually use (check voice profile if available)
- When in doubt, use the simplest word that preserves meaning
- Example: "This multifaceted approach underscores the nuanced landscape" → "This approach highlights the complexity"

### Rhythm Fixes
- Break one long sentence into two
- Combine two short sentences with a conjunction or semicolon
- Add a fragment (1-4 words) — "Not always." / "The opposite, actually." / "Worth noting."
- Start a sentence with "And" or "But"
- Add a parenthetical aside
- Vary paragraph length: follow a long paragraph with a one-sentence paragraph

### Structural Fixes
- Cut summary paragraphs entirely, or replace with a single forward-looking sentence
- Convert mechanical lists back to prose paragraphs
- Break identical sub-structures by varying section formats (one section uses examples, another uses a question, another uses a contrasting viewpoint)
- Remove headings that don't earn their place

### Transition Fixes
- Delete the transition word and start with the substance: "Moreover, the data shows..." → "The data shows..."
- Replace formal transitions with conversational ones: "Furthermore" → "And" / "Also" / "Plus" / just start the sentence
- Vary the connection: use a question, a short sentence, a callback to an earlier point, or just start a new thought without a bridge

### Punctuation Fixes
- Replace 1-2 em dashes with commas, parentheses, or colons
- Add one semicolon somewhere natural
- Add a parenthetical aside
- Add contractions in informal text ("it is" → "it's", "do not" → "don't")
