<required_reading>
**Read these reference files NOW:**
1. references/core.md
</required_reading>

<process>

**Step 0 — Check User Context first (Mode 1 behavior)**

Before the Opening, scan the user's uploaded User Context file:
- Read **Section B** (product type + audience), **Section D.2** (Scope — pulls product type), **Section D.4** (Sprint — current build state)
- If Sections B + D.2 are populated, infer Q1 (product type), Q3 (audience size at launch), Q8 (scale-to-$10K shape) from context. Always ASK Q2 (technical level), Q4 (budget), Q5 (existing tools — changes), Q6 (compliance), Q7 (integration preference).
- If User Context is empty, run the full 8-question intake.

Don't ask what you can read. Draft what you can infer.

---

**Opening (Mode 2 — empty context — output verbatim):**

> "Time to lock your stack. You're between scope-locked (you know what you're building) and build-day (you need to wire payment + ESP + hosting + landing-page + analytics + DB + auth + forms + domain). Eight questions. Twelve minutes. You'll walk away with: a 9-category stack manifest with 1-2 specific picks per category, monthly cost estimate at launch, setup-order recommendation, migration paths when each pick hits its ceiling, and Claude/MCP-friendly priorities called out where vendors have first-class Claude integration.
>
> **The bias I'm bringing:** I prefer vendors that are Claude-friendly (MCP servers or clean APIs) because future Kit-stack-wire skills will automate the setup. If you have a strong preference for a different vendor I'll respect it — just tell me.
>
> **One ground rule:** for any question, three ways out — `hint` / `guide me` / `draft it`.
>
> Ready?"

**Opening (Mode 1 — context populated):**

> "Reading your User Context. I see your scope and product type. I need 5 things: your technical level, your tooling budget, what tools you already have set up, any compliance constraints, and your integration preference. Then I'll draft the manifest."

---

**Section 1: Product type (Q1)**

**What we're capturing:** What you're shipping — different product shapes need different stacks.

"What's the product type? Pick one: SaaS / Digital download (PDF, ebook, kit) / Course / Newsletter / Community / Service / Physical."

**Example of a 5/5 answer:**
> "Digital download — a $79 ebook + Notion template bundle. One-time purchase, no subscription, no login required after delivery."

Each type has a default stack shape:
- **SaaS** → Stripe + Resend + Supabase + Vercel + PostHog + Clerk-or-Supabase-Auth + Tally + Cloudflare
- **Digital download** → Stripe-or-LemonSqueezy + Resend + Vercel/Carrd + PostHog + (no DB, no auth needed) + Tally + Cloudflare
- **Course** → LemonSqueezy-or-Stripe + ConvertKit-or-Resend + Vercel-or-Teachable-host + (Searchie or Vimeo for video) + Discord/Slack for community
- **Newsletter** → Substack-or-Beehiiv (no separate stack needed; the platform IS the stack) OR Resend + custom site for "newsletter-first SaaS" shape
- **Community** → Skool-or-Circle-or-Discord + Stripe-or-the-platform's-native-payments
- **Service** → Stripe-or-Tally-Pro + Cal.com-or-SavvyCal + Notion-or-ClickUp for client tracking
- **Physical** → Shopify (no contest at this scale) — outside scope of this skill

Push back if they pick "SaaS + digital download + course" all-at-once. Pick the V1 shape. Add complexity later.

---

**Section 2: Technical level (Q2)**

**What we're capturing:** What you'll actually wire yourself vs. delegate.

"Pick one: I code yourself / I use no-code tools / I hire devs / I do hybrid (code some, no-code some)."

**Example of a 5/5 answer:**
> "Hybrid. I write Next.js + Tailwind for the marketing site (4 years React experience). I no-code Stripe + Resend wiring. I do NOT touch DB schema design — I use Supabase's UI and hire a contractor when I need migrations."

Push back if "I code" is theoretical. "I built tutorials" is not the same as "I shipped a production app." Ask: "What's the most recent thing you wired end-to-end?"

---

**Section 3: Audience size at launch (Q3)**

**What we're capturing:** The volume your stack needs to handle on day 1. Determines free-tier vs. paid-tier picks.

"How many people are on your launch list / target traffic at Day 1? Under 100, 100-1k, or 1k+?"

**Example of a 5/5 answer:**
> "Launch list ~280 (newsletter subs + LinkedIn connections who said they'd buy). Expected Day 1 traffic ~600 unique visits across the launch. So 100-1k bucket."

Push back if they say "thousands" without naming where the audience lives. Hopes aren't traffic. Use real-audience-asset numbers.

---

**Section 4: Tooling budget (Q4)**

**What we're capturing:** What you'll pay monthly for the whole stack.

"Monthly tooling budget? Free-tier-only / under $50/mo / under $200/mo / $500+/mo. Real budget, not aspirational."

**Example of a 5/5 answer:**
> "Under $50/mo. I want everything on free tier or near-free at launch volume. I'll upgrade when something hits its ceiling."

Push back if they go "free-tier only" with SaaS as Q1. Free-tier SaaS hits ceilings at 100-500 users; you'll be paying within month 2. Budget for that.

**Cost calibration cheat:**
- $0 free-tier — works for V1 of digital downloads, newsletters, simple services. NOT for SaaS at scale.
- Under $50/mo — covers ~all V1 stacks at <1k users. Stripe (free) + Resend ($20) + Vercel (free hobby) + PostHog (free tier) + Supabase (free).
- Under $200/mo — covers most V1 + V1.1 stacks. Adds Resend paid + Supabase Pro + PostHog paid analytics.
- $500+/mo — V2 / scale tier. Adds dedicated infra, paid auth (Clerk), heavier analytics.

---

**Section 5: What you already have (Q5)**

**What we're capturing:** Existing accounts, deployed projects, paid subscriptions.

"Multi-select: which of these do you already have set up?

Payment: Stripe / LemonSqueezy / Paddle / Gumroad / Paypal-Business
ESP: Resend / ConvertKit / Mailchimp / Loops / GHL / Kit / Substack / Beehiiv
Hosting: Vercel / Netlify / Cloudflare-Pages / Render / Railway
Landing: Custom-Next/React / Framer / Webflow / Squarespace / Carrd / WordPress
Analytics: PostHog / Plausible / GA / Fathom / Mixpanel
DB: Supabase / Neon / Turso / PlanetScale / Firebase / Postgres-self-hosted
Auth: Supabase-Auth / Clerk / Auth0 / Better-Auth
Forms: Tally / Typeform / Google-Forms / Jotform
Domain: Cloudflare / Vercel-domains / Namecheap / GoDaddy / Other

Also note any I missed."

**Example of a 5/5 answer:**
> "Have: Stripe (Standard), Resend, Vercel, Cloudflare (domain + DNS), Supabase (one project, dormant), Tally (Pro), PostHog (free tier). Don't have: any course platform, auth service, video host."

Push back if they say "I have all of those." Almost nobody actually has all 9 wired AND working. Ask which are wired vs. signed up.

---

**Section 6: Privacy / compliance (Q6)**

**What we're capturing:** What constraints narrow your vendor choices.

"Any compliance constraints? None / GDPR-only (EU customers) / HIPAA (health data) / SOC2 (enterprise sales) / FERPA (education) / other."

**Example of a 5/5 answer:**
> "GDPR-only. I'll have EU customers from day 1 (mailing list has 23% EU). No HIPAA / SOC2 — consumer-facing digital product."

Push back if they say "no constraints" for a SaaS that touches B2B. Even if you're not selling to enterprises, your customers may be. SOC2 readiness matters by Year 2.

---

**Section 7: Integration preference (Q7)**

**What we're capturing:** How Claude-friendly your stack needs to be. Determines the bias on tied picks.

"Which integration preference: Claude/MCP-friendly first (you want the future Kit-stack-wire plugins to automate setup) / API-friendly is fine (clean REST APIs) / Web-UI only (you don't care about programmability)?"

**Example of a 5/5 answer:**
> "Claude/MCP-friendly first. I'm a heavy Claude Code user and would love to fire `/kit-stripe-init` later when those plugins ship."

If they pick Claude/MCP-friendly, the skill biases:
- Payment: Stripe (MCP-able) > LemonSqueezy (clean API) > Gumroad (no public API, locks out automation)
- ESP: Resend (clean API + MCP-able) > Loops > ConvertKit > Mailchimp (legacy API)
- DB: Supabase (existing MCP server) > Neon (good API) > Firebase (vendor-lock, no MCP)
- Hosting: Vercel (great API + MCP-able) > Cloudflare Pages > Netlify
- Forms: Tally (clean API + MCP-able) > Typeform (API but expensive) > Google Forms (basic)

If they pick Web-UI only, the skill biases toward Carrd / Squarespace / native-platform-builders even when those have worse APIs.

---

**Section 8: Scale-to-$10K shape (Q8)**

**What we're capturing:** What "successful" looks like. Determines whether DB / auth are needed.

"What does scale-to-$10K MRR look like? Pick the closest shape:
- Digital downloads (lots of one-time purchases)
- Cohort cohorts (3-4 cohorts/year, ~$500-2K each)
- Recurring SaaS ($X/mo subscriptions)
- Hourly services (consulting / coaching / done-for-you)
- Physical (products you ship)
- Hybrid (any combination)"

**Example of a 5/5 answer:**
> "Digital downloads + cohort cohorts hybrid. The $79 ebook is the front-end. Quarterly $500 cohorts are the upsell. $10K MRR = ~80 ebook sales/mo + 7 cohort seats/qtr (which is $1.2K/mo amortized). Total ~$7.5K/mo from one-time + $1.2K/mo from cohorts."

Push back on "I don't know yet" — pick the most likely shape based on the V1 product. You can change later, but the V1 stack should support V1's shape, not a hypothetical V3.

---

**Draft the manifest**

Once you have all 8 inputs, generate the stack manifest. Use this priority logic:

### Vendor selection — per category

For each of 9 categories, recommend 1-2 specific vendors. Use this decision tree:

```
1. Does Q5 already include something in this category?
   YES → recommend keeping it unless it directly conflicts with Q1 or Q7
   NO → continue
2. What does Q1 (product type) need by default?
3. What does Q7 (Claude/MCP / API / Web-UI) bias toward?
4. What does Q4 (budget) allow?
5. What does Q6 (compliance) require?
6. What does Q8 (scale shape) need over the next 90 days?
7. Output: 1 primary pick + 1 alternative + reasoning + monthly cost
```

### The 9 categories + opinionated defaults (calibrated to Q1=SaaS unless Q1 differs)

| Category | Claude-MCP pick | API-friendly pick | Web-UI pick | Notes |
|---|---|---|---|---|
| **Payment** | Stripe (MCP-able) | LemonSqueezy (clean API, EU MoR) | Gumroad (UI-driven, no API) | LemonSqueezy is the EU-MoR shortcut for GDPR + tax handling. Stripe wins if you're handling tax yourself. Gumroad only if Q2 = no-code AND Q1 = digital download. |
| **ESP** | Resend (clean API + MCP-able) | Loops, ConvertKit | Substack, Beehiiv | Resend for transactional + marketing-light. ConvertKit if you need ESP-as-CRM with tags/sequences. Substack/Beehiiv only if Q1 = newsletter. |
| **Hosting** | Vercel (great API, MCP-able) | Cloudflare Pages | Webflow, Framer | Vercel for Next.js / React. Cloudflare Pages for static or for full-stack with Workers. |
| **Landing page** | Custom Next.js/React | Framer (no MCP but exportable) | Carrd ($19/yr), Squarespace | Custom if Q2 = code. Framer if Q2 = no-code AND you want design control. Carrd for V1 single-page. |
| **Analytics** | PostHog (clean API, MCP-able) | Plausible (clean API, privacy-friendly EU) | GA (heavy, slow) | PostHog for product analytics (events, funnels, retention). Plausible if Q6 = GDPR + you only need page views. |
| **DB** | Supabase (MCP server EXISTS) | Neon, Turso | (no DB; static product) | Supabase wins unless you have strong reasons otherwise. Neon if you want serverless-Postgres without auth bundled. No DB at all if Q1 = digital download. |
| **Auth** | Supabase Auth (bundled with DB) | Clerk (clean API, Claude-friendly) | (no auth; download via secure-link) | Supabase Auth if you already have Supabase DB. Clerk if you need social-login + magic-link + better UX. Skip entirely if Q1 = digital download. |
| **Forms** | Tally (clean API, MCP-able) | Typeform (API but expensive) | Google Forms (basic) | Tally for V1. Typeform for conditional logic if your form has 10+ branching questions. |
| **Domain** | Cloudflare (great API, free DNS) | Vercel domains, Porkbun | Namecheap, GoDaddy | Cloudflare wins on price + speed + DNS API. If Q5 already has Vercel domains, keep that. |

### The total monthly cost at launch (Q3 volume)

Sum the picks at Q3 audience size:

| Category | Pick | Cost at Q3 volume |
|---|---|---|
| [...] | [...] | [$X/mo] |
| **Total** | | **$X/mo** |

Compare to Q4 budget. If over, propose 2-3 swaps (e.g., Resend → Loops, Vercel Pro → Cloudflare Pages, Supabase Pro → Supabase free tier with usage caps).

### Setup order recommendation (the "wire in this order" plan)

Don't wire alphabetically. Wire in dependency order:

1. **Domain first** — 24-48 hour DNS propagation; do it Day 11 of sprint
2. **Hosting** — your site needs somewhere to go before anything else
3. **Landing page** — at minimum, a one-page placeholder so the domain isn't dead
4. **ESP** — set up sender domain + first 4-email automation; takes hours to days for DKIM/SPF
5. **Analytics** — drop the snippet before traffic arrives
6. **Forms** — wire the lead-magnet form
7. **DB + Auth** (if applicable) — wire after the form, before payment
8. **Payment** — LAST. Most-broken. Wire after everything else works.

### Migration paths

For each pick, note when you'll outgrow it:

- "Resend → enterprise ESP when newsletter hits 50k subs" (Resend's pricing scales worse than Mailchimp at high volume but better at low)
- "Tally Pro → Typeform when you need branching with conditional show/hide on >5 questions"
- "Supabase free tier → Supabase Pro at >500MB DB or >2GB egress/mo"
- "Stripe → LemonSqueezy if you launch in EU and tax compliance becomes painful"

### Claude/MCP-friendly priorities callout

Explicitly list which vendors in the manifest have first-class Claude integration:

> **Already MCP-ready (use today):**
> - Supabase (existing MCP server — read/write to DB directly from Claude Code)
> - Notion (existing MCP server — read/update Notion docs from Claude)
>
> **MCP-able / planned:**
> - Stripe (clean API, likely MCP server coming)
> - Vercel (clean API, MCP-able)
> - Resend (clean API, MCP-able)
> - PostHog (clean API, MCP-able)
> - Tally (clean API, MCP-able)
>
> **No MCP / locked out:**
> - Gumroad (no public API)
> - Mailchimp legacy users (deprecated API)

### Future-plugin callout (if Q7 = Claude/MCP-friendly)

> **Future Kit-stack-wire skills (Run 6 Track C — not built yet):**
> - `/kit-stripe-init` — wires Stripe payment links + webhooks for your product
> - `/kit-resend-init` — sets up Resend domain, sender, first 4-email automation
> - `/kit-vercel-deploy` — deploys your landing-page repo with env vars + domain
> - `/kit-supabase-bootstrap` — spins up Supabase project with Kit-recommended schema
>
> These plugins don't exist yet. When they ship, your Claude/MCP-friendly stack will be wireable in minutes instead of hours. Picking that bias now is a forward-investment.

---

**Present the artifact**

Use template at `templates/pick-my-stack.md`. Save to User Context Section D.4.5 (sits between D.4 Sprint and D.5 Conversations — fires during the build phase).

**Chain to next module**

- If Q1 needs DB + Auth (SaaS) → recommend wiring sprint Day 11-12, chain to `/unstuck sprint` for the build-day breakdown
- If Q1 doesn't need DB + Auth (digital download) → wiring is faster; chain to T13 Tech Stack as a companion reference card + recommend the setup-order list above as the Day 11 actual checklist
- Always: pair with T14 Build Vault for saving your wiring docs (auth tokens, env vars, webhook URLs)

</process>

<success_criteria>
This module is complete when:
- [ ] All 8 inputs collected with specifics
- [ ] 9-category manifest filled with 1-2 picks each + reasoning + monthly cost
- [ ] Total monthly cost compared to Q4 budget (with swaps offered if over)
- [ ] Setup-order recommendation explicit (NOT alphabetical)
- [ ] Migration paths noted for each pick's ceiling
- [ ] Claude/MCP-friendly priorities called out where applicable
- [ ] Future-plugin callout shown if Q7 = Claude/MCP-friendly
- [ ] Artifact saved to User Context Section D.4.5
- [ ] Chain to `/unstuck sprint` or T13/T14 reference per Q1 branch
</success_criteria>

<anti_patterns>
**Things this module must NOT do:**

1. Generate text containing banned vocab (unlock, unleash, manifest, journey, transformation, level up, etc.)
2. Use the number 47 or the price $47 anywhere
3. Recommend vendors Molly doesn't actually use — examples and picks must trace to real Molly usage OR be labeled `[example]` per `feedback_never_fabricate_case_studies`
4. Recommend Gumroad if Q7 = Claude/MCP-friendly — Gumroad has no public API, locks out future automation (per `run-6-vendor-picks-notes.md`)
5. Recommend Telegram for anything (killed 2026-05-12)
6. Default to alphabetical setup order — payment goes LAST (most-broken thing)
7. Skip the budget cost-total math — Q4 budget cap is load-bearing; over-budget recommendations get rejected silently
8. Recommend SaaS Q1 + free-tier-only Q4 without flagging the ceiling — you'll be paying within month 2
9. Bundle V1 + V2 + V3 vendor picks in the V1 manifest — pick for now; flag the upgrade triggers explicitly
10. Suggest building everything from scratch when an off-the-shelf vendor handles 95% of the use case
</anti_patterns>
