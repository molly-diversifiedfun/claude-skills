# CARL Manager

**Add persistent rules to your Claude Code setup through conversation, not config files.**

CARL = Context Augmentation & Reinforcement Layer. Instead of repeating the same instructions every session, you define rules once and they auto-load when relevant. This skill lets you build and edit them by talking, not by hand-editing `.carl` files.

## The Problem

Every Claude Code user eventually accumulates the same set of unwritten rules: *"always use TypeScript strict,"* *"never auto-commit,"* *"check for tests before refactoring."* You either re-type them every session, paste them into CLAUDE.md (which then bloats), or build a rule system manually. The rule system route is the right answer; building it manually is friction.

## What It Does

Auto-activates when you say things like:
- *"Make this a rule"*
- *"Add this to CARL"*
- *"Create a domain for [topic]"*
- *"Which domain does this belong in?"*

Then walks you through:

1. **Domain selection.** Names the right CARL domain for your rule (or proposes a new one). Domains scope when the rule loads — global vs. when-editing-a-config-file vs. when-touching-database-migrations.
2. **Rule drafting.** Writes the rule in the CARL format (clear directive, concrete trigger, named exception cases).
3. **Manifest update.** Edits the CARL manifest so the rule actually loads.
4. **Verification.** Tells you exactly when the rule will fire next so you can confirm it works.

Read `CONTEXT-RULES.md` and `DOMAIN-GUIDE.md` for the underlying rule format and the available domains. `MANIFEST-REFERENCE.md` documents the manifest structure if you're editing manually. `COMMANDS-GUIDE.md` covers the star-command system (`*dev`, `*review`, `*brief`).

## How to Use It

### In Claude Code

```bash
cp -r carl-manager ~/.claude/skills/carl-manager
```

Then in any session: *"Make this a rule: [the rule]"* or *"Add this to CARL: [the behavior]"*

### In Claude.ai

Less useful here — CARL is specifically for Claude Code's persistent context system. If you're on Claude.ai, custom instructions or Project Knowledge cover the same ground.

## What Makes This Different

- **Conversational, not config-edit.** You describe the rule; the skill handles the format.
- **Domain-aware.** Won't dump everything into a global "always" rule — proposes the most-scoped domain that still catches your case.
- **Pairs with carl-help** for new users — read that first if you don't know what CARL is.

## Pairs With

- **[carl-help](/carl-help/)** — Read this BEFORE using carl-manager if you've never touched CARL. Covers what it is, how loading works, what domains exist
- **[voice-extractor](/voice-extractor/)** — Use to build a CARL rule that locks in your tone across all writing sessions

## License

MIT. CARL is part of Molly's Claude Code configuration — see [claude-config-public](https://github.com/molly-diversifiedfun/claude-config-public) for the full setup.
