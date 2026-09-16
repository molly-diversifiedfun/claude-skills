# AI Build Partner — Changelog

All dated changes to the Build Partner skill. Format loosely follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

Note: AI Build Partner lives inside the [claude-skills](../) repo. The root `CHANGELOG.md` covers cross-skill changes. This one is scoped to Build Partner only.

---

## [Unreleased]

_Working on:_ followability audit fixes — CHANGELOG, fast-path surface, synthesized artifact example, ref-tagged share attribution, explicit Marketing OS upgrade CTA.

---

## [2.4.0] — 2026-09-16

### Changed
- **`/unstuck launch` moved onto the five.** The module asked a money-first seven — Big Idea, Who It's For, Core Offer, MVP Scope, Three First Steps, Launch Date, Success Metric — with pushback written around "why would they pay" and "prove people will pay". It now asks what the prompt at theshipitsystem.com/launch-prompt asks: the one action someone takes when it works, the first real person by name, everything that has to be true first, what that person would notice missing (V1), and the day plus the hours plus the arithmetic between them.
- **Money is out of the exercise entirely.** No price, no "first sale by when", and no "which tool would you use" — from the other side of the screen that last one reads exactly like the price question. A first subscriber, member, reader or reply counts the same as a first customer.
- **The vehicle question arrives**, between the dump and the cut: what is the smallest thing in the world that produces that action? One proposal, freely refused. Most lists are long because the vehicle is too big, not because the list is badly pruned.
- **`templates/launch-plan.md`** rewritten to the five, and it now carries the cut list beside V1 — a shorter list is not visibly a decision; a list with its cuts next to it is.
- **`/unstuck launch` added to the command table.** It was reachable only by keyword; the website had been advertising `/unstuck launch-plan`, which was never a command.

### Fixed
- **Section D.6's contract changed, and its readers were updated with it.** `launch-day.md` read a "success metric — the number that decides if the day worked" out of D.6, and the module no longer writes one. It now reads the ONE ACTION, which is the better signal on the day: "Priya replies about work" tells you more than "eight signups". `templates/context.md` and `day-job-decision.md` were describing the old shape too.

### Why
Four artifacts rendered the same One-Page Launch Plan and all four asked different questions — the prompt, the fill-in page, the PDF, and this module. Only the prompt had been through persona testing, and it was the only one that did not assume you are selling something. This audience ships newsletters, communities, open-source tools and portfolio pieces that never take a payment.

The prompt's v12 also deliberately stops short of two things it used to do — sizing each V1 item in hours, and laying out the sessions between now and the date — on the grounds that the skill has the sittings to do them properly. That claim is now true rather than aspirational: the module's exit routes to `/unstuck scope` when V1 does not fit the hours, and to `/unstuck roadmap`, which already locks specific days and times, when it does.

## [2.3.0] — 2026-05-16

### Added
- **`/unstuck idea-bank`** — new module #36. Generates side-project ideas from the user's own behavioral data (paid subscriptions, daily apps they resent, newsletters/podcasts compulsively opened, things recommended to friends, browser tab graveyard, asymmetry between work-paid skill and free-time skill, the 3+ year carry project). 7-question Socratic flow → 3 pattern surface → 5 idea candidates → Project Selector kill 2 → THE ONE worth shipping. Chains into `/unstuck scope` or `/unstuck validate`. 10-15 min. Free baseline skill (works in Standalone mode).
- Discovery Path 1 chaining updated: "no idea" now routes through `/unstuck idea-bank` first, then `/unstuck scope` (was diagnose).

### Why
Discovery is a router, not an idea generator. Path 1 ("I don't have an idea yet") landed users on a thin sub-flow that didn't actually generate ideas — it just asked them what they wanted to build. The new skill mines revealed-preference data (what the user already pays for / opens / recommends / keeps in tabs) to surface ideas already in their behavior. Higher hit rate than brainstorming from scratch because the pattern was always there — just unread.

---

## [2.2.0] — 2026-05-16

### Added
- **`install.sh`** — first-class installer. Copies skill to `~/.claude/skills/ai-build-partner/`, generates a local `install_id`, and (with explicit consent) sends one `ai_build_partner_installed` event to PostHog so Molly can attribute installs to ads/channels.
- **Session-use telemetry** in SKILL.md — best-effort `build_partner_invoked` ping once per Claude session, fire-and-forget, no prompt/file/conversation content sent. Opt out anytime with `rm ~/.ai-build-partner/install_id`.
- **Shipped event** — `build_partner_shipped` fires when user runs `/unstuck shipped`, marking the warmest retargeting audience for downstream offers.
- **README Telemetry section** — explicit table of what's sent, where it goes, and how to opt out at every level.

### Why
To run paid ads to the free skill without going blind. Install + invocation + shipped events make the funnel measurable. The skill works identically with telemetry off.

---

## [2.1.0] — 2026-05-15

### Added
- **`/unstuck context`** — Socratic User Context intake. Replaces the questionnaire with conversational discovery that produces the same one-page profile.
- **`/unstuck wrap`** — session close skill that captures decisions, blockers, and next moves before the chat ends.
- Discovery → Context wiring: Discovery now hands off directly into Context-building instead of leaving the User Context template empty.

### Changed
- v2.1 voice principles propagated across all 21+ modules (consistency pass).
- 7 skills that didn't have READMEs now do (per session checklist).

---

## [2.0.0] — 2026-05-14

### Added — 16 new modules across two waves
**Tier A (Run 5.5):** `funnel`, `pmf`, `v1.1`, `scaling-lever`, `smoke-test`, `weekly`, `build-in-public`, `landing-page`.
**Tier B/C:** `launch-emails`, `automate`, `support-refund`, `pricing-iteration`, `stuck`, `time-protect`, `pricing`, `v2-backlog`.

The skill is now a 21+ module library — Mode 1 helpers, Mode 2 launch sequence, post-launch ops.

---

## [1.5.0] — 2026-05-13

### Added
- **`/unstuck ship-announcement`** — Day 27 launch-announcement kit. Generates full IG/LinkedIn/Twitter/Substack drafts + SHIPPED-stamp image prompt + `/shipped` Wall submission mailto.
- 3 ABP companion skills shipped: `audience-from-zero` (30-day audience build for Path 4 buyers), `day-job-decision` (STAY/NEGOTIATE/QUIT verdict), `pick-my-stack` (9-category stack manifest).

---

## [1.4.0] — 2026-05-12

### Added
- **Mode C activation** — detects Marketing OS extension declaration and routes marketing tasks to marketing-os skills instead of running Build Partner equivalents.
- **In-character check** at every session start — confirms mode, names a framework from canon, names a banned word avoided. Non-optional.
- **Discovery precedence rule** (BLOCKING) — when User Context Section B is empty, Discovery wins over module name triggers.
- **Hours-reality blocking step** in Discovery — Section B.2 (weekly hours) is required before any planning skill runs. All downstream modules calibrate to actual hours.
- **`ten-hour-week` module** — post-launch sustainable operating mode (10-15 min).
- 4 friction-reduction modules (Package C wave 2).
- Embedded examples in 7 module prompts.
- 3-way answer assistance pattern (`hint` / `guide me` / `draft it`) on all diagnostic moments.

### Fixed
- Marketing-os rename refs updated (was `solopreneur-skills`).

---

## [1.3.0] — 2026-05-11

### Added
- **`kit-files/`** — 4 supporting knowledge files (master system prompt, brand guide, voice DNA, audience personas, user context template).
- Canonical 10-layer MSP regeneration into `claude-project.md`.

### Renamed
- `unstuck-coach` → `ai-build-partner` repo-wide.

---

## Cadence — what to expect AFTER install

This isn't a one-shot tool. Expect:

- **Day 1:** Run Discovery (20-60 min). Get your User Context.
- **Days 2-11:** Run a 10-Day Sprint. Daily check-ins.
- **Day 28:** Ship-announcement kit.
- **Every Sunday, forever:** 20-min Sunday Ship Check (`/unstuck weekly`).

The Build Partner is a relationship, not a tool. The Sunday cadence is the part that compounds.
