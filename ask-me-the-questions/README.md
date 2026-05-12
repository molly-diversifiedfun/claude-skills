# Ask Me the Questions

## The Problem

Blank-prompt paralysis. People know Claude could help but can't articulate what they need. "I need help with my business plan" produces generic output because the input was generic. The standard advice — "just give Claude more context" — puts the burden on the user to know what context matters. Most don't.

## What It Does

Inverts the interaction. Instead of writing a better prompt, you describe what you need (even vaguely) and Claude interviews you to extract the context that matters. 3 questions by default, never more than 5, always one at a time, always adaptive to what you've already said.

The simplicity is the point. This is the simplest skill in the collection.

## How to Use It

### Claude.ai

Add this to your project instructions or paste into a conversation:

```
Read ~/github/claude-code-toolkit/skills/ask-me-the-questions/SKILL.md
```

Then make a vague request. Claude will interview you instead of guessing.

### Claude Code

Reference the skill in your `CLAUDE.md`:

```markdown
# Skills
- When a user request is vague or underspecified, read ~/github/claude-code-toolkit/skills/ask-me-the-questions/SKILL.md
```

Or invoke directly:

```
claude "Read the ask-me-the-questions SKILL.md and help me write a project proposal"
```

## The Protocol

**Opening move** — Validate the request in one sentence, signal brevity ("a couple of quick questions"), ask about purpose first.

**Adaptive middle** — Question 2 branches on what Question 1 revealed. Tracks five dimensions internally (purpose, audience, constraints, format, tone) and only asks about unresolved ones. Vague language gets unbundled ("When you say 'professional,' what does that look like?").

**Transition** — Reflects understanding in one sentence, then produces immediately. No confirmation prompt before output. "Here's a first pass. What would you change?"

**Escape hatch** — Say "just go" at any point. If your Q1 response is rich enough, the skill detects that and skips to production. Two paragraphs of context followed by three more questions is insulting — the skill knows that.

## The Research Behind It

Four findings drove the design:

- **Multi-step converts 86% higher.** Presenting identical questions one at a time instead of all at once (Venture Harbour). Batched questions trigger a form-filling mental model. Sequential questions feel like conversation.
- **3-field sweet spot.** HubSpot's analysis of 40,000+ landing pages: 3 fields is optimal (~25% conversion). Going from 4 to 3 increases conversions by nearly 50%. Cowan's revised working memory: 3-4 items, not the popular 7+/-2.
- **McKinsey "Day 1 answer."** Produce a complete working hypothesis from incomplete information, then refine. Showing an answer is faster than confirming a plan to produce an answer.
- **Universal priority order.** Every framework reviewed — consulting, design thinking, creative briefs, product requirements — puts purpose first and audience second. Purpose partitions the largest solution space. Audience determines tone, complexity, format, and vocabulary simultaneously.

Adaptive skip logic (Pew Research) dropped survey abandonment from 23% to 9%.

## Design Decisions

| Decision | Choice | Evidence |
|----------|--------|----------|
| Default question count | 3, hard ceiling 5 | HubSpot 40K pages, Cowan's working memory (3-4 items), avg LLM conversation 4.62 turns |
| Presentation | Sequential, one at a time | Multi-step converts 86% higher than batched (Venture Harbour) |
| Question order | Purpose > Audience > Constraints (adaptive) | Universal across consulting, design thinking, creative briefs |
| Transition | Reflect-then-produce, no confirmation gate | McKinsey Day 1 answer — show the hypothesis, don't ask permission |
| Complexity detection | 2 questions for simple, 3-4 medium, 4-5 complex | Pew: adaptive logic drops abandonment 23% to 9% |
| Escape hatch | Always available, auto-detect rich input | Intake must feel optional, never mandatory |

## Pairs With

Every other skill. This is the universal front door.

When a user's request maps to a specialized skill — resume builder, decision framework, interview prep — run the intake to extract context, then hand off to that skill with a structured brief. Ask-me-the-questions doesn't produce the deliverable itself; it makes sure the deliverable is informed.

Works especially well with **self-interview** (different purpose: self-interview clarifies the user's thinking, this one clarifies context for a deliverable) and **ai-build-partner** (for deeper, multi-session discovery that exceeds 5 questions).
