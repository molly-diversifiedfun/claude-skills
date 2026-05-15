# Precision Editor

**Pick the editing level before the AI touches your text. Then make it stay in scope.**

## The Problem

You paste a draft and say "edit this." The model decides on its own how deep to go, and almost always goes too deep. A 2026 Berkeley study found LLMs make 3x the lexical changes a human editor makes — even when prompted for "minimal grammar edits." Niche's cognitive-debt research found heavy LLM editing produces a 70% jump in neutral argumentative stances and significant loss of personal voice.

The complaint is universal: "I asked for a light edit, not a rewrite." The model sees a slightly idiosyncratic sentence ("She bought eggs and was furious about it.") and rewrites it into something safer ("Frustrated, she purchased the eggs."). The original was fine. A professional copyeditor would have left it alone — the American Copy Editors Society explicitly trains them to: "if your only reason for revising is 'I would never write it like that,' leave the sentence alone."

The publishing industry solved this 80 years ago with named editorial tiers, each with explicit scope boundaries. A copyeditor who restructured an author's chapter would get fired. An LLM does it on the first prompt.

## What It Does

Forces you to pick an editing level before it touches your text, then enforces that level's scope through specific prohibitions.

Four levels, mapped to the publishing industry's named tiers:

1. **Flag only** — The skill tells you what it noticed. No fixes. You decide.
2. **Suggest as comments** — Your text reproduced verbatim, with bracketed suggestions inline. Nothing applied.
3. **Light copy edit** — Mechanical fixes only (grammar, spelling, punctuation, formatting). Your sentences survive even if the AI would write them differently. Clean copy + change log.
4. **Heavy developmental edit** — Editorial memo first. Rewrite is optional and only happens if you ask.

At levels 1-3, your sentences survive. The skill works around them, not through them.

Every output ends with a "Wanted to change but didn't" section — a refusal channel that traps the rewrite reflex by naming what the model wanted to do but the level forbade.

## How to Use It

### In Claude.ai

1. Start a new conversation
2. Open the skill: say "Use the precision-editor skill" (if added to your Project) or paste the contents of `SKILL.md` as your first message
3. Pick a level (1-4) when the skill asks
4. Paste your text
5. Answer the one calibration question
6. Get the edit in the format that matches the level
7. Iterate — escalate specific paragraphs to a higher level if you want

### In Claude Code

1. Add the skill to your config:
   - Copy `SKILL.md` to `~/.claude/skills/precision-editor/SKILL.md`
   - Or reference it in your `.claude/CLAUDE.md`: `When editing text, read path/to/precision-editor/SKILL.md`
2. Tell Claude Code: "Edit this draft" and let the skill ask you for a level
3. Pick a level, paste the text, answer the calibration question
4. Save the output if you want a record of the change log

### Tips for Better Results

- **If you're unsure which level to pick, pick 2.** Suggest is the safest non-trivial level. Your sentences stay intact. You can copy-paste with surgical changes.
- **If you want the AI to fix things, pick 3.** Level 3 applies changes but only mechanical ones. Your voice survives.
- **If the piece needs structural work, pick 4.** Level 4 looks at argument, pacing, and structure. You'll get an editorial memo before any rewrite — and the rewrite is opt-in.
- **For long documents (over 2,000 words), edit one section at a time.** Voice degradation compounds across long passes.
- **Read the "Wanted to change but didn't" section.** It's where the model lists everything the level scope blocked. If something there matters to you, escalate that one paragraph to a higher level.

## What You Get

### Level 1 output

```
## Issues found
1. Paragraph 2, sentence 3: "agile methodologies" — plural; check whether singular intended.
2. Paragraph 4, sentence 1: "utilized" and "in a timely manner" — corporate jargon, flag for review.

## Wanted to change but didn't
- Wanted to suggest cutting paragraph 5 (felt redundant with paragraph 2). Out of scope at flag-only.
```

### Level 2 output

```
## Annotated text
The team utilized [suggest: "used" — corporate jargon] agile methodologies to ship the feature in a timely manner [suggest: "on time" — filler].

## Wanted to change but didn't
- Wanted to rewrite the second sentence for punch. Bracketed comments don't fit a full rewrite.
```

### Level 3 output

```
## Edited copy
[Clean text with mechanical fixes applied]

## Change log
### Punctuation
- "despite, the rough start" → "despite the rough start" — restrictive clause, no comma needed.

## Wanted to change but didn't
- Wanted to swap "utilize" for "use" — style preference, not an error. Out of scope at level 3.
```

### Level 4 output

```
## Editorial memo
Two sentences doing four jobs (process, outcome, emotion, history). Suggest splitting into a process sentence + a result sentence + a brief story callback. The corporate-jargon vocabulary fights the personal pride beat — recommend reaching for plainer verbs.

## Want me to draft the rewrite?
[Skill stops here unless you say yes]
```

## The Research Behind It

Four findings shaped the design:

**The publishing industry already solved the level problem.** The Editorial Freelancers Association and the Chicago Manual of Style converge on a four-tier hierarchy — developmental, line, copy, proof — with stable scope boundaries that have survived for decades. AI editing tools fail because they don't know which tier they're operating at. The skill imports those tiers verbatim.

**Generic "preserve voice" prompts fail.** Atari et al. (2026) showed that even with explicit voice-preservation prompts, frontier models still pushed function words and first-person pronouns down and increased vocabulary diversity. Voice-preserving prompts only softened the rewrite reflex by 32%. The fix is specific prohibitions per level, not a generic instruction.

**LLMs are trained to generate, not preserve.** Junia.ai's analysis: "To the model, everything is editable because nothing is sacred." When you say "improve this," the model interprets it as "rewrite this in the safest, smoothest, most statistically common style possible." The skill counters this with explicit forbidden-action lists at every level.

**A refusal channel beats a constraint.** The most reliable pattern across the prompt-engineering literature is forcing the model to surface what it wanted to change but didn't. The accountability structure is the constraint. Without it, the model silently rewrites. With it, the model lists the urge and lets you decide.

## Design Decisions

| Decision | Choice | Why |
|----------|--------|-----|
| When the user picks the level | Before the skill touches a single sentence | Picking last means the model picks for you |
| Number of levels and naming | Four, named after publishing tiers (flag / suggest / copy edit / developmental) | Industry-standard names import scope conventions for free |
| Default if unsure | Level 2 (suggest) | Safest non-trivial level. Original preserved verbatim, AI input visible but unapplied |
| Refusal channel | Required at every level | Models that can't say "out of scope" silently rewrite instead |
| Voice-preservation enforcement | Specific block lists, not generic "preserve voice" | Generic preservation prompts only soften the rewrite reflex by 32% |
| Change-log requirement | Mandatory at levels 2-4 | The change log is the accountability mechanism — without it, scope creep is invisible |
| Output format per level | Match the publishing convention for that tier | Each tier has an established format that signals scope |
| Long input handling | Edit one section at a time over ~2,000 words | Voice degradation compounds across long output |
| Repeating constraints | Front-loaded AND end-loaded in every output | Counters the "Lost in the Middle" attention-decay effect |

## Pairs With

- **[voice-extractor](/voice-extractor/)** — Extract a voice profile first if you want the AI to write in your voice. Precision Editor edits what's already there; Voice Extractor builds the spec for new writing.
- **[humanize-ai-writing](/humanize-ai-writing/)** — Strip AI patterns from a draft before editing it. Run humanize first, then bring the cleaned-up draft to Precision Editor for the structural pass.
- **[ai-tell-killer](/ai-tell-killer/)** — Hunt down the specific phrases AI overuses. Pair with level 1 or 2 to flag and replace the worst offenders without restructuring your prose.
- **[devils-advocate](/devils-advocate/)** — Stress-test the argument before you edit the prose. Pair with level 4 to make sure the developmental edit fixes real weaknesses, not surface ones.
