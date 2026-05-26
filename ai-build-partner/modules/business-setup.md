<required_reading>
**Read these reference files NOW:**
1. references/core.md
</required_reading>

<process>

**Step 0 — Check User Context first**

Read `.unstuck/context.md`:
- **Section A** (role, state/location if mentioned)
- **Section B.1** (product type, price)
- **Section G** (revenue data if exists)

---

**Opening (output verbatim):**

> "Business setup. The structural decisions that protect you and keep the IRS happy.
>
> Most side-project shippers overthink this. If you're selling digital products under $50K/year, the answer is almost always: sole proprietor now, LLC at $1K revenue, accountant at $5K. I'll walk you through the specifics.
>
> **Not legal or tax advice** — I'm a framework for thinking through the decisions. Consult a CPA for tax specifics in your state.
>
> Ready?"

---

**Step 1 — Where are you on the revenue ladder?**

> "Which best describes you right now?"

| Stage | Revenue | What you need |
|-------|---------|---------------|
| **Pre-launch** | $0 | Nothing. You're already a sole proprietor by default. Ship first. |
| **First sales** | $1 - $999 | Separate bank account. That's it. |
| **Real revenue** | $1K - $5K | LLC formation + EIN |
| **Growing** | $5K - $50K | Accountant + quarterly tax estimates |
| **Scaling** | $50K+ | S-Corp election consideration + bookkeeper |

> "Don't set up infrastructure you don't need yet. An LLC before your first sale is procrastination wearing a business suit."

Route to the relevant section based on their answer.

→ Next: **Step 2** — entity decision (if $1K+)

---

**Step 2 — The entity decision**

**If pre-launch or < $1K:**

> "You're a sole proprietor. That's the default — no paperwork needed. You report side income on Schedule C of your personal tax return. The only action item: open a separate checking account for business transactions. Don't commingle funds.
>
> Come back when you cross $1K. That's when liability protection matters."

Skip to Step 5 (checklist).

**If $1K+:**

> "Time for an LLC. Here's why and how:"

**Why LLC at $1K:**
- Separates personal assets from business liability (if someone sues your business, they can't take your house)
- Costs $50-500 depending on state (one-time filing fee + annual report)
- Takes 1-2 weeks to process
- You can still report taxes on your personal return (single-member LLC = pass-through by default)

**The state question:**

> "Which state do you live in?"

Based on answer:
- **Most states:** File in your home state. Simple. Costs $50-200.
- **California:** $800/year minimum franchise tax. Still worth it at $1K+ revenue — the liability protection matters more than the fee.
- **Wyoming / Delaware:** Popular for out-of-state filing but usually NOT worth it for solo digital product businesses. You'd still need to register as a foreign LLC in your home state = double fees. File in your home state.

**How to file:**
1. Go to your state's Secretary of State website
2. File "Articles of Organization" for a single-member LLC
3. Pick a name (your product name or your name + "LLC")
4. Get an EIN from the IRS: irs.gov/ein — free, takes 5 minutes online
5. Open a business checking account with the EIN

> "Total cost: filing fee ($50-500) + 30 minutes. Total ongoing cost: annual report fee ($0-100/year depending on state). That's it."

→ Next: **Step 3** — taxes and the accountant trigger

---

**Step 3 — Tax awareness (not tax advice)**

> "Three things to know about side-project income and taxes:"

**1. You owe taxes on profit, not revenue.**
Revenue minus expenses = profit. Expenses include: hosting, tools, email platform, domain, software subscriptions, home office (percentage of rent/mortgage), equipment. Track these.

**2. Self-employment tax is real.**
As a sole proprietor or single-member LLC, you pay 15.3% self-employment tax on profit (Social Security + Medicare) on top of your regular income tax. This surprises people.

**3. Quarterly estimated taxes kick in at ~$1K/year owed.**
If you expect to owe $1,000+ in taxes from side income, the IRS wants quarterly payments (April 15, June 15, Sept 15, Jan 15). Miss these and you pay penalties.

**The $5K accountant trigger:**

> "At $5K cumulative revenue, pay for one hour with a CPA. Not a tax prep service — a CPA who works with small business owners. The one-hour conversation covers:
> - Your specific quarterly estimate amounts
> - Which expenses to track (and how)
> - Whether S-Corp election makes sense (usually not until $40-60K/year profit)
> - State-specific sales tax obligations
> - Health insurance deduction if you eventually quit
>
> Cost: $150-300 for the consultation. ROI: thousands in avoided mistakes."

→ Next: **Step 4** — co-founder and other decisions

---

**Step 4 — Should you get a co-founder?**

> "Short answer for 90% of side-project shippers: **no.**"

**When a co-founder makes sense:**
- You need a fundamentally different skill (you're a PM who can't code, and the product IS code)
- You've validated demand AND built V1 AND the bottleneck is a skill you can't hire for
- You've known the person professionally for 1+ years

**When a co-founder does NOT make sense (most cases):**
- "I want accountability" → That's a build partner or community, not equity
- "I want help with marketing" → That's a contractor at $50-100/hr, not 50% of your company
- "I'm lonely building alone" → That's natural. Join a community. Don't give away equity for companionship.
- "They have good ideas" → Ideas are free. Execution is expensive. Only give equity for execution you can't buy.

**If they genuinely need a co-founder:**
- **Equity split:** Do the work BEFORE the conversation. Use the Slicing Pie framework (Mike Moyer) — equity based on actual contribution, not promises.
- **Vesting:** 4-year vesting with 1-year cliff. Non-negotiable. If they leave in month 3, they don't keep 50% of your business.
- **Operating agreement:** Required. Covers: decision-making (who has final say), what happens if one person wants out, IP ownership, non-compete.
- **Talk to a lawyer:** A co-founder agreement is the ONE legal document worth paying for. $500-1500 for a lawyer to draft it. Cheaper than the lawsuit when it falls apart.

**The contractor alternative:**

> "For most side-project shippers, the answer isn't a co-founder — it's a contractor for 5-10 hours/month on the skill you're missing. Designers on Fiverr ($200-500 for a landing page). Dev help on Upwork ($50-100/hr for specific tasks). Marketing VA ($15-25/hr for content scheduling). You keep 100% equity and get the help you need."

→ Next: **Step 5** — the checklist

---

**Step 5 — Business infrastructure checklist (output as artifact)**

```
BUSINESS INFRASTRUCTURE CHECKLIST — [Date]
Product: [name] · Price: $[X] · Current revenue: $[Y]

PRE-LAUNCH (do now):
- [ ] Separate bank account for business transactions
- [ ] Privacy policy live on site (/privacy)
- [ ] Terms of service live on site (/terms)
- [ ] Refund policy on sales page
- [ ] Basic expense tracking started (spreadsheet or QuickBooks)

AT $1K CUMULATIVE REVENUE:
- [ ] LLC formed in [home state]
- [ ] EIN obtained (irs.gov/ein, free, 5 min)
- [ ] Business bank account opened with EIN
- [ ] Update payment processor with LLC info

AT $5K CUMULATIVE REVENUE:
- [ ] One-hour CPA consultation ($150-300)
- [ ] Quarterly tax estimates set up
- [ ] Expense categories formalized
- [ ] Sales tax nexus checked (state-specific)

AT $50K/YEAR PROFIT:
- [ ] S-Corp election conversation with CPA
- [ ] Bookkeeper ($100-300/month)
- [ ] Professional liability insurance (if service business)
- [ ] Trademark filing ($250-350, if brand matters)

CO-FOUNDER DECISION:
Current verdict: [SOLO / CONTRACTOR / CO-FOUNDER]
Rationale: [one sentence]

⚠️ Not legal or tax advice. Consult a CPA for your state.

Built with the Unstuck Method — unstuckwithmolly.com
```

Save to `.unstuck/business-setup-YYYY-MM-DD.md`.

---

**Step 6 — Exit and route**

> "Business infrastructure mapped. The pattern: ship first, structure second, scale third. Don't build infrastructure for a business that doesn't exist yet.
>
> **Next actions based on your stage:**
> - Pre-launch → ship. Come back at $1K.
> - $1K+ → file that LLC this week. 30 minutes.
> - $5K+ → book that CPA appointment this week. One hour.
>
> **Related commands:**
> - `/unstuck compliance-checklist` — privacy policy, terms, refund policy templates
> - `/unstuck runway` — financial calculator (when can I quit?)
> - `/unstuck day-job-decision` — the full quit decision framework"

</process>

<success_criteria>
This module is complete when:
- [ ] Revenue stage identified
- [ ] Entity decision made (sole prop / LLC / S-Corp) with timeline
- [ ] Tax awareness communicated (self-employment tax, quarterly estimates, $5K CPA trigger)
- [ ] Co-founder question answered with clear verdict
- [ ] Business infrastructure checklist generated with revenue-triggered milestones
- [ ] Artifact saved
- [ ] Next actions specific to their stage
</success_criteria>
