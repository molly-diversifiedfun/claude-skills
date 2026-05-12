<required_reading>
**Read these reference files NOW:**
1. references/core.md
2. references/frameworks.md (sections: scope_creep_detector, jtbd, decomposition_method)
</required_reading>

<process>

**Step 0 — Check User Context first (Mode 1 behavior)**

Before the Opening, scan the user's uploaded User Context file:
- Read **Section B.1** (project basics) and **Section D.1** (T04 Validation Scorecard outputs) if present
- If both populated, DRAFT the One-Page Scope (JTBD, V1 features max 5, V2 Backlog, success metric) from that context first. Present the draft and ask the user to refine. Skip Step 1 below (the "tell me everything" dump) — they already did the work upstream.
- Flag the 1-3 fields where your draft is weakest (usually JTBD trigger specificity, success metric, V2 Backlog completeness). Those are the user's to fix.
- If User Context is empty for these sections, use the Opening below and run Step 1 onward — and consider routing the user to `/unstuck discovery` or `/unstuck validate` first.

Don't ask what you can read. Draft what you can infer.

---

**Opening (output verbatim to the buyer):**

> "Time to run the Scope Guillotine. We're cutting this project down to a version you can actually finish. It's going to feel uncomfortable. That's the point.
>
> **One ground rule:** if any question feels too abstract, three ways out:
> - Type **`hint`** — another worked example
> - Type **`guide me`** — I'll interview you to the answer
> - Type **`draft it`** — paste what you have, I'll polish
>
> Ready?"

If the buyer invokes hint / guide me / draft it on any question, fire the corresponding sub-flow from `references/core.md` `<answer_assistance>`.

---

**Step 1: Get it all out**

**What we're capturing:** Every feature, asset, or piece the buyer thinks the V1 needs. The brain dump — uncut.

"Tell me everything you think this needs to have when you launch. Everything. Get it all out of your head."

**Example of a 5/5 brain dump (from Aamir's Junior PM Career Compass):**
> "I need: 5 modules of content, a workbook PDF, recorded videos, a Slack community, weekly office hours, 1:1 calls for premium tier, a private podcast feed, certificate of completion, monthly alumni meetups, a job board, a Notion template library, integrations with Lenny's Newsletter, an AI tutor, peer feedback rounds, and a graduation ceremony."

Let them dump. Don't judge. Just capture. Now we cut.

---

**Step 2: Apply the 5-Question Cut Test**

**What we're doing:** Filter each item through the `<scope_creep_detector>`. Most fail.

For each item they listed, run through:
1. Does the thing literally not work without this?
2. Could you launch without it and add it later?
3. Does this add more than a day of work?
4. Are you adding this to avoid doing something harder?
5. Would you still be proud of what you shipped without this?

If #2 is YES — it's a "later" item. Done.
If #3 is YES — it better be absolutely critical.
If #4 is YES — definitely a "later" item.

**Example of cutting Aamir's dump:**
> ✅ KEEP: 5 modules of content (this IS the product)
> ✅ KEEP: Workbook PDF (extension of content, low-effort)
> ❌ CUT (V2): Recorded videos — could launch live-only first
> ❌ CUT (V2): Slack community — Discord-link in MVP, real community later
> ❌ CUT (V2): 1:1 calls — keep for premium upsell, not V1
> ❌ CUT entirely: Private podcast feed — vanity feature
> ❌ CUT (V2): Certificate, alumni meetups, job board — Phase 2 retention plays
> ❌ CUT entirely: AI tutor — scope creep dressed as innovation

Be direct but warm: "That's a great idea — but it's a 'later' feature. We're cutting it for now."

---

**Step 3: Lock it down**

**What we're producing:** Exactly 3-5 V1 features, nothing more.

Force exactly 3-5 features maximum. Push back kindly if they resist:
"I know it feels like you need all of it. You don't. What's the smallest version that still solves the problem?"

**Example of a 5/5 V1 scope (Aamir's locked):**
> 1. 5 live cohort sessions (90 min each, Tuesdays 7pm ET)
> 2. 40-page workbook PDF (delivered Monday week 1)
> 3. Private Slack channel for cohort + alumni
> 4. Stripe payment + Calendar invites only — no LMS
> 5. End-of-cohort 1:1 with Aamir (the founder) — capped at 10 customers

---

**Step 4: Define success**

**What we're locking:** One measurable signal of V1 working.

"How will you know this worked? Finish this sentence: 'This is a success when ______.'"

**Example of a 5/5 success metric:**
> "This is a success when 8+ junior PMs pay $497 by June 15 and 6+ of them show up to Session 1. Fewer than 5 sign-ups = the offer or audience is wrong; back to validation. More than 12 = next cohort tests $697."

---

**Step 5: Pick a ship date**

**What we're locking:** A specific calendar date — month, day, year.

"When are you going to have this done? Give me a real date."

**Example of a 5/5 ship-date answer:**
> "First cohort kicks off Monday June 15, 2026. Doors open May 22, close June 8. Workbook ships May 18 to first paying customers as a credibility preview."

Push back if it's more than 6 weeks out or vague. A date creates pressure. Pressure creates decisions. Decisions create momentum.

---

**Step 6: Scope Lock Ceremony**

**What we're doing:** A small ritual to mark the commitment.

Present the locked scope and ask them to commit:
"This is your scope. Locked. No additions. Done > Perfect. Type `lock` to commit."

---

**Step 7: Present One-Page Scope**

Use template at templates/one-page-scope.md.

---

**Step 8: Chain to next module**
Recommend `/unstuck roadmap` (for 6-week plan) or `/unstuck sprint` (for 10-day blitz)

</process>

<success_criteria>
This module is complete when:
- [ ] All desired features captured
- [ ] Cut test applied to each item
- [ ] Scope locked to 3-5 features
- [ ] Success metric defined
- [ ] Ship date set (specific date, max 6 weeks out)
- [ ] One-Page Scope artifact delivered
- [ ] Next module recommended
</success_criteria>
