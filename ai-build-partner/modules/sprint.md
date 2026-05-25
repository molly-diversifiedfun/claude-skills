<required_reading>
**Read these reference files NOW:**
1. references/core.md
2. references/frameworks.md (sections: decomposition_method, daily_build_protocol, seventy_thirty_ai_rule)
</required_reading>

<process>

**Step 0 — Check User Context first (Mode 1 behavior)**

Before the Opening, read `.unstuck/context.md` and scan:
- Read **Section E** (scope decisions) for V1 features + ship date, **Section F.1** (build blocks) for protected time
- If both populated, DRAFT the 10-day plan: map V1 features to days 1-5 in dependency order, reserve days 6-10 for path-to-customer (landing page, emails, payment), one task per day, each under 3 hours. Flag the balloon day. Present the draft + ask the user to refine.
- If `.unstuck/context.md` is missing those sections, use the Opening below — and tell the user they should run `/unstuck scope` first (sprint planning needs locked V1 features).

Don't ask what you can read. Draft what you can infer.

---

**Opening (output verbatim to the buyer):**

> "Let's set up a 10-day sprint. Ten days. One goal per day. At the end, you'll have something real.
>
> **One ground rule:** if any question feels too abstract, three ways out:
> - Type **`hint`** — another worked example
> - Type **`guide me`** — I'll interview you to the answer
> - Type **`draft it`** — paste what you have, I'll polish
>
> Sound good?"

If the buyer invokes hint / guide me / draft it on any question, fire the corresponding sub-flow from `references/core.md` `<answer_assistance>`.

→ Next: **Step 1** — Confirm V1 scope is locked before planning.

---

**Step 1: Confirm locked scope**

**What we're checking:** V1 features are locked from `/unstuck scope`.

"Do you have a locked V1 scope — 3-5 features, ship date set?"
- If yes: proceed
- If no: "Let's lock that first. Run `/unstuck scope` and come back."

→ Next: **Step 2** — Pick 10 specific calendar days with real time slots.

---

**Step 2: Pick 10 calendar days**

**What we're locking:** Ten specific dates with at least 90 minutes of focused build time each.

"Look at your calendar for the next 2-3 weeks. Which 10 days can you commit at least 90 minutes of focused build time? They don't have to be consecutive — just real."

**Example of a 5/5 10-day commit (Aamir):**
> "Tues May 13 (8-10am), Thu May 15 (8-10am), Sat May 17 (10am-12pm), Sun May 18 (2-4pm), Tues May 20 (8-10am), Wed May 21 (8-10am), Thu May 22 (8-10am), Sat May 24 (10am-1pm), Tues May 27 (8-10am), Wed May 28 (8-10am). All blocked on calendar. Phone in drawer. DND on."

Help them be realistic. Push back on "I'll find time." If they can't name 10 real slots, the sprint is wishful thinking.

→ Next: **Step 3** — Decompose V1 scope into one deliverable per day.

---

**Step 3: Decompose scope into 10 daily goals**

**What we're producing:** One concrete deliverable per day. Verb-first. 60-120 min.

Using the `<decomposition_method>`:
- Break their V1 features into milestones (Level 1)
- Break milestones into 60-120 minute tasks (Level 2)
- Assign one task per sprint day, ordered by dependency and priority
- Make each task verb-first and specific

**Example of a 5/5 10-day plan (Aamir's Junior PM Career Compass):**
> Day 1: Outline Module 1 (Strategy vs. Tickets) — verb: outline, deliverable: 2-page outline
> Day 2: Draft Module 1 content (3,000 words) — verb: draft
> Day 3: Outline Modules 2-5 — verb: outline, deliverable: 5x1-page outlines
> Day 4: Draft Module 2 (Strategy Doc Workshop) — verb: draft
> Day 5: Design workbook PDF in Canva (intro + Module 1) — verb: design
> Day 6: Build landing page (Carrd + Stripe link) — verb: build
> Day 7: Write 5 outreach DMs to interested PMs — verb: write
> Day 8: Send DMs + open enrollment to first 5 — verb: send
> Day 9: Buffer day (catch up + breathe) — verb: catch-up
> Day 10: Polish Module 1 + Workbook based on first 3 buyer signals — verb: polish

→ Next: **Step 4** — Install the daily startup/shutdown ritual.

---

**Step 4: Set up the Daily Build Protocol**

**What we're installing:** A 3-part ritual around every session — Startup / Park Downhill / Shutdown.

Walk them through the `<daily_build_protocol>`:
- Startup Ritual (5 min): phone away, DND, review outcome, open the file
- Park Downhill: write tomorrow's exact next action at end of each session
- Shutdown Ritual (5 min): stop, save, park downhill, close tabs, acknowledge

**Example of a 5/5 Park Downhill note (end of Day 1):**
> "Tomorrow: open Module-1.md, start at 'The 4 levels of PM strategy' heading, write the section on the 'levels' model (Wardley-inspired), aim for 800 words by 9:30am."

→ Next: **Step 5** — Split what AI handles vs. what must be you.

---

**Step 5: Establish the 70/30 AI Rule**

**What we're splitting:** What AI handles (70%) vs. what must be them (30%).

Using `<seventy_thirty_ai_rule>`, help them identify:
- What AI can handle (first drafts, structure, research, boilerplate)
- What must be them (voice, personal examples, judgment calls, final polish)
- Non-negotiable: the product must sound like them

**Example of a 5/5 70/30 split (Aamir):**
> AI does: outline structures, research summaries, first-draft workbook copy, landing page first-pass, email subject lines.
> Aamir does: every personal story from his own PM career, judgment calls on what to cut, the final voice pass on everything, all DMs to real humans.

→ Next: **Step 6** — Lock the exact Day 1 action in concrete terms.

---

**Step 6: Set Day 1 action**

**What we're locking:** The exact first task in concrete terms.

"What's the exact thing you'll do on Day 1? Not 'start building.' Tell me the file you'll open, the paragraph you'll write, the screen you'll design."

**Example of a 5/5 Day 1 action:**
> "Tuesday May 13, 8:00am. Open Module-1.md (already created). Write the section titled 'Why most junior PMs get stuck doing JIRA grooming.' Aim for 600 words by 9:45am. Park downhill: leave a one-line note for the 'Strategy vs. Tickets' section."

→ Next: **Step 7** — Generate and save the sprint plan artifact.

---

**Step 7: Present Sprint Plan**

Use template at templates/sprint-plan.md.

Save the completed artifact to `.unstuck/sprint-<YYYY-MM-DD>.md` using the Write tool.

→ Next: **Step 8** — Update context with the sprint plan.

---

**Step 8: Update context**

Read `.unstuck/context.md`, then update:
- **F.2:** sprint plan — 10 daily goals
Save the updated file.

→ Next: the exit block below.

---

**After completing this module:**

**→ Pick My Stack (`/unstuck pick-my-stack`)**
Sprint plan is locked. Now wire the tools — you need infrastructure before you write code.
Run it: Day 1 of the sprint (before coding).

↩ Come back to `/unstuck sprint` when: every new sprint cycle, or when the current plan derails.

</process>

<success_criteria>
This module is complete when:
- [ ] Locked scope confirmed
- [ ] 10 calendar days identified
- [ ] Scope decomposed into 10 daily goals
- [ ] Daily Build Protocol explained
- [ ] 70/30 AI Rule applied to their project
- [ ] Day 1 action set (specific and scheduled)
- [ ] Sprint Plan artifact delivered
- [ ] Artifact saved to `.unstuck/sprint-<YYYY-MM-DD>.md`
- [ ] Context updated — F.2 written in `.unstuck/context.md`
- [ ] Next module recommended
</success_criteria>
