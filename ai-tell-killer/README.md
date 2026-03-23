# AI Tell Killer

A Claude skill that detects and surgically removes AI writing patterns from text.

## The Problem

AI-generated text has a statistical fingerprint. Not just "delve" — sentence-length uniformity, structural repetition, vocabulary clustering, sterile grammatical perfection. Readers who encounter AI output regularly spot it instantly.

Existing "humanizer" tools make this worse, not better. The DAMAGE paper (Masrour et al., ACL 2025) studied 19 humanizer tools and found the best one improved fluency in only 26% of cases. **74% of rewrites degraded text quality.** The dominant approach — full-rewrite black boxes that trade quality for detector evasion — is fundamentally broken. Undetectable.ai introduces deliberate errors. WriteHuman produces different (often unreadable) output on repeated runs. These tools destroy the author's voice to chase unreliable detector scores.

The tells aren't vocabulary. They're structural. Synonym swapping doesn't change the statistical fingerprint. Sentence-length variation and structural variety do.

## What It Does

Surgical editing, not rewriting. The skill identifies specific AI patterns with confidence ratings and fixes only those patterns. Everything else stays untouched.

**Two-pass architecture:**
1. **First pass** scans text against a categorized taxonomy of AI tells — rhythm and structure first, vocabulary second. Produces an annotated report with every flagged pattern numbered, categorized, and paired with a specific fix.
2. **Second pass** re-reads the edited text as a skeptical human reader. Catches structural patterns that only become visible after vocabulary fixes, plus rhythm problems the first-pass edits may have introduced.

**Genre presets** (blog, business, academic, creative, social media) adjust detection thresholds. Academic text tolerates hedging phrases. Creative text tolerates em dashes. Social media tolerates almost nothing from the AI playbook.

**Core constraint:** Change fewer than 20% of sentences. If you're changing more, something is wrong. The author should recognize the output as their own text with targeted fixes.

## How to Use It

### Claude.ai

Paste your text and say something like:
- "This sounds like AI wrote it — fix the tells"
- "Make this more human"
- "Remove the AI fingerprint from this blog post"

The skill will ask for the genre (if you didn't specify), scan the text, present an annotated report of every detected pattern, and wait for your approval before changing anything. You can apply all fixes, review each one individually, or skip specific fixes by number.

### Claude Code

```bash
claude "humanize this draft" < draft.txt
```

Or reference the skill directly:

```
/ai-tell-killer
```

Then paste your text. Same flow — genre selection, annotated report, user review, two-pass editing.

## The Tell Taxonomy

The skill's detection system is organized into three confidence tiers. The full taxonomy with thresholds, genre-specific rules, and fix strategies lives in [`references/tell-taxonomy.md`](references/tell-taxonomy.md).

### Tier 1: Always Flag (high confidence)

Co-occurring AI vocabulary clusters (3+ words like *multifaceted, nuanced, robust* in proximity), summary paragraphs that restate everything with zero new information, heading inflation, list overuse, and sentence-length uniformity (SD < 4 words across 5+ sentences).

Single words are never flagged alone. "Robust" in an engineering paper is fine. "Robust, nuanced, and multifaceted" in a blog post is a tell.

### Tier 2: Flag If Excessive (medium confidence)

Hedging phrases stacking up ("It's important to note" + "It bears mentioning" in 500 words), elegant variation (unnatural synonym cycling for the same referent), em dash density exceeding 3-4 per 500 words alongside other markers, consecutive paragraphs opening with "Furthermore" / "Moreover" / "Additionally," and mechanical tricolon.

### Tier 3: Flag Only With Context (low confidence individually)

False balance ("While X, it's also true that Y" when Y is unwarranted), excessive signposting, the "Challenges + Future Prospects" formula, perfect Oxford comma consistency, and cliche openers like "In today's fast-paced world." These only get flagged when Tier 1 or 2 tells are already present.

## The Research Behind It

Key findings from the research that shaped this skill:

**Structure beats vocabulary.** GPTZero's core methodology uses burstiness (sentence-length variance) and perplexity (word-choice predictability). Desaire et al. (2023) found sentence-length standard deviation was a "valuable differentiator" — SD > 25 words per paragraph = human, SD < 25 = AI, with >99% accuracy on academic writing. The statistical fingerprint is rhythmic uniformity, not word choice.

**Em dashes are a weak signal.** The em dash became a cultural meme as "the ChatGPT hyphen," but a study found people who identified em dashes as AI tells had detection accuracy only marginally better than chance. The *New Yorker* is notoriously em-dash-heavy. Flag density only when it co-occurs with other markers.

**Co-occurrence is the real signal.** Kobak et al. (2025) found 454 words with excess frequency post-ChatGPT. But any individual word can appear in legitimate writing. Three or more AI-associated words clustering in proximity is a far stronger marker than any single instance.

**False positive risks for ESL writers are severe.** Liang et al. (2023) found 7 GPT detectors misclassified >61% of TOEFL essays as AI-generated. At UC Davis, 15 of 17 flagged students were false positives — disproportionately non-native speakers. This is why the skill never flags single words in isolation and defaults to conservative thresholds.

**Humans detect AI text at chance level (~50%).** But frequent ChatGPT users substantially outperform commercial detectors. Their top giveaways: AI vocabulary *clusters*, formulaic *structures*, and lack of originality. The goal isn't detector evasion — it's removing patterns that make text feel AI-generated to perceptive human readers.

## Design Decisions

| Decision | Choice | Why |
|----------|--------|-----|
| Detection scope | Human perception, not detector evasion | Detector evasion chases a moving target. Removing patterns that make text *feel* AI-generated produces durably better writing. |
| Edit granularity | Sub-sentence surgical editing | Sentence-level replacement changes too much voice. Surgical swaps preserve surrounding text. |
| Architecture | Two-pass (fix then audit) | Second pass catches structural patterns that only surface after vocabulary fixes. Validated by blader/humanizer (10.5k GitHub stars). |
| Default aggression | Conservative — co-occurring clusters and high-confidence structural patterns only | ESL writers, academic writers, and formal prose share features with AI output. Single-word flags produce unacceptable false positives. |
| Explanation model | Annotated editing with user approval | Builds trust, enables learning, lets user override bad calls. The #1 risk is overcorrection — transparency mitigates it. |
| Context gating | Genre presets with explicit thresholds | More predictable and debuggable than dynamic inference. User picks the preset; thresholds adjust. |
| Priority | Structural and rhythm first, vocabulary second | Research is unambiguous: synonym swapping doesn't change the statistical fingerprint. |

## Pairs With

**voice-extractor** — Load the user's voice profile before running ai-tell-killer. Fixes will match the user's natural style instead of generic alternatives. The skill removes the machine fingerprint; voice-extractor ensures what replaces it sounds like *you*.

**precision-editor** — Different tool for a different job. precision-editor works on human-written text at configurable edit levels. ai-tell-killer targets the machine fingerprint in AI-generated text. If the text was written by a human, use precision-editor instead.
