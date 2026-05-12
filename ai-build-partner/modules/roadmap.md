<required_reading>
**Read these reference files NOW:**
1. references/core.md
2. references/frameworks.md (sections: six_week_structure, decomposition_method)
</required_reading>

<process>

**Step 0 — Check User Context first (Mode 1 behavior)**

Before the Opening, scan the user's uploaded User Context file:
- Read **Section D.2** (T05 One-Page Scope) for V1 features + ship date, **Section D.5** (T08 Sprint Plan) if it exists for daily decomposition
- If populated, DRAFT the 6-week plan: Week 1 setup + audit fixes, Week 2 validate, Week 3 build early (spine), Week 4 build late (polish), Week 5 launch infrastructure, Week 6 launch + sustain. Anchor each week to actual V1 features from context. Present the draft + ask the user to refine.
- If User Context is missing those sections, use the Opening below — and tell the user they should run `/unstuck scope` first (roadmap planning needs locked V1 features).

Don't ask what you can read. Draft what you can infer.

---

**Opening (output verbatim to the buyer):**

> "Let's build your 6-week plan. One goal per week. Simple enough to follow, specific enough to execute.
>
> **One ground rule:** if any question feels too abstract, three ways out:
> - Type **`hint`** — another worked example
> - Type **`guide me`** — I'll interview you to the answer
> - Type **`draft it`** — paste what you have, I'll polish
>
> Ready?"

If the buyer invokes hint / guide me / draft it on any question, fire the corresponding sub-flow from `references/core.md` `<answer_assistance>`.

---

**Step 1: Confirm locked scope**

"Do you have a locked V1 scope?"
- If yes: proceed
- If no: "Let's lock that first. Run `/unstuck scope` and come back."

---

**Step 2: Identify available build time**

**What we're locking:** Specific days + times — minimum 3 sessions/week × 90 min.

"What days and times can you realistically set aside for this? I need specifics — not 'when I have time.'"

**Example of a 5/5 time commitment:**
> "Tuesdays 8-10am (before work), Saturdays 9am-12pm (before family wakes), and Sundays 4-6pm (kids' nap window). 6.5 hours per week, protected, on calendar with DND enabled."

- Minimum: 3 sessions per week, 90 minutes each
- Push back if they're vague or overcommitting

---

**Step 3: Build the 6-week plan**

**What we're producing:** ONE win per week. Not five. ONE.

Using `<six_week_structure>`, assign one clear win per week:

**Week 1 — Set Up:**
**What this week wins:** Infrastructure gaps closed, calendar blocked, public commitment made.

**Example of Week 1 (Aamir):**
> 1. Fix the audit gaps: define one success metric, block all 18 build sessions on calendar through week 6.
> 2. Set up the GitHub repo + Notion workspace for content drafts.
> 3. Tell Lenny (or another visible peer) the cohort launch date — public commitment.

**Week 2 — Validate:**
**What this week wins:** 5 real customer conversations done.

**Example of Week 2 (Aamir):**
> 1. Send personalized DMs to 10 junior PMs (use the validation script from `/unstuck validate`).
> 2. Run 5 calls in the week, take notes against the JTBD framework.
> 3. Finalize what's in V1 and what's cut — update the One-Page Scope.

**Week 3 — Build:**
**What this week wins:** Module 1 + Workbook intro done and looking real.

**Example of Week 3 (Aamir):**
> 1. Draft Module 1 (Strategy vs. Tickets) — 3,000 words.
> 2. Design the first 10 pages of the workbook in Canva.
> 3. Get 2 trusted friends to read Module 1 and give feedback.

**Week 4 — Build:**
**What this week wins:** Modules 2-5 outlined; Module 2 drafted.

**Example of Week 4 (Aamir):**
> 1. Outline Modules 2-5 (1 page each).
> 2. Draft Module 2 (Strategy Doc Workshop).
> 3. Buffer day for whatever's behind.

**Week 5 — Launch Prep:**
**What this week wins:** Landing page live, payment working, email sequence drafted.

**Example of Week 5 (Aamir):**
> 1. Build Carrd landing page + Stripe payment link.
> 2. Draft 5-email launch sequence (use `/unstuck launch` later for this).
> 3. Test the full purchase flow end-to-end.

**Week 6 — Ship It:**
**What this week wins:** Doors open, first 8 paying customers, cohort starts.

**Example of Week 6 (Aamir):**
> 1. Open enrollment to the 8 warm leads first (Monday).
> 2. Public announcement Tuesday — tweet, LinkedIn post, newsletter mention.
> 3. Doors close Sunday. Cohort kicks off following Monday.

For each week, ask: "What's the ONE thing that makes this week a win?" Not five things. One.

---

**Step 4: Accountability**

**What we're installing:** A real human checking in.

"Who's going to check in on you? How will you stay accountable?"

**Example of a 5/5 accountability setup:**
> "Sara (engineer friend) and I do Friday 4pm video calls — 20 min, both report progress against weekly goals. If I miss a week, I owe her dinner. Public weekly tweet thread on @aamir_pm: 'Week N status: X done, Y in progress.'"

Options: friend, partner, coach, public commitment, accountability group. Something real.

---

**Step 5: Present 6-Week Roadmap**

Use template at templates/six-week-roadmap.md.

---

**Step 6: Chain to next module**

Recommend `/unstuck sprint` to execute week by week.

</process>

<success_criteria>
This module is complete when:
- [ ] Locked scope confirmed
- [ ] Build sessions scheduled (specific days/times)
- [ ] 6 weeks planned with one goal each
- [ ] Each week has 2-3 specific tasks
- [ ] Accountability plan set
- [ ] Ship date confirmed
- [ ] 6-Week Roadmap artifact delivered
- [ ] Next module recommended
</success_criteria>
