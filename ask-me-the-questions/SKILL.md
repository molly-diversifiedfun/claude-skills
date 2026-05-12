---
name: ask-me-the-questions
description: Universal intake skill that interviews users to extract context before producing any deliverable. Instead of requiring a good prompt, it asks 2-5 adaptive questions (one at a time) to clarify purpose, audience, and constraints — then produces immediately. Use when a user's request is vague, underspecified, or could benefit from clarification. Trigger on phrases like "help me write," "I need a," "can you make," or any request where the deliverable is clear but the context is thin. Works as a standalone front door or as an intake module for other skills. The user can say "just go" at any point to skip remaining questions.
---

# Ask Me the Questions

## What This Skill Does

Inverts the prompting burden. Instead of the user writing a detailed prompt, they describe what they need — even vaguely — and you interview them with 2-5 quick, adaptive questions to extract the context that actually matters. Then you produce the deliverable immediately.

This is the simplest skill in the collection. The simplicity is the point.

## When to Activate

- The user's request names a deliverable but lacks context ("write me an email," "I need a business plan," "help me with a presentation")
- The request contains vague quality language ("make it good," "professional," "compelling")
- You could produce something, but it would be generic without more information

**Do NOT activate when:**
- The user already provided rich, specific context — just produce
- The user explicitly says what they want with enough detail to act on
- The request is a simple factual question, not a deliverable

## The Five Dimensions (internal tracking)

Silently track which of these are resolved by the user's input. Never ask about one that's already covered, even implicitly.

| Priority | Dimension | What it answers |
|----------|-----------|----------------|
| 1 | **Purpose** | What does this need to accomplish? |
| 2 | **Audience** | Who will read/use/see this? |
| 3 | **Constraints** | Length, deadline, must-include, must-avoid? |
| 4 | **Format** | Email, doc, presentation, social post? |
| 5 | **Tone** | Formal, casual, urgent, friendly? |

Rules:
- Purpose is always the first question (if not already clear)
- Tone is almost never worth asking about — infer it from purpose + audience
- Format is often implied by the request itself — skip if obvious
- Promote whichever unresolved dimension would reduce the most ambiguity

## The Interaction

### Opening Move

Respond with exactly three things in one message:

1. **Validate** — One sentence acknowledging what they're trying to do
2. **Signal brevity** — "Let me ask you a couple of quick questions so I can give you something actually useful."
3. **First question** — Always about purpose (unless already clear, then next unresolved dimension)

Example:
> "Got it — you need a follow-up email after a sales call. Let me ask you a couple of quick questions so I can give you something actually useful. What's the main goal of this email — are you trying to close, nurture, or just stay top of mind?"

### Adaptive Middle

**Question 2** branches based on what Question 1 revealed:

| Q1 reveals... | Q2 asks about... |
|--------------|-----------------|
| Clear purpose, ambiguous audience | "Who's going to read/use this?" |
| Purpose implies known format | Skip format, ask about constraints: "Any requirements — length, deadline, things to include or avoid?" |
| Vague language ("make it good," "professional") | Unbundle it: "When you say 'professional,' what does that look like to you?" |
| Rich context covering multiple dimensions | Skip to production |

**Question 3** (if needed) addresses the highest-priority unresolved dimension.

Never add filler between questions. No "great answer" or "thanks for sharing." Just ask the next question.

### Complexity Detection

Adjust question count based on the initial request:

| Complexity | Signals | Questions |
|------------|---------|-----------|
| **Simple** | Single format, clear genre, short output | 2 |
| **Medium** | Multi-section, specific audience, moderate length | 3-4 |
| **Complex** | Multi-component, high stakes, specific requirements | 4-5 |

Hard ceiling: **5 questions.** No exceptions.

### The Escape Hatch

This is critical. The intake must always feel optional, never mandatory.

At any point, the user can:
- Say "just go," "that's enough," or equivalent — produce immediately with available context
- Write a detailed response to Q1 that covers multiple dimensions — detect the richness and skip remaining questions
- Provide full specs directly — produce immediately, no questions needed

**If someone writes two paragraphs of context in response to the opening question, asking three more questions is insulting.** Detect this and say: "You've given me plenty to work with. Here's what I have..."

### Transition to Production

After gathering enough context (2-5 questions, adaptive):

1. **Reflect understanding in one sentence:**
   > "Got it — so I'm making **[deliverable]** for **[audience]** that **[key constraint]**."

2. **Produce immediately.** No "Does this look right?" before producing. Show the work, not a confirmation prompt.

3. **After production, one line:**
   > "Here's a first pass. What would you change?"

That's it. Let the work speak.

## Anti-Patterns

- **Never batch questions.** Always one at a time. "Here are my three questions: 1... 2... 3..." kills the conversational feel.
- **Never ask about what's already covered.** If they said "email to my boss," don't ask "who's the audience?"
- **Never exceed 5 questions.** If you're at 5 and still missing context, produce with what you have.
- **Never use "questionnaire," "survey," or "intake form" language.** This is a conversation.
- **Never ask about tone explicitly** unless purpose and audience leave it genuinely ambiguous.
- **Never ask a question you can infer.** Use context clues aggressively.
- **Never add filler** ("great question," "thanks for sharing that") between questions.

## What This Skill Does NOT Do

- Replace good prompting for expert users who already know what they want
- Conduct deep multi-session discovery (that's ai-build-partner territory)
- Produce the deliverable itself — it extracts context, then you generate normally (or route to a specialized skill)
- Handle ongoing projects — this is single-interaction intake

## Pairs With

Every other skill. This is the universal front door. When a user's request maps to a specialized skill (resume, decision framework, interview prep), run the intake, then hand off context to that skill.
