<required_reading>
**Read these reference files NOW:**
1. references/core.md
</required_reading>

<process>

**Step 0 — Check User Context first (Mode 1 behavior)**

This skill drafts the 8-section landing page customized to the buyer's project. Day 22 of Module 4 (Equip), after price is locked (T06) and product is built (T08). Before the Opening, scan the user's uploaded User Context file:

- **Section B** (project + audience + JTBD): Hero formula needs all three
- **Section D.1** (T04 Validation Scorecard): pain quotes — use verbatim where possible in Problem section
- **Section D.2** (T05 One-Page Scope): V1 features → "What's Inside"
- **Section D.3** (T06 Pricing Calculator): locked price + outcome value-claim
- **Section A** (voice / register): creator bio + sentence-level voice

If Sections B + D.2 + D.3 are populated, DRAFT all 8 sections — don't ask. If anything's missing, run `/unstuck scope` or `/unstuck validate` first.

**Marketing OS detection (load-bearing).** If Marketing OS is loaded, this skill DEFERS to paid framework skills for the load-bearing sections:

- **Hero + offer architecture** → `build-irresistible-offer` (Hormozi Value Equation: Dream Outcome × Likelihood / Time × Effort)
- **Hero copy + Schwartz awareness calibration** → `funnel-landing-page-designer` (Cialdini Pre-Suasion + landing-page architecture)
- **Long-form / sales-letter version** → `build-conversion-sales-letter` (Belcher 21-Step Sales Letter + Schwartz 5 Levels of Awareness opening calibration + Cialdini 7 Principles woven throughout)
- **FAQ + objections section** → `generate-faq-from-objections`
- **Voice review** → `audit-design-tells` (catches AI-tells, weak persuasion moves)

If Marketing OS is NOT loaded, run the 8-section frame below using free-tier references already in core.md: **Cialdini (1984)** on social proof, **Cagan (2017)** on outcome over features, **Sugarman (1984)** on slippery-slide structure + hook anatomy, **Sean Welsh** on first-line discipline, **Joey Sanchez** on contrarian gap hooks.

Tell the buyer up front which mode you're running.

Don't ask what you can read. Draft what you can infer.

---

**Opening (output verbatim to the buyer):**

> "Eight sections. AI drafts first, you edit. The copy drives the design — not the other way around.
>
> Sections we're producing:
> 1. **Hero** — Headline + Subhead + CTA
> 2. **Problem** — make them feel seen, in their own words
> 3. **Solution** — introducing [product]
> 4. **What's Inside** — Features → Benefits table
> 5. **Who it's for / NOT for** — the honest both-sides section
> 6. **Creator bio** — short, credibility-anchored
> 7. **Price + recap CTA**
> 8. **FAQ** — real objections, no strawmen
>
> **One ground rule:** specificity sells. 'Save time' is a vibe. 'Save 4 hours every Sunday' is a sale. I'm going to push back on vague language every time I see it.
>
> Ready?"

---

**Step 1 — Specificity audit on the V1 outcome (BEFORE drafting)**

Before drafting the Hero, audit the V1 outcome itself.

Read User Context Section D.2 V1 features + Section B JTBD. Ask:

> "Your one-sentence V1 outcome — paste it here. If it contains 'save time,' 'improve workflow,' 'boost productivity,' or any vague verb, I'm going to push back and ask for the specific version before we draft anything."

If the outcome is vague, force specificity:

> "'Save time' is a vibe. How much time, on what task, in what unit? '47 minutes' is banned — use a real number. '4 hours every Sunday' is concrete. '20 minutes per JIRA grooming session' is concrete. Rewrite once, then we draft."

If Marketing OS is loaded: fire `map-awareness-to-messaging` (Schwartz 5 Levels of Awareness) to calibrate the outcome to the audience's actual awareness level. Most-aware audiences need product/price framing; least-aware audiences need problem framing first.

---

**Step 2 — Section 1: Hero**

**Headline formula:** "[Outcome] in [Timeframe] — without [Pain Point]"

Generate 2 variants. Each must:
- Lead with the outcome (not the tool)
- Name a specific timeframe (days/weeks/sessions/hours)
- Name a specific pain point being avoided
- Pass the "would a non-customer pass on this in 3 seconds" test

**Example (Junior PM career product):**

> Variant A: "Run real product strategy in 5 weeks — without grinding through another year of JIRA grooming"
> Variant B: "Build a strategy practice in 35 days — without a manager to teach you"

**Subhead:** Adds specificity, names the format/medium ("5-week paid cohort + workbook," not "transformative experience").

**CTA button text:** "Get Access" / "Show Me How" / "Start Now" / "Reserve My Spot" — pick based on price + cohort vs. evergreen.

Output the two variants. Ask the buyer to pick or rewrite. Lock the Hero before moving on — every other section anchors to it.

---

**Step 3 — Section 2: Problem**

Job: make them feel seen. Name the specific pain in their language.

**Framework:** "You know that feeling when ___. You've tried ___, but ___."

Pull from User Context Section D.1 (validation pain quotes) — use VERBATIM phrases where possible. Three slots:

- "You know that feeling when [specific moment, sensory detail — Tuesday afternoon backlog grooming, not 'when work is hard']"
- "You've tried [specific previous attempt — taking a Coursera course, reading Inspired, asking your manager]"
- "But [why it didn't work — specific failure mode]"

If User Context D.1 has zero pain quotes, ask the buyer for 2-3 verbatim phrases their customers actually used during validation. Don't make them up.

Cialdini (1984): social proof works because people use others' reactions as decision shortcuts. Embedding real customer language in the Problem section IS social proof, before any testimonials appear.

---

**Step 4 — Section 3: Solution**

**Framework:** "Introducing [Product Name] — the [format] that [promise]."

One sentence. The "promise" reuses Hero language verbatim (Sugarman slippery-slide — every sentence delivers the reader to the next).

**Example:** "Introducing the Junior PM Career Compass — the 5-week cohort + workbook that hands you a real discovery loop, run on your actual job, in 35 days."

If the Solution sentence doesn't reuse Hero language: rewrite. Hero → Solution is the load-bearing handoff. If they don't echo, the page reads disjointed.

---

**Step 5 — Section 4: What's Inside (Features → Benefits)**

Format: **[Feature]: [Benefit]**

Pull V1 features from User Context D.2. For each feature (max 7), generate a benefit. Rules:

- Feature = what it IS (a 30-page workbook, 5 live calls, a Notion template)
- Benefit = what they GET (a discovery loop they can run Monday, a manager who treats them as a strategist by Week 4)
- Benefit > feature. Cagan (2017): customers don't buy features, they buy outcomes.

| # | Feature | Benefit |
|---|---|---|
| 1 | [paste from D.2] | [outcome-anchored] |
| ... | ... | ... |

Stress-test: if any benefit reads like a vague claim ("better strategic thinking"), rewrite with a specific outcome ("a one-page strategy memo your manager forwards to her director").

---

**Step 6 — Section 5: Who it's for / NOT for (honesty audit)**

**This is where most copy whiffs.** The strongest "for you" sentences are made stronger by an honest "not for you" right next to them.

Generate 3 ✓ lines + 3 ✗ lines.

**✓ This is for you if…**
- Specific demographic + situation
- Specific pain currently experiencing
- Specific aspiration on the other side

**✗ This is NOT for you if…**
- Specific people who'd refund within 30 days
- Specific use cases the product doesn't solve
- Specific phases of buyer journey it's wrong for

Push back on weak "NOT for you" lines:

> "'Not for people who don't want to do the work' is a generic non-answer. Name 3 SPECIFIC people you would refund if they bought. Those are your real 'not for you' lines. Examples: 'Already a Director of Product' / 'Looking for a job-hunting bootcamp, not a strategy practice' / 'Want video lessons not live calls.'"

Refuse to ship the section until the ✗ lines are as specific as the ✓ lines.

---

**Step 7 — Section 6: Creator bio**

**Framework:** "[Your Name] spent [X years] doing [credibility]. Now [what you do]."

One sentence. Two if absolutely necessary. Credibility-anchored, not aspirational.

Pull from User Context Section A (creator credentials, career timeline). If empty, ask:

> "Two lines: what's the credential you actually have (years doing X, role at Y, results shipped), and what are you doing now? No fluff."

Banned: "I'm passionate about helping people unleash their potential." Replace with "I spent 8 years as a Senior PM at observability SaaS companies. Now I teach junior PMs the strategy practice my managers expected me to know on day one."

---

**Step 8 — Section 7: Price + recap CTA**

Format:

> Get the **[Product Name]** for **$[Price]**.
>
> What you get:
> - [Benefit 1 — recap, top 3 only]
> - [Benefit 2]
> - [Benefit 3]
>
> [Final CTA button] — "Buy Now" / "Give Me Access" / "Let's Go"
>
> [Optional guarantee / risk reversal]

Pull price from User Context D.3. Pull top 3 benefits from Step 5 table (not all 7 — recap is shorter than the original).

Guarantee recommendation: if Marketing OS is loaded, fire `build-irresistible-offer` to design the guarantee (Hormozi: a strong guarantee multiplies offer value). Otherwise, default to: "30-day no-questions-asked refund. If it didn't work, get your money back."

---

**Step 9 — Section 8: FAQ (5 Q&A)**

5 questions, real objections only. No strawmen.

Pull from:
- User Context Section D.1 validation conversations (real objections raised)
- Sales-page common objections for this product type (price, time, fit, support, refund)
- Marketing OS `generate-faq-from-objections` if loaded

For each Q&A, audit:

> "Real objection a real buyer would raise? → keep it. Strawman the seller wanted to answer ('Q: Is this for serious people? A: Yes!') → replace it with a real objection."

Common real objections by product type:
- Course: "How is this different from Lenny's / [established competitor]?" / "Do I get access if I miss live sessions?"
- Tool: "Does this work with [my existing stack]?" / "What if I cancel?"
- Service: "What if it doesn't work for my niche?" / "Is the price negotiable?"

Each answer ≤ 60 words. Direct. No deflecting.

---

**Step 10 — Copy best-practice checklist (BEFORE shipping)**

Run the buyer through the checklist:

- [ ] Total page under 300 words (excluding FAQ)? If over 400, cut.
- [ ] One CTA per section?
- [ ] Sounds like a human, not a corporation?
- [ ] Numbers > vague claims everywhere?
- [ ] Leads with outcome, not tool?
- [ ] "NOT for you" section as specific as "for you" section?
- [ ] Hero language echoes in Solution + Price recap?
- [ ] FAQ has zero strawmen?
- [ ] AI-tell vocabulary stripped (no unlock / journey / transform / level up / dive in)?

If any check fails → fix before shipping.

---

**Step 11 — Output the Landing Page artifact**

```
SECTION D.8 — T11 The Landing Page Frame
Locked: [Date]
Source: /unstuck landing-page

HERO
- Headline: [paste]
- Subhead: [paste]
- CTA: [paste]

PROBLEM
- [paste 3-sentence "you know that feeling when…"]

SOLUTION
- [paste one-sentence "Introducing…"]

WHAT'S INSIDE
| # | Feature | Benefit |
| 1 | [paste] | [paste] |
| ... | ... | ... |

WHO IT'S FOR / NOT FOR
✓: [paste 3 lines]
✗: [paste 3 lines]

CREATOR BIO
- [paste 1-2 sentences]

PRICE + RECAP CTA
- Price: $[paste]
- Top 3 benefits recap: [paste]
- CTA: [paste]
- Guarantee: [paste]

FAQ (5 Q&A)
| # | Question | Answer |
| 1 | [paste] | [paste] |
| ... | ... | ... |

VOICE-CHECK PASSES: [Yes/No]
SPECIFICITY-CHECK PASSES: [Yes/No]
NOT-FOR-YOU-AUDIT PASSES: [Yes/No]

Built with the Unstuck Method — unstuckwithmolly.com
```

---

**Step 12 — Chain to next module**

- "Landing page drafted. Three moves next:
> 1. **`/unstuck launch-emails`** — write the 5-email sequence that reuses Hero language verbatim (T12)
> 2. **Build the page** — paste copy into Carrd / Framer / Webflow / etc. Don't let design rewrite copy.
> 3. **Add live-tester DM ask** — 3 humans from your warm list review the page before public launch. They flag the vague claim you missed."

</process>

<success_criteria>
This module is complete when:
- [ ] V1 outcome passes the specificity audit (no "save time"-class vagueness)
- [ ] Hero formula filled (2 variants, one picked)
- [ ] Problem section uses verbatim customer pain language (from D.1 if available)
- [ ] Solution sentence echoes Hero language
- [ ] What's Inside table has 5-7 features mapped to outcome-anchored benefits
- [ ] Who-it's-NOT-for is as specific as Who-it's-for (named refundable people)
- [ ] Creator bio = credibility-anchored, not aspirational
- [ ] Price + recap echoes top 3 benefits + guarantee included
- [ ] FAQ has 5 real objections, zero strawmen
- [ ] Copy best-practice checklist passed
- [ ] Section D.8 paste block delivered
- [ ] Next-module recommendation given (`/unstuck launch-emails`)
</success_criteria>
