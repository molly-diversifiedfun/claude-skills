# Learn Anything

**A skill that refuses to lecture. You ask "what is X?" — it asks what you already know first, fills gaps through questioning, and confirms understanding through teach-back.**

## The Problem

The default way people use AI to learn is the worst way to learn. You ask "what is X?", read the answer, and forget it by Friday. Recognition feels like understanding, and isn't.

Roediger & Karpicke's 2006 study: students who took practice tests remembered 50% more than students who reread the same material. Bjork's desirable-difficulty meta-analysis: g = 0.74 across 29 studies. Active recall has roughly 2x the retention of passive review. Every "explain X to me" prompt produces a lecture. Every lecture gets forgotten.

The existing tools don't fix this. Claude's Learning Mode nudges Socratically but doesn't enforce retrieval. Khanmigo enforces retrieval but is closed, K-12, and famously annoying about it. Learn Faster Kit ships syllabi for developers and assumes you'll come back daily. Nothing in the public skill ecosystem implements the "refuse to lecture, force teach-back, calibrate from misconceptions" loop as an explicit protocol that works in a single ad-hoc 20-minute session for any topic.

## What It Does

Five phases:

1. **Pin the target.** "What do you want to be able to do by the end?" The skill won't accept "understand X" — it pushes for a verb you can perform.
2. **Diagnose.** One or two short questions whose wrong answers map to common misconceptions. Distractor-based, not "rate your knowledge from 1-10" (which is unreliable for novices — Dunning-Kruger 1999).
3. **Teach in chunks.** 3-5 chunks max. One concept per chunk. After each: "why would that be true?" or "what would break if we removed this piece?" If you're stuck, the skill drops one rung of scaffolding at a time — hint, leading question, partial answer, full answer (last resort).
4. **Teach-back checkpoint.** You explain the concept back in your own words, as if to a smart friend. The skill listens for jargon parroting, missing causal links, and residual misconceptions.
5. **Stopping point + next.** Three lines: what you can now do, one between-session retrieval prompt, one logical next concept.

There's also an escape hatch. If you say "just tell me," the skill redirects once with the honest framing ("a wrong guess tells me where to scaffold"). Push again, you get a hint. Push a third time, you get the answer plus an immediate recall-back question. It never refuses three times in a row — that's how Khanmigo annoys people.

## How to Use It

### In Claude.ai

1. Start a new conversation.
2. Either:
   - Add `SKILL.md` to a Claude Project as Project Knowledge, then say "use the learn-anything skill," OR
   - Paste the contents of `SKILL.md` as your first message in any chat.
3. Tell Claude what you want to learn: "I want to learn bayesian updating," "explain CSS grid," "teach me how options pricing works."
4. Answer the questions. Don't skip ahead. The questions ARE the work.

### In Claude Code

1. Copy `SKILL.md` to `~/.claude/skills/learn-anything/SKILL.md`, OR reference it in your project `CLAUDE.md`: "When the user asks to learn something, read path/to/learn-anything/SKILL.md first."
2. Tell Claude Code: "I want to learn X" or "teach me Y."
3. Same five-phase loop. Same escape hatch. Same teach-back checkpoint.

## What You Get

The output is the conversation itself. By the end, you've actively produced every key concept at least once — not just read about it. You've teach-back'd the whole thing in your own words. And you walk away with a three-line wrap:

```
## You can now:
- [the concrete thing you can demonstrate]

## Before you come back, try this:
- [one between-session retrieval prompt]

## Next session, we'll cover:
- [the logical next concept]
```

No syllabus. No certificate. No "great job today." Just the next handle to grab.

## When NOT to Use It

- **One-line factual lookups** ("what year was X born?") — just ask. Don't make yourself earn a date.
- **Drill-and-practice repetition** — Anki and Duolingo are built for that.
- **Spaced repetition across days** — the skill is one session. It produces a between-session prompt, but doesn't manage spacing itself.
- **Long-form syllabus generation** — one session, one outcome.
- **Subject-specific tutoring depth** (medical board prep, organic chemistry) — it's a learning protocol, not a domain expert. Pair it with a domain skill or textbook.

## The Research Behind It

Five findings shaped the design:

**Active recall has 2x the retention of passive review.** Roediger & Karpicke (2006): testing produced 50% better long-term recall than re-reading. Schwieren et al. (2017) meta-analysis: d = 0.56. The single most replicated finding in cognitive psychology. The skill exists to enforce retrieval — that's the whole point.

**Self-assessment is unreliable, especially for novices.** Dunning-Kruger (1999): low performers systematically overestimate. "Rate your knowledge from 1-10" is noise. Diagnostic questions whose distractors map to common misconceptions are signal. The wrong answer the user picks tells you exactly which mental model they're operating with.

**Bloom's "two-sigma" effect was mostly the mastery threshold, not the 1:1 format.** The 2024 Education Next replication review concluded that holding learners to a high mastery threshold before advancing — not the magic of human tutoring — drove most of Bloom's 1984 result. The skill borrows the mastery-before-advance pattern: don't move on until the user can teach the concept back.

**The Khanmigo failure mode is being annoying about refusal.** ~700K users by 2024-25, real mastery gains, and a documented complaint that the Socratic method "requires patience" — younger users and people who just want help find question-after-question frustrating. The three-strike escape hatch is a direct response. Refuse once, hint twice, answer-then-recall on the third push. Never refuse three times in a row.

**Cognitive load drops sharply after ~10 minutes of continuous input.** Working memory holds about 4 active items (Miller 1956). Long sessions don't compound retention — they degrade it. The 20-30 minute session ceiling and the 3-5 chunk limit come straight from this.

## Design Decisions

| Decision | Choice | Why |
|----------|--------|-----|
| Lecture vs. interrogate by default | Always interrogate first, even if user says "just teach me" | Active recall has 2x the retention of passive review |
| Self-assessment vs. diagnostic questions | Distractor-based diagnostic only | Dunning-Kruger: novices can't accurately self-assess |
| Single vs. multi-session | One 20-30 minute session, with between-session retrieval prompt | Spacing requires infrastructure; honest punt > fake spacing |
| Show full syllabus vs. progressive disclosure | Progressive — destination + next checkpoint only | Cognitive load + Khanmigo's overwhelm-produces-dropout finding |
| Hard refusal vs. graduated escape hatch | Three-strike escape: redirect → hint → answer-then-recall | Refusing too long feels like gatekeeping |
| Generic "teach me" vs. specific outcome | Always pin a concrete, performable verb upfront | ZPD requires knowing the target; outcomes enable the teach-back checkpoint |
| Mastery threshold vs. time-box | Mastery-before-advance, with explicit stopping-point callouts | The actual mechanism behind the 2-sigma effect |
| Difficulty calibration | From response quality (fluent vs. fragmented), not just correctness | Keeps the user in the ZPD — the band where learning happens |
| Chunk size | 3-5 concepts per session, one per teaching beat | Working memory holds ~4 active items (Miller 1956) |

## Pairs With

- **[ask-me-the-questions](/ask-me-the-questions/)** — When you have a vague problem and need help getting specific. learn-anything teaches concepts; ask-me-the-questions clarifies your own thinking.
- **[self-interview](/self-interview/)** — Surface what you already believe but haven't articulated. Useful before a learning session to figure out what you actually need to know.
- **[mental-models](/mental-models/)** — Once you've learned a concept, mental-models helps you apply it to a real decision.
- **[devils-advocate](/devils-advocate/)** — After learning something new, stress-test your understanding by having it challenged.
