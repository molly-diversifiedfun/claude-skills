# Prompt Factory

> When you need external knowledge, don't guess. Generate a prompt you can run.

## What this is

You're working on something — a product, a piece of copy, a launch, a decision. You hit a moment that needs real information: current tool pricing, what your audience actually says online, which platform to use, how competitors are positioned. Claude can't answer that reliably — it doesn't have live data, and its training on your specific niche is patchy.

The Prompt Factory pattern: instead of getting a guess, you get a research-grade prompt pre-loaded with your context that you run in a new conversation with web search enabled.

Result: current, specific, actionable research — not a fabricated answer.

## When to use it

Fire the Prompt Factory when the answer depends on:
- **Current market data** — pricing, competitors, tools, platform fees, feature availability
- **Your specific industry's norms** — what people in your niche charge, what channels they use, what language they use
- **Tool/platform selection** — "which should I use" questions where the right answer depends on current pricing and features
- **Audience research** — where your buyers hang out, what frustrations they're expressing publicly
- **Platform setup instructions** — UIs change; don't trust cached steps

Do NOT use it for:
- Questions where you (or the person you're asking) already have the answer
- Emotional or strategic decisions that don't need external data
- Methodology questions where the skill IS the answer
- Quick picks where the answer is obvious (e.g. "should I use Carrd or a custom Rails app for a $19 ebook landing page" — Carrd, done)

## The pattern

Tell Claude:

```
Use the Prompt Factory pattern. I need to research [topic].

My context:
- Product: [what you're building]
- Audience: [who it's for]
- Price: [if relevant]
- Constraints: [time, budget, technical skill, timeline]
- What I need: [specific deliverable — a recommendation, a comparison, a list]
```

Claude will generate a self-contained research prompt pre-filled with your specifics. You copy it, open a new conversation with web search enabled (Perplexity, Claude with search, ChatGPT with browsing), paste it, and come back with the result.

## What a good generated prompt looks like

Every prompt the Factory generates follows this structure:

```
[One sentence stating exactly what needs to be found out]

Context:
- Product: [specific]
- Audience: [specific]
- Price point: [if relevant]
- Constraints: [hours/week, budget, technical skill, timeline]

What I need:
- [Specific deliverable — one recommendation, a ranked list, a comparison table]

Don't:
- Recommend enterprise solutions for a solo project
- Tell me to "evaluate multiple options" — pick one and tell me why
- Give me pricing from 2023 — check current rates
- Suggest I "consider my needs" — I've told you my needs above

Output format:
- [Table / ranked list / decision with rationale — whatever fits]
- Include: [specific fields you need]
```

## Prompt must-haves

A bad prompt asks a general question. A good prompt gives the LLM no room to be generic:

- **Specifics baked in** — product name, price, audience, timeline, budget. The person running the prompt should not need to fill anything in.
- **One recommendation, not five options** — "give me a recommendation" is useful; "here are 5 options to consider" is not.
- **Current data explicitly requested** — tell the LLM to check current pricing and features, not rely on what it knows.
- **Output format specified** — table, numbered list, 3-paragraph answer. Vague output instructions produce vague output.
- **What to bring back** — end every prompt with "come back and share [specific thing]."

## Examples

### Tech stack selection

You're building a digital download product, non-technical, 8 hours/week. You ask "what should I use?"

Generated prompt:
```
I need to pick a simple tech stack for a digital download product. I'm not a developer.

Context:
- Product: Notion template for new engineering managers
- Type: digital download ($29 one-time)
- Audience: newly promoted EMs at mid-stage startups
- My skills: PM background; can use no-code tools, copy-paste code, but not building a React app
- Hours/week: 8
- Timeline: launch in 14 days
- Budget: under $20/month total for tools

What I need:
- Landing page tool (one recommendation)
- Payment processing (one recommendation)
- File delivery after purchase (one recommendation)
- Email collection + 3-email post-purchase sequence (one recommendation)

For each: name the tool, current free tier limits, monthly cost at my scale, and setup time in minutes.

Output: a table — Tool | What it does | Free tier | Paid cost | Setup time | Why this one.

Check current pricing — don't give me 2023 numbers.
```

### Audience research

You know your buyer roughly but need real language and channels.

Generated prompt:
```
I need to understand where my target buyers hang out and what language they use about their problems.

My product: a spec-writing course for junior PMs at SaaS companies ($49)
My one-liner: junior PMs learn to write one-pagers that get buy-in instead of PRDs that get ignored

Research:
1. Where do junior PMs at SaaS companies hang out online? (specific Slack communities, subreddits, newsletters, Twitter/X accounts)
2. What do they currently pay for professional development? (price ranges for courses, books, subscriptions)
3. What are the top 3 frustrations they express publicly? (search Reddit, LinkedIn, Glassdoor — I need exact phrases, not paraphrases)
4. Who are the 3-5 existing courses or products competing for their attention and money? (with current prices)
5. What specific language do they use to describe the "PRD that gets ignored" problem?

For each section: cite where you found it (subreddit name, community, specific post if possible). I need real language from real people, not marketing persona templates.
```

### Competitive pricing

You're pricing a new product and need to know what the market actually charges.

Generated prompt:
```
I need to understand current pricing in the market for [category] targeted at [audience].

My product: [one-liner]
My context: [relevant constraints]

Research:
1. What are the 5 most direct competitors? List their current pricing tiers.
2. What's the most common price point in this category for [specific customer type]?
3. Are there any products charging significantly more than the median? What justifies the premium?
4. What does the free tier (if any) typically include vs. the paid tier?

Output: a table of competitors with their pricing, plus a 1-paragraph summary of where I should price and why.

Check actual current pricing pages — don't rely on cached data.
```

## Anti-patterns

- **Generating a prompt for everything** — if you can just answer directly with high confidence, do that. The Factory is for external knowledge, not a way to avoid answering.
- **Vague prompts** — "research my market" sent to another LLM produces generic output. Every prompt must have their specific product, price, audience, and constraints baked in.
- **Forgetting what to bring back** — every prompt should end with "come back with [specific thing]." Otherwise you get a wall of research with no clear handoff.
- **Using it for decisions that are already made** — if you know the answer is Stripe for payments, don't generate a prompt. Say Stripe.
