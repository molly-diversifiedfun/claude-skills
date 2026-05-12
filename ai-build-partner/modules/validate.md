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

**Opening:** "Before you build anything, let's make sure this idea is worth your time. I'm going to help you score it and build a validation script you can run with real people."

**Step 1: One-sentence idea**
"Describe your idea in one sentence. Plain language — like you're explaining it to a friend at a bar."

**Step 2: RICE Scoring**
Walk through each RICE dimension one at a time. Help them score honestly — push back on inflated numbers.

- **Reach (1-10):** "How many people could this realistically reach in the first 6 months?"
- **Impact (1-10):** "How big of a difference does this make in someone's day/week/life?"
- **Confidence (1-10):** "How sure are you that people actually want this — based on evidence, not hope?"
- **Effort (1-10):** "How much work is this to build a shippable V1? 1 = weekend project, 10 = six months."

Calculate: (Reach x Impact x Confidence) / Effort

Present the verdict:
- Below 50: "This one's not worth your time right now. Let's talk about what else you're considering."
- 50-150: "There's something here, but you need more evidence. Let's build a validation script."
- Above 150: "Strong signal. Let's validate it and then scope it."

**Step 3: Build the 10-Conversation Script (if RICE > 50)**
Customize the 5 Core Questions from `<ten_conversation_method>` for their specific idea. Make the questions feel natural, not clinical.

**Step 4: Define who to talk to**
"Who are the 10 people you'd talk to? Be specific — not 'entrepreneurs' but 'freelance designers making $80K+ who struggle with client invoicing.'"
Help them identify where to find these people.

**Step 5: Set signal thresholds**
Explain: 8+/10 = build it. 4-7 = refine. 3 or fewer = kill or pivot.

**Step 6: Present Validation Kit**
Use template at templates/validation-kit.md.

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
