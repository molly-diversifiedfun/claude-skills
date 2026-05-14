<required_reading>
**Read these reference files NOW:**
1. references/core.md
</required_reading>

<process>

**Step 0 — Check User Context first (Mode 1 behavior)**

This skill designs the lead-magnet → tripwire funnel that sits in front of the core product. Before the Opening, scan the user's uploaded User Context file:

- **Section B** (project + audience): you need a locked core product, a target audience, and a price.
- **Section D.1** (T04 Validation Scorecard): pain quotes, themes, RICE verdict. Use verbatim pain language in lead-magnet headlines.
- **Section D.2** (T05 One-Page Scope): the core product the funnel feeds into.
- **Section D.3** (T06 Pricing Calculator): the core product price. Tripwire price is typically ~10–20% of this.

If Section B + D.2 + D.3 are populated, DRAFT the funnel — don't ask. If any are empty, ask the buyer to run the upstream module first:

- Empty B → route to `/unstuck discovery`
- Empty D.2 → route to `/unstuck scope`
- Empty D.3 → ask buyer for the locked price in one line

Don't ask what you can read. Draft what you can infer.

**Marketing OS detection.** If a Marketing OS extension is loaded, this skill DEFERS to Marketing OS skills for the load-bearing steps:

- **Step 1 (Lead Magnet Topic)** → use Marketing OS `map-awareness-to-messaging` (Schwartz 5 Levels of Awareness) to pick a topic that matches where the audience actually sits on the awareness spectrum.
- **Step 2 (Tripwire Designer)** → use Marketing OS `design-micro-commitment-ladder` (Brunson Value Ladder + Freedman-Fraser foot-in-the-door + tripwire/SLO economics) for the tripwire architecture, then `build-irresistible-offer` (Hormozi Value Equation: Dream Outcome × Likelihood / Time × Effort) to maximize value/minimize friction.
- **Step 3 (Lead Magnet Content)** → use Marketing OS `build-content-repurposing-pipeline` or `viral-hook-generator` for the actual content draft.
- **Step 4 (Tripwire Email Sequence)** → use Marketing OS `build-email-story-engine` (Brunson Soap Opera Sequence + Epiphany Bridge) for the 3-email arc.

If Marketing OS is NOT loaded, run the steps below using the free-tier frameworks already in references/core.md (Cialdini, Sugarman, Welsh, Sanchez) + Molly's frameworks (Scope Guillotine, V1 Manifesto, 70% Rule).

Tell the buyer up front which mode you're running:

> "Mode: [Marketing OS loaded — deferring to paid framework skills] OR [AI Build Partner free tier — running with Cialdini/Sugarman + Molly's frameworks]. The free version produces a real funnel; the paid version produces the same funnel with Hormozi/Brunson/Schwartz architecture baked in."

---

**Opening (output verbatim to the buyer):**

> "We're going to design the funnel that gets cold strangers to your core product without you doing a launch every six weeks. Four steps:
>
> 1. Pick a **lead-magnet topic** that maps to your core product
> 2. Design a **$19 tripwire** that solves one slice of the same problem
> 3. Draft the **lead-magnet content** (the actual deliverable)
> 4. Write the **3-email tripwire sequence** that converts opt-ins
>
> Each step ends with a paste-ready artifact. We'll spend ~30 minutes total.
>
> **One ground rule:** if any step feels too abstract, three ways out:
> - Type **`hint`** — another worked example from a different niche
> - Type **`guide me`** — I'll interview you to the answer
> - Type **`draft it`** — paste what you have, I'll polish
>
> Ready?"

If the buyer invokes hint / guide me / draft it on any step, fire the corresponding sub-flow from `references/core.md` `<answer_assistance>`.

---

**Step 1 — Lead Magnet Topic Selector**

**What we're locking:** a single lead-magnet topic that earns the email AND primes the buyer for the core product.

Read User Context Section B (audience + pain) + Section D.1 (validation pain quotes) + Section D.2 (core product).

Produce **3 candidate lead-magnet topics**, ranked. Each candidate gets:

- **Topic title** (10 words max, headline-style)
- **Format** (PDF checklist / mini-guide / scorecard / template pack / 5-day email course / video walkthrough)
- **Time-to-consume** (≤ 20 minutes — longer means it won't get consumed)
- **Bridge to core product** (one sentence: how does finishing this lead magnet make the core product the obvious next purchase?)
- **Ranking score** (1–5 on: pain proximity, deliverability in <2 hrs of build time, bridge strength)

**Example of a 5/5 ranking (for a $97 course on "Junior PM career strategy"):**

> **Candidate A (rank 1, score 5/5):** "The 5-Question Career Compass for Junior PMs"
> - Format: PDF scorecard, ~15 min to fill
> - Bridge: scoring reveals 2-3 gaps the course directly fixes — they finish the scorecard knowing exactly what they need
> - Why rank 1: pain quotes from D.1 said "I don't know what to focus on" 4 times. The scorecard answers that question and surfaces the course as the answer.
>
> **Candidate B (rank 2, score 4/5):** "12 Phrases That Get You Promoted (and 8 That Don't)"
> - Format: PDF mini-guide, ~10 min to read
> - Bridge: teaches *what* to say but not *how* to do real strategy work — the course is the how
> - Why rank 2: more shareable than the scorecard but weaker bridge to course
>
> **Candidate C (rank 3, score 3/5):** "5-Day Strategy Sprint: Run Your First Discovery Loop"
> - Format: 5 daily emails
> - Bridge: hands-on practice; people who finish typically want more structure → course
> - Why rank 3: highest commitment ask, slowest opt-in-to-tripwire timing

Present the 3 candidates. Ask:

> "Which one matches your gut + your audience pain? Pick A, B, or C — or push back if none feels right and I'll regenerate. The pick locks the next 3 steps."

Lock the pick. Add it to the artifact bucket.

---

**Step 2 — Tripwire Product Designer**

**What we're locking:** a $19 product that resolves ONE specific slice of the same pain the lead magnet surfaced.

Tripwire rules (non-negotiable):

- **Price: $19** (default — adjust to $9 / $27 only if the audience/niche math forces it)
- **Outcome: ≤ 1 hour to produce a result** for the buyer
- **Scope: ONE slice** — not a "mini course," not a "starter kit." One template, one walkthrough, one swipe file, one calculator
- **Build effort: ≤ 4 hours** of your time to produce
- **Bridge: finishing the tripwire makes the core product the obvious next purchase** (same logic as lead magnet, one rung higher)

Given the locked lead-magnet pick, generate ONE tripwire concept that:

1. Solves the highest-friction sub-problem the lead magnet exposed
2. Hands the buyer a result they can hold (template / artifact / walkthrough)
3. Naturally surfaces the limitation that the core product fixes

**Example (continuing the Junior PM career example):**

> **Tripwire: "The Strategy Loop Worksheet — $19"**
> - Format: 1 fillable PDF + 1 video walkthrough (~20 min total)
> - Outcome: the buyer runs ONE discovery loop on a real problem at their job within 48 hours
> - Bridge: "you ran one loop. The course teaches you to run them weekly until your manager treats you as a strategist, not a ticket-grooming PM."
> - Build effort: 3 hrs (worksheet ~30 min, video script ~45 min, recording + edit ~90 min)
> - Why it works: lead-magnet scorecard revealed "no structure for strategy work" was the most-flagged gap. Tripwire gives them ONE structured loop. Course gives them the system.

Present the tripwire. Ask:

> "Does this feel like the right $19 slice — small enough to ship in 4 hours, big enough to deliver a real result? Edit any field that's off, or say `regenerate` to try a different angle."

Lock the tripwire. Add to the artifact bucket.

---

**Step 3 — Lead Magnet Content Writer**

**What we're producing:** the actual lead-magnet content. Not an outline — the deliverable.

For the locked lead-magnet pick:

- If it's a **PDF / scorecard / mini-guide:** draft the full document, section by section. Headline + intro (≤ 120 words) + 5–7 content sections + close with the bridge to tripwire (one short paragraph + button text).
- If it's an **email course (5-day):** draft 5 emails. Each ≤ 200 words. Day 5 ends with the tripwire offer.
- If it's a **template pack:** draft the actual templates (3–5 of them) with usage instructions.

Use User Context Section B (audience language) + Section D.1 (verbatim pain quotes from the 10-conversation method, where available) + buyer's voice register from Section A.

**Voice rules (load-bearing):**

- Lead with the pain in the buyer's own language. No "Welcome!" openers.
- Specific numbers > vague claims. "Run the loop in 47 minutes" is banned (47 is an AI tell). Use real, varied numbers.
- No filler paragraphs. Every section advances the bridge.
- Banned: unlock / journey / transform / level up / dive in.
- Close every lead-magnet section with a one-line reflective question, not a generic CTA.

Output the full lead-magnet content in a single message. Mark any section where you defaulted to a placeholder (e.g., "[INSERT BUYER'S OWN EXAMPLE]") so the buyer can spot it.

After the draft, ask:

> "Voice check: read section 1 and the closing bridge. Does it sound like you, or does it sound like a generic lead magnet? Flag specific sentences that feel off and I'll regenerate just those — don't redo the whole thing."

Spot-fix loop until the buyer says ship.

---

**Step 4 — Tripwire Email Sequence**

**What we're writing:** a 3-email sequence sent immediately after the lead-magnet opt-in. Job: convert ~3–8% of opt-ins into $19 tripwire buyers.

Cadence:

- **Email 1 — Delivery (immediate):** lead magnet attached / linked + one-line acknowledgment + first soft tripwire mention
- **Email 2 — Bridge (Day 1, ~24 hrs later):** the gap the lead magnet exposed + how the tripwire fills it + clear $19 offer + countdown to launch-discount expiration
- **Email 3 — Last call (Day 3, ~72 hrs after opt-in):** discount or bonus expiring + objections handled + final CTA

Email rules (non-negotiable):

- Each email **≤ 220 words**
- **One CTA** per email
- Subject line: question or specific number, no "Re:" tricks
- Sound like a human, not a corporation

Use the locked lead-magnet name + tripwire name + buyer's voice. Reuse hero language from the lead-magnet bridge in Email 2.

**Example skeleton (Junior PM example):**

> **Email 1 — Subject A: "Your Career Compass is inside ↓"** / **Subject B: "Here's the scorecard"**
> Hi [First Name] — your Career Compass scorecard is attached. Run it in 15 minutes. Most people score themselves a 6/10 and can't articulate why. That's the gap.
> If you finished it and want the *next* move — the Strategy Loop Worksheet runs ONE real discovery loop on a real problem at your job in 48 hours. $19, launch price for the next 72 hours.
> [Get the worksheet →]
> — Molly
>
> **Email 2 — Subject A: "The 47% number"** (banned — change to "The half-rule"). **Subject B: "Why most PMs stay stuck"**
> Hi [First Name] — yesterday you scored your strategy practice. Most junior PMs score themselves on "doing strategy" at half the level they score themselves on "shipping tickets." That gap is what gets them stuck at L4.
> The Strategy Loop Worksheet hands you ONE loop, in 48 hours, on a real problem you already have. The course teaches the system. The worksheet teaches the *move*.
> $19. Launch price ends Friday 11:59pm Pacific. After that it goes to $29.
> [Run your first loop →]
> — Molly
>
> **Email 3 — Subject A: "Final 6 hours"** / **Subject B: "Closing this"**
> Hi [First Name] — last email. Strategy Loop Worksheet drops to launch price tonight at 11:59pm Pacific. After that, it's $29.
> Common question: "Will the course teach me the same thing?" The course teaches the system across 5 weeks. The worksheet runs ONE loop in 48 hours. Different speed.
> If you're on the fence, the worksheet is the cheaper test.
> [Run the loop →]
> — Molly

Adjust the example to the buyer's actual lead-magnet + tripwire. Output all 3 emails in a single message.

After the draft, ask:

> "Voice check: read Email 2. Does the bridge from lead magnet → tripwire feel honest, or does it feel like an upsell? Flag the specific sentence and I'll regenerate just that section."

Spot-fix loop.

---

**Step 5 — Output the Funnel Artifact**

After Steps 1–4 are locked, output the paste-ready block:

```
SECTION D — Funnel Design
Locked: [Date]
Source: /unstuck funnel

LEAD MAGNET
- Title: [paste]
- Format: [paste]
- Time-to-consume: [paste]
- Bridge to tripwire: [one sentence]

TRIPWIRE
- Name: [paste]
- Format: [paste]
- Price: $19
- Outcome: [one sentence]
- Build effort: [hours]
- Bridge to core product: [one sentence]

LEAD MAGNET CONTENT
- [Paste full draft from Step 3, or link to where it's stored]

TRIPWIRE EMAIL SEQUENCE
- Email 1 (immediate): [subject + first 2 lines]
- Email 2 (Day 1): [subject + first 2 lines]
- Email 3 (Day 3): [subject + first 2 lines]

SHIP CHECKLIST
- [ ] Lead magnet built and hosted
- [ ] Opt-in form wired (Kit / Beehiiv / MailerLite / Substack)
- [ ] Tripwire built (worksheet + video / template / etc)
- [ ] Stripe checkout link live for tripwire
- [ ] 3 emails loaded into ESP with delays (immediate / Day 1 / Day 3)
- [ ] End-to-end test: signed up with a fresh email, received all 3 emails, bought the tripwire

Built with the Unstuck Method — unstuckwithmolly.com
```

---

**Step 6 — Chain to next module**

- "Funnel is designed. Build order: lead magnet first (~2 hrs), tripwire second (~4 hrs), email sequence third (~1 hr to write into your ESP). Total ship time ~7 hrs across 2 working days. Once it's live, run `/unstuck weekly` next Sunday to check the opt-in → tripwire conversion rate. If you don't have a landing page for the lead magnet opt-in yet, run `/unstuck landing-page` next — the funnel needs a front door."

</process>

<success_criteria>
This module is complete when:
- [ ] Lead-magnet topic locked (1 of 3 candidates picked, with bridge to tripwire)
- [ ] Tripwire designed ($19, ≤ 4 hr build, ≤ 1 hr to produce a buyer result)
- [ ] Lead-magnet content drafted (full deliverable, not an outline)
- [ ] 3-email tripwire sequence drafted (≤ 220 words each, one CTA each)
- [ ] Voice check passed on lead-magnet content + Email 2
- [ ] Section D — Funnel Design paste block delivered with ship checklist
- [ ] Next-module recommendation given (`/unstuck weekly` or `/unstuck landing-page`)
</success_criteria>
