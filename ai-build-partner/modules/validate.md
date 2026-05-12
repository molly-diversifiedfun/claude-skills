<required_reading>
**Read these reference files NOW:**
1. references/core.md
2. references/frameworks.md (sections: rice_scoring, ten_conversation_method)
</required_reading>

<process>

**Step 0 — Check User Context first (Mode 1 behavior)**

Before the Opening, scan the user's uploaded User Context file:
- Read **Section B.1** (project + audience) if present
- If populated, ANCHOR the RICE numbers before asking: estimate Reach from audience size + niche, estimate Impact from the audience's stated pain, propose a defensible Confidence ceiling (cap at 3 if zero conversations done), apply Cargill (1985) bias to Effort. Present opening scores + one-line reasoning per dimension, then ask the user to refine.
- If User Context is empty, use the Opening below and run the question-by-question RICE intake — and consider routing the user to `/unstuck discovery` first if they have no project picked yet.

Don't ask what you can read. Draft what you can infer.

---

**Opening (output verbatim to the buyer):**

> "Before you build anything, let's check if this idea is worth your time. I'll help you score it (RICE) and build a validation script you can run with real people.
>
> **One ground rule:** if any question feels too abstract, three ways out:
> - Type **`hint`** — another worked example
> - Type **`guide me`** — I'll interview you to the answer
> - Type **`draft it`** — paste what you have, I'll polish
>
> Ready?"

If the buyer invokes hint / guide me / draft it on any question, fire the corresponding sub-flow from `references/core.md` `<answer_assistance>`.

---

**Step 1: One-sentence idea**

**What we're locking:** A plain-language idea statement. No jargon.

"Describe your idea in one sentence. Plain language — like you're explaining it to a friend at a bar."

**Example of a 5/5 answer:**
> "A 5-week paid cohort + workbook that teaches junior PMs how to do real product strategy work instead of grooming JIRA tickets."

Push back if it has jargon ("synergize," "leverage") or is too abstract ("a platform for thought leadership").

---

**Step 2: RICE Scoring**

**What we're producing:** A defensible (R x I x C) / E score.

Walk through each RICE dimension one at a time. Help them score honestly — push back on inflated numbers.

**Each dimension with an example:**

- **Reach (1-10):** "How many people could this realistically reach in the first 6 months?"
  > Example: "There are ~50K junior PMs at SaaS companies in the US per LinkedIn. I can realistically reach 2-3K of them via Lenny's audience + my own network in 6 months. Reach = 6."

- **Impact (1-10):** "How big of a difference does this make in someone's day/week/life?"
  > Example: "Aamir's specifically said this would be a career-pivot moment for him. Impact on income (next role 30% higher salary) + identity (PM not admin). Impact = 8."

- **Confidence (1-10):** "How sure are you that people actually want this — based on evidence, not hope?"
  > Example: "Zero paid customers yet. 8 PMs said they'd be interested but none have paid. Confidence cap at 3 until I get 5 real conversations. Confidence = 3."

- **Effort (1-10):** "How much work is this to build a shippable V1? 1 = weekend project, 10 = six months."
  > Example: "I have the content in my head from doing this work for 8 years. Workbook = 2 weeks. Live sessions = me running 5 webinars. Effort = 4. (Cargill: assume 2x, so really 8.)"

Calculate: (Reach x Impact x Confidence) / Effort.
Aamir's example: (6 × 8 × 3) / 8 = **18** → below 50, kill or refine.

Present the verdict:
- **Below 50:** "This one's not worth your time right now in current form. Either talk to 5 people to raise Confidence, or cut the scope to drop Effort. Let's do one of those."
- **50-150:** "There's something here, but you need more evidence. Let's build a validation script."
- **Above 150:** "Strong signal. Let's validate it and then scope it."

---

**Step 3: Build the 10-Conversation Script (if RICE > 50)**

**What we're writing:** 5 questions Aamir-type people will actually answer.

Customize the 5 Core Questions from `<ten_conversation_method>` for their specific idea. Make the questions feel natural, not clinical.

**Example of a 5/5 customized question (for Junior PM Career Compass):**
> ❌ Clinical: "What is your current pain point regarding product strategy execution?"
> ✅ Natural: "Walk me through a Tuesday afternoon. What's actually happening? Where does it go off the rails?"

---

**Step 4: Define who to talk to**

**What we're listing:** 10 named humans (or a tight specification of where to find them).

"Who are the 10 people you'd talk to? Be specific — not 'entrepreneurs' but 'junior PMs at B2B SaaS companies 1-3 years in, who've engaged with Lenny's content or commented in r/ProductManagement.'"

**Example of a 5/5 sourcing answer:**
> "1. Aamir (my own network, observability SaaS). 2-3. Two PMs from Lenny's Slack who DM'd me last month. 4-7. Four PMs from r/ProductManagement who post about backlog grooming. 8-10. Three more from my LinkedIn connections, 1-3 years in PM at SaaS."

---

**Step 5: Set signal thresholds**

**What we're locking:** Numbers that decide build / refine / kill.

Explain: 8+/10 = build it. 4-7 = refine. 3 or fewer = kill or pivot.

---

**Step 6: Present Validation Kit**

Use template at templates/validation-kit.md.

---

**Step 7: Chain to next module**

- If RICE > 150: recommend `/unstuck scope`
- If RICE 50-150: "Run the 10 conversations first, then come back for `/unstuck scope`"
- If RICE < 50: "Kill it. What else are you considering?"

</process>

<success_criteria>
This module is complete when:
- [ ] Idea stated in one sentence
- [ ] RICE scored with honest numbers
- [ ] Verdict delivered clearly
- [ ] 10-Conversation Script customized (if RICE > 50)
- [ ] Target audience and sourcing identified
- [ ] Validation Kit artifact delivered
- [ ] Next step recommended
</success_criteria>
