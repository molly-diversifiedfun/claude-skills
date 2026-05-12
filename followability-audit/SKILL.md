---
name: followability-audit
description: Diagnose where a system (product, repo, onboarding flow, course, habit plan, policy, team process) is breaking down for the people meant to use it. Use when user says "audit this", "is this followable", "why aren't people doing the thing", "where does this break", "color check", "followability audit", "find the crack", "score this against the rubric", "diagnose this onboarding/flow/repo/product", or asks for a structured review of a deliverable from the perspective of someone who has to follow through. Outputs scores on 5 rungs (Understand / Believe / Do / Repeat / Share), a ranked fix list, and a Monday plan. Based on The Followable System / Color Check methodology by Molly Shelestak.
---

# Followability Audit (The Color Check)

A diagnostic for any system where "people aren't doing the thing" describes the problem. Works on products, repos, courses, onboarding flows, policies, team processes, habit plans, lead magnets, sales funnels — anything with a target behavior and humans expected to repeat it.

## The reframe

**If people aren't doing the thing, the system — not the person — needs to be redesigned.**

Not "they aren't motivated." Not "they don't understand the value." Not "we need better copy." The system has a gap. The audit finds it.

## When to invoke

Trigger phrases (in any combination):
- "audit this", "is this followable", "followability audit", "color check"
- "where does this break", "find the crack", "diagnose this"
- "why aren't people doing the thing", "people aren't following through"
- "score this against the rubric", "rate this on understand/believe/do"
- Any request for structured review of a deliverable from a user's perspective

NOT for:
- Code review (use the reviewer agent / code-review skill)
- Content QA against brand voice (use content-qa agent)
- Pure security audit (use security agent / audit-context-building)
- Pure technical correctness (use reviewer / dhh-rails-reviewer / etc.)

This skill is about **whether a human can follow through**, not whether the code/copy is correct.

---

## The 5 rungs

Score each rung **0-5**. Scoring generously is the same as going grocery shopping and pretending you'll remember the paper towels. Be honest.

### UNDERSTAND (0-5)

> In 10 seconds, can a new person say what this is and what to do next?

| Score | What it means |
|---|---|
| 0 | People have no idea what this is |
| 1 | They get the general category but not the specifics |
| 2 | They understand it after reading for 30+ seconds |
| 3 | They get it in 10-15 seconds but can't explain it to someone else |
| 4 | They get it fast but the "for who" is unclear |
| 5 | Crystal clear — name, promise, audience, next step all obvious |

**Signal it's broken:** click-arounds, jargon, hedged value props, FAQ-required.

### BELIEVE (0-5)

> Is there proof — not claims — at the moment of decision?

| Score | What it means |
|---|---|
| 0 | No proof anywhere. Just claims. |
| 1 | Proof exists but it's buried (testimonials page, case study PDF) |
| 2 | Some social proof ("10,000 users") but nothing specific |
| 3 | Specific proof exists but it's not at the moment of decision |
| 4 | Good proof, well-placed, but mechanism isn't visible |
| 5 | Claim + mechanism + specific proof + safety — all visible at decision point |

**Signal it's broken:** "trust me, this works," generic numbers, no before/after, no mechanism visibility, no specific named result.

### DO (0-5)

> Is the first action obvious, small, and completable right now?

| Score | What it means |
|---|---|
| 0 | No clear first action. User has to figure out what to do. |
| 1 | First action exists but requires 10+ minutes of setup first |
| 2 | Setup takes 5-10 minutes before any value |
| 3 | First win is reachable in 5 minutes but the path has unnecessary steps |
| 4 | Quick first win, but it doesn't feel like real value (tutorial, not real use) |
| 5 | Real value in under 2 minutes. First win before account setup. |

**Signal it's broken:** account-creation walls before value, configuration before output, multi-step onboarding before "show me the thing".

### REPEAT (0-5)

> Is progress visible, and is there a system that makes coming back likely?

| Score | What it means |
|---|---|
| 0 | No cadence, no signals, no recovery. Use it once and it goes silent. |
| 1 | Some notifications but no visible progress or cadence |
| 2 | Progress tracked but not surfaced to the user |
| 3 | Cadence exists but missing a beat means starting over |
| 4 | Good cadence + visible progress, but no re-entry path for lapsed users |
| 5 | Cadence + signals + checkpoints + graceful re-entry after any gap |

**Signal it's broken:** silence after first use, no progress UI, missing a day = punishment, no "minimum day" option.

### SHARE (0-5)

> Is the outcome packaged into something that travels?

| Score | What it means |
|---|---|
| 0 | Outcomes are completely private. Nothing shareable. |
| 1 | User could manually screenshot but nothing is designed for sharing |
| 2 | Share button exists but the shared artifact isn't compelling |
| 3 | Decent shareable artifact but requires multiple steps to share |
| 4 | Good proof artifact, easy to share, but no CTA for the viewer |
| 5 | Auto-generated proof artifact + one-tap share + viewer CTA = growth loop |

**Signal it's broken:** private results, manual screenshot, no viewer CTA, multi-step share flow.

---

## The procedure

### Step 1 — Name the thing

Ask (or infer if obvious):

> **The single behavior I want reliably repeated:** ___________

Not the mission. Not the vision. The specific, observable behavior a real human is supposed to perform.

Examples:
- Product: "Activate within 7 days of signup."
- Repo: "Clone, read README, install or cherry-pick one piece, use it."
- Course: "Complete module 1 within 48 hours of enrolling."
- Newsletter: "Open and click through to the linked piece weekly."

**If you can't say it in one sentence, that's the first problem.** A system isn't followable if its builder can't name what "following" means.

### Step 2 — Score each rung

Walk through Understand → Believe → Do → Repeat → Share. Score 0-5 each, with one or two sentences of evidence per score. Cite specific elements of the system being audited.

### Step 3 — Find the first crack

Output:

```
| Rung | Score | Evidence |
|------|-------|----------|
| Understand | _ | ... |
| Believe    | _ | ... |
| Do         | _ | ... |
| Repeat     | _ | ... |
| Share      | _ | ... |
```

Identify:
- **Primary problem** (lowest score)
- **Secondary problem** (second-lowest)

### Step 4 — Apply "closest to the ground" rule

> Fix the crack closest to the ground. If Understand is broken, nothing above it matters. Don't jump to Share fixes when the Do rung has a crack.

If two rungs are tied, the lower one in the order (Understand < Believe < Do < Repeat < Share) wins. Understanding gates believing gates doing gates repeating gates sharing.

### Step 5 — Recommend one fix per affected rung

For the primary + secondary rungs, propose **the smallest possible intervention shippable in 48 hours**. Not a redesign. A single move.

See `references/fix-library.md` for fix candidates per rung.

### Step 6 — Output format

```markdown
## Followability Audit — <system being audited>

**Target behavior:** <the one sentence>

### Scores

| Rung | Score | Why |
|------|-------|-----|
| Understand | _ | <evidence> |
| Believe    | _ | <evidence> |
| Do         | _ | <evidence> |
| Repeat     | _ | <evidence> |
| Share      | _ | <evidence> |

**Primary problem:** <rung name + score> — <one-sentence diagnosis>
**Secondary problem:** <rung name + score> — <one-sentence diagnosis>

### Fix list

**For <primary rung>:**
- [ ] <smallest intervention, 48h shippable>
- [ ] <alternate>

**For <secondary rung>:**
- [ ] <smallest intervention>

### Monday plan

The single thing to ship first: <one sentence>
```

---

## Hard rules

- **Be specific.** "Understand is weak" is useless. "The first sentence under the title uses 4 jargon words" is actionable.
- **Cite the system being audited.** Quote actual text. Reference actual UI elements. Reference actual file paths or commit hashes.
- **Score generously = score wrong.** A "3" out of charity is a "1" in reality. The user is asking because something is broken.
- **Don't skip rungs.** Even if Understand is clearly the problem, score all 5. The pattern matters.
- **Don't redesign.** The fix list is for 48-hour interventions, not month-long projects. If the audit reveals a fundamental rebuild is needed, say so explicitly — but the fix list still names the smallest cracks.
- **Cite the rule.** Every fix recommendation should map to its rung. Don't propose Share fixes when fixing Do.

---

## Integration with other skills

- **brand-voice-router** (if active) — voice-check the audited system separately from the followability check; both can fail independently
- **devils-advocate** — pair with this skill when the user wants both "what's the crack" AND "what's the strongest objection"
- **mental-models** — when the audit reveals a structural problem (not just surface), route to mental-models for the deeper diagnosis
- **content-qa** — content-qa checks the writing; this skill checks the experience

---

## References

- `references/fix-library.md` — Fix candidates per rung, organized for fast scanning
- The full methodology lives in The Followable System by Molly Shelestak. The Color Check lead magnet (`launch/platform/followability-audit-lead-magnet.md` in the source project) is the canonical short-form.

---

## Provenance

This skill packages The Followable System's "Color Check" — the diagnostic at the heart of the book by Molly Shelestak. The 5-rung model (Understand / Believe / Do / Repeat / Share) is the structural innovation: the system's progression matches the human's journey.
