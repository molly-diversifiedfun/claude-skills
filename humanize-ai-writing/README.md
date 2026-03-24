# Humanize AI Writing

A Claude skill that aggressively strips AI patterns from text and injects human voice. The power washer, not the scalpel.

## The Problem

AI text has a fingerprint. Not just vocabulary — sentence-length uniformity, structural formulas, diplomatic neutrality, sterile grammar. Modern detectors (GPTZero, Originality.ai, Pangram Labs) use multi-model classifiers trained on specific LLM families. Claude, GPT, Gemini each leave distinct stylistic patterns that survive prompting tricks, custom styles, and even manual editing.

Existing "humanizer" tools make it worse. The DAMAGE paper (ACL 2025) found 74% of humanizer rewrites degraded text quality. Most just synonym-swap and introduce deliberate errors. That's not fixing the problem — it's creating a different flavor of uncanny valley.

The tells aren't words. They're shapes. Rhythm uniformity. Structural predictability. The absence of opinion. You can't ctrl+F your way out.

## What It Does

Full aggressive rewrite in two passes. This isn't surgical editing — it's a complete de-AI treatment that strips patterns AND actively injects human voice: opinion, specificity, rhythm variation, model-specific fingerprint removal.

Pass 1 audits and rewrites. Pass 2 re-reads the rewrite cold and catches patterns that survived. Two passes is not optional — AI-isms are recursive. Fixing one often introduces another.

## How It Does It

### Pass 1: Seven Checks (in order, they compound)

1. **Claude-Specific Fingerprints** — Thoughtful qualifiers, balanced-perspective reflex, ethical insertion, helpful disclaimers, the warmth pattern ("That's a great question!"). Kill all of it.
2. **AI Vocabulary** — 278-term tiered kill list. Tier 1 gets replaced on sight. Tier 2 flagged when 3+ cluster. Tier 3 flagged at document-level density. Era-specific tracking for GPT-4, GPT-4o, GPT-5, and Claude fingerprints.
3. **Structural Patterns** — Copula avoidance ("serves as" -> "is"), significance inflation, present participial clause-endings, the formulaic challenges/future section, hourglass structure, even paragraphing, negative parallelisms, rule of three.
4. **Rhythm/Burstiness** — AI averages ~27 words/sentence with minimal variance. Humans swing between 3-word fragments and 40-word run-ons. Force variation: no two consecutive sentences within 5 words of each other, fragments for emphasis, intentional grammar breaks.
5. **Specificity** — Replace every vague reference with a named tool, real number, specific person, actual date. Add at least one detail per section that only someone present would know.
6. **Voice and Opinion** — State unhedged opinions. Add parenthetical asides. Switch emotional registers. Write at least one sentence you'd say at a bar. If a brand voice is loaded, apply it here.
7. **Formatting Tells** — Em dash limit (1 per 500 words), synonym cycling (pick one word, repeat it), strip bold/emoji formatting from conversational content, normalize curly quotes, limit hyphenated word pairs.

### Pass 2: Verification

Re-reads the rewrite and checks for 10 specific survival patterns: recycled transitions, lingering copula swaps, inflation creep, rhythm relapse, unearned emotion, chatbot artifacts, template phrases, filler phrases, generic conclusions, cutoff disclaimers. If more than 3 survive, it runs Pass 1 again.

## The Kill List

Three-tier vocabulary system sourced from Wikipedia's AI Cleanup project, Max Planck Institute research, Pangram Labs' 560+ term database, and several open-source humanizer projects.

- **Tier 1 (Always replace):** 53 verbs, 19 adjectives, 17 adverbs, 28 nouns. Words that appear 50%+ more in AI text. "Delve," "leverage," "robust," "tapestry" — gone on sight.
- **Tier 2 (Clustered):** Normal words that become tells when 3+ appear in ~200 words. One "crucial" is fine. "Crucial" + "dynamic" + "innovative" in the same paragraph is a flag.
- **Tier 3 (Density):** Common words flagged only at 5+ per 1,000 words. "Significant," "effectively," "framework" — fine individually, suspicious in volume.

Plus era-specific vocabulary tracking and 50+ phrases to delete entirely (opening cliches, hedging filler, transition crutches, closing cliches, performative enthusiasm).

Full list: [`references/kill-list.md`](references/kill-list.md)

## Content-Type Quick Reference

| Format | Key Rules |
|--------|-----------|
| **DMs / Texts** | 1-3 sentences. Lowercase. No formatting. Zero em dashes. |
| **Social Posts** | Start mid-thought. One emoji max. End with a real question, not a polished CTA. |
| **Emails** | Open with the point. One ask per email. No "I hope this finds you well." |
| **Sales Copy** | Real numbers, real names. State the price without flinching. |
| **Long-Form** | Vary section lengths dramatically. Same word for same concept. Break the analytical register. |
| **LinkedIn** | No "thrilled to announce." One line per paragraph, but vary. Genuine question at end. |

## How to Use It

### Claude.ai

Paste your text and say any of:
- "Make this sound human"
- "De-AI this"
- "This sounds like a robot wrote it"
- "Humanize this email"

The skill triggers on any variation of wanting content to sound less AI-generated.

### Claude Code

```bash
claude "humanize this" < draft.txt
```

Or invoke directly:

```
/humanize-ai-writing
```

Then paste your text. If you have a voice profile loaded via voice-extractor, the rewrite will match your natural style.

## ai-tell-killer vs. humanize-ai-writing

| | ai-tell-killer | humanize-ai-writing |
|---|---|---|
| **Metaphor** | Scalpel | Power washer |
| **Approach** | Surgical — identifies specific tells, fixes only those, leaves everything else | Aggressive — full rewrite through 7-check system, actively injects human voice |
| **Edit scope** | <20% of sentences changed | Entire text gets reworked |
| **Output** | Annotated report with numbered fixes, user approves each one | Clean rewrite, two passes, delivered ready to use |
| **Best for** | Text that's mostly good but has detectable AI patterns | Text that reads like AI top to bottom and needs a full overhaul |
| **Preserves** | Maximum original voice | Original meaning and intent (voice gets rebuilt) |

Use ai-tell-killer when you wrote something with AI assistance and want to sand off the edges. Use humanize-ai-writing when the whole thing sounds like a chatbot and you need it reborn.

## Pairs With

- **voice-extractor** — Load your voice profile first. The rewrite will sound like you instead of generic-human. This is the single biggest upgrade to output quality.
- **ai-tell-killer** — If you want the surgical version instead. Annotated report, user-approved fixes, <20% of text changed.
