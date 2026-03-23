# Self-Interview

## The Problem

"I know what I think but I can't put it into words."

This happens before every big talk, career decision, strategy shift, or hard conversation. You have the thinking — you just can't access it.

AI makes this worse. Every AI coaching tool defaults to validation. Your half-baked plan becomes "mythic," your simple observation becomes "profound." If everything is always good, nothing is truly good. People need extraction, not addition.

## What It Does

Claude asks YOU questions. Not a quiz, not feedback, not brainstorming. A structured self-interrogation that follows your thinking using five distinct questioning channels, surfaces your OWN contradictions, and produces a clarity map showing what's solid vs. what's still fuzzy.

The session runs 15-25 minutes, 8-12 substantive questions. Claude never gives advice, never validates, never summarizes mid-session. It asks one question at a time, uses your exact words for emotionally weighted terms, and tracks what you've said so it can hold your statements side by side later.

## How to Use It

### Claude.ai

Start a conversation and say something like:

- "I need to think through my position on X"
- "Help me figure out what I actually believe about Y"
- "Self-interview me on Z"

Claude will open with a single question. Answer it. The session takes shape from there.

### Claude Code

```
/self-interview
```

Or reference the skill in your prompt: "Use the self-interview skill to help me think through X."

## The Five Questioning Channels

The skill doesn't use one technique. It interleaves five based on what your responses reveal.

| Channel | When It Fires | What It Does |
|---------|--------------|--------------|
| **Socratic elenchus** | You hold a confident, unexamined belief | Surfaces implications: "If that's true, what follows? Are you comfortable with ALL the implications?" |
| **Clean Language** | You're vague, emotional, or metaphorical | Mirrors your exact words back: "What kind of [your word] is that [your word]?" Zero contamination from the interviewer. |
| **MI directional pull** | You're stuck between options | Pulls for reasons: "You said 6, not 1 — why not lower?" Uses self-perception to strengthen commitment. |
| **Sensory specificity** | You give rehearsed-sounding answers | Drops to episodic memory: "What's the first moment you knew?" Bypasses the verbal narrative track. |
| **Contrast questions** | You've said two conflicting things | Holds both side by side: "You said X matters most, but you've been doing Y. What's happening there?" |

**Channel-switching rule:** When a question produces surprise — stay. When it produces repetition — shift.

## The Diamond Shape

Sessions follow a diamond: narrow opening, broad middle, narrow close.

```
        ◇ Opening — Thesis extraction
       / \
      /   \  Expansion — Pressure testing through multiple channels
     /     \
    /       \
   ◇ The Turn — Contrast question (your own contradictions, side by side)
    \       /
     \     /
      \   /  Resolution — Crystallization + gap-marking
       \ /
        ◇ Clarity Map
```

**Opening (1-2 questions):** "What's the one thing you're most trying to figure out?" or "State your current position on [topic] in one sentence." Creates a concrete target.

**Expansion (3-6 questions):** Pressure testing through whichever channels fit. Confident belief gets elenchus. Vague language gets Clean Language. Ambivalence gets MI. Rehearsed answers get sensory specificity.

**The Turn (questions 5-8):** A contrast question holding two things you said side by side. The contradiction comes from your own statements. Claude never says "you contradicted yourself."

**Resolution (2-3 questions):** "What's clearer now than when we started?" / "What's still fuzzy?" / "What's the next thing you'd need to figure out?" Unresolved questions are valuable output, not failure.

## The Research Behind It

Every technique bypasses rehearsed narrative through a different cognitive channel. That's the core insight — effective questioning redirects attention away from pre-processed verbal narrative toward something you haven't rehearsed.

- **Socratic elenchus** forces your beliefs into the same room until contradictions surface from within your own belief set
- **Clean Language** (David Grove) uses only your exact words, eliminating interviewer contamination. People use ~6 metaphors per minute — each one is cognitive infrastructure
- **MI open questions** (Miller & Rollnick) are engineered to elicit specific kinds of self-talk. The balance of change talk vs. sustain talk is the strongest predictor of behavior change
- **Sensory specificity** forces episodic memory retrieval, activating sensory and emotional processing rather than the rehearsed verbal track
- **Gendlin's Focusing research** (15 years, University of Chicago) found the single factor distinguishing successful therapy clients was attention to vague bodily sensation until it clarified

**On insight quality:** Insight-derived solutions are correct 94% of the time vs. 78% for analytical solutions (Salvi et al.). The felt shift — that "oh!" moment — is a real signal, not just a feeling.

**On the reflection-rumination boundary:** Self-analysis focused on gaining new insight produces positive outcomes. Repetitive negative dwelling produces negative outcomes. The session's soft cap at 10-12 questions and check-in at question 7-8 exist specifically to keep you on the insight side of that line.

## The Clarity Map

After the session, Claude produces a map using only your words:

```
## Clarity Map

### What's Solid
- [Position stated with confidence, tested through questioning]

### What's Emerging
- [Insight that surfaced during the session — new, not fully formed]

### What's Still Fuzzy
- [Area where you said "I don't know" or gave contradictory signals]

### The Tension
[The core contradiction or unresolved question — in your words]

### Next Question to Answer
[What you said you need to figure out next]
```

Fuzzy areas aren't failures — they're the most valuable part. They show you exactly where your thinking needs more work.

## Pairs With

| Skill | Handoff |
|-------|---------|
| **devil's-advocate** | Self-interview helps you figure out what you think. Devil's-advocate challenges it once you've decided. |
| **decision-maker** | If the session reveals a decision between options, hand off for a structured decision brief. |
| **ask-me-the-questions** | Different purpose. ask-me-the-questions extracts context for a deliverable. Self-interview clarifies your thinking for yourself. |
| **voice-extractor** | If the session is about "what's my voice / brand / positioning," the clarity map feeds directly into voice-extractor. |
