# CLAUDE.md

## What This Is

Public free skill library for Claude Code and Claude.ai. Taster menu for the paid [solopreneur-skills](https://github.com/molly-diversifiedfun/solopreneur-skills) collection. 18 skills across thinking, writing, career, learning, shipping, and Claude Code power-user categories.

## Skill Structure

Each skill is a self-contained directory:
```
skill-name/
  SKILL.md        # The skill itself (plain markdown, works in any LLM)
  references/     # Optional: templates, examples, reference material
  README.md       # Optional: what the skill does, how to use it
```
`SKILL.md` is the only required file. Everything else is supporting material.

## Research Pipeline

Skills are research-first, not vibes-first:
1. **Research prompts** (`docs/research-prompts.md`) -- reusable prompts for investigating a problem space
2. **Research briefs** (`docs/research/`) -- what users struggle with, what existing tools get wrong
3. **PRDs** (`docs/prds/`) -- design decisions, tradeoffs, interaction model, anti-patterns
4. **SKILL.md** -- built from research and PRD, not from scratch

## Adding a New Skill

1. Run research prompts against the problem space
2. Write a research brief in `docs/research/`
3. Write a PRD in `docs/prds/`
4. Create `skill-name/SKILL.md` (required) + `README.md` (recommended)
5. Add the skill to the table in the root `README.md`

## Conventions

- Kebab-case directory names
- SKILL.md is plain markdown -- no code dependencies, no API keys
- Skills must work in both Claude Code and Claude.ai
- Content voice: check `~/.claude/rules/brands/` and `/github/.claude/rules/content-voice.md`

## Paid Collection

The marketing/shipping skills here are samples from [solopreneur-skills](https://github.com/molly-diversifiedfun/solopreneur-skills) -- 25 skills covering ATTRACT, CONVERT, DELIVER & GROW, plus a skill-router meta-skill.
