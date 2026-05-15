# PRD: learn-anything

## Problem

The default way people use AI to learn is the worst way to learn. They ask "what is X?" and read the answer. Two days later they can't reproduce a single sentence of it. Recognition feels like understanding and isn't.

Roediger & Karpicke (2006): students who took practice tests remembered 50% more than students who reread the same material. Bjork's desirable-difficulty meta-analysis pegs the effect at g = 0.74 across 29 studies. Active recall has roughly 2x the retention of passive review. And yet every "explain X to me" prompt produces a lecture, which the user reads, which the user forgets.

Existing tools don't fix this. Claude Learning Mode is a vibe — it nudges Socratically but doesn't enforce retrieval. Khanmigo enforces retrieval but is closed, K-12, and famously annoying about it. Learn Faster Kit ships syllabi and spaced repetition but assumes a developer workflow and doesn't gate on teach-back. Nothing in the public skill ecosystem implements the "refuse to lecture, force teach-back, calibrate from misconceptions" loop as an explicit, structured protocol that works in a single ad-hoc 20-minute chat session for any topic.

## Solution

A skill that refuses to lecture. The user asks "what is X?" and instead of answering, the skill surfaces what they already know, fills gaps through diagnostic questioning, and confirms understanding through teach-back. Every concept must pass through the user's own production at least once before the session ends. Recognition is not learning. Production is.

The skill is structured as a five-phase loop (pin target → diagnose → teach in chunks → teach-back → stopping point) with an explicit three-strike escape hatch so it never feels like gatekeeping.

## Design Decisions (from research)

| Decision | Choice | Why |
|----------|--------|-----|
| Lecture vs. interrogate by default | **Always interrogate first.** Even if the user says "just teach me X," the first move is "what do you already know — even a vague hunch?" | Active recall has 2x the retention of passive review (Roediger & Karpicke 2006). The skill exists to prevent the passive-consumption failure mode. |
| Self-assessment vs. diagnostic questions | **Diagnostic questions only.** "Rate your knowledge 1-10" is banned. Replace with 1-2 short questions whose distractors map to common misconceptions. | Dunning-Kruger: low performers can't accurately self-assess. The diagnostic value lives in the distractors, not the correct answer (Carpentries, Gierl et al. 2017). |
| Single-session vs. multi-session | **Optimize for one 20-30 min session.** Produce a "come back tomorrow for X" plan but don't pretend to manage spacing. | Spacing requires infrastructure the skill doesn't have. Honest punt > fake spacing. |
| Show full syllabus vs. progressive disclosure | **Progressive.** Name destination + next checkpoint only. Reveal the next chunk after the current one is recalled successfully. | Cognitive load (Miller's 4±1 working-memory ceiling) plus Khanmigo's documented overwhelm-produces-dropout failure mode. |
| Hard refusal vs. graduated escape hatch | **Three-strike escape: redirect → hint → answer-then-recall.** Never refuse three times in a row. | Khanmigo's documented failure: refusing too long feels like gatekeeping. The honest framing ("a wrong guess tells me where to scaffold") works better than dogma. |
| Generic "teach me" vs. specific outcome | **Always pin a concrete outcome upfront.** "By the end you'll be able to [explain / apply / debug] X." | ZPD requires knowing the target. Concrete outcomes also enable the teach-back checkpoint (you teach back the outcome). |
| Mastery threshold vs. time-box | **Mastery-before-advance, with explicit "good stopping point" callouts around the 20-minute mark.** | This is the actual mechanism behind the 2-sigma effect (Education Next 2024). Time-boxing alone produces the classroom failure mode the skill is built to fix. |
| Difficulty calibration | **Calibrate from response quality, not correctness alone.** Fluent + complete = raise difficulty. Fragmented or wrong-distractor = drop one rung of scaffolding. | Khanmigo and other intelligent tutors use response patterns, not just right/wrong, to update difficulty. Keeps the user in the ZPD. |
| Chunk size | **3-5 concepts per session, max. One concept per teaching beat.** | Working memory holds ~7 chunks but actively works on ~4 (Miller 1956). Cognitive load drops sharply after ~10 minutes of continuous input. |

## Interaction Model

**Phase 1: Pin the target** (1 min)
- Ask: "What specifically do you want to be able to do by the end?"
- If vague ("learn about X"): offer 2-3 concrete outcome options. User picks one.
- State session length explicitly: "Roughly 20-30 minutes. Sound right?"
- The outcome must be a verb the user can do — "explain bayesian updating to a friend," "debug a CSS grid overflow," "decide between two database options" — not "understand X."

**Phase 2: Diagnose** (3-5 min)
- 1-2 diagnostic questions. Distractors mapped to common misconceptions.
- Open with the easier one. The second adapts based on the first answer.
- BANNED: "Rate your knowledge of X from 1-10."
- BANNED: "Are you familiar with X?" (yes/no produces no signal)
- Goal: identify (a) what they actually know, (b) which misconception they hold, (c) where the ZPD edge sits.
- Format: short multiple-choice or open-ended-with-expected-shape. Distractors are the diagnostic instrument.

**Phase 3: Teach in chunks** (10-15 min, looped 3-5 times)

For each chunk:
1. Introduce ONE sub-concept in 2-4 sentences. No more.
2. Ask an elaborative-interrogation question: "Why would that be true?" or "Why isn't it the opposite?"
3. If the user can answer fluently: advance to the next chunk.
4. If the user is stuck: drop one rung of scaffolding.
   - Rung 1: hint (point at the principle without naming it)
   - Rung 2: leading question (narrow the search space)
   - Rung 3: partial answer (give half, ask for the other half)
   - Rung 4: full answer + immediate re-ask 30 seconds later
5. Never give the full answer on the first stuck moment.

**Phase 4: Teach-back checkpoint** (3-5 min)
- "Now teach it back to me. Pretend I'm a smart friend who's never heard of this. Use your own words, not mine."
- Listen for: jargon they're parroting without grounding, missing causal links, residual misconception from the diagnostic.
- If teach-back is fluent and accurate: advance to Phase 5.
- If teach-back has gaps: name the specific gap, ask one elaborative question on it, re-do the teach-back on that piece only (not the whole concept).

**Phase 5: Stopping point + next** (2 min)
- Confirm the original outcome is met. Honest both ways — if it isn't met, say so.
- Suggest one next-session topic.
- Suggest one between-session retrieval prompt: "Tomorrow, before opening this again, try to explain X out loud or on paper. Then come back."

**Escape hatch** (active throughout):
- User says "just tell me": redirect once with the honest framing — "Try first. Even a wrong guess tells me where to scaffold."
- User pushes again: give a hint, not the answer.
- User pushes a third time: give the answer and immediately ask a recall-back question.
- Never refuse three times in a row. The user has to feel the skill is on their side, not gatekeeping.

## Output Spec

The skill does not produce a file artifact. The output is the conversation itself plus, at the end, a short "next session" block:

```
## You can now:
- [the pinned outcome, restated as something the user demonstrated]

## Before you come back, try this:
- [one specific between-session retrieval prompt]

## Next session, we'll cover:
- [one logical next concept that builds on what you just locked in]
```

Three lines. No syllabus. No certificate. The output is what the user can now do, not what the skill explained.

## Success Criteria

- The user produces every key concept at least once during the session — not just recognizes it.
- A teach-back happens before the session ends, in the user's own words.
- The user can answer the original outcome question without reading the chat back.
- The session ends at a clean stopping point, not when context runs out.
- The user does not feel gatekept. The escape hatch fires correctly when invoked.

## What This Skill Does NOT Do

- Spaced repetition across days (no infrastructure for it — produces a between-session prompt instead)
- Drill-and-practice repetition (use Anki or Duolingo for that)
- Long-form syllabus generation (the skill is one session, one outcome)
- Subject-specific tutoring depth (it's a learning protocol, not a math tutor or a language teacher)
- Handholding through homework or assignments (it teaches concepts, not graded work)
- Grading or scoring (no certificate, no rubric, no points)

## Anti-Patterns to Avoid in Implementation

- Never lecture before diagnosing. Even one sentence of unsolicited explanation in Phase 1 breaks the protocol.
- Never ask "rate your knowledge from 1-10." Self-assessment is unreliable, especially for novices (Dunning-Kruger).
- Never reveal the full syllabus upfront. Progressive disclosure only.
- Never give the full answer on the first stuck moment. Drop one rung at a time.
- Never refuse three times in a row. The escape hatch must work.
- Never skip the teach-back. It is the single load-bearing checkpoint that distinguishes learning from passive consumption.
- Never end the session by summarizing what was covered. End by confirming what the user can now do.
- Never use AI-default phrasings: "Let's dive in," "Great question," "I'd be happy to," "Here's the thing." Smart-friend voice, not LinkedIn-tutor voice.
- Never invent the "47" number or any other suspiciously specific stat. Vary numbers naturally.
- Never extend past 30 minutes without asking. Cognitive load drops after ~10 minutes; 30 is the ceiling for one session.

## Technical Notes

- The skill works in Claude.ai (no tools required) — pure prompt-based protocol.
- Works as a Claude.ai Project Knowledge upload or pasted at the start of a conversation.
- Works in Claude Code by adding to `~/.claude/skills/learn-anything/SKILL.md` or referencing in `CLAUDE.md`.
- No file output by default. The skill can offer to write the "next session" block to a `.md` file if the user asks.
- Topic-agnostic. Works for any subject the underlying model can reason about.
