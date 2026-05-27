<required_reading>
**Read these reference files NOW:**
1. references/core.md
</required_reading>

<process>

**Step 0 — Entry detection**

This module fires when a user enters with "I have users but no revenue" or "I built something and people use it but I don't know how to charge." It runs a compressed Phase 3 against their EXISTING user base before routing to pricing.

Read `.unstuck/context.md` if it exists. If the user is new, seed context from their answers.

→ Next: **Opening** — frame the retro-validation.

---

**Opening (output verbatim to the buyer):**

> "You have users — that's further than most people get. But users ≠ revenue. Before we talk pricing, we need to figure out: do your users care enough to PAY?
>
> We're going to run a quick test on your existing user base. Takes about 30 minutes of your time + a few days for responses."

→ Next: **Step 1** — understand the current state.

---

**Step 1: What exists today?**

**What we're capturing:** The product, the users, the current state.

Ask one at a time:
1. "What's the product? One sentence."
2. "How many users / subscribers / members?"
3. "How are they using it? (Daily, weekly, signed up and forgot?)"
4. "How long has it been live?"
5. "Have you talked to ANY of them directly? How many?"

**Example of a 5/5 state snapshot:**
> Product: AI interview prep tool that generates system design practice questions.
> Users: 200 registered, ~30 active in last 30 days.
> Usage: Most sign up, try 1-2 questions, leave. Power users (10-15) use it weekly.
> Live since: November 2025 (6 months).
> Direct conversations: 0. Never talked to a user.

→ Next: **Step 2** — identify the 10.

---

**Step 2: Name 10 users to test**

**What we're producing:** 10 specific users to contact for the Sean Ellis test.

"Name 10 users you can actually email or message. Ideally the most active ones — the people who use your thing repeatedly, not the ones who signed up and left."

If they don't know their users by name: "Can you pull your last-30-days active users from your analytics / database / email list? We need real names, not numbers."

If they truly can't identify individuals: "That's a signal in itself — you have users but no relationship with them. The first step before pricing is talking to the people who already showed up."

→ Next: **Step 3** — run the Sean Ellis test.

---

**Step 3: The Sean Ellis Test**

**What we're measuring:** Would users be "very disappointed" if this product disappeared?

"Send these 10 people ONE question: 'How would you feel if [product] disappeared tomorrow?' Give them three options: Very Disappointed, Somewhat Disappointed, Not Disappointed."

**Draft the email/message for them:**

> "Hey [name] — quick question about [product]. If [product] disappeared tomorrow, how would you feel?
>
> A) Very disappointed
> B) Somewhat disappointed
> C) Not disappointed
>
> One-click reply. Takes 5 seconds. Your honest answer helps me decide what to do next."

**Routing by results:**

| % "Very Disappointed" | Verdict | Route |
|---|---|---|
| **40%+** | Strong signal — people NEED this | → Step 4 (pricing) |
| **20-39%** | Moderate signal — some care, most don't | → Step 5 (diagnose) |
| **<20%** | Weak signal — users are tourists, not customers | → Step 6 (hard conversation) |

Wait for them to send the emails and collect responses. This takes 3-5 days. Set a follow-up date.

→ Next: **Step 4, 5, or 6** depending on results.

---

**Step 4: Strong signal (40%+ very disappointed) → Route to pricing**

> "Good news: [X]% of your users would be very disappointed if this went away. That's above the PMF threshold. These people would pay.
>
> **The question now isn't IF to charge — it's HOW.** Let's figure out what they'd pay and how to introduce pricing without losing the people who love it."

Capture insights from the responses, then route to `/unstuck pricing` (Kit module).

**Before routing, ask one more question:**
"What do the 'very disappointed' users have in common that the 'not disappointed' users don't? (Job title, use case, frequency, anything.)"

This surfaces the REAL target customer — often a subset of the current user base.

→ Update context and route to pricing.

---

**Step 5: Moderate signal (20-39%) → Diagnose first**

> "Some people care, but not enough for PMF. Before pricing, we need to understand WHY only [X]% would miss it.
>
> Let's dig deeper: what's different about the users who said 'very disappointed' vs. the ones who didn't?"

Ask:
- "Look at the 'very disappointed' users. What do they have in common? (Same use case? Same job? Same frequency?)"
- "Look at the 'not disappointed' users. Why did they sign up in the first place? What were they hoping for that they didn't get?"
- "Is your product trying to do too many things for too many people?"

**Common findings:**
- **The product is great for a niche subset** → pivot to serve that subset (like James finding his tool was great for system design, not general prep)
- **The product is mediocre for everyone** → needs a core feature improvement before pricing
- **The product onboards poorly** → users never experienced the value

Route to: `/unstuck diagnose` for deeper stuck-pattern analysis, or back to Step 3 after improvements.

---

**Step 6: Weak signal (<20%) → Hard conversation**

> "Honest moment: [X]% would be very disappointed if this disappeared. That means [100-X]% wouldn't miss it.
>
> That doesn't mean you failed — it means the current version isn't solving a painful-enough problem for a specific-enough audience. Charging for this right now would likely lose most of your users without meaningful revenue.
>
> **Two paths:**
> 1. **Find the niche** — is there a subset (even 5 people) who use it intensely? Serve THEM.
> 2. **Restart the journey** — go back to Phase 1 with what you've learned. The toy was the product itself. The data is the 200 users who showed you what works and what doesn't."

→ Next: **Step 7** — save and route.

---

**Step 7: Save artifact + update context**

Save to `.unstuck/retro-validate-<YYYY-MM-DD>.md` using the Write tool. Include:
- Product snapshot (from Step 1)
- 10 users contacted
- Sean Ellis results (% breakdown)
- Verdict and routing decision
- Insights about who cares and why

Update `.unstuck/context.md`:
- **D.1:** `Retro-validate: Sean Ellis [X]% very disappointed. Verdict: [strong/moderate/weak]. Niche: [if identified]. [Date].`
- **D.7:** The 10 users contacted (becomes the warm list for pricing/launch)

---

**After completing this module:**

| Verdict | Next module | Why |
|---|---|---|
| Strong (40%+) | `/unstuck freemium-conversion` (Kit) then `/unstuck pricing` (Kit) | Convert free users to paid without losing them |
| Moderate (20-39%) | `/unstuck diagnose` → then re-run retro-validate | Fix before charging |
| Weak (<20%) | `/unstuck one-liner` or `/unstuck idea-bank` | Restart with learnings |

↩ Come back to `/unstuck retro-validate` when: you've made improvements and want to re-test user sentiment.

</process>

<success_criteria>
This module is complete when:
- [ ] Product state captured (users, usage, conversations)
- [ ] 10 users identified for Sean Ellis test
- [ ] Email/message drafted and sent
- [ ] Results collected and % calculated
- [ ] Verdict delivered (strong/moderate/weak)
- [ ] Niche identification attempted (what "very disappointed" users share)
- [ ] Artifact saved to `.unstuck/retro-validate-<date>.md`
- [ ] Context updated (D.1, D.7)
- [ ] Next module routed per verdict
</success_criteria>
