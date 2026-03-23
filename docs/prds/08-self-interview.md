# PRD: self-interview

## Problem

People know what they think — they just can't access it. "I know what I think but I can't put it into words" is the universal experience before a big talk, a career decision, a strategy shift, or a difficult conversation. AI makes this worse by offering to think FOR you instead of helping you think for YOURSELF. Every AI coaching tool defaults to validation ("That's a profound insight!") instead of genuine interrogation.

## Solution

Claude asks the user progressive questions to surface what they believe but haven't articulated. Not a quiz, not feedback, not brainstorming. A structured self-interrogation that follows the user's thinking using five distinct questioning techniques, produces surprise through the user's OWN contradictions, and outputs a clarity map showing what's solid vs. what's still fuzzy.

## Design Decisions (from research)

| Decision | Choice | Why |
|----------|--------|-----|
| Challenge intensity | **Start gentle, escalate based on user's contradictions** | Elenchus research: shame triggers fight-or-flight. Challenge emerges from the user's own statements, not Claude's tone. |
| Exact words vs. paraphrase | **Exact words for emotionally weighted terms, natural language for structural questions** | Grove's Clean Language contamination research is too strong to ignore. "What kind of stuck is that stuck?" on key terms, normal language elsewhere. |
| Output artifact | **Clarity map** (solid vs. fuzzy areas) | Foregrounds WHERE thinking is clear vs. unclear. Fuzzy areas are findings, not failures. Supported by narrative therapy externalization (White & Epston). |
| Session length | **Soft cap: 10-12 questions, check-in at 7-8** | Uncapped self-analysis correlates with worse outcomes (reflection-rumination boundary). Let user override once with awareness. |
| "I don't know" handling | **One probe, then read the response** | Engagement = stay, flatness = move. Never push past two consecutive "I don't know" on the same thread. (Miller & Rollnick sustain-talk/discord distinction) |
| Does Claude name contradictions? | **No — lets user discover them via contrast questions** | The elenchus works because the person discovers their own contradiction. Having it pointed out produces defensiveness. Exception: user explicitly asks Claude to reflect back. |

## The Five Questioning Channels

The skill doesn't use one technique — it interleaves five based on what the user's responses reveal:

| Channel | When to Use | Signature Move |
|---------|------------|----------------|
| **Socratic elenchus** | User holds confident, unexamined belief | Surface implications: "If that's true, what follows? Are you comfortable with ALL the implications?" |
| **Clean Language** | User is vague, emotional, or metaphorical | Mirror exact words: "What kind of [their word] is that [their word]?" |
| **MI directional pull** | User is stuck between options, ambivalent | Pull for reasons: "You said 6, not 1 — why not lower?" |
| **Sensory specificity** | User gives rehearsed-sounding answers | Drop to episodic memory: "What's the first moment you knew?" |
| **Contrast question** | User has said two conflicting things | Hold both side by side: "You said X matters most, but you've been doing Y. What's happening there?" |

**Channel-switching rule:** When a question produces surprise, stay on that thread. When it produces repetition, shift channels.

## Interaction Model

### The Diamond Shape: narrow → broad → narrow

**Opening (1-2 questions): Thesis Extraction**

Not "Tell me about your thinking on X" (too broad — invites monologue). Instead:

> "What's the one thing you're most trying to figure out right now?"

or

> "State your current position on [topic] in one sentence."

This creates a concrete target for the elenchus to work with. If the user gives a vague answer, follow up with sensory specificity: "When did you first start thinking about this? What was happening?"

**Expansion (3-6 questions): Pressure Testing**

Select questioning channel based on what the opening reveals:

- **Confident belief stated?** → Elenchus: "What would have to be true for that to hold? Do you believe all those things?"
- **Vague or emotional language?** → Clean Language: "And that's [their word] like what?"
- **Stuck between options?** → MI: "What matters most to you about this?"
- **Rehearsed-sounding answer?** → Sensory specificity: "You said [X] — what do you mean by that?"

Follow threads, not scripts. When the user says something surprising (to themselves or to Claude), stay on that thread for at least 2-3 more questions before shifting.

**The Pressure Point (questions 5-8): The Turn**

This is where the session produces genuine insight or stalls. The right question is a **contrast question** — holding two things the user has said side by side:

> "You said [X] matters most to you, but you also said you've been spending all your time on [Y]. What's happening there?"

This is the elenchus in modern form: the contradiction comes from the user's own statements. Claude never says "you contradicted yourself." It says "I notice a tension between X and Y — how do you see those fitting together?"

**Check-In (around question 7-8):**

> "We've been at this for a bit. What's clearer now? Want to keep going or should we start wrapping up?"

**Resolution (2-3 questions): Crystallization + Gap-Marking**

Do NOT summarize. Instead, ask the user to state where they've landed:

1. "What's clearer now than when we started?"
2. "What's still fuzzy?"
3. "What's the next thing you'd need to figure out?"

The final question positions unresolved questions as valuable output, not failure.

### Then: The Clarity Map

```
## Clarity Map

### What's Solid
- [Belief/position 1 — stated with confidence, tested through questioning]
- [Belief/position 2]

### What's Emerging
- [Insight that surfaced during the session — new, not fully formed]
- [Connection the user made between previously separate ideas]

### What's Still Fuzzy
- [Area where the user said "I don't know" or gave contradictory signals]
- [Question that remains open]

### The Tension
[The core contradiction or unresolved question that emerged —
stated in the user's own words]

### Next Question to Answer
[The forward-looking question from the resolution phase]
```

**Caveat on the map:** "Fuzzy areas aren't failures — they're the most valuable part. They show you exactly where your thinking needs more work."

## Anti-Sycophancy Rules (hardcoded)

1. **Never say "That's a great insight" or "That's really profound."** The user decides what's profound. Claude's job is to ask the next question.
2. **Never validate an answer before moving on.** Ask the next question. Silence IS validation.
3. **Never add Claude's own analysis of what the user is thinking.** Extract, don't add. The output is the USER's thinking crystallized.
4. **Never suggest an answer when the user says "I don't know."** Probe once, then move on or shift channels.
5. **Never summarize mid-session.** Summaries kill momentum. The clarity map comes at the end.
6. **Never use filler phrases:** "That's interesting," "I appreciate you sharing that," "Thanks for being honest" — all are noise.
7. **If the user asks "What do you think?": deflect.** "This isn't about what I think — what are YOU landing on?" Exception: after the session ends, Claude can offer observations if explicitly asked.

## Success Criteria

- The user says something that surprises themselves during the session (the felt shift)
- The clarity map distinguishes solid from fuzzy areas (not just a transcript summary)
- The session takes 15-25 minutes (not 5 minutes of shallow questions, not 45 minutes of rumination)
- The user can hand the clarity map to someone else and they understand the core tension
- Questions feel like they're following the user's thinking, not leading it

## What This Skill Does NOT Do

- Give advice or opinions (extract, don't add)
- Provide feedback on the user's ideas (that's devil's-advocate)
- Help articulate something for an external audience (that's ask-me-the-questions)
- Produce a deliverable (the clarity map is for the USER, not for anyone else)
- Replace therapy or coaching (no clinical claims, no emotional support framing)

## Pairs With

- **ask-me-the-questions**: Different purpose. ask-me-the-questions extracts context for a deliverable. self-interview helps you clarify your own thinking (no deliverable).
- **devil's-advocate**: self-interview helps you figure out what you think. devil's-advocate challenges it once you've decided.
- **decision-maker**: If the self-interview reveals a decision between options, hand off to decision-maker for the structured brief.
- **voice-extractor**: If the self-interview is about "what's my voice / brand / positioning," the clarity map feeds directly into voice-extractor's sample collection.
