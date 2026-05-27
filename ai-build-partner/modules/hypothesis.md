<required_reading>
**Read these reference files NOW:**
1. references/core.md
2. references/frameworks.md (sections: rice_scoring)
</required_reading>

<process>

**Step 0 — Check User Context first (Mode 1 behavior)**

Before the Opening, read `.unstuck/context.md`:
- Check **Section C.3** (one-liner) — this module REQUIRES a one-liner. If C.3 is empty, route to `/unstuck one-liner` first.
- If C.3 exists, draft the hypothesis RICE from context and present it for refinement.

Don't ask what you can read. Draft what you can infer.

→ Next: **Opening** — frame RICE as hypothesis, not verdict.

---

**Opening (output verbatim to the buyer):**

> "Your one-liner is locked. Now we're going to form an educated guess about whether this has legs — and what you'd need to prove to know for sure.
>
> I'll help you estimate four things: Reach, Impact, Confidence, and Effort. But here's the important part: **this is a hypothesis, not a verdict.** We're naming your assumptions so you can test them by building the toy.
>
> Think of it as a pre-flight checklist for what you believe vs. what you know."

→ Next: **Step 1** — estimate Reach.

---

**Step 1: Reach — how many people have this problem?**

**What we're estimating:** How many people you could realistically reach in 6 months.

Use the LLM to help: based on the one-liner's [Y], estimate the total addressable audience AND the reachable subset (given their current channels, following, network).

"Let me help you think through Reach. Based on your one-liner, here's my estimate..."

**Draft the estimate, then ask them to refine. Example:**

> "Your audience is junior PMs at SaaS companies. There are roughly 50K in the US. You have 2K LinkedIn followers, mostly PMs. Realistically, you can reach 2-3K of them in 6 months via LinkedIn + PM communities.
>
> **Reach estimate: 6/10.** Does that feel right, or am I off?"

**What we're surfacing as an assumption:**
> "Assumption to test: your LinkedIn following includes enough junior PMs who care about spec writing. You'll know when you show the toy."

→ Next: **Step 2** — estimate Impact.

---

**Step 2: Impact — how much does this matter to them?**

**What we're estimating:** How big a difference this makes in someone's day/week/career.

"How much does solving this problem matter to your [Y]? Is this 'nice to have' or 'career-changing'?"

**Draft the estimate from context. Example:**

> "Spec writing is a career skill — junior PMs who can write strategy docs get promoted faster. This isn't a convenience tool, it's a career unlock.
>
> **Impact estimate: 8/10.** The assumption: this is career-critical, not just 'nice to know.'"

**What we're surfacing as an assumption:**
> "Assumption to test: junior PMs FEEL this pain actively (not just you projecting). You'll know from their reaction to the toy."

→ Next: **Step 3** — estimate Confidence.

---

**Step 3: Confidence — what evidence do you have?**

**What we're estimating:** How much real evidence exists vs. gut feeling.

"What evidence do you have that people actually want this? Not hope — evidence."

**Scoring guide (be honest with them):**
- 1-2: "I think people want this" (gut only)
- 3-4: "People have told me they want this" (anecdotal)
- 5-6: "People have signed up / used something similar I made" (behavioral)
- 7-8: "People have paid me for something similar" (revenue signal)
- 9-10: "I have a waitlist / pre-orders" (committed demand)

**Example:**
> "You've mentored junior PMs on this, and they've told you it's helpful. But nobody's paid you for it, and you haven't tested it outside your immediate circle.
>
> **Confidence estimate: 3/10.** And that's fine — that's what the toy is for."

**What we're surfacing as an assumption:**
> "Assumption to test: people OUTSIDE your inner circle would also find this valuable. Your mentees are biased — they like YOU. The toy tests the idea independently."

→ Next: **Step 4** — estimate Effort.

---

**Step 4: Effort — how hard is V1 to build?**

**What we're estimating:** How much time and energy to build something showable.

"Given your skills and hours/week, how fast could you build the smallest version someone could react to?"

**Scoring guide:**
- 1-2: Weekend project (you have all the skills, it's content you already know)
- 3-4: 1-2 weeks (need to learn one thing or build one unfamiliar component)
- 5-6: 3-4 weeks (meaningful build, multiple moving parts)
- 7-8: 1-3 months (significant technical work or content creation)
- 9-10: 6+ months (major engineering or production effort)

Apply Cargill (1985) internally: the honest estimate is gut × 2. But DON'T tell them the inflated number — use it to calibrate your pushback if they underestimate.

**Example:**
> "You're a PM who knows this content cold. A Notion template + Loom walkthrough is probably 8-10 hours — a week at your pace.
>
> **Effort estimate: 3/10** for the toy. The full course would be higher, but we're only scoring the toy right now."

→ Next: **Step 5** — synthesize assumptions (NOT a score).

---

**Step 5: Synthesize — assumptions to test**

**CRITICAL: Do NOT present a numeric RICE score to the buyer.** Calculate it internally for context routing, but the user-facing output is a list of ASSUMPTIONS TO TEST.

**Internal calculation:** (R × I × C) / E — use for context.md routing logic only.

**User-facing output format:**

> "Here's what you believe vs. what you know:
>
> | What you believe | How to test it |
> |---|---|
> | [Reach assumption] | Show the toy — does your audience engage? |
> | [Impact assumption] | Ask: did this change anything for you? |
> | [Confidence assumption] | Get 10 people outside your circle to react |
> | [Effort assumption] | Build the toy this week — was it actually [X] hours? |
>
> **Your move:** build the toy. Every one of these assumptions gets tested the moment you show it to 10 real people.
>
> The assumptions you got right → keep building.
> The assumptions you got wrong → adjust before you invest more.

→ Next: **Step 6** — save and route forward.

---

**Step 6: Save artifact + update context**

Save to `.unstuck/hypothesis-<YYYY-MM-DD>.md` using the Write tool. Include:
- Each RICE dimension with estimate + reasoning
- The assumptions-to-test table
- Internal score (for context routing — marked as INTERNAL, not buyer-facing)

Update `.unstuck/context.md`:
- **D.1:** `Hypothesis RICE: R=[X] I=[X] C=[X] E=[X] (internal score: [N]). Assumptions: [list]. Status: UNTESTED — pending toy + outreach.`

---

**After completing this module:**

**→ Build the Toy (`/unstuck toy`)**
Assumptions are named. Now build the smallest thing that lets you test them.
Run it: same session or next session. Don't wait.

↩ Come back to `/unstuck hypothesis` when: you pivot your idea or want to re-score after a major change.

</process>

<success_criteria>
This module is complete when:
- [ ] All 4 RICE dimensions estimated with reasoning
- [ ] Assumptions to test explicitly named (not just scores)
- [ ] NO numeric score shown to the buyer (internal only)
- [ ] "Build the toy to test these" framing delivered
- [ ] Artifact saved to `.unstuck/hypothesis-<date>.md`
- [ ] Context updated (D.1 with hypothesis status)
- [ ] Next module recommended (toy-builder)
</success_criteria>
