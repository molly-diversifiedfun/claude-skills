# Molly's Claude Skills

Free skills I've built for Claude Code and Claude.ai. Take them. Use them. Ship something.

Each skill is a self-contained folder with a `SKILL.md` file that teaches Claude how to do something specific. Most also have reference files, templates, or examples. Every skill works in both Claude Code and Claude.ai.

---

## The Skills

### Think Better

Skills that make you a sharper thinker, not just a faster one.

| Skill | What It Does |
|-------|-------------|
| [`mental-models`](./mental-models/) | 12 thinking frameworks with an intelligent router. Describe your problem, it matches you to the right model and walks you through it step-by-step. Pre-Mortem, First Principles, Steel-Manning, 5 Whys, and 8 more. |
| [`devils-advocate`](./devils-advocate/) | Adversarial thinking partner that actually stays adversarial. Built with anti-sycophancy architecture so it won't fold when you push back. Steel-mans your argument first, then tears it apart. |
| [`decision-maker`](./decision-maker/) | Produces a one-page decision brief when you're stuck between options. 7 sections, ~350 words, with 6 cognitive biases silently countered by the template structure. Sleep on it, hand it to a co-founder, revisit in 90 days. |
| [`self-interview`](./self-interview/) | Claude asks YOU questions to surface what you actually think but haven't articulated. Five questioning techniques, diamond-shaped session, produces a clarity map of solid vs. fuzzy areas. |
| [`ask-me-the-questions`](./ask-me-the-questions/) | The simplest skill here. You describe what you need vaguely, Claude interviews you to extract the right context, then produces the deliverable. Solves blank-prompt paralysis. 3 questions, never more than 5. |

### Write Better

Skills that fix the #1 complaint about AI: "It doesn't sound like me."

| Skill | What It Does |
|-------|-------------|
| [`voice-extractor`](./voice-extractor/) | Feed it 3-5 writing samples, get a reusable voice profile (.md file). Sample-based extraction, not adjective-based — because research shows descriptions like "engaging and punchy" produce generic output. The profile works in any Claude conversation. |
| [`ai-tell-killer`](./ai-tell-killer/) | The scalpel. Surgical removal of AI writing patterns — identifies specific tells with confidence ratings and fixes only those. Annotated report shows what it found before changing anything. For writers who want to preserve their voice. |
| [`humanize-ai-writing`](./humanize-ai-writing/) | The power washer. Aggressive 7-step rewrite that strips AI fingerprints AND injects human voice — opinion, specificity, rhythm variation, Claude-specific pattern removal. Includes a 278-term tiered kill list. For when you need content de-AI'd fast. |
| [`precision-editor`](./precision-editor/) | *Coming soon.* Pick an editing level (flag only / suggest / light edit / heavy edit) and the skill stays within bounds. Solves "I asked for a light edit and got a complete rewrite." |

### Build Your Career

Skills grounded in what recruiters and hiring managers actually say in 2026.

| Skill | What It Does |
|-------|-------------|
| [`resume-rebuilder`](./resume-rebuilder/) | Evidence-bank-first resume building. Extracts your real achievements through structured interview, THEN generates the resume. No competitor does this — they all generate from job titles, which is why their output gets flagged. |
| [`interview-coach`](./interview-coach/) | *Coming soon.* Mock interviews with real scoring, JD analysis, and salary negotiation scripts. Anti-sycophantic by design — no "Great answer!" |
| [`career-experiment`](./career-experiment/) | *Coming soon.* Instead of "should I switch careers?", designs 3 low-stakes experiments you can run in your current role to test the hypothesis. |

### Learn Faster

Skills backed by learning science, not just AI convenience.

| Skill | What It Does |
|-------|-------------|
| [`learn-anything`](./learn-anything/) | *Coming soon.* Active recall tutor — refuses to lecture. Makes you explain back, catches misconceptions, adapts to your level. |
| [`explain-like`](./explain-like/) | *Coming soon.* Explain any concept using analogies from YOUR domain. "Explain Kubernetes like I'm a chef who understands kitchen stations." |
| [`research-brief`](./research-brief/) | *Coming soon.* Structured research briefs with confidence ratings per claim. Won't fabricate citations — tells you what to search to verify. |
| [`book-distiller`](./book-distiller/) | *Coming soon.* Opinionated book analysis, not summaries. Core thesis, genuinely new ideas, what's recycled, who should skip it, and questions the book doesn't answer. |

### Ship Your Product

Skills for side-project builders and solopreneurs.

| Skill | What It Does |
|-------|-------------|
| [`ai-build-partner`](./ai-build-partner/) | The AI Build Partner from Unstuck with Molly — **Layer 1 of [The Ship It System](https://www.theshipitsystem.com), free.** Diagnoses stuck patterns, audits builds, cuts scope, validates ideas, plans sprints, and creates roadmaps. 8 modules, each produces a concrete artifact. |
| [`build-irresistible-offer`](./build-irresistible-offer/) | Architect offers people feel stupid saying no to. Value stacking, named IP, guarantee structure, urgency mechanics. Based on the Hormozi Value Equation. |
| [`funnel-ad-creator`](./funnel-ad-creator/) | Complete ad script bible — 12-16 storyboarded ads across TOFU/MOFU/BOFU/Retargeting with a 4-week testing protocol. |
| [`instagram-reels-framework`](./instagram-reels-framework/) | Production-ready Reel scripts with timed beats, filming notes, 7 hook types, 5 beat structures, and a 12-point scoring rubric. |

### Work With Meetings

| Skill | What It Does |
|-------|-------------|
| [`meeting-distiller`](./meeting-distiller/) | *Coming soon.* Paste a transcript, get action artifacts — not a summary. Decisions, action items with owners, open questions, and the one thing that mattered most. |

### Claude Code Power User

| Skill | What It Does |
|-------|-------------|
| [`carl-manager`](./carl-manager/) | Manage CARL (Context Augmentation & Reinforcement Layer) domains and rules. Persistent memory for how you work — define rules once, they load automatically when relevant. |
| [`carl-help`](./carl-help/) | Reference docs for CARL — what it is, how it works, file structure, rule format, troubleshooting. |
| [`nano-banana`](./nano-banana/) | Image generation via Gemini CLI. Blog images, thumbnails, icons, diagrams, illustrations — any visual asset. Requires [Gemini CLI](https://github.com/google-gemini/gemini-cli) installed. |

---

## How to Use

### Claude.ai (easiest)

1. Open a [Claude Project](https://claude.ai)
2. Upload any skill's `SKILL.md` file as Project Knowledge
3. Claude picks it up automatically — just start talking

### Claude Code

```bash
# Clone the repo
git clone https://github.com/molly-diversifiedfun/claude-skills.git

# Copy a skill to your local skills directory
cp -r claude-skills/voice-extractor ~/.claude/skills/voice-extractor
```

Or reference the skill directly in a conversation — Claude reads the `SKILL.md` when you point it at the folder.

### Any LLM

The `SKILL.md` files are plain markdown. Paste them into any LLM's system prompt or context window. They're designed for Claude but the techniques work anywhere.

---

## How These Were Built

Every skill in this repo started with research, not vibes. Each one has:

- **A research brief** — what problems real users are having, what existing tools get wrong, what the evidence says works
- **A PRD** — design decisions with tradeoffs, interaction model, success criteria, anti-patterns
- **The SKILL.md** — the actual skill, built from the research and PRD

The research and PRDs live in [`docs/`](./docs/) if you want to see the thinking behind any skill.

---

## Want the Full Marketing Toolkit?

The marketing skills here are samples from **[Solopreneur Skills](https://github.com/molly-diversifiedfun/solopreneur-skills)** — a 25-skill system that covers the entire solopreneur pipeline from audience research through referral engines.

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
