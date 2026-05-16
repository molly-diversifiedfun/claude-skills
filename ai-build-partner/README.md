# AI Build Partner

**Stop spinning on the same side project for the third year. Get a build partner who calls your scope creep, audits your build, and keeps you shipping.**

Layer 1 of [The Ship It System](https://www.theshipitsystem.com), free.

> **What's new:** v2.1 shipped 2026-05-15 — Socratic `/unstuck context` intake + `/unstuck wrap` session-close skill. Full history in [CHANGELOG.md](./CHANGELOG.md).

## The Problem

Side projects die in two places: the planning phase ("I'll start when I have time to do it right") and the 60% phase ("I'll polish a little more before launching"). Both are scope creep wearing different hats. Most accountability tools give you streaks; what you actually need is someone who'll tell you the truth about what you're avoiding.

## 5-Minute Quick Start

Don't read this whole README. Don't run Discovery yet. Just do this:

1. Install:
   ```bash
   cp -r ai-build-partner ~/.claude/skills/ai-build-partner
   ```
2. Open Claude Code. Say:
   > *"Use the ai-build-partner skill. Run the **Diagnose** module. I'll describe my situation in one paragraph and you tell me which stuck pattern I'm in."*

3. Paste one paragraph about your stuck project. You'll get back a named stuck pattern + one move to make today. ~5 minutes.

If that felt useful, come back for Discovery (20-60 min) when you have time. Discovery builds the User Context that every other module uses — but Diagnose works without it.

## What An Output Actually Looks Like

> **Provenance:** synthesized example, not a real client. Generated as a faithful representation of what the Scope Guillotine module produces, to show mechanism. Real outputs in your sessions will be specific to your build.

### Input

> *"I've been building a habit tracker app for 14 months. Currently it has 23 features in the Notion roadmap. I work on it Sunday nights but I haven't shipped anything to friends in 7 weeks. I keep finding 'one more thing' to add before I'm willing to show people."*

### Scope Guillotine output

**Stuck pattern:** *60% Polish Spiral* — you're avoiding the discomfort of shipping by adding scope.

**Survives V1 (4 features):**
1. Manual habit entry (one tap)
2. 7-day streak view
3. One reminder per habit per day
4. Local-only storage

**Dies (19 features):**
- Social sharing → *kills focus, not your moat*
- Insights/analytics → *V2 — nobody asked*
- Cloud sync → *adds infra you'll babysit forever*
- Friend leaderboards → *you're building this for you, not them*
- AI suggestions → *the algorithm IS the product if you add this; do that later*
- ...14 more on the cut list

**Ship constraint:** Friday 2026-05-22 (7 days). If you're not done by Friday, you don't add features — you cut more.

**Next module:** `/unstuck sprint` to plan the 7 days. Then `/unstuck weekly` every Sunday after launch.

*Built with the Unstuck Method — [unstuckwithmolly.com](https://unstuckwithmolly.com?ref=ai-build-partner&module=scope)*

---

That's a real Scope Guillotine. Every module produces an artifact like this. You can do this for your project right now (5 minutes).

## What It Does

The AI Build Partner is the [Unstuck with Molly](https://www.unstuckwithmolly.com) build-partnership methodology, packaged as a skill. It runs as 8 core modules + 13 utility skills — each one a focused conversation that ends with a concrete artifact:

| Module | Trigger | Artifact |
|--------|---------|----------|
| **Discovery** | First session, or no User Context exists | One-page User Context profile |
| **Diagnose** | "I'm stuck" / "Help me figure out what's blocking me" | Stuck Pattern diagnosis + one move |
| **Audit** | "Help me audit my build" | Build Audit with stuck patterns named |
| **Scope** | "What can I cut?" / "I'm overscoping" | Scope Guillotine output — what survives, what dies |
| **Validate** | "Should I build this?" | Validation report with kill criteria |
| **Sprint Plan** | "Plan my next 10 days" | 10-Day Sprint Plan with daily commitments |
| **Roadmap** | "What's next?" | 90-day roadmap chained from current state |
| **Stuck Coach** | "I can't ship" / "I'm stuck" | Stuck Pattern diagnosis + unblock |
| **Marketing** | "How do I launch this" | Launch plan (chains into Marketing OS) |

Plus 13 utility skills (warm-list, DM-personalizer, smoke-test, landing-page, pick-my-stack, day-job-decision, weekly Sunday Ship Check, ship-announcement, and more). Full list in [SKILL.md](./SKILL.md).

Every artifact carries the Unstuck Method attribution. Modules chain — each one ends with a recommendation for the next.

## The Cadence (this is the point)

The Build Partner isn't a one-shot tool. It's a relationship with a structure:

- **Day 1:** Discovery → one-page User Context profile.
- **Days 2-11:** 10-Day Sprint → daily focused work with check-ins.
- **Day 28:** Ship-announcement kit (`/unstuck ship-announcement`).
- **Every Sunday, forever:** 20-min Sunday Ship Check (`/unstuck weekly`).

If you ship once and never come back, you got partial value. The Sunday check is the part that compounds — it's how you stop being someone who has projects and become someone who finishes them.

## How to Use It

### In Claude.ai

1. Open a Claude Project
2. Upload `SKILL.md` + the contents of `references/` and `modules/` as Project Knowledge
3. Start with: *"I want to work on my side project"* — the skill routes you to Discovery if needed (or jump straight to `/unstuck diagnose` for the 5-min path above)

### In Claude Code

```bash
cp -r ai-build-partner ~/.claude/skills/ai-build-partner
```

Then in any session: *"Use the ai-build-partner skill"* and answer the in-character check.

## What Makes This Different

- **In-character check** at every session start — you know you're talking to the Build Partner, not generic Claude
- **One question at a time** — no overwhelming intake forms
- **Artifacts, not lectures** — every module ends with a document you can act on
- **Banned vocabulary enforced** — no "unlock," no "level up," no "dive in"
- **Mode-aware** — runs standalone, or as part of the Ship It Kit, or with Marketing OS extensions

## Pairs With

- **[build-irresistible-offer](/build-irresistible-offer/)** — Use when the Build Partner surfaces "I don't know how to price/package this"
- **[funnel-ad-creator](/funnel-ad-creator/)** — When the launch module needs paid acquisition
- **[followability-audit](/followability-audit/)** — When something you shipped isn't getting used; diagnose the gap
- **[humanize-ai-writing](/humanize-ai-writing/)** — Run on every artifact before you publish anything externally

## When You Ship: Layer 3 (Marketing OS)

The Build Partner gets you to ship. Once you've shipped, the next problem is selling. That's [Marketing OS](https://github.com/molly-diversifiedfun/marketing-os) — Layer 3 of The Ship It System, paid.

It's 26 skills: persona, offer architecture (Hormozi), sales letters (Belcher 21-step), pricing (Van Westendorp + decoy), email sequences (Soap Opera + Seinfeld), launch campaigns (Jeff Walker PLF), referral engines (Dream 100), and more. Same skill-chain logic you used here, applied to the post-ship side.

When the Build Partner Marketing module surfaces "I need a sales page" or "I don't know how to price this," Marketing OS is what answers. They're designed to compose — Mode C in the Build Partner detects the Marketing OS extension and chains them automatically.

→ [theshipitsystem.com](https://theshipitsystem.com?ref=ai-build-partner&placement=upgrade-cta) · $79

## License

MIT. The methodology is from Unstuck with Molly. Attribution required on shared artifacts: *"Built with the Unstuck Method — unstuckwithmolly.com"*
