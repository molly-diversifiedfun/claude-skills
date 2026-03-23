# PRD: voice-extractor

## Problem

AI output doesn't sound like you. Describing your voice with adjectives ("engaging, punchy, humorous") produces generic output — what Ian Brodie called a "pixelated mess." 82% of writers worry about AI homogenizing their style (Authors Guild survey). The workaround ecosystem — .md voice files, banned-phrase lists, multi-step prompt chains — proves demand but requires expertise most users don't have.

## Solution

A skill that takes 3-5 writing samples and produces a reusable voice profile (.md file). The profile uses directives, not descriptions. Sample-based extraction, not self-reported adjectives. The user pastes the profile into any Claude conversation and gets output that sounds like them.

## Design Decisions (from research)

| Decision | Choice | Why |
|----------|--------|-----|
| Fixed vs. emergent dimensions | **Hybrid** — fixed Tier 1 skeleton + open-ended "distinctive patterns" section | Consistency on reproducible dimensions, flexibility for what makes each voice unique |
| Metrics vs. examples | **Hybrid** — metrics as guardrails, 2-3 raw excerpts as calibration anchors | Jemama (2025): statistical summaries alone are "incapable of style mimicry." 25-35% better adherence with examples. |
| Directive vs. analytical format | **Directives only** | No tradeoff. Every successful implementation uses directives. "The author tends to..." is an error. |
| Monolithic vs. chunked profiles | **Single profile, architected to support chunking later** | Cupareanu split into three after one skill "kept mixing up audiences." Start simple, tag by context. |
| Positive patterns vs. anti-patterns | **60% anti-patterns, 40% positive** | Both Cupareanu and the Taste Interviewer converge: what you reject is more instructable than what you do. AI has strong defaults — overriding them requires explicit prohibitions. |
| Profile length | **Generate both** — 3,000-word extraction artifact, auto-distilled to 1,000-1,500-word operational profile | "Lost in the middle" effect (Liu et al.) means long profiles lose influence mid-document. Critical rules front-loaded and repeated at end. |
| Pure extraction vs. hybrid + interview | **Samples primary, 3-5 targeted questions secondary** | Samples capture unconscious patterns (most authentic per Pennebaker). Questions fill gaps on humor intent, audience awareness, and things-to-avoid. Weight sample evidence over self-report when they conflict. |

## Interaction Model

**Phase 1: Sample Collection** (2 min)
- User provides 3-5 writing samples (500-1,000 words each, ideally 5,000+ words total)
- Skill confirms receipt, checks total word count
- If under 2,000 words total: warn that profile quality will be limited, ask for more
- Guidance: "Your best samples are ones you wrote fast without overthinking. Same-format samples (all blog posts, all newsletters) produce cleaner signal. Add 1-2 varied samples for range."

**Phase 2: Extraction** (automatic, no user input)
- Analyze samples across Tier 1 dimensions:
  - Sentence length distribution (mean, SD, min/max, short:long ratio)
  - Pronoun patterns (I/we/you ratios, direct-address frequency)
  - Punctuation habits (em dash density, semicolon usage, parenthetical frequency, exclamation rate)
  - Active/passive voice ratio
  - Vocabulary register (Anglo-Saxon vs. Latinate preference, rare word frequency)
- Analyze Tier 2 dimensions:
  - Paragraph structure (length, sentence count, topic-sentence placement)
  - Transition mechanics (connective density, conjunction patterns)
  - Opening/closing patterns (from available samples)
- Scan for emergent distinctive patterns not covered by fixed dimensions
- Identify anti-patterns: words the author never uses, structures they avoid, places where AI would "correct" intentional choices

**Phase 3: Targeted Questions** (3-5 questions, 3 min)
Only ask about dimensions that are hard to extract from samples:
1. "What writing makes you cringe? Give me an example of a sentence you'd never write."
2. "How do you use humor — frequently, rarely, never? Sarcasm, wit, self-deprecation, or something else?"
3. "Who is your typical audience? How do you want them to feel after reading?"
4. (If samples span formats): "Is your voice different in [format A] vs. [format B], or the same?"
5. (If samples show ambiguous patterns): One clarifying question about the specific ambiguity.

**Phase 4: Profile Generation** (automatic)
Produce two artifacts:

**Artifact 1: Voice Extraction Report** (~3,000 words)
Full analysis document with metrics, examples, and reasoning. Reference artifact — not for pasting into conversations.

**Artifact 2: Operational Voice Profile** (~1,000-1,500 words)
The .md file the user actually uses. Structure:

```
## Identity
[2-3 sentences: who you are, who you write for, what you sound like at your best]

## Structural Rules
[Sentence length targets, paragraph style, formatting preferences — as directives]

## Vocabulary
### Always Use
[Specific words, transition phrases, industry terms — with examples]
### Never Use
[Banned words, AI-isms, corporate filler — with examples of what to use instead]

## Anti-Patterns
[Specific things to never do: structures to avoid, tonal moves that are off-brand,
AI defaults to override]

## Tone Dimensions
[Measurable dimensions, not adjectives. E.g., "Formality: 3/10. Use contractions
freely. Address the reader as 'you.' Swear occasionally when it lands."]

## Calibration Samples
[2-3 paragraphs from the user's actual writing — the voice in action.
These are few-shot examples for Claude to match.]

## [Repeat critical rules]
[Front-loaded rules repeated at end to counter "lost in the middle" effect]
```

**Phase 5: Validation** (optional, 2 min)
- Generate a short paragraph in the user's voice on a topic from their samples
- Ask: "Does this sound like you? What's off?"
- If corrections needed: update the profile and regenerate

## Success Criteria

- Profile produces output that the user would publish without heavy editing
- The user can paste the operational profile into any new Claude conversation and get consistent voice matching
- Profile takes under 10 minutes to generate (sample prep excluded)
- Works across writing formats (blog posts, emails, social media) without requiring separate profiles

## What This Skill Does NOT Do

- Real-time voice matching during conversation (it produces a profile; other skills/conversations consume it)
- Fine-tuning or model training
- Voice matching for fiction characters (this is for YOUR voice, not a character's voice — story-craft handles fiction)
- Voice matching from audio/video (text samples only)

## Anti-Patterns to Avoid in Implementation

- Never describe voice with unsupported adjectives ("engaging, warm, professional")
- Never produce a profile shorter than 800 words (too thin to be useful)
- Never produce a profile longer than 2,000 words for the operational version (lost-in-the-middle effect)
- Never include analysis ("the author tends to...") — only directives ("Use...", "Never...", "Always...")
- Never weight self-reported preferences over sample evidence when they conflict
- Never extract jargon density as a voice dimension (overfits to topic, not style — Stamatatos 2009)

## Technical Notes

- Minimum input: 3 samples, 2,000 words total (warn below this)
- Optimal input: 5-10 samples, 5,000-10,000 words total
- Samples should be from the most recent 1-2 years (voice drifts over time)
- The skill works in Claude.ai (no tools required) — pure prompt-based extraction
- Profile format is plain markdown, portable to any LLM or Claude Project
