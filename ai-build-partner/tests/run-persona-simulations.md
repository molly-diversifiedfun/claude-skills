# AI Build Partner v2 — Persona Simulation Test Suite

> **Run with:** `claude -p --model claude-haiku-4-5-20251001 < tests/run-persona-simulations.md`
> **Or manually:** paste this into a Claude session with the ABP skill loaded and say "run all 12"

This is the regression test for the v2 journey. After any module edit, re-run all 12 to check routing, context writes, and module chaining.

---

## Instructions for the test runner

You are testing the AI Build Partner skill modules. For each persona below:

1. Read the SKILL.md intake heuristics and determine which module fires first
2. Read that module's Step 0 and verify the context check matches the persona's state
3. Trace the module chain (what module does the exit routing point to next?)
4. Verify each module writes the context sections it claims
5. Check the kill gate fires with correct signal weighting for the persona's results
6. Verify the paywall transition fires between Phase 3 and Phase 4
7. Check Kit-specific modules fire for the right product types

Report: PASS / FAIL per persona + specific break description if FAIL.

---

## The 12 Personas

### 1. Sarah — Course, Happy Path
- **Entry:** "I have an idea but haven't started"
- **Product type:** content/course
- **Context state:** empty (new user)
- **Entry path:** 🎯 The Builder → intake routes to `/unstuck one-liner`
- **Expected chain:** one-liner (🃏 Declarer) → hypothesis → toy-builder (🃏 Toymaker) → outreach (warm, can name 10+) → kill-gate (GO → 🃏 Listener, scope cuts → 🃏 Bouncer) → PAYWALL → prioritize → pricing
- **Kill gate signals:** 1 money (3x) + 4 usage (2x) + 2 trust (1x) + 1 pull (2x) = 15
- **Product-type module:** none special (standard pricing)
- **Cards earned:** Declarer, Toymaker, Listener, Bouncer (if scope cuts). Creep likely mid-build.

### 2. Mike — Dev Tool, Cold Discovery
- **Entry:** "I have an idea but haven't started"
- **Product type:** dev-tool
- **Context state:** empty
- **Entry path:** 🎯 The Builder → intake routes to `/unstuck one-liner`
- **Expected chain:** one-liner (🃏 Declarer) → hypothesis → toy-builder (🃏 Toymaker, dev-tool: working CLI + README) → outreach (can't name anyone → cold-discovery) → kill-gate (GO → 🃏 Listener) → PAYWALL → dev-tool-monetize (Kit) → (NOT standard pricing)
- **Cold discovery trigger:** outreach Step 1 routes "names 0-2" to cold path
- **Kill gate signals:** 0 money + 3 usage (2x) + 12 trust (capped 5, 1x) + 28 stars (capped 5 pull, 2x) = 0+6+5+10 = 21
- **Product-type module:** dev-tool-monetize.md (Kit-only)
- **Cards earned:** Declarer, Toymaker, Listener. Guillotine if cold outreach forces a pivot.

### 3. Priya — Templates, Serial Killer
- **Entry:** "I have an idea but haven't started" (4th time)
- **Product type:** content (templates)
- **Context state:** has 3 previous `Status: KILLED` entries
- **Entry path:** 🎯 The Builder → intake routes to `/unstuck one-liner`
- **Expected chain:** one-liner (🃏 Declarer) → hypothesis → toy-builder (🃏 Toymaker) → outreach → kill-gate (serial-kill protocol: threshold lowered to 7, forced 2 iterations)
- **Serial-kill trigger:** kill-gate Step 0 counts 3+ kills → Step 3b activates
- **Kill gate signals (attempt 1):** 0 money + 2 usage (2x) + 14 downloads (capped 5, 1x) + 2 pull (2x) = 0+4+5+4 = 13
- **Cards earned:** Declarer, Toymaker, Guillotine (4th kill → increments), Mortician (at 5 cumulative). Priya is the card-richest persona for Kill cards.

### 4. James — SaaS, Retro-Validate
- **Entry:** "I have users but no revenue"
- **Product type:** software/SaaS
- **Context state:** empty but has existing product
- **Entry path:** ⚰️ The Resurrector → intake routes to `/unstuck retro-validate`
- **Expected chain:** retro-validate → IF strong (40%+): freemium-conversion (Kit) → pricing. IF moderate (20-39%): diagnose. IF weak (<20%): one-liner (restart).
- **Product-type module:** freemium-conversion.md (Kit-only, after retro-validate)
- **Cards earned:** Merchant (if conversion works). Skips Declarer/Toymaker/Listener (enters mid-journey). Fewest total cards of any persona.

### 5. Kayla — Community, Non-Technical
- **Entry:** "I have an idea but haven't started"
- **Product type:** community/membership
- **Context state:** empty
- **Expected chain:** one-liner → hypothesis → toy-builder (community: ONE live event, stack DEFERRED) → outreach (warm, can name 10+) → kill-gate (GO) → PAYWALL → prioritize → pricing (community variant)
- **Stack timing check:** toy-builder Step 3 should say "For community: Skip pick-stack"
- **Kill gate signals:** 2 money (3x) + 7 usage (2x) + 4 trust (1x) + 1 pull (2x) = 6+14+4+2 = 26

### 6. Marcus — Newsletter, Stalled
- **Entry:** "I started building but stalled"
- **Product type:** newsletter
- **Context state:** empty but has existing 3 issues + 45 subs
- **Expected chain:** toy-builder (detects existing work, routes "your toy already exists") → outreach → kill-gate (GO with re-engagement signals) → PAYWALL → pricing
- **Stall detection:** toy-builder Step 0 checks duration. <3 months = normal toy-builder flow

### 7. Anita — App, 8-Month Scope Creep
- **Entry:** "I started building but stalled" (8 months of building)
- **Product type:** software/SaaS
- **Context state:** empty but has 8 months of code
- **Entry path:** "halfway built" → routing routes to `/unstuck toy-builder` → detects >3 months → re-routes to outreach
- **Expected chain:** toy-builder (redirect) → outreach → kill-gate (🃏 Listener + 🃏 Bouncer on scope cuts) → PAYWALL → prioritize
- **Cards earned:** Listener, Bouncer (likely), Guillotine (if kill). Creep Easter egg very likely.

### 8. David — Consulting, Imposter Syndrome
- **Entry:** "I have an idea but haven't started"
- **Product type:** service/consulting
- **Context state:** empty
- **Expected chain:** one-liner → hypothesis → toy-builder (service: offer page + 1 free delivery, stack DEFERRED) → outreach → kill-gate (GO) → PAYWALL → pricing (service variant)
- **Stack timing check:** toy-builder Step 3 should say "For service: Skip pick-stack"

### 9. Lin — Physical Product, Analysis Paralysis
- **Entry:** "I have an idea but haven't started"
- **Product type:** physical
- **Context state:** empty
- **Expected chain:** one-liner → hypothesis → toy-builder (physical: 1 sample + photos + interest form) → outreach → kill-gate (GO) → PAYWALL → physical-economics → pricing
- **Product-type module:** physical-economics.md

### 10. Rachel — Ebook, Perfectionism (80% done)
- **Entry:** "I started building but stalled" + "it's 80% done"
- **Product type:** ebook/guide
- **Context state:** empty but 80% written
- **Expected chain:** toy-builder (perfectionism detection: "ship one chapter") → outreach (show one chapter as free PDF) → kill-gate → PAYWALL → pricing
- **Perfectionism detection:** toy-builder Step 0 or intake heuristic line 145

### 11. Tomas — Mobile App, Over-Engineering (14 months)
- **Entry:** "I started building but stalled" (14 months, rebuilt 3x)
- **Product type:** mobile
- **Context state:** empty but has 14 months of code
- **Expected chain:** intake detects >3 months → routes to outreach DIRECTLY → kill-gate → PAYWALL → app-store-economics → pricing
- **Over-engineer detection:** intake line 139 + line 146
- **Product-type module:** app-store-economics.md

### 12. Jess — Cohort Course, Over-Planning (40-page doc)
- **Entry:** "I have an idea but haven't started" (but has 40-page curriculum)
- **Product type:** cohort course
- **Context state:** empty but has curriculum doc
- **Expected chain:** one-liner → hypothesis → toy-builder (cohort: ONE live workshop, stack DEFERRED) → outreach → kill-gate (GO) → PAYWALL → pricing (cohort variant)
- **Over-planning handling:** toy-builder forces "one workshop, not the full 6-week program"

---

## Expected Results Summary

| # | User | Expected | Break if... | Cards |
|---|---|---|---|---|
| 1 | Sarah | PASS — Builder path → one-liner → toy → outreach → gate | intake doesn't route to one-liner for Builder path | 🃏 Declarer, Toymaker, Listener, Bouncer |
| 2 | Mike | PASS — cold path + dev-tool-monetize (Kit) | cold-discovery not triggered, or dev-tool-monetize not routed | 🃏 Declarer, Toymaker, Listener |
| 3 | Priya | PASS — serial-kill protocol at gate | kill count not read from context, or threshold not lowered | 🃏 Declarer, Toymaker, Guillotine, Mortician |
| 4 | James | PASS — retro-validate → freemium (Kit) | retro-validate routes to pricing instead of freemium-conversion | 🃏 Merchant only (enters mid-journey) |
| 5 | Kayla | PASS — community path, stack deferred | stack not deferred, or toy defined as software | 🃏 Declarer, Toymaker, Listener |
| 6 | Marcus | PASS — toy-builder detects existing work | forced to rebuild something he already has | 🃏 Toymaker (existing work), Listener |
| 7 | Anita | PASS — toy-builder detects >3mo → outreach | sent to toy-builder to build more (instead of redirect) | 🃏 Listener, Bouncer, Guillotine |
| 8 | David | PASS — service path, stack deferred | stack not deferred, or toy defined as software | 🃏 Declarer, Toymaker, Listener, Crossroads |
| 9 | Lin | PASS — physical-economics (Kit) | sent to standard pricing without COGS | 🃏 Declarer, Toymaker, Listener |
| 10 | Rachel | PASS — perfectionism intervention at toy | told to finish book before showing (should say ship ONE chapter) | 🃏 Declarer, Toymaker, Listener, Creep |
| 11 | Tomas | PASS — >3mo redirect + app-store (Kit) | sent to toy-builder to build, or standard pricing without cuts | 🃏 Listener, Bouncer, Guillotine, Creep |
| 12 | Jess | PASS — cohort + workshop toy | toy = full program, not one workshop |

---

## Running This Test

**Automated (Haiku):**
```bash
claude -p --model claude-haiku-4-5-20251001 --system-prompt "You are a test runner. Read the test file and the actual module files. Report PASS/FAIL per persona." < ~/github/claude-skills/ai-build-partner/tests/run-persona-simulations.md
```

**Manual (in a session):**
1. Load the AI Build Partner skill
2. Say: "Run persona simulation #[N]" for a specific user
3. Or: "Run all 12 persona simulations" for the full suite

**After any module edit:** re-run the full suite. If a persona fails, the edit broke something.
