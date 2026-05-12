# PRD: ask-me-the-questions

## Problem

Most people stare at Claude's input box with a vague sense of what they need but can't articulate it. "I need help with my business plan" or "write me an email" — then get generic output because the input was generic. The workaround ("just give Claude more context") puts the burden on the user to know what context matters. Most don't. This is blank-prompt paralysis — the gap between "I know AI could help" and "I can get AI to help."

## Solution

The simplest skill in the collection. Instead of the user writing a good prompt, they describe their situation vaguely and the skill inverts the interaction: Claude interviews them to extract the context it needs, then produces the deliverable. 3 questions by default, never more than 5, always sequential, always adaptive. The intake must always feel optional, never mandatory.

## Design Decisions (from research)

| Decision | Choice | Why |
|----------|--------|-----|
| Default question count | **3, hard ceiling 5** | HubSpot (40K pages): 3 fields optimal. Cowan's working memory: 3-4 items. Average LLM conversation: 4.62 turns. The cliff between 3 and 6 fields drops conversion from ~50% to ~20%. |
| Presentation | **Always sequential, one at a time** | Multi-step forms convert 86% higher than all-at-once with identical content (Venture Harbour). Batched questions trigger form-filling mental model instead of conversation. |
| Question order | **Hybrid: universal priority backbone + adaptive thread-following** | Purpose → Audience → Constraints is universal across consulting, design thinking, creative briefs. But skip already-addressed dimensions and follow unexpected threads. |
| Transition to production | **Reflect-then-produce with explicit checkpoint** | "Got it — so I'm making [deliverable] for [audience] that [key constraint]. Should I go ahead?" McKinsey "Day 1 answer" pattern — working hypothesis from incomplete info. |
| Complexity adaptation | **Yes — detect and adjust** | Simple tasks (email, social post) get 2 questions. Medium tasks (plans, drafts) get 3-5. Pew Research: adaptive logic drops abandonment from 23% to 9%. |
| Architecture | **Standalone first, composable interface for other skills** | Clean internal contract: question selection engine + context completeness detector + brief generator. Same logic serves direct users and programmatic callers. |

## Interaction Model

### The Opening Move

When Claude receives a vague request, it responds with exactly three things in one message:

1. **Validate** (one sentence): Acknowledge what they're trying to do
2. **Signal brevity**: "Let me ask you a couple of quick questions so I can give you something actually useful."
3. **First question** (always purpose): "What's the main goal here — what do you need this to accomplish?"

The framing ("a couple of quick questions") sets expectations. Formstack data: framing the value proposition before the first question is the single largest predictor of completion.

### The Adaptive Middle

**Question 2** branches based on what Question 1 revealed:

| Q1 reveals... | Q2 asks about... |
|--------------|-----------------|
| Clear purpose, ambiguous audience | "Who's going to read/use this?" |
| Purpose implies known format | Skip format → "Any requirements I should know about — length, deadline, things to include or avoid?" |
| Vague language ("make it good," "professional") | Unbundle: "When you say 'professional,' what does that look like to you?" |
| Rich context already | Skip to production |

**Question 3** (if needed) addresses the highest-priority unresolved dimension from the priority stack: Purpose → Audience → Constraints → Format → Tone.

The skill internally tracks which dimensions are resolved. It never asks about something the user already covered, even implicitly.

### The Escape Hatch (critical design element)

At every question, the user can:
- Say "just go" or "that's enough" → skill immediately produces with available context
- Write a detailed response to Q1 that covers multiple dimensions → skill detects richness and skips remaining questions
- Provide the full spec directly → skill produces immediately, no questions asked

**The intake must always feel optional, never mandatory.** If someone writes two paragraphs of context in response to the opening question, asking three more questions is insulting. The skill should detect this and say: "You've given me plenty to work with. Here's what I have..."

### The Transition

After 2-5 questions (adaptive), Claude reflects understanding in one sentence:

> "Got it — so I'm making **[deliverable]** for **[audience]** that **[key constraint]**. Here's what I have..."

Then produces the deliverable immediately. No "Does this look right?" before producing — produce first, ask for feedback after. The McKinsey "Day 1 answer" principle: a complete working output from incomplete information, refined through iteration. Showing a hypothesis is faster than confirming a hypothesis.

### After Production

> "Here's a first pass. What would you change?"

One sentence. Not a list of caveats or explanations. Let the work speak.

## The Five Dimensions (internal tracking)

The skill silently tracks which of these five dimensions are resolved:

| Dimension | Priority | Example questions |
|-----------|----------|------------------|
| **Purpose** | 1 (always first) | "What's the main goal?" / "What do you need this to accomplish?" |
| **Audience** | 2 | "Who's going to read/use this?" / "Who are you writing to?" |
| **Constraints** | 3 | "Any requirements — length, deadline, must-include, must-avoid?" |
| **Format** | 4 | "What format — email, doc, presentation, social post?" |
| **Tone** | 5 | "What tone — formal, casual, urgent, friendly?" |

Rules:
- Skip any dimension the user's input already addressed (even implicitly)
- Promote whichever unresolved dimension would reduce the most ambiguity
- For simple tasks, Purpose alone may be sufficient
- Tone is almost never worth asking about explicitly (infer from purpose + audience)

## Task Complexity Detection

| Complexity | Signals | Question count | Examples |
|------------|---------|---------------|----------|
| **Simple** | Single output format, clear genre, short expected output | 2 | Email, social post, text message, quick answer |
| **Medium** | Multi-section, specific audience, moderate length | 3-4 | Blog post, plan, report, proposal |
| **Complex** | Multi-component, high stakes, specific requirements | 4-5 | Business plan, strategy doc, technical spec |

Detection runs on the user's initial input. Signals: output type keywords, length/complexity indicators, stakes language ("important," "client," "presentation").

## Success Criteria

- Users who would have written a one-sentence prompt produce output that's significantly more relevant (measured by: did they use the output without heavy editing?)
- Average question count per session: 2.5-3.5 (not hitting the ceiling regularly)
- Fewer than 10% of users say "just go" before Q2 (if more do, Q1 isn't providing enough value to justify the process)
- The intake adds under 2 minutes to the interaction
- Users report "it asked the right questions" or "I didn't think to mention that"

## What This Skill Does NOT Do

- Replace good prompting for expert users (if you know what you want, just say it)
- Conduct deep discovery for complex projects (that's ai-build-partner's job)
- Handle multi-session projects (this is a single-interaction intake)
- Produce the deliverable itself (it extracts context, then passes to Claude's normal generation — or routes to a specialized skill)

## Anti-Patterns to Avoid in Implementation

- Never batch questions ("Here are my three questions: 1... 2... 3...") — always one at a time
- Never ask about a dimension the user already covered
- Never ask more than 5 questions under any circumstances
- Never use the word "questionnaire," "survey," or "intake form" — this is a conversation
- Never ask about tone explicitly unless the user's purpose and audience leave it genuinely ambiguous (it almost never does)
- Never add "great question" or "thanks for sharing that" filler between questions — just ask the next question
- Never ask a question you can infer the answer to from context (if they said "email to my boss," don't ask "who's the audience?")

## Pairs With

- **Every other skill**: ask-me-the-questions is the universal front door. It can detect when a user needs a specific skill (resume, decision, interview prep) and route accordingly.
- **self-interview**: Different purpose. ask-me-the-questions extracts context for a deliverable. self-interview helps the user clarify their own thinking (no deliverable).
- **ai-build-partner**: For deeper, multi-session intake on complex projects, hand off to ai-build-partner's module system.
