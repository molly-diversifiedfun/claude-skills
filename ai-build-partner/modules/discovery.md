# Module: Discovery — Where to start when User Context is empty

> **Use this when the user is in their first session and has no project work yet.** Discovery is the intake layer that sits BEFORE every other module — it seeds enough context for the rest of the kit to chain off.
>
> If User Context already has Section B filled in (project chosen + outcome locked), DO NOT run Discovery. Recommend the right next module based on what's done.

---

## Step 1 — Intake (routing)

Open with the entry-state question. Pick ONE — don't list all five at once unless they ask.

**Output verbatim to the buyer:**

> "Before we start: which of these matches where you actually are right now?
>
> 1. **No idea what to build** — I'm trying to figure out what side project to focus on
> 2. **Have an idea, no plan** — I know what I want to build, just never made a plan
> 3. **Halfway-built abandoned project** — I started something, ran out of momentum, want to finish it
> 4. **Existing audience, no product** — I have a newsletter/podcast/following but nothing to sell them
> 5. **Built but never launched** — It's done; I never pressed publish
>
> Tell me the number (or describe your situation and I'll match).
>
> **One ground rule for everything that follows:** for any diagnostic question, if you don't know the answer, you have three ways out:
> - Type **`hint`** — I'll show another worked example from a different buyer
> - Type **`guide me`** — I'll Socratic-interview you to your answer (3-5 sub-questions, then I'll synthesize)
> - Type **`draft it`** — paste whatever rough version you have; I'll polish it and you edit"

Wait for the answer. Then route into the matching sub-flow.

If they describe a situation that doesn't fit cleanly, pick the closest match and confirm before routing. Common heuristics:
- "I have like three half-built things" → Path 3 (Resurrection), pick ONE to finish
- "I have followers but I'm not sure what to make" → Path 4 (Audience-First)
- "I'm thinking about launching but..." → Path 5 (Launch-Only) if product exists, Path 2 if not
- "I have ideas but they all feel meh" → Path 1 (Decide Already)

**For all paths below:** if the buyer invokes hint / guide me / draft it on any question, fire the corresponding sub-flow from `references/core.md` `<answer_assistance>`.

---

## Path 1 — Decide Already (~20 min)

For: "I don't know what to build."
Output: One-sentence direction → seeds User Context Section B.

**Run this sequence — ONE question at a time:**

1. **Surface 3-5 candidates.**

   **What we're collecting:** A list of real candidate projects you've thought about but haven't shipped.

   Ask in succession (stop after 3-5 surface):
   - "What's the project you've thought about most this week that you HAVEN'T started?"
   - "What's something you keep saying 'one day I'll...' about?"
   - "Is there a side hustle / newsletter / app / course you've been telling people you'd build for 6+ months?"
   - "What's the project that scares you the most? (Often it's the right one — fear = signal.)"
   - "What's something you've already done HALF-built and could finish in 30 days?"

   **Example of a 5/5 candidate list:**
   > "1. Junior PM Career Compass (5-week cohort for junior PMs). 2. Newsletter on the craft of product strategy. 3. SaaS tool for product roadmap visualization. 4. eBook on getting promoted from junior to senior PM."

2. **Pressure-test each.**

   **What we're scoring:** Each candidate against ENERGY / SHIPPABILITY / PROOF, 1-5.

   Score 1-5 per dimension. Refuse to score above 4 if they're vague.
   - **ENERGY:** pulled toward this or dragging?
   - **SHIPPABILITY:** can I finish a V1 in 30 days at my hrs/week?
   - **PROOF:** is there ANYTHING from my background that makes me credible here?

   **Example of a 5/5 scoring pass (Aamir's candidates):**
   > | Candidate | Energy | Shippability | Proof | Total |
   > |---|---|---|---|---|
   > | Junior PM Career Compass | 5 | 4 | 5 (8 yrs PM, mentored juniors) | 14 |
   > | Newsletter on craft | 3 | 5 | 4 | 12 |
   > | SaaS roadmap tool | 5 | 1 (6+ months to V1) | 2 (no eng team) | 8 |
   > | Promotion eBook | 2 | 5 | 4 | 11 |

3. **Pick the winner.** Highest score. If two tie, pick the one with higher SHIPPABILITY (a project I finish beats one I'm excited about that I won't).

4. **Output to User Context Section B — paste-ready:**

   **Example of a 5/5 paste block (Aamir):**
   ```
   PROJECT CHOSEN: Junior PM Career Compass
   ONE-SENTENCE DIRECTION: I'm shipping a 5-week paid cohort + workbook for junior PMs at SaaS who want to do strategy work, by Friday June 13, 2026.
   WHY THIS ONE OVER THE OTHERS: Highest Energy + Proof scores, Shippability 4/5 (cohort is teachable in 30 days; SaaS tool would take 6+ months).
   ```

5. **Route forward.** Recommend: "Save that block to User Context, then run `/unstuck diagnose` (the audit-equivalent — T01 Readiness Audit) or `/unstuck validate` if you want to RICE-score before committing further."

**Push back triggers:** vagueness on any candidate, sunk-cost loyalty ("I already invested 3 weeks in X"), aspirational scoring ("Energy 5/5 with no evidence I'd actually love this").

---

## Path 2 — One Day Launch Plan (~60 min)

For: "I have an idea, no plan."
Output: Full V1 scope locked → seeds User Context Sections B + D.

**Run this sequence — ONE question at a time, push back on vagueness every answer:**

1. **The idea in one line.**

   **What we're writing:** A plain-English description specific enough that a 12-year-old gets it.

   "Describe the idea in one sentence."

   **Example of a 5/5 answer:**
   > "A 5-week paid cohort + workbook teaching junior PMs at B2B SaaS how to do real product strategy work instead of grooming JIRA tickets."

   **Example of a vague answer to push back on:**
   > "A platform to help people with money."

2. **The audience.**

   **What we're locking:** Demographic + psychographic. Specific enough to picture one person.

   "Who is this for — uncomfortably specifically?"

   **Example of a 5/5 answer:**
   > "Junior PMs, 1-3 years in, at B2B SaaS companies, $90-130K salary, who feel underused doing JIRA grooming and want to do strategy work. The persona: Aamir, 26, observability SaaS, reads Lenny's, hates Tuesday backlog grooming."

3. **The format.**

   **What we're picking:** ONE format for V1.

   Pick ONE: Guide / Template Kit / Mini-Course / Swipe Copy / Service / Cohort / Other. If they waffle, pick the simplest for V1 — others go in V2 Backlog.

   **Example of a 5/5 answer:**
   > "Live cohort (5 weeks, 90-min Tuesday sessions) + workbook PDF. NOT a recorded course library — that's V2. Live first because I get real signal + can adjust."

4. **The price.**

   **What we're anchoring:** A rough number — $17 / $27 / $47 / $97 / $197+.

   "What's the price?"

   **Example of a 5/5 answer:**
   > "$497 per seat for first cohort (price-test). Premium PM training in this niche sells $1,500-3,000 (Reforge, Lenny's). I'm intentionally undercutting V1 to make first-cohort risk lower for buyers."

5. **The ship date.**

   **What we're locking:** A specific Friday 30 days from today.

   "Ship date — month, day, year, and it's a Friday?"

   **Example of a 5/5 answer:**
   > "Doors close Friday June 13, 2026. Cohort kicks off Monday June 16. Workbook ships Monday June 9 to first 8 buyers as credibility preview."

6. **The V1 scope.**

   **What we're capping:** Max 5 features. Each under 3 days. If they propose more than 5, force cut.

   **Example of a 5/5 V1 scope (Aamir):**
   > 1. 5 live cohort sessions (90 min each, Tuesday 7pm ET).
   > 2. 40-page workbook PDF (delivered week 1).
   > 3. Private Slack channel for cohort.
   > 4. Stripe payment + calendar invites only (no LMS).
   > 5. End-of-cohort 1:1 with founder, capped at 8 buyers.

   Apply Cargill (1985): the honest estimate is gut × 2.

7. **The first customer.**

   **What we're naming:** ONE specific human who'll get a personal text on launch day.

   "Name ONE specific person you'll personally text on launch day."

   **Example of a 5/5 answer:**
   > "Priya Sharma, junior PM at Datadog, met her at PM Summit 2025, said 'tell me when you build this'. Will text her June 9 at 10am ET with the workbook + pre-sale offer."

8. **Output to User Context — paste-ready (two blocks):**

   **Example of a 5/5 paste blocks (Aamir):**
   ```
   SECTION B — Project + audience:
   Project name: Junior PM Career Compass
   One-sentence outcome: I'm shipping a 5-week paid cohort + workbook for junior PMs at B2B SaaS who want to do real product strategy work, by Friday June 13, 2026.
   Target customer: Junior PMs 1-3 yrs in at B2B SaaS, $90-130K, frustrated with JIRA grooming. Persona: Aamir, 26.
   Ship date: Friday June 13, 2026
   First customer (named human): Priya Sharma (Datadog)

   SECTION D — Scope + price:
   Format: Live cohort + workbook PDF
   Price: $497
   V1 features (5): 5 live sessions, 40pg workbook, private Slack, Stripe checkout, end-of-cohort 1:1
   V2 Backlog (5+): recorded video library, AI tutor, certificate, alumni meetups, job board, peer feedback rounds
   Success metric: 8+ paying customers by June 13, 6+ show to Session 1
   ```

9. **Route forward.** Recommend: "Save both blocks to User Context, then run `/unstuck diagnose` to audit your readiness, OR skip to `/unstuck validate` if you want to RICE-score before committing."

**Push back triggers:** vague answers on any question, scope creep on V1 features, fake-urgency on ship date.

---

## Path 3 — Resurrection (~30 min)

For: "I have a half-finished project. Help me ship the version that's already 60% built."
Output: Re-scoped V1 from current state → seeds User Context Sections B + D + 30-day finishing plan.

**Run this sequence — ONE question at a time:**

1. **The project in one line.**

   **What we're capturing:** Name + one-sentence description of the abandoned project.

   "Name + one-sentence description. If multiple half-builds, pick ONE."

   **Example of a 5/5 answer:**
   > "Indie-Engineer Compass — a Notion-based career planning template for senior engineers thinking about going indie. Built about 60% in 2025, abandoned September."

2. **When did you last touch it?**

   **What we're checking:** Recency. >12 months = is this guilt or genuine project?

   **Example of a 5/5 honest answer:**
   > "Last commit: September 14, 2025. Eight months ago. Looked at the doc twice since."

   If >12 months, push back: is this still your project, or just guilt? Sometimes the right move is to formally kill it.

3. **Why did you stop?**

   **What we're diagnosing:** Resurrection works for some reasons, not others.

   - Scope ballooned → Resurrection works (cut scope)
   - Validation went sideways (no one wanted it) → Resurrection is wrong; run Decide Already
   - Life got in the way → Resurrection works
   - Boredom / shiny object → push back on whether the underlying project is still right
   - Waiting for [thing I never got] → identify the actual block

   **Example of a 5/5 honest answer:**
   > "Scope ballooned. Started as 'one Notion template', became 'template + course + community + AI tutor'. Got overwhelmed, stopped. Underlying idea is still good — just too big."

4. **What's currently done?**

   **What we're inventorying:** Every concrete thing that exists. Specific.

   **Example of a 5/5 inventory:**
   > "Notion template built (5 pages, 80% formatted). Landing page wireframe in Figma (not built). 30-min interview videos with 3 indie engineers (raw, unedited). Stripe account opened, no products. Email list of 47 (from my newsletter)."

5. **What's V1 from where it IS now?**

   **What we're scoping:** A finishable version in 30 days from current state. Ruthless cut.

   **Example of a 5/5 resurrected V1:**
   > 1. The Notion template (already 80% done — finish formatting + write the 5-page intro).
   > 2. Stripe payment link selling the template at $47.
   > 3. ONE landing page (Carrd, not Figma — pick what's faster).
   > 4. Email the 47 newsletter subs with the launch.
   > CUT FROM ORIGINAL: course, community, AI tutor, interview videos — all V2.

6. **New ship date.** 30 days from today, on a Friday.

   **Example of a 5/5:**
   > "Friday June 13, 2026."

7. **Output to User Context — paste-ready:**

   **Example of a 5/5 paste block (Indie-Engineer Compass):**
   ```
   SECTION B — Project + audience:
   Project name: Indie-Engineer Compass
   One-sentence outcome (re-scoped from CURRENT state): I'm shipping the Notion-template version of Indie-Engineer Compass to my existing newsletter audience, by Friday June 13, 2026.
   Target customer: Senior engineers in my newsletter list thinking about going indie
   Ship date: Friday June 13, 2026
   Status: RESURRECTION — 60% built, finishing V1 in 30 days

   SECTION D — Scope + price:
   Format: Notion template (digital download)
   Price: $47
   V1 features (3): finished Notion template, Carrd landing page, Stripe checkout
   V2 Backlog: course, community, AI tutor, interview videos
   Success metric: 20 paying customers from newsletter list by June 13
   ```

8. **Avoidance check.** Tell them straight: "Are you resurrecting because the project is genuinely good, or because you feel guilty about abandoning it? If guilt, the right move is to formally kill it and run Decide Already instead. Sunk cost is not a reason."

9. **Route forward.** "Save both blocks, then SKIP T01-T03 — you already have a project. Go to `/unstuck scope` to lock the resurrected V1, then `/unstuck sprint` to map the remaining work."

**Push back triggers:** guilt-driven resurrection, "I'll redo X while I'm at it" (scope creep on a resurrection is doom).

---

## Path 4 — Audience-First Product (~45 min)

For: "I have an audience but no product."
Output: Product anchored to existing audience → seeds User Context Sections B + D + named first customers.

**Run this sequence — ONE question at a time:**

1. **The audience.**

   **What we're describing:** Where, how many, how long, current monetization.

   Ask:
   - Where are they? (Newsletter / Twitter / Podcast / YouTube / IG / Discord / Substack / multiple)
   - How many active people? (open rate × subs / engaged followers)
   - How long? (start date + last-90-days growth)
   - What do they pay you for today? ($0 / sponsorships / paid posts)

   **Example of a 5/5 audience description:**
   > "Newsletter: 4,200 subs, 38% open rate (~1,600 active readers). Started Jan 2024, growing ~80/week last 90 days. Currently making $1,500/mo from sponsorships, $0 from products."

2. **What do they ask you for?**

   **What we're mining:** Verbatim DMs / replies / comments. These quotes ARE the product.

   **Example of a 5/5 quote inventory:**
   > "Last 60 days I got 14 DMs asking 'do you have a course on getting from senior to staff PM?' and 9 replies asking 'where can I learn this framework you used in last week's post?' Same theme: senior→staff career framework."

3. **What do they pay others to solve?**

   **What we're anchoring:** Pricing reference. Who else are they buying from?

   **Example of a 5/5:**
   > "They buy Lenny's Reforge programs ($1,800-2,800), Pragmatic Engineer career guides ($150-300), and Will Larson's Staff Engineer book ($35). The Reforge price is the anchor for a serious cohort."

4. **My unfair advantage.**

   **What we're surfacing:** Why ME for this audience. Specific, not generic.

   "Why YOU? Be specific. 'I have experience' doesn't count."

   **Example of a 5/5 advantage:**
   > "I've personally navigated senior→staff at 2 different SaaS companies in the last 4 years. Documented it publicly in my newsletter. 6 of my readers DM'd me after their own senior→staff promo and credited my frameworks. I'm the only PM-track writer in this audience who's actually staff and writing about it."

   If they can't name an advantage, the audience is BORROWED (they like them but won't pay) — different play needed.

5. **Product-from-audience pick.**

   **What we're choosing:** Format + promise + price, anchored to Q2 + Q3 + Q4.

   - Format: course / template kit / community / consulting / paid newsletter tier / cohort / digital download
   - Promise: one-sentence outcome (uses words from Q2)
   - Price: anchored to Q3

   **Example of a 5/5 pick:**
   > "Format: 5-week cohort (live). Promise: 'Get the senior→staff promo within 12 months using the public-PM-portfolio framework.' Price: $1,200 (between Reforge and the eBook, anchored at 'serious but cheaper than incumbents')."

6. **First 10 customers.**

   **What we're naming:** 10 named humans from the audience already in DMs/comments.

   "Name 10 specific humans who'd buy this Day 1."

   **Example of a 5/5 list:**
   > "1. Priya (DM'd 3 weeks ago). 2. Marcus (commented on last 4 posts). 3. Jen (asked about staff prep in May). 4-7. The four people who DM'd 'do you have a course'. 8-10. My three closest newsletter friends, all senior PMs at SaaS, all moved roles in 2025."

   If can't name 10, the pick is wrong — go back to Q2 and re-read DMs.

7. **Ship date.** 30 days from today, on a Friday.

8. **Output to User Context — paste-ready:**

   **Example of a 5/5 paste block:**
   ```
   SECTION B — Project + audience:
   Project name: Senior→Staff Compass (working title)
   One-sentence outcome (uses words from their DMs): I'm shipping a 5-week cohort that helps senior PMs at SaaS get the staff promo within 12 months, by Friday June 13, 2026.
   Target customer: Senior PMs on my newsletter who DM'd / commented about senior→staff career moves
   Ship date: Friday June 13, 2026
   First 10 customers (named): Priya, Marcus, Jen, [the 4 DMs], [3 newsletter friends]

   SECTION D — Scope + price:
   Format: Live 5-week cohort
   Price: $1,200 (anchored to Reforge but cheaper)
   V1 features (4): 5 live sessions, public-portfolio workbook, peer feedback round, end-of-cohort 1:1
   V2 Backlog: recorded library, certificate, alumni community
   Success metric: 10 paying customers from existing list by June 13
   ```

9. **Route forward.** "Save both blocks, SKIP `/unstuck validate` — your DMs are validation. Go to `/unstuck scope` to lock V1, then `/unstuck launch` to plan the launch sequence (uses your audience's exact language from Q2)."

**Push back triggers:** borrowed audience (engaged but never bought anything), wishful-thinking on the first-10 list, product NOT anchored to actual DM quotes.

---

## Path 5 — Launch-Only Plan (~30 min + 14-day exec)

For: "I built it but never launched. Skip the build, jump to launch."
Output: 14-day launch plan → seeds User Context Sections B + D (read-only — product complete).

**Run this sequence — ONE question at a time:**

1. **The product.**

   **What we're capturing:** Name + one-sentence description + current location.

   "Name + one-sentence description. Where does it live right now?"

   **Example of a 5/5 answer:**
   > "Junior PM Toolkit — a 60-page workbook PDF + 20 Notion templates for junior PMs starting at SaaS. Lives on Google Drive (Drive + Stripe link, never publicized)."

2. **When did you finish it?**

   **What we're checking:** Staleness. >6 months = does it need a refresh?

3. **Why haven't you launched?**

   **What we're diagnosing:** The primary block.

   Common blocks:
   - Perfectionism — "it's not quite right yet" (it never will be)
   - No audience — "no one to launch to"
   - No copy — "I don't know how to describe it"
   - Fear — "what if no one buys"
   - No infrastructure — "I haven't set up Stripe / email / landing"

   Pick ONE as PRIMARY.

   **Example of a 5/5 honest answer:**
   > "Primary: fear. I've had it done for 5 months. Stripe is live, Carrd is live, I have an email list of 800. I'm just terrified of pressing the 'announce' button because of the rejection signal if nobody buys."

4. **Launch date.**

   **What we're locking:** A specific Friday 14 days from today (shorter than the 30-day default because product exists).

5. **Who are you launching to?**

   **What we're naming:** 5 specific humans for personal-text on launch day.

   **Example of a 5/5 list:**
   > "1. Aamir (knows about this since draft, asked when it ships). 2. Priya (newsletter sub, replied to my last post). 3-5. Three closest friends in the PM industry who've cheered the project privately."

6. **Output to User Context — paste-ready:**

   **Example of a 5/5 paste block:**
   ```
   SECTION B — Project + audience:
   Project name: Junior PM Toolkit
   One-sentence outcome: I'm publicly launching the Junior PM Toolkit to my email list, by Friday May 29, 2026.
   Target customer: Junior PMs 1-3 yrs in at SaaS, on my email list
   Launch date: Friday May 29, 2026 (14 days)
   First 5 customers (named): Aamir, Priya, [3 friends]
   Status: LAUNCH-ONLY — product complete, building path to customer

   SECTION D — Scope + price (already locked, no rebuild):
   Format: PDF workbook + Notion templates (digital download)
   Price: $47
   V1 features (already shipped): 60pg workbook, 20 Notion templates, Stripe checkout, Carrd landing
   V2 Backlog: course version, premium tier with 1:1, alumni community
   Success metric: First 10 paying customers within 14 days
   ```

7. **14-day launch plan:**
- Day 1-3: T11 Landing Page Frame (will draft from product description in Q1)
- Day 4-6: T12 5-Email Launch (reuses hero copy from T11)
- Day 7-8: T13 Tech Stack (payment + delivery + email tool)
- Day 9-12: Personal outreach to the 5 named humans + 5 more from network
- Day 13: Final QA, schedule emails
- Day 14: SHIP

8. **Avoidance check.** "Is the product genuinely done, or are you telling yourself it's done to skip the hard parts? If 'done-ish with caveats,' run Resurrection instead — finish V1 properly before launching."

9. **Route forward.** "Save both blocks, SKIP `/unstuck diagnose` through `/unstuck sprint` entirely (no build phase). Go to `/unstuck launch` for the email sequence and landing page work."

**Push back triggers:** perfectionism disguised as "not quite ready," fake done-ness, no named first 5.

---

## Closing — Every Path Ends With This

Whichever path ran, end the conversation with:

1. **Confirm the User Context blocks they need to save** (paste-ready format above)
2. **The exact next module** they should run (`/unstuck diagnose` / `/unstuck scope` / `/unstuck launch` etc.)
3. **One sentence on what they're committing to** — read it back to them in their own words

> Example: "OK Aamir — you're shipping Junior PM Career Compass to junior PMs at B2B SaaS on a 30-day clock. Save Section B + D to your User Context, re-upload to your Project, then run `/unstuck diagnose` to audit your readiness. Built with the Unstuck Method — unstuckwithmolly.com"

---

## When NOT to run Discovery

If the user's first message indicates ANY of the following, do NOT run Discovery — route directly:

- They quote a template name (T01, T05, "Scope Guillotine", etc.) → assume context exists, route to that template's module
- They describe an active sprint in progress → route to `/unstuck sprint` or `/unstuck audit`
- They quote their User Context content back to you → context exists, skip Discovery
- They explicitly ask for a module ("I need to validate my idea") → route to that module

Discovery is the **empty-context** intake. If context is partially or fully present, use the existing modules.
