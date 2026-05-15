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
| [`precision-editor`](./precision-editor/) | Pick an editing level BEFORE Claude touches your text — flag only, suggest as comments, light copy edit, or heavy developmental. At levels 1-3 your sentences survive. Mandatory "Wanted to change but didn't" log so the model can't silently expand scope. Solves "I asked for a light edit and got a complete rewrite." |

### Build Your Career

Skills grounded in what recruiters and hiring managers actually say in 2026.

| Skill | What It Does |
|-------|-------------|
| [`resume-rebuilder`](./resume-rebuilder/) | Evidence-bank-first resume building. Extracts your real achievements through structured interview, THEN generates the resume. No competitor does this — they all generate from job titles, which is why their output gets flagged. |
| [`interview-coach`](./interview-coach/) | Four modes: JD analysis, question prep, mock interviews scored on 5 dimensions (Substance / Structure / Relevance / Credibility / Differentiation), and salary negotiation scripts (Patio11 strategy + Voss tactics). Anti-sycophantic by design — "Great answer!" is banned; every score requires evidence. Credit to noamseg for the rubric. |
| [`career-experiment`](./career-experiment/) | Outputs exactly 3 testable career experiments at 3 effort tiers (≤3 hrs / 5 hrs/wk × 2 wks / 10+ hrs over 2-4 wks). 14-day first-signal cap forces falsifiability. Refuses vague success signals — "see how it feels" gets rewritten to a specific observable. Never recommends quitting your job as the experiment. |

### Learn Faster

Skills backed by learning science, not just AI convenience.

| Skill | What It Does |
|-------|-------------|
| [`learn-anything`](./learn-anything/) | Active recall tutor — refuses to lecture. Surfaces what you already know via diagnostic distractor questions (no Dunning-Kruger self-rating), fills gaps through questioning, confirms understanding through teach-back. 3-strike escape hatch when you really just want the answer. One 20-30 minute session per topic. |
| [`explain-like`](./explain-like/) | Explain a concept by mapping it onto a domain you already know deeply. Built on Gentner's structure-mapping (relations, not surface). 5 levels calibrated to your prior knowledge of the *target* domain, not your age. Refuses with one of three named patterns when domains don't actually map — no forcing bad analogies. |
| [`research-brief`](./research-brief/) | Structured brief with explicit GRADE confidence rating on every claim (High / Moderate / Low / Very Low). Never fabricates citations — emits search-handles like `Search: "[query]" — type: [source]` instead. Tags every claim by source type: trained-knowledge / inference / speculation. Direct countermeasure to the lawyer-sanctions failure mode. |
| [`book-distiller`](./book-distiller/) | Opinionated book analysis, not a summary. 2-sentence thesis *about* the book, 5 genuinely new ideas, what's recycled (with required prior-work + year citations), who should skip it, 3 questions the book doesn't answer. Three-tier confidence routing: refuses to fake distillations on books with thin training data — asks for your notes instead. |

### Ship Your Product

Skills for side-project builders and solopreneurs.

| Skill | What It Does |
|-------|-------------|
| [`ai-build-partner`](./ai-build-partner/) | The AI Build Partner from Unstuck with Molly — **Layer 1 of [The Ship It System](https://www.theshipitsystem.com), free.** Diagnoses stuck patterns, audits builds, cuts scope, validates ideas, plans sprints, and creates roadmaps. 8 modules, each produces a concrete artifact. |
| [`build-irresistible-offer`](./build-irresistible-offer/) | Architect offers people feel stupid saying no to. Value stacking, named IP, guarantee structure, urgency mechanics. Based on the Hormozi Value Equation. |
| [`funnel-ad-creator`](./funnel-ad-creator/) | Complete ad script bible — 12-16 storyboarded ads across TOFU/MOFU/BOFU/Retargeting with a 4-week testing protocol. |
| [`instagram-reels-framework`](./instagram-reels-framework/) | Production-ready Reel scripts with timed beats, filming notes, 7 hook types, 5 beat structures, and a 12-point scoring rubric. |

### Audit & Diagnose

Skills that find the gap between "what we built" and "what people are actually doing."

| Skill | What It Does |
|-------|-------------|
| [`followability-audit`](./followability-audit/) | The Color Check from **[The Flamingo Effect](https://www.theflamingoeffect.com)** (book 2). Diagnoses where any system — product, repo, onboarding flow, course, habit plan, policy, team process — is breaking down for the humans meant to use it. 5-rung rubric (Understand / Believe / Do / Repeat / Share), ranked fix list, "fix the crack closest to the ground" sequencing rule. |

### Work With Meetings

| Skill | What It Does |
|-------|-------------|
| [`meeting-distiller`](./meeting-distiller/) | Turn a transcript into a one-page project management artifact. Section headers are PM nouns only — Decisions, Action Items, Open Questions, Disagreements, Parking Lot. Implicit decisions (nobody said "decided" but everyone moved on) get surfaced with a `[implicit — confirm]` flag. Mandatory "The One Thing" paragraph forces editorial judgment. The word "summary" is banned at the prompt level. |

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

The marketing skills here are samples from **[Marketing OS](https://github.com/molly-diversifiedfun/marketing-os)** (formerly Solopreneur Skills) — a 25-skill system that covers the entire solopreneur pipeline from audience research through referral engines.

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
