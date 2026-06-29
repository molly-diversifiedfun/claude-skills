# prompt-factory

Generate research-grade prompts when you need external knowledge — not guesses.

## The problem it solves

When you ask an LLM a question that requires current market data, tool comparisons, platform pricing, or audience research, you get a confident answer that may be months or years out of date. The Prompt Factory pattern skips the guess: instead of an answer, you get a self-contained research prompt pre-filled with your specific context, ready to paste into a search-enabled AI conversation.

## When to use it

- "Which tool should I use for X?"
- "What do people in my niche charge?"
- "Where does my audience hang out online?"
- "How do I set up [specific platform]?" (UIs change constantly)
- Any question where the right answer depends on current data you don't have

## How it works

1. Tell Claude you want to use the Prompt Factory
2. Give it your context: product, audience, price, constraints, what you need
3. Claude generates a pre-filled, copy-paste-ready research prompt
4. You run it in a new conversation with web search on (Perplexity, Claude with search, ChatGPT with browsing)
5. You bring back the result and continue

## Usage

```
Use the Prompt Factory pattern. I need to research [topic].

My context:
- Product: [what you're building]
- Audience: [who it's for]
- Price: [if relevant]
- Constraints: [time, budget, technical skill, timeline]
- What I need: [specific deliverable]
```

## Origin

Extracted from the [`ai-build-partner`](../ai-build-partner/) skill where it was used to delegate external knowledge questions from inside a multi-module coaching session. Works as a standalone pattern in any context.
