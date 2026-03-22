# Molly's Claude Skills

Free skills I've built for Claude Code and Claude.ai. Take them. Use them. Ship something.

---

## What's Here

7 skills across three categories. Each one is a self-contained folder with a `SKILL.md` file that teaches Claude how to do something specific.

### For Builders & Shippers

| Skill | What It Does |
|-------|-------------|
| [`unstuck-coach`](./unstuck-coach/) | Modular coaching system for side-project shippers. Diagnoses stuck patterns, audits builds, cuts scope, validates ideas, plans sprints, and creates roadmaps. 8 modules, each produces a concrete artifact. |

### For Marketers

Three skills from my [Solopreneur Skills](https://github.com/molly-diversifiedfun/solopreneur-skills) collection — free samples so you can see if the approach clicks.

| Skill | What It Does |
|-------|-------------|
| [`build-irresistible-offer`](./build-irresistible-offer/) | Architect offers people feel stupid saying no to. Value stacking, named IP, guarantee structure, urgency mechanics. Based on the Hormozi Value Equation. |
| [`funnel-ad-creator`](./funnel-ad-creator/) | Generate a complete ad script bible — 12-16 storyboarded ads across TOFU/MOFU/BOFU/Retargeting with a 4-week testing protocol. |
| [`instagram-reels-framework`](./instagram-reels-framework/) | Production-ready Reel scripts with timed beats, filming notes, 7 hook types, 5 beat structures, and a 12-point scoring rubric. |

### For Claude Code Power Users

| Skill | What It Does |
|-------|-------------|
| [`carl-manager`](./carl-manager/) | Manage CARL (Context Augmentation & Reinforcement Layer) domains and rules. Persistent memory for how you work — define rules once, they load automatically when relevant. |
| [`carl-help`](./carl-help/) | Reference docs for CARL — what it is, how it works, file structure, rule format, troubleshooting. |
| [`nano-banana`](./nano-banana/) | Image generation via Gemini CLI. Blog images, thumbnails, icons, diagrams, illustrations — any visual asset. Requires [Gemini CLI](https://github.com/google-gemini/gemini-cli) installed. |

---

## Install

### Claude Code

Clone and point Claude Code at the skill you want:

```bash
git clone https://github.com/molly-diversifiedfun/claude-skills.git
```

Then install a skill to your Claude Code environment:

```bash
# Copy a skill to your local skills directory
cp -r claude-skills/unstuck-coach ~/.claude/skills/unstuck-coach
```

Or reference the skill directly in a conversation — Claude will read the `SKILL.md` when you point it at the folder.

### Claude.ai

Upload any skill's `SKILL.md` file as a Project Knowledge file. Claude picks it up automatically.

---

## Want the Full Marketing Toolkit?

The three marketing skills here are samples from **[Solopreneur Skills](https://github.com/molly-diversifiedfun/solopreneur-skills)** — a 25-skill system that covers the entire solopreneur pipeline from audience research through referral engines.

The skills chain together: output from one feeds directly into the next. Run `skill-router` with your situation and it maps the exact skills to run, in order.

**ATTRACT** (8 skills) — personas, messaging, hooks, content, ads, brand voice
**CONVERT** (10 skills) — offers, pricing, sales letters, landing pages, launches
**DELIVER & GROW** (6 skills) — onboarding, email, automation, win-back, referrals
**META** (1 skill) — skill-router that sequences everything for your situation

---

## Who Made These

[Molly Shelestak](https://github.com/molly-diversifiedfun) — Principal PM by day, builder of too many things by night. I make tools that help people stop planning and start shipping.

- **Unstuck with Molly** — Build partnership for side-project shippers
- **Diversified Fun** — Strategic consulting for creative businesses
- **The Flamingo Effect** — Book on building followable systems (coming 2026)

---

## License

These skills are free to use, modify, and share. If you build something cool with them, I'd love to hear about it.
