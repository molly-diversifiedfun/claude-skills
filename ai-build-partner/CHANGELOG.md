# AI Build Partner — Changelog

All dated changes to the Build Partner skill. Format loosely follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

Note: AI Build Partner lives inside the [claude-skills](../) repo. The root `CHANGELOG.md` covers cross-skill changes. This one is scoped to Build Partner only.

---

## [Unreleased]

_Working on:_ followability audit fixes — CHANGELOG, fast-path surface, synthesized artifact example, ref-tagged share attribution, explicit Marketing OS upgrade CTA.

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
