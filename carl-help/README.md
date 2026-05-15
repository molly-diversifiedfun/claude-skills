# CARL Help

**Reference docs for the CARL rule system. Read this before [carl-manager](/carl-manager/) if you've never used CARL.**

## What's CARL?

**Context Augmentation & Reinforcement Layer.** It gives Claude Code persistent rules that load just-in-time based on what you're doing — instead of you re-typing instructions every session or bloating a CLAUDE.md file.

How loading works:

```
You type: "help me fix this bug"
   │
   ▼
Hook scans your prompt for keywords
   │
   ▼
Matches "fix bug" → DEVELOPMENT domain
   │
   ▼
Rules from that domain load into context
```

The full overview lives in `CARL-OVERVIEW.md` — read it for the architecture, the domain list, and the manifest format.

## How to Use It

This isn't an active skill — it's reference material. Two ways to read it:

### In Claude Code

```bash
cp -r carl-help ~/.claude/skills/carl-help
```

Then in any session: *"Explain CARL"* or *"How does CARL work?"* — Claude pulls from `CARL-OVERVIEW.md`.

### In Claude.ai

Open `CARL-OVERVIEW.md` in the repo and read it directly. There's no interactive component.

## When to Read This

- Before using [carl-manager](/carl-manager/) for the first time
- Before editing a `.carl` file by hand
- When you're trying to figure out which domain a rule belongs in
- When CARL isn't loading a rule you expect it to load (debugging mental model)

## Pairs With

- **[carl-manager](/carl-manager/)** — The active skill that uses what this teaches. Read carl-help first, then carl-manager does the work.

## License

MIT. CARL is part of Molly's Claude Code configuration — see [claude-config-public](https://github.com/molly-diversifiedfun/claude-config-public) for the full setup.
