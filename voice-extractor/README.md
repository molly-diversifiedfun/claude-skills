# Voice Extractor

**Stop describing your voice with adjectives. Start extracting it from samples.**

## The Problem

82% of writers worry about AI homogenizing their style (Authors Guild survey). The standard fix — tell the AI you're "engaging, punchy, and conversational" — produces what Ian Brodie called a "pixelated mess." Adjective-based voice descriptions don't work. Jasper users report that "casual and conversational" turned into every sentence starting with "Hey there!" The AI latches onto the most obvious interpretation and produces a caricature.

The workaround ecosystem tells the story: .md voice files, banned-phrase lists, multi-step prompt chains. Everyone's building these by hand. Most of them fail because they describe the writer instead of instructing the AI.

## What It Does

You paste 3-5 writing samples. The skill analyzes them across dimensions that are both extractable from small corpora and reproducible by an LLM — sentence length distribution, pronoun patterns, punctuation habits, active/passive ratio, vocabulary register, paragraph structure, and more. It then asks 3-5 targeted questions about things samples can't reveal (humor intent, audience, what makes you cringe).

You get two artifacts:

1. **Voice Extraction Report** (~3,000 words) — the full analysis with metrics, examples, and reasoning. Reference document.
2. **Operational Voice Profile** (~1,000-1,500 words) — the .md file you actually use. Paste it into any Claude conversation and get output that sounds like you.

The profile uses directives ("Keep sentences under 15 words in openings"), not analysis ("The author tends to use short sentences"). Every line is an instruction the AI can follow.

## How to Use It

### In Claude.ai

1. Start a new conversation
2. Open the skill by saying: "Use the voice-extractor skill" (if added to your Project) or paste the contents of `SKILL.md` as your first message
3. Paste 3-5 writing samples (500-1,000 words each, 5,000+ total words is ideal)
4. Answer the 3-5 targeted questions
5. Receive your extraction report and operational profile
6. Copy the operational profile into a Claude Project's custom instructions, or paste it at the start of any new conversation

### In Claude Code

1. Add the skill to your Claude Code configuration:
   - Copy `SKILL.md` to `~/.claude/skills/voice-extractor/SKILL.md`
   - Or reference it in your `.claude/CLAUDE.md`: `When extracting voice, read path/to/voice-extractor/SKILL.md`
2. Tell Claude Code: "Extract my voice profile from these samples"
3. Paste or point to your writing samples
4. Answer the follow-up questions
5. Save the operational profile as a `.md` file in your project or `~/.claude/` directory

### Tips for Better Results

- **Best samples:** things you wrote fast without overthinking. Those capture your unconscious patterns.
- **Same-format samples** (all blog posts, all newsletters) produce cleaner signal. Add 1-2 varied samples for range.
- **Recent samples** — from the last 1-2 years. Voice drifts over time.
- **Minimum:** 3 samples, 2,000 words total. Below this, the skill will warn you.
- **Optimal:** 5-10 samples, 5,000-10,000 words total.

## What You Get

### The Operational Profile Structure

```markdown
# Voice Profile: [Your Name]

## Identity
Write as a [role] speaking to [audience]. Sound like [concrete description].

## Critical Rules
- Never use "delve," "landscape," or "I'd be happy to"
- Keep opening sentences under 12 words
- Lead with the problem, never with a definition

## Structural Rules
- Average 14 words per sentence, ranging from 4 to 28
- Paragraphs: 2-4 sentences. Use one-sentence paragraphs for emphasis.
- ...

## Vocabulary
### Use These
- "ship" instead of "launch" — example: "We shipped the fix Tuesday"
### Never Use
- Never write "utilize" — write "use" instead
- Never write "leverage" — write "use" instead
- ...

## Anti-Patterns
[~60% of the profile's weight lives here]

## Tone Dimensions
- Formality: 3/10 — Contractions always. "You" freely. Swear if it lands.
- Humor: 5/10 — Dry wit and self-deprecation. Never explain the joke.
- ...

## Calibration Samples
[2-3 paragraphs from YOUR actual writing]

## Critical Rules (repeated)
[Same rules from the top — intentional repeat to counter attention decay]
```

The profile is self-contained. It works when pasted into a blank conversation with zero other context.

## The Research Behind It

Four findings shaped the design:

**Only 5 of 11 voice dimensions are both extractable and reproducible.** Stylometry catalogs 239+ features (Writeprints, Abbasi & Chen 2008). Most are either impossible to extract from 3-5 samples or impossible for an LLM to reproduce. The sweet spot — Tier 1 dimensions — is sentence length, pronouns, punctuation, active/passive ratio, and vocabulary register. The skill builds profiles around these.

**Directives beat descriptions every time.** Statistical style summaries are "incapable of style mimicry" (Jemama 2025). Raw examples with directive framing produce 25-35% better adherence. Every successful open-source implementation uses instructions ("Use short sentences in openings"), not analysis ("The author tends to use short sentences").

**What you reject matters more than what you do.** Both Daria Cupareanu's Voice DNA method and the Taste Interviewer approach converge on the same finding: AI has strong defaults, and telling it what NOT to do overrides those defaults more reliably than positive instructions. The skill weights profiles 60% anti-patterns, 40% positive patterns.

**Long profiles lose their middles.** Liu et al.'s "Lost in the Middle" research shows models retrieve best from the beginning and end of long inputs. The operational profile front-loads critical rules and repeats them at the end. The full extraction report exists as a reference document — the operational profile is the one that does the work.

## Design Decisions

| Decision | Choice | Why |
|----------|--------|-----|
| Fixed vs. emergent dimensions | Hybrid — fixed Tier 1 skeleton + open-ended "distinctive patterns" section | Consistency on reproducible dimensions, flexibility for what makes each voice unique |
| Metrics vs. examples | Hybrid — metrics as guardrails, 2-3 raw excerpts as calibration anchors | Statistical summaries alone can't produce mimicry. Examples close the gap. |
| Directive vs. analytical format | Directives only | No tradeoff. "The author tends to..." is treated as an error. |
| Single vs. chunked profiles | Single profile, architected for future chunking | Start simple. Tag by context if samples span formats. |
| Positive patterns vs. anti-patterns | 60% anti-patterns, 40% positive | What you reject is more instructable. AI defaults need explicit overrides. |
| Profile length | Two artifacts — 3,000-word report + 1,000-1,500-word operational profile | Long profiles lose mid-document attention. Critical rules front-loaded and repeated. |
| Extraction vs. interview | Samples primary, 3-5 targeted questions secondary | Samples capture unconscious patterns (most authentic). Self-reports fill gaps on humor, audience, and things-to-avoid. Sample evidence wins conflicts. |

## Pairs With

- **[self-interview](/self-interview/)** — Extract your thinking patterns and expertise before writing. Voice Extractor captures *how* you write; Self-Interview captures *what* you know.
- **[build-irresistible-offer](/build-irresistible-offer/)** — Build an offer, then write the copy in your voice.
- **[funnel-ad-creator](/funnel-ad-creator/)** — Create ad copy that actually sounds like your brand.
- **[instagram-reels-framework](/instagram-reels-framework/)** — Script reels in your voice instead of generic influencer-speak.
