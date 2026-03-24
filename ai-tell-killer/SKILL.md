---
name: humanize-ai-writing
description: Strip AI patterns from any written content and make it sound like a real human wrote it. Use this skill whenever the user says anything like "make this sound human," "this sounds like AI," "de-AI this," "make it sound like me," "humanize this," "this sounds robotic," "rewrite this naturally," "this doesn't sound right," "make it less AI," "sound more natural," or any variation of wanting content to feel authentic and human-written rather than machine-generated. Also trigger when reviewing any draft, copy, script, email, DM, social post, or marketing content where the user hasn't explicitly asked for humanization but the output clearly contains AI patterns. If the user has a brand voice skill active, combine this skill with that voice. This skill is about the WAY writing sounds, not WHAT it says.
---

# Humanize AI Writing v2

## Why AI Text Gets Caught

Detectors measure two core signals: **perplexity** (how predictable each word choice is) and **burstiness** (how much sentence length varies). AI scores low on both because every token converges toward the most statistically likely next word. The result reads like the average of everything on the internet — technically correct, stylistically dead.

But modern detectors (GPTZero, Originality.ai, Pangram Labs) now go far beyond those two signals. They use multi-model classifiers trained on outputs from specific LLM families. Claude, GPT, Gemini, and Llama each leave distinct **stylistic fingerprints** that survive prompting tricks, custom writing styles, and even manual editing — unless you break the underlying structural patterns.

This skill targets those structural patterns. Not surface swaps.

## The Two-Pass System

Every piece of content runs through **two passes**. The second pass re-reads the rewrite and catches patterns that survive the first edit. This is not optional — AI-isms are recursive. Fixing one often introduces another.

---

## PASS 1: Audit and Rewrite

Run these seven checks in order. They compound.

### 1. Strip Claude-Specific Fingerprints

Claude has model-specific tells that other LLMs don't share. These are the first things to kill because they're what Claude-trained detectors look for.

**Thoughtful qualifiers.** Claude constantly hedges with "I think," "it seems," "from my understanding," "it's worth noting," "broadly speaking." Delete or replace with direct statements.

**Balanced-perspective reflex.** Claude presents both sides even when the topic has a clear answer. "While some argue X, others contend Y" — if you have a position, state it. Don't false-balance.

**Ethical insertion.** Claude reflexively adds ethical implications, caveats about responsible use, or disclaimers about limitations. Strip these unless the content genuinely requires them.

**Helpful disclaimers.** "This is a complex topic," "results may vary," "it's important to consult a professional" — delete unless legally necessary.

**Structured over-organization.** Claude defaults to headers, numbered lists, and bullet points even in conversational content. If the format is a DM, email, social post, or script — strip all structural formatting.

**The warmth pattern.** Claude opens with validation ("That's a great question," "I appreciate you sharing that," "Absolutely!") and closes with offers ("I hope this helps," "Let me know if you'd like me to expand on any section"). Delete all of it.

### 2. Kill AI Vocabulary

Consult `references/kill-list.md` for the complete tiered list. The tiers work like this:

- **Tier 1 (Always flag):** These words appear 50%+ more in AI text than human text. Replace on sight. No exceptions. Examples: delve, leverage, utilize, robust, comprehensive, multifaceted, pivotal, seamless, tapestry, landscape (metaphorical), moreover, furthermore.
- **Tier 2 (Flag when clustered):** These are normal English words that become AI tells when 3+ appear in the same section. Examples: foster, illuminate, crucial, dynamic, innovative, catalyst, trajectory, spectrum.
- **Tier 3 (Flag at density):** Common words that only signal AI when they appear at unusually high frequency. Examples: significant, effectively, potential, approach, framework, context, enhance.

Also kill **era-specific vocabulary** — detectors now track which words cluster by model generation:
- 2023-era (GPT-4): delve, tapestry, testament, vibrant, intricate, meticulous
- 2024-era (GPT-4o): fostering, showcasing, highlighting, bolstered, align with
- 2025+ era (GPT-5): emphasizing, enhance, highlighting, showcasing
- Claude-specific at any era: nuanced, straightforward, genuinely, I'd be happy to

### 3. Fix Structural Patterns

These are shapes, not words. You can't ctrl+F for them.

**Copula avoidance.** The single most underrated AI tell. AI writes "serves as," "functions as," "acts as," "features," "boasts," "presents" instead of "is" and "has." Replace aggressively. "The platform serves as a unified hub" → "The platform is a dashboard." "The building features a rooftop garden" → "The building has a rooftop garden."

**Significance inflation.** AI can't describe anything without inflating its importance. "Marking a pivotal moment in the evolution of..." → "was founded in 2019." "A watershed moment for the industry" → just state the fact. If a sentence claims something is significant, pivotal, transformative, or groundbreaking, delete the claim and let the fact speak.

**Present participial clause-endings.** This is one of the top detection signals flagged by Wikipedia's AI Cleanup project. AI ends sentences with "-ing" clauses that make vague claims of importance: "...highlighting the need for continued innovation," "...underscoring the significance of this development," "...reflecting broader industry trends." These appear 2-5x more in AI text. Cut them. End sentences directly.

**The formulaic challenges/future section.** AI writes a "Despite challenges... continues to thrive" paragraph, often followed by "Future Prospects." This rigid formula — positive → acknowledge challenges → pivot back to positive — is a top detection signal. Either be specific about the actual challenge and response, or cut the section.

**Hourglass structure.** AI opens with a synthesis, narrows to details, then closes with another synthesis. Human writing doesn't follow this pattern reliably. Vary your structure. Start mid-argument sometimes. End abruptly sometimes.

**Even paragraphing.** AI produces paragraphs of roughly equal length, creating visual symmetry that detectors flag. Vary dramatically. One sentence can be a paragraph. A ten-sentence paragraph is fine if it flows.

**Negative parallelisms.** "It's not just X — it's Y." "It's not about the technology — it's about the people." AI uses this construction constantly. State the point directly instead.

**The rule of three.** "Smart, strategic, and scalable." "Clear, concise, and compelling." AI defaults to triple constructions. Use two items. Use four. Use one. Vary.

### 4. Fix Rhythm (Burstiness)

This is the most mechanically measurable signal. AI averages ~27 words per sentence with minimal variance. Humans swing between 3-word fragments and 40-word run-ons.

**Rules:**
- No two consecutive sentences should be within 5 words of each other in length
- Include at least one sentence under 5 words per paragraph
- Include at least one sentence over 25 words per section
- Start at least one sentence with "And" or "But"
- Use a fragment for emphasis at least once
- Break a grammar rule intentionally at least once (start with a conjunction, use a comma splice, end with a preposition)
- Vary paragraph length: some 1 sentence, some 6+

### 5. Replace Generality with Specificity

AI generalizes because it doesn't have lived experience. Every vague reference is a flag. Every specific detail is proof of a person.

**Replace:**
- "a popular tool" → name the tool (Notion, Figma, Linear)
- "a recent study" → name the study or at minimum the source and year
- "industry experts" → name one person or cite one org
- "a significant amount" → state the number
- "over time" → state the timeframe
- "various stakeholders" → name who specifically
- "the meeting went well" → what specifically happened

**Add at least one detail per section that only someone present would know.** A day of the week. An exact dollar amount. A named person. A real tool version number. A specific metric.

### 6. Inject Voice and Opinion

AI is diplomatically neutral. Humans take sides.

- State at least one unhedged opinion per piece ("This is wrong" not "Some might consider this suboptimal")
- Include a parenthetical aside, tangent, or "but I digress" moment
- Switch emotional register at least once (analytical → frustrated → amused)
- Write one sentence you'd actually say at a bar — if it's too polished for that, rewrite it
- Add self-deprecation, sarcasm, or dry humor where the content supports it
- If a brand voice exists (check brand-voice-router), apply it here

### 7. Kill Remaining Formatting Tells

**Em dashes.** One per 500 words maximum. Replace with periods, commas, or restructure.

**Synonym cycling.** AI rotates words for the same concept — "platform" → "solution" → "ecosystem" → "framework." Pick one word. Repeat it. Real writers repeat themselves.

**Boldface/formatting in conversational content.** Bold headers, inline bold labels ("**Key insight:**"), emoji headers (🚀💡✅) — strip all of it in DMs, emails, social posts, scripts.

**Curly quotes.** Claude sometimes produces typographic curly quotes (" ") instead of straight quotes (" "). Normalize to straight quotes.

**Hyphenated word pair clustering.** "Cross-functional, data-driven, client-facing, solution-oriented" — AI stacks these. Use one, maximum two, per paragraph.

**Title Case in headings.** AI capitalizes "Strategic Negotiations And Partnerships." Use sentence case: "Strategic negotiations and partnerships."

---

## PASS 2: Verify Rewrite

Read the rewrite fresh. Check for these survivals:

1. **Recycled transitions.** Did "moreover" become "additionally" become "furthermore"? All three are AI tells. Use "and," "also," "plus," or restructure.
2. **Lingering copula swaps.** Did "serves as" become "functions as" or "acts as"? Still AI. Use "is."
3. **Inflation creep.** Did you cut "groundbreaking" but introduce "transformative" or "game-changing"? Same problem, different word.
4. **Rhythm relapse.** Read the rewritten version aloud. Did sentence lengths re-flatten? Check word counts.
5. **The emotional flatline.** Did the rewrite claim "What surprised me most was..." or "I was fascinated to discover..." without earning the emotion? Either make the reader feel it through specifics, or cut the emotional claim.
6. **Chatbot artifacts.** Any surviving "I hope this helps," "Let me know if," "Feel free to," "Great question," "Absolutely!" — delete.
7. **Template phrases.** "A [adj] step towards [adj] [noun]" — this mad-libs construction is an instant tell. Rewrite as a specific claim.
8. **Filler phrases.** "In order to" → "To." "Due to the fact that" → "Because." "It is worth noting that" → delete.
9. **Generic conclusions.** "The future looks bright," "Exciting times lie ahead," "Only time will tell" — cut or replace with a specific closing thought.
10. **Cutoff disclaimers.** "While specific details are limited..." "Based on available information..." — either find the information or remove the sentence.

If the Pass 2 audit finds more than 3 surviving patterns, run the rewrite through Pass 1 again before delivering.

---

## Content-Type Quick Reference

### DMs / Text Messages
- 1-3 sentences per message. No transitions. One thought per message.
- Lowercase where natural. Abbreviations fine. No formatting.
- Zero em dashes. Zero bold. Zero structure.

### Social Posts / Captions
- Start mid-thought, not with "In today's..."
- One emoji maximum (or zero). No hashtag stuffing.
- Write like you're texting a group chat. End with a real question or a half-thought, not a polished CTA.

### Emails
- Open with the point. No "I hope this finds you well."
- End with a specific ask, not "Please don't hesitate to reach out."
- One ask per email. One.

### Sales Copy / Scripts
- Real numbers, real names, real stories. Be specific about who this is NOT for.
- State the price without flinching. No "Imagine a world where..."

### Long-Form (Articles, Guides, Docs)
- Vary section lengths dramatically. Some get two sentences. Some get a full page.
- Use the same word for the same thing. Don't cycle synonyms.
- Include a personal observation that breaks the analytical register.

### LinkedIn Posts
- No "I'm thrilled to announce." Start with the insight or the tension.
- One line per paragraph (LinkedIn formatting). But vary — some paragraphs get 2-3 lines.
- End with a genuine question, not a performative one.

---

## What NOT to Do

- Don't just add contractions and call it human. That's surface-level.
- Don't over-correct into chaos. The goal is natural, not sloppy.
- Don't add fake typos or "um"s. That's cosplay.
- Don't swap AI words for simpler synonyms while keeping the same structure. The structure IS the problem.
- Don't use AI-humanizer tools or paraphrasers. They create a different flavor of uncanny valley — detectors are now trained on humanizer outputs specifically.
- Don't assume one pass is enough. It never is.

## Reference Files

- `references/kill-list.md` — Complete tiered vocabulary kill list with era-specific tracking and replacement tables. Consult during Pass 1, Step 2.
