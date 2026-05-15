# PRD: precision-editor

## Problem

AI editing tools fail not because they edit badly — they fail because they don't know what level they're operating at. The user pastes a draft and says "edit this." The model decides on its own how deep to go, and almost always goes too deep. A 2026 Berkeley study found LLMs make 3x the lexical changes a human editor makes, even when prompted for "minimal grammar edits." Niche's cognitive-debt research found heavy LLM editing produces a 70% increase in neutral argumentative stances and significant loss of personal voice.

The complaint is universal: "I asked for a light edit, not a rewrite." The model sees a slightly idiosyncratic sentence ("She bought eggs and was furious about it.") and rewrites it to be slightly less interesting ("Frustrated, she purchased the eggs."). The original was fine. A professional copyeditor would have left it alone — ACES explicitly trains them to: "if your only reason for revising is 'I would never write it like that,' leave the sentence alone."

The publishing industry solved this 80 years ago with named editorial tiers — developmental, line, copy, proof — each with explicit scope boundaries. A copyeditor who restructured an author's chapter would get fired. An LLM does it on the first prompt. Existing AI editing tools each operate at one fixed level (Hemingway flags only; Grammarly does copy + proof; Sudowrite rewrites). None let the user pick a tier and then enforce that tier's scope.

## Solution

A skill that forces the user to pick an editing level before the AI touches a single sentence, then enforces that level's scope through explicit prohibitions. Four levels, mapped 1:1 to the publishing industry's named tiers. Each level has a fixed output format, a forbidden-actions list, and a "wanted to change but didn't" channel that traps the rewrite reflex.

At levels 1-3, the user's sentences survive. The skill works around them, not through them.

## Design Decisions (from research)

| Decision | Choice | Why |
|----------|--------|-----|
| When the user picks the level | **Before the skill touches a single sentence** — the first thing the skill does is force a level choice | Atari et al. (2026) showed that even "preserve voice" prompts only soften the rewrite reflex by 32%; the model still pushes vocabulary diversity up and function words down. Picking the level last means the model picks for you. |
| Number of levels and naming | **Four, named after publishing tiers** (flag / suggest / copy edit / developmental) | Industry-standard names import 80 years of scope conventions for free. Inventing "level 1.5" or "moderate edit" loses that signal. |
| Default level when unsure | **Level 2 (suggest as comments)** | Suggest is the safest non-trivial level. Original is preserved verbatim. AI's input is visible but unapplied. Author decides what to keep. Default at a level that can't damage the original. |
| Refusal channel | **Required at every level** — every output ends with a "wanted to change but didn't" section | Models that can't say "I'd want to change this but it's out of scope" silently rewrite instead. Naming the urge defuses it. |
| Voice-preservation enforcement | **Specific block lists, not generic "preserve voice"** — at levels 1-3, no word swaps for style ("utilize" → "use"), no sentence restructuring, no idiom replacement, no tone shifts unless the level explicitly allows it | Generic preservation prompts fail (Atari et al. 32% softener). Specific prohibitions work. |
| Change-log requirement | **Mandatory at levels 2-4** (optional at level 1, since level 1 changes nothing) | The change log is the accountability mechanism. Without it, scope creep is invisible. With it, the author can audit every change and reject any of them. |
| Output format per level | **Match the publishing convention for that tier** — proofreader's marked margin (L1), tracked-changes comments (L2), clean copy + change log (L3), editorial memo + optional rewrite (L4) | Each tier has an established format that signals scope. Inventing new formats loses the signal. |
| Original preservation | **Verbatim at levels 1-2, side-by-side at level 3, optional at level 4** | At level 3 the change log is the original. At level 4 the user has explicitly opted into restructuring — but the memo precedes the rewrite, so the user can stop before the rewrite. |
| Repeating constraints | **Front-loaded AND end-loaded in every output** | Liu et al.'s "Lost in the Middle" effect applies to long edits too. Critical instructions like "do not rewrite" lose attention by the time the model generates the change log. |
| Long input handling | **Edit one section at a time, never rewrite the whole thing in one pass** | Voice degradation compounds across long output (Berkeley 2026 found Sudowrite's voice preservation degrades over long-form). Section-by-section keeps each pass under the degradation threshold. |

## Interaction Model

**Phase 1: Level Selection (BLOCKING — happens before any text is read)**

The skill's first message is the level menu. The user must pick before pasting.

```
Pick your editing level. I won't touch your text until you do.

1. Flag only — I tell you what I notice. I don't suggest fixes. You decide what to act on.
2. Suggest as comments — I show your text verbatim with bracketed suggestions inline. Nothing gets applied. You copy-paste with surgical changes.
3. Light copy edit — Mechanical fixes only (grammar, spelling, punctuation, formatting). Your sentences survive even if I'd write them differently. You get a clean copy + a change log.
4. Heavy developmental edit — I look at structure, argument, pacing, voice. You get an editorial memo first. Rewrite is optional and only happens if you ask.

Default if you're unsure: 2. Suggest. It's the safest non-trivial level.
```

If the user pastes text without picking, the skill stops and re-asks. No exceptions.

**Phase 2: Text Intake**

After the user picks a level, the skill asks for the text. For long pieces (over ~2,000 words), the skill warns that it will edit one section at a time and asks the user to either paste a section or confirm full-document mode (which switches the skill into chunked-pass mode).

The skill also asks one calibration question per level:

- Level 1: "Anything specific you want me to focus on (grammar, voice, argument, all of it)?"
- Level 2: "Same — anything specific?"
- Level 3: "Any style guide to follow (Chicago, AP, MLA, house style)? Otherwise I'll go with general best practice."
- Level 4: "What's the goal — make it tighter, make it land harder, restructure for clarity, fix a specific weak section?"

**Phase 3: Edit Pass**

The skill performs the edit at the chosen level. Output format is fixed per level (see Output Spec section below).

**Phase 4: Refusal Channel (mandatory at every level)**

Every output ends with a "Wanted to change but didn't" section. This lists things the model wanted to do but the level's scope forbade. The user can decide whether to escalate to a higher level for those specific items.

If the section is empty, the skill says so explicitly: "Wanted to change but didn't: nothing — the level fit the text."

**Phase 5: Iteration (offer this, don't force it)**

After delivery, the skill offers:

> Want me to escalate any of these to a higher level? Or want to re-edit a specific paragraph at a different level?

The user can request specific paragraphs at a different level without re-running the whole edit.

## Output Spec Per Level

### Level 1 — Flag Only

**What changes:** Nothing in the original.

**Output format:**
```
## Issues found
1. [Location] [Quoted excerpt] — [Issue type: grammar / clarity / voice / fact / structure]
2. ...

## Wanted to change but didn't
[Anything the model wanted to suggest but flag-only scope forbids — e.g., specific word swaps]
```

**Forbidden:** Any rewriting. Any "and here's how to fix it" content. Any unsolicited improvement suggestions in the issue list itself.

### Level 2 — Suggest as Comments

**What changes:** Nothing in the original. Suggestions live in inline brackets.

**Output format:**
```
## Annotated text
[Original text reproduced verbatim, with bracketed suggestions inline like:
"The team utilized [suggest: 'used' — corporate jargon] agile methodologies..."]

## Wanted to change but didn't
[Things the model wanted to suggest but couldn't fit into bracketed comments — usually structural concerns]
```

**Forbidden:** Replacing sentences. Producing an "edited version." Any output where the original isn't preserved verbatim alongside the suggestions.

### Level 3 — Light Copy Edit

**What changes:** Grammar errors, spelling errors, punctuation, capitalization, formatting consistency, style-guide violations. Mechanical redundancies only when fix is purely mechanical (double words, dropped articles, "in order to" → "to").

**Output format:**
```
## Edited copy
[Clean text with mechanical fixes applied]

## Change log
### Grammar / mechanics
- [Original] → [Revised] — [reason]
### Punctuation
- ...
### Formatting / consistency
- ...

## Wanted to change but didn't
[Things the model wanted to revise but level-3 scope forbids — almost always style-not-error word choices]
```

**Forbidden:** Rewriting sentences for style. Replacing word choices that aren't errors ("until" → "till," "may" → "might"). Restructuring paragraphs. Smoothing transitions. Changing tone. Adding or removing content. ACES rule applies: "If the only reason is 'I would never write it like that,' leave it alone."

### Level 4 — Heavy Developmental Edit

**What changes:** Anything, with the author's explicit permission, after the editorial memo.

**Output format:**
```
## Editorial memo
[2-5 paragraphs naming the structural and substantive issues. Each issue gets a proposed direction. No rewrite yet.]

## Suggested restructuring
- [Specific structural change] — [why]
- ...

## Want me to draft the rewrite?
[Explicit ask. The skill stops here unless the user says yes.]

## Wanted to flag but didn't
[Anything the model noticed that wasn't worth raising in the memo]
```

If the user says yes to the rewrite:

```
## Rewrite (draft)
[The rewrite]

## What I changed (high-level)
- Restructured: [...]
- Cut: [...]
- Added: [...]
- Voice-preservation notes: [where the model held back vs. where it intervened]
```

**Forbidden:** Surprising the author. Skipping the editorial memo. Producing a rewrite without the memo first. Treating opting into level 4 as opting into a single specific style of rewrite — the model still asks before substituting voice.

## Success Criteria

- The user's sentences survive at levels 1-3, even ones the model would have written differently
- The user can audit every change at level 3 against the change log and reject any of them
- The "wanted to change but didn't" section is non-empty in most edits — proof that the scope is being enforced, not silently violated
- A level-3 edit doesn't introduce changes a professional copyeditor wouldn't make
- A level-4 edit never produces a rewrite without the user explicitly asking for it
- The user reports the output sounds like their writing, not the AI's writing

## What This Skill Does NOT Do

- Pick the editing level for the user
- Guess what the user "really meant" by "edit this" — it asks
- Edit without producing a change log at levels 2-4
- Rewrite at level 4 without the user explicitly accepting the offered rewrite
- Generate new content (it edits what exists; it doesn't invent)
- Translate, summarize, or change format — those are different jobs
- Ghostwrite (the user's draft is the input, not a brief)
- Operate on audio, video, or image-only documents

## Anti-Patterns to Avoid in Implementation

- Never let the model start editing before the user picks a level
- Never collapse "preserve voice" into a single line of generic prompt — every level needs explicit prohibitions
- Never produce a level-3 output without a change log
- Never produce a level-4 output without an editorial memo first
- Never silently expand scope — if the model wants to do more, it goes in the "wanted to change but didn't" section
- Never replace word choices for style at levels 1-3 ("utilize," "in a timely manner," "leverage" all survive unless the user asked for level 4)
- Never restructure paragraphs at levels 1-3
- Never produce an "improved" version that swaps sentence structures — that's a rewrite, not an edit
- Never use 47 in examples or numbers in examples — vary numbers naturally
- Never use AI filler ("Let's dive in," "I'd be happy to," "Great question")

## Technical Notes

- Works in Claude.ai (no tools required) — pure prompt-based logic
- Works in Claude Code as a markdown skill loaded into context
- For documents over ~2,000 words, the skill switches to section-by-section mode automatically
- Style guides supported at level 3: Chicago, AP, MLA, plus user-supplied house style
- The skill produces plain markdown output — portable to any editor or Doc tool
- No fine-tuning, no model training, no external API calls
