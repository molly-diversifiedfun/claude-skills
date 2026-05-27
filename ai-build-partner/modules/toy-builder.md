<required_reading>
**Read these reference files NOW:**
1. references/core.md
2. references/frameworks.md (sections: seventy_thirty_ai_rule)
</required_reading>

<process>

**Step 0 — Check User Context first (Mode 1 behavior)**

Before the Opening, read `.unstuck/context.md`:
- Check **Section C.3** (one-liner) — REQUIRED. If missing, route to `/unstuck one-liner`.
- Check **Section A.4** (hours/week) — if missing, ask Q1 from the hours-reality block below before proceeding.
- Check **Section D.1** (hypothesis) — useful but not required. If present, reference the assumptions to test.
- **Pre-existing work import:** If the user describes work done OUTSIDE the skill (e.g., "I already have 3 newsletter issues and 45 subscribers" / "I built a landing page last month" / "I have a prototype sitting in my garage") AND context Sections C-E are empty — catalog it before routing:

  > "You've already done real work. Let me capture it so the system knows what exists."

  Then write to context:
  - **C.3:** one-liner (draft from what they described — ask them to confirm)
  - **E.1:** what exists (list every asset: issues published, subscribers, code, prototypes, landing pages, email lists)
  - **E.2:** stack used (whatever tools they already chose)
  - **F.1:** when they last worked on it

  After import, the routing logic picks up normally — if they have a showable thing, route to outreach. If not, proceed to define the toy. The point: don't make someone who already has 45 subscribers start from "what's your one-liner?" as if they're brand new.

- **Stuck-type detection:** If the user says they've been building for 3+ months, they don't need this module — they need to SHOW what they have. But if they've been building for **6+ months**, the redirect needs an emotional reframe first. The structural advice ("show what you have") is correct, but without acknowledging the investment, it sounds like "those months were wasted."

  **For 3-6 months:** Write to context: `E.1: Toy definition — subset of existing [duration] build (user describes what exists).` Route: "You already have a toy — it's a subset of what you built. Skip to `/unstuck outreach` and show it to 10 people."

  **For 6+ months (over-builder reframe):**

  > "You've been building for [N] months. I'm not going to tell you that was wasted — it wasn't. You now know this domain better than most people who'll ever try to build in it. That knowledge is the asset. The code is the proof-of-work.
  >
  > What I AM going to tell you: scope-cutting on a [N]-month build doesn't mean those months were wrong. It means you explored, and now you know which 20% of what you built is the part people actually need.
  >
  > Describe what exists right now. Every screen, every feature, everything. I'll help you find the subset that IS the toy — the piece 10 people can react to this week."

  Write to context: `E.1: Toy definition — subset of existing [duration] build. Over-builder reframe delivered.` Then work through Steps 1-2 to identify the subset, skip Steps 3-5 (they already have a stack and timeline is "now"), and route to `/unstuck outreach`.
- **Perfectionism detection:** If they say something like "it's 80% done but not ready" — intervene: "Your toy isn't the finished thing. It's the smallest piece someone can react to. Ship one chapter / one feature / one session. The toy is how you learn what to finish."
- **Perfectionism re-entry:** If context shows a toy was ALREADY defined (E.1 populated) AND the last interaction was 7+ days ago AND they say something like "I went to fix one thing" / "I've been polishing" / "I need to make it better first" — this is the perfectionism loop. Intervene:

  > "You left to fix one thing. It's been [N] days. That's the pattern — not the fix.
  >
  > The thing you went to fix? It either matters to your 10 people or it doesn't. Here's how we find out: show what you have RIGHT NOW to the next person on your list. Their reaction tells you whether the fix was necessary.
  >
  > If they don't mention the thing you were fixing, it wasn't blocking them. If they do, you fix it AFTER you have that data — not before.
  >
  > Ready to pick up where you left off?"

  Then route to `/unstuck outreach` — NOT back to building. The perfectionism loop breaks by showing, not by fixing.

- **Imposter syndrome detection:** If the user says something like "I feel like a fraud" / "who am I to charge for this" / "I'm not qualified" / "imposter syndrome" / any variant of feeling unqualified despite clear professional credentials — deliver the reframe BEFORE the structural toy definition:

  > "You just described [N] years as a [role] at [company], shipping [what they've shipped]. The thing stopping you isn't skill — it's the gap between knowing you're good at your job and believing someone would pay YOU directly for that same expertise.
  >
  > That gap isn't evidence. It's a story. The evidence is [specific thing from their background — quote what they told you]. The story is 'but that was my employer's brand, not mine.'
  >
  > Here's what we're going to do: write the offer. Not to sell it yet — to see if you can describe what you do clearly enough that a stranger says yes. The words fix the fraud feeling faster than any amount of thinking about it."

  Then proceed to the standard service/consulting toy definition (offer page + one free delivery, stack deferred). The reframe must reference THEIR specific credentials, not generic encouragement.

Don't ask what you can read. Draft what you can infer.

→ Next: **Opening** — frame the toy.

---

**Opening (output verbatim to the buyer):**

> "Time to build something real. Not a product. Not a prototype. A **toy** — the smallest tangible thing someone can react to.
>
> The rules:
> 1. You have **one week** (5-10 hours at your pace).
> 2. It has to be something you can **show someone** and they can interact with it.
> 3. It does NOT need to be finished, polished, or complete. It needs to exist.
>
> What's the fastest thing you could put in front of someone and ask 'what do you think?'"

→ Next: **Step 1** — detect product type and define the toy.

---

**Step 1: Detect product type**

**What we're identifying:** The shape of the product — this determines what "toy" means.

Read their one-liner (C.3) and ask if needed: "What form does this take? Is this an app, a course, a community, a service, a newsletter, a physical product, or something else?"

**Product type → Toy definition → Stack timing:**

| Product type | Toy = | Pick-stack timing |
|---|---|---|
| **Software / SaaS** | Working prototype with ONE feature | Now (Phase 2) |
| **Content / Course** | First module + landing page + waitlist | Now (Phase 2) |
| **Community / Membership** | One live event (Zoom roundtable, workshop, AMA) | Deferred to Phase 4 |
| **Service / Consulting** | Offer page + one free delivery | Deferred to Phase 4 |
| **Dev tool / CLI** | Working tool that does the ONE thing + GitHub README | Now (Phase 2) |
| **Newsletter** | 3 issues + subscriber page (or: resurface existing issues) | Now (Phase 2) |
| **Physical product** | One sample/prototype + photos + interest form | Now (Phase 2) |
| **Cohort course** | One live workshop (standalone, not the full program) | Deferred to Phase 4 |
| **Mobile app** | TestFlight / beta with ONE flow working | Now (Phase 2) |
| **Ebook / Guide** | One chapter as a free PDF + download page | Now (Phase 2) |

Present the match and confirm: "Based on your one-liner, this sounds like a [type] product. Your toy would be: [definition]. Does that fit?"

**If they already have something built:** "You said you've been building for [X months]. What exists right now? Describe it." Then determine if any subset IS the toy. If yes: "Your toy already exists — it's [subset]. Don't build more. Show THIS to 10 people."

→ Next: **Step 2** — define the specific toy.

---

**Step 2: Define the toy — specific and concrete**

**What we're producing:** A one-paragraph toy definition with exactly what to build.

"Let's get specific. In one week with [X hours], what EXACTLY will you build?"

Help them scope ruthlessly. The toy must be:
- **Showable** — someone can look at it, use it, or experience it
- **Reactable** — they can form an opinion ("this is useful" or "meh")
- **Buildable in one week** — if it can't be built in their available hours, cut more

**Example of a 5/5 toy definition (course product):**
> "Notion template with Module 1: 'The One-Pager Framework.' Includes the 5-part template (Context → Problem → Proposal → Metrics → Ask) + one filled-in example from a real project (anonymized). Plus a 15-minute Loom walking through how to fill it out. Carrd landing page with email capture: 'Free spec-writing framework for PMs.'"

**Example of a 5/5 toy definition (community product):**
> "One 60-minute Zoom roundtable. Topic: 'The research insight your PM ignored — and what you did about it.' Cap at 8 people. Google Form for RSVP. LinkedIn post to recruit."

**Example of a 5/5 toy definition (dev tool):**
> "Go binary: `dotsync`. Syncs .zshrc and .gitconfig between 2 machines via a git repo. 300 lines. Published on GitHub with MIT license and a README with a demo GIF."

**Example of a 5/5 toy definition (physical product):**
> "One handmade prototype of the leather cardholder — cut from scrap leather I already have, hand-stitched, not factory-perfect. Photos taken on my kitchen table with natural light (phone camera is fine). Google Form interest page: 'Handmade leather cardholder — $35 — would you buy this? Drop your email.' Share the form + photos to 10 people in r/LeatherCraft and my Instagram."

**Physical product sourcing guidance (for buyers who don't know where to start):**
- **If you can make one by hand:** make ONE. It doesn't need to be production-quality. A hand-sewn version, a 3D-printed version, a cobbled-together-from-parts version. The toy is the proof that the THING can exist, not that it can be manufactured.
- **If you can't make it yourself:** look for a local maker, makerspace, or Etsy seller who does custom work in that material. One prototype, not a batch. Budget $50-200 for a single custom piece.
- **If it's too expensive to prototype:** sketch it, render it (Canva, Figma, even hand-drawn), and pair the render with a landing page. "This is what I'm building. Would you buy it at $X?" A render + interest form IS a valid toy for physical products. You're testing demand, not manufacturing.
- **If you're stuck on sourcing:** the sourcing research IS the first build session. Day 1 action: "Find 3 options for getting one prototype made. Pick the fastest. Order it." The toy ships when the prototype arrives + photos + interest form go live.

Push back on:
- "I'll build the full thing" → "No. One feature. One module. One session. The toy is small on purpose."
- "But it won't be good enough" → "It's a toy. Toys aren't finished products. They're things people play with and react to."
- Anything that takes >10 hours → "Cut it. What's the one piece someone could react to?"

→ Next: **Step 3** — pick the stack (if applicable).

---

**Step 3: Pick the stack (conditional)**

**For software / content / dev-tool / newsletter / ebook / physical / mobile:** Pick stack NOW.

"What tools will you use to build this? Fastest, not best. What can you ship with in a week?"

**Guiding principles:**
- Tools they already know beat tools that are "better"
- Free tiers beat paid subscriptions for a toy
- One tool per function (don't compare 5 landing page builders — pick one and go)

**Example of a 5/5 stack pick (course):**
> "Notion (free, already know it) + Loom (free, 5 min setup) + Carrd ($19/yr, one-page site builder). Total cost: $19. Total setup time: 30 min."

**For community / service / cohort:** Skip pick-stack. Output:
> "You don't need a platform for the toy — just Zoom (which you have) and a Google Form. We'll pick the real stack in Phase 4 when you build V1. For now: zero setup, zero cost."

→ Next: **Step 4** — set the build timeline.

---

**Step 4: Set the build timeline**

**What we're locking:** Specific days/times this week when they'll build the toy.

"Look at your calendar. Which days this week can you work on this? I need specific days + time slots. Minimum 3 sessions."

**Example of a 5/5 build timeline:**
> "Tuesday 8-10am (before family wakes), Thursday 8-10am (same), Saturday 9am-noon (kids at swim). Total: 7 hours across 3 sessions. Toy done by Saturday night."

If they can't name 3 sessions: "Without protected time, this won't happen. Name the slots or we're just planning — not building."

→ Next: **Step 5** — lock Day 1 action.

---

**Step 5: Lock Day 1 action**

**What we're making concrete:** The exact first thing they'll do in their first build session.

"What's the exact thing you'll do in your first session? Not 'start building' — the file you'll open, the thing you'll create, and what 'done' looks like for that session."

**Example of a 5/5 Day 1 action:**
> "Tuesday 8am: Open Notion. Create the Module 1 page. Write the 5-part framework (Context → Problem → Proposal → Metrics → Ask) with explanations of each section. Done = framework page complete, ready for the worked example Wednesday."

→ Next: **Step 6** — save and route forward.

---

**Step 6: Save artifact + update context**

Save to `.unstuck/toy-<YYYY-MM-DD>.md` using the Write tool. Include:
- Product type detected
- Toy definition (the specific one-paragraph description)
- Stack pick (or "deferred to Phase 4")
- Build timeline (days + hours)
- Day 1 action

Update `.unstuck/context.md`:
- **C.3:** Update format if not already set (from product type)
- **E.1:** Toy definition (replaces old V1 features — the toy IS the V1 scope for now)
- **E.2:** Stack (if picked now; or "deferred")
- **F.2:** Build timeline (the 3+ sessions)

---

**Phase 2 complete — drop 🃏 The Toymaker card** (read `references/fun.md` for card generation + announcement). A toy exists. Most side projects die before this point.

**After completing this module:**

| If your toy... | Next module | Why | When |
|---|---|---|---|
| Is a thing you show to named people | `/unstuck outreach` | Find 10 people, show the toy, collect signal | After the toy is built (end of week 1) |
| Is a thing you post publicly | `/unstuck outreach` | Same — but outreach includes cold discovery for public-post toys | After the toy is built |
| Already exists (over-builder) | `/unstuck outreach` | Skip building — show what you have NOW | Today |

↩ Come back to `/unstuck toy` when: you pivot and need to redefine the smallest showable thing.

</process>

<success_criteria>
This module is complete when:
- [ ] Product type detected
- [ ] Toy defined in one specific paragraph
- [ ] Stack picked (or deferred for community/service/cohort)
- [ ] Build timeline locked (3+ specific sessions)
- [ ] Day 1 action set (file to open, thing to create, done criteria)
- [ ] Over-builder / perfectionism detection ran (if applicable)
- [ ] Artifact saved to `.unstuck/toy-<date>.md`
- [ ] Context updated (E.1, E.2, F.2)
- [ ] Next module recommended (outreach)
</success_criteria>
