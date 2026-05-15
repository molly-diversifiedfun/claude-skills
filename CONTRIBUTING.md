# Contributing

Built a skill that fits this collection? Open a PR. Found a bug or a confusing instruction in an existing skill? Open an issue.

## Built a skill?

The bar isn't "perfect." It's: **does this solve a real problem a Claude user keeps running into, and is the SKILL.md crisp enough that someone can use it without you in the room?**

To open a PR:

1. Fork the repo
2. Add a top-level directory: `your-skill-name/` (kebab-case)
3. Inside, add at minimum a `SKILL.md` with valid YAML frontmatter (`name`, `description`)
4. A `README.md` is strongly recommended — what it does, who it's for, how to use it, what it pairs with
5. A `references/` folder is welcome for templates, kill lists, examples
6. Add an entry to the root `README.md` table in the right category (or propose a new category)
7. Open the PR

What works well:

- The skill solves ONE problem cleanly (not five problems mediocre-ly)
- The SKILL.md is under 500 lines
- The description names what activates the skill (trigger phrases) — see existing skills
- There's at least one anti-pattern named ("don't do X")
- It works in both Claude.ai (Project Knowledge upload) and Claude Code

What I'll push back on:

- Skills that wrap an existing API and call it a skill (it's usually a tool, not a skill)
- Skills that depend on private/paid services without a free alternative
- Skills with no opinion (great skills take a position; mediocre ones list options)

## Found a problem?

Open an issue. Tell me:
- Which skill
- What you tried
- What happened vs. what you expected
- Bonus: the exact prompt you used

## Want a skill that doesn't exist yet?

Open a Discussion under "Ideas." If it's solving a real recurring problem and I haven't built it elsewhere, I'll add it to the research backlog.

## Voice

Skills in this collection are direct, opinionated, mechanism-first, and free of corporate filler. If your skill reads like a SaaS landing page, I'll ask you to revise. The model knows how to write like an executive — that's not what users come here for.
