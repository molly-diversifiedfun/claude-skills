# Critique Frameworks — Detailed Mechanics

Reference material for the devil's-advocate skill. Each framework below defines how to structure the critique when that framework is selected in Phase 2.

---

## Pre-Mortem (Business Plans, Strategies, Projects)

**Source:** Gary Klein (HBR, 2007). Prospective hindsight increases cause identification by ~30%.

**Mechanism:** Declare the plan has already failed. Work backward from that imagined future.

**How to run it:**

1. State the failure as fact: "It's [timeframe]. This has failed. Not a little — spectacularly. Here's what happened."
2. Generate failure causes in four categories:
   - **Assumption failures** — What did they believe that turned out to be wrong?
   - **Execution risks** — What went wrong in the doing, not the thinking?
   - **External shocks** — What changed in the market, competition, or environment?
   - **Resource gaps** — What did they not have enough of (time, money, people, skills)?
3. Rank by likelihood and severity.
4. Map each failure cause to the Challenge Report format (Fatal Flaw = most likely/severe, Significant Risks = next 2-3).

**Common pitfall:** Generating generic failures ("ran out of money," "bad market timing") instead of failures specific to THIS plan. Every failure cause must reference specific elements of the user's proposal.

---

## WWHTBT — What Would Have to Be True (Decisions Between Options)

**Source:** Roger Martin, *Playing to Win* (HBR Press, 2013).

**Mechanism:** Convert adversarial debate into collaborative assumption-mapping. Don't argue whether an idea is good — map the conditions required for it to succeed, then test the weakest ones.

**How to run it:**

1. List 5-7 conditions that must hold for this to be a sound choice. Categories:
   - **Market conditions** — demand, timing, competition, pricing power
   - **Capability conditions** — skills, resources, team, technology
   - **Behavioral conditions** — customer behavior, adoption patterns, willingness to pay
   - **Environmental conditions** — regulatory, economic, platform dependency
   - **Execution conditions** — timeline, coordination, sequencing
2. For each condition, assess: Is this TESTED (evidence exists), ASSUMED (believed but unverified), or HOPED (desired but no basis)?
3. Design a specific, cheap test for each ASSUMED or HOPED condition.
4. The Fatal Flaw = the condition most critical to success AND least tested.
5. Stress-Test Questions target the HOPED conditions.

**Common pitfall:** Listing conditions so broad they're unfalsifiable. "The market must want this" is useless. "Enterprise CIOs must prioritize this over their current vendor within 6 months of first contact" is testable.

---

## Steel-Man + Red Team (Arguments, Positions, Theses)

**Source:** Daniel Dennett's four steps (2013) + military red teaming protocols.

**Mechanism:** Demonstrate complete understanding of the strongest version, then attack it from defined adversary positions.

**How to run it:**

1. **Steel-man** (Phase 3 of the main skill — always required, but especially critical here):
   - Re-express the position so clearly the user says "I wish I'd said that"
   - List points of agreement, especially non-obvious ones
   - Identify what's genuinely strong about the position
   - Fill in gaps with the best available evidence
2. **Red team** (Phase 4):
   - Define 2-3 adversary perspectives relevant to the domain
   - For each adversary, generate the strongest possible counter-argument
   - Adversaries should have DIFFERENT attack vectors (e.g., one attacks the logic, one attacks the evidence, one attacks the implications)
3. Map the strongest adversary argument to Fatal Flaw, the rest to Significant Risks.

**Common pitfall:** Generating straw-man adversaries who make weak arguments. Each adversary must make the strongest possible case against the position.

---

## Named Adversary Personas (Creative Work, Pitches, Products)

**Source:** Red teaming adapted for creative evaluation.

**Mechanism:** Critique from specific, named perspectives that represent real-world resistance the work will face.

**Default personas (adapt based on domain):**

| Persona | Attacks | Voice |
|---------|---------|-------|
| **The Skeptical Customer** | Value proposition, pricing, differentiation. "Why should I care? Why is this different from X?" | Busy, impatient, has seen it all before. |
| **The Hostile Reviewer** | Quality, originality, execution. "This has been done before, and done better." | Knowledgeable, unimpressed, looking for flaws. |
| **The Competitor** | Market position, defensibility, timing. "Here's how I'd crush this." | Strategic, opportunistic, looking for weaknesses to exploit. |

**How to run it:**

1. Announce the personas and what each one attacks.
2. Generate 1-2 paragraphs of critique FROM each persona (in their voice).
3. Synthesize across personas to identify the Fatal Flaw (the critique that appears from multiple perspectives).
4. Significant Risks = the strongest single-persona critiques.
5. Stress-Test Questions come from the persona whose critique was hardest to dismiss.

**Common pitfall:** Making all personas say the same thing in different words. Each must attack a DIFFERENT dimension.

---

## Socratic Method (Uncertainty, "I'm Not Sure About This")

**Source:** Foundation for Critical Thinking — six question types.

**Mechanism:** The user already has doubts. Don't assert problems — ask questions that surface contradictions in their own reasoning.

**Six question types (use in this order):**

1. **Clarification:** "What exactly do you mean by [X]?" — Forces precision on vague terms.
2. **Assumption-probing:** "What are you assuming about [Y] that might not be true?" — Surfaces hidden premises.
3. **Evidence-probing:** "What evidence supports [Z]? What would change your mind?" — Tests the basis.
4. **Perspective-exploring:** "How would [specific stakeholder] see this differently?" — Breaks single-perspective lock-in.
5. **Implication-probing:** "If [X] is true, what follows? What are you committing to?" — Maps consequences.
6. **Meta-questions:** "Why do you think you're uncertain? What would make you confident?" — Surfaces the real blocker.

**How to run it:**

1. Ask ONE question at a time. Wait for the answer.
2. Build on previous answers — each question should reference something the user said.
3. When contradictions emerge, surface the tension explicitly: "You said [A] earlier and [B] just now. Those point in different directions. Which one holds?"
4. After 4-6 questions, synthesize into the Challenge Report format.
5. The Fatal Flaw = the contradiction or unresolved tension that emerged most clearly.
6. Stress-Test Questions = the questions the user struggled most to answer.

**Common pitfall:** Asking generic philosophical questions instead of questions specific to THIS situation. Every question must reference the user's specific claims or assumptions.

---

## De Bono's Black Hat (Supplementary — Use Within Other Frameworks)

**Source:** Edward de Bono, *Six Thinking Hats* (1985).

**Mechanism:** Explicitly labeled critique mode with clear boundaries.

This is rarely the primary framework. Use it as a supplementary technique when the user requests "just tell me what could go wrong" without a specific situation type. Apply the Black Hat label, then default to WWHTBT structure for the report.

---

## Framework Selection Edge Cases

- **User presents multiple ideas:** Ask which one to challenge first. Don't combine.
- **User's situation doesn't fit any category:** Default to Steel-Man + Red Team. It's the most general-purpose.
- **User asks for a specific framework by name:** Use that framework regardless of situation type.
- **User asks to switch frameworks mid-conversation:** Generate a new complete report using the requested framework. Don't try to merge.
