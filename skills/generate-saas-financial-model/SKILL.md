---
name: generate-saas-financial-model
description: Generate multi-tab Excel financial models for SaaS businesses with editable assumptions driving live formulas across revenue, COGS, OpEx, P&L, and unit economics. Use when founder needs financial projections, mentions fundraising, investor deck, cash runway, unit economics, pricing modeling, or asks "how long will my money last," "what should I charge," "how do I model my SaaS finances," "I need a financial model for investors," "revenue projections," "burn rate," or any request to build or evaluate a SaaS financial plan.
---

# Generate SaaS Financial Model

## What This Skill Does

Takes a SaaS business at any stage — pre-revenue, early traction, or growth — and produces a complete financial model specification with six interconnected sections. Every calculated output traces back to editable assumptions, so the founder can model different scenarios instantly. The output is structured to generate an Excel file with live formulas, or to serve as a detailed financial plan for investor conversations.

This follows the Blue Cell Assumption Architecture: all editable inputs are clearly separated from calculated outputs, so changing one assumption ripples through every tab.

## Phase 1: Business & Financial Inputs

Ask these questions one at a time. Wait for the user's answer before moving to the next.

**If the user is stuck on any question:** Don't just repeat it. Help them think through it — suggest industry benchmarks, offer ranges based on their stage, or reframe the question. The goal is a real number, not a placeholder.

**If the user truly can't answer one** (e.g., no churn data because they're pre-revenue), note it with an industry benchmark default and flag it in Section 7.

### The 8 Questions

**Q1: "What does your SaaS product do, who pays for it, and what's your current stage?"**
Pre-revenue, early revenue (how much MRR?), or growth stage? B2B or B2C? How many customers today? This sets the baseline for everything.

*If stuck, ask:* "How many paying customers do you have right now, and how much total monthly revenue are they generating?"

**Q2: "What are your pricing tiers and monthly prices?"**
List every tier: name, monthly price, what's included. If you have annual pricing, what's the discount? If you're still deciding on pricing, give me your best guess and we'll model scenarios.

*If stuck, ask:* "What are 2-3 competitors charging? That's usually a good starting anchor. We can adjust from there."

**Q3: "How many customers do you expect to add each month for the next 12-18 months?"**
Be honest, not optimistic. If you have 2 customers today, saying "50 per month" needs justification. What's your acquisition channel and what conversion rates are you seeing?

*If stuck, ask:* "How are customers finding you right now? Inbound, outbound, referrals? How many conversations per month turn into customers?"

**Q4: "What percentage of customers do you expect at each tier, and how does this change over time?"**
Early on, most customers land on the cheapest tier. Over time, the mix usually shifts upward. What's your assumption?

*If stuck, ask:* "Most SaaS companies see 60-70% on the entry tier in year one, shifting to 40-50% by year two as the product matures. Does that feel right for your business?"

**Q5: "What's your monthly churn rate?"**
Percentage of customers who cancel each month. If you don't know yet, we'll use industry benchmarks.

*If stuck:* "B2B SaaS averages 3-7% monthly churn for SMB, 1-2% for mid-market, under 1% for enterprise. Where does your target customer sit?"

**Q6: "What are your variable costs per customer?"**
Costs that scale with each customer added. Common ones: cloud hosting/infrastructure, third-party API calls, email/SMS sending, payment processing fees (usually 2.9% + $0.30), customer support time.

*If stuck, ask:* "Let's go line by line. What do you pay for hosting per customer? Any API costs? Payment processing? Email/SMS? Support tools?"

**Q7: "What are your fixed monthly operating expenses?"**
Costs that don't change with customer count. Break into four categories:
- **Engineering/Product:** Salaries, contractors, tools
- **Infrastructure:** Monitoring, CI/CD, dev tools
- **GTM/Sales:** Marketing spend, sales tools, ads
- **Ops/Legal/Admin:** Accounting, legal, insurance, office

*If stuck, ask:* "Start with the big ones: engineering salaries or contractor costs, then marketing budget, then everything else."

**Q8: "How much cash do you have, and what are your fundraising plans?"**
Starting cash balance for the model. If you're planning to raise — how much, what instrument (SAFE, priced round), and when?

*If stuck, ask:* "How much is in the business bank account today? And are you planning to raise money in the next 6-12 months?"

## Phase 2: Generate the Financial Model

After gathering all 8 answers, generate a structured financial model specification with these 8 sections. Use the user's answers as inputs — calculate, don't just repeat back.

### Section 1: Assumptions Summary

Consolidate all editable inputs in one place. These are the "blue cells" — every other number in the model derives from these.

**Pricing Assumptions:**
- Tier names, monthly prices, annual discount %
- Add-on revenue % (if applicable)

**Growth Assumptions:**
- Starting customer count
- Monthly new customer additions (by month)
- Tier mix evolution (% at each tier by quarter)
- Monthly churn rate

**COGS Assumptions (per customer/month):**
- Each variable cost line item with dollar amount

**OpEx Assumptions (fixed monthly):**
- Each category with line items and amounts

**Cash Assumptions:**
- Starting cash balance
- Planned fundraise amount and timing

### Section 2: Revenue Model (Monthly, 18 months)

For each month, calculate:
- Customer count by tier (new adds × tier mix - churn)
- Total active customers
- Blended ARPU (weighted average across tiers)
- Subscription MRR (customers × tier prices)
- Add-on revenue (% of subscription MRR)
- Total MRR
- ARR run rate (MRR × 12)
- MoM MRR growth %
- Cumulative revenue

### Section 3: COGS & Gross Margin

For each month, calculate:
- Each per-customer cost × total customers
- Total COGS
- Gross profit (Revenue - COGS)
- Gross margin % (target: 70-85% for SaaS)

Flag if gross margin falls below 65% — this is a red flag for investors.

### Section 4: Operating Expenses

For each month, show:
- Engineering/Product total
- Infrastructure total
- GTM/Sales total
- Ops/Legal/Admin total
- Total OpEx
- OpEx as % of revenue

### Section 5: P&L Summary

Monthly waterfall:
- Total Revenue
- (-) COGS
- = Gross Profit (and margin %)
- (-) Total OpEx
- = EBITDA (and margin %)
- Starting Cash
- (+/-) Net Cash Flow
- = Ending Cash Balance
- **Runway (months)** = Cash Balance ÷ Monthly Burn Rate

Highlight the month where cash hits zero if no fundraise occurs.

### Section 6: Unit Economics

Calculate and benchmark:
- **ARPU** (Average Revenue Per User/month)
- **LTV** (ARPU × Gross Margin % × (1 / Monthly Churn Rate))
- **CAC** (Monthly Sales & Marketing Spend ÷ New Customers)
- **LTV:CAC Ratio** (target: 3:1 or higher)
- **CAC Payback Period** (CAC ÷ (ARPU × Gross Margin %)) in months
- **Monthly burn rate**
- **Revenue per employee** (if headcount known)

Include industry benchmarks:
| Metric | Your Model | Healthy SaaS | Red Flag |
|--------|-----------|-------------|----------|
| Gross Margin | X% | 70-85% | <65% |
| LTV:CAC | X:1 | 3:1+ | <2:1 |
| CAC Payback | X months | <18 months | >24 months |
| Monthly Churn | X% | <5% (SMB), <2% (MM) | >8% |

### Section 7: Scenario Analysis

Model three scenarios using the same structure:
- **Conservative:** 50% of projected growth, 1.5x churn assumption
- **Base:** User's stated assumptions
- **Optimistic:** 150% of projected growth, 0.75x churn assumption

For each scenario, show: Month-18 ARR, Runway, LTV:CAC, Cash position.

### Section 8: Model Gaps & Recommendations

Audit the model and flag:
- **Unrealistic assumptions:** Growth rates that require channels not yet built, churn rates below industry floor, etc.
- **Missing data:** Any question the user couldn't answer — show the default used and recommend how to get real data
- **Investor concerns:** Metrics that would raise red flags in due diligence
- **Scenario risks:** What breaks first in the conservative case?
- **Pricing recommendations:** Is there room to raise prices? Is the tier structure leaving money on the table?
- **Pilot pricing note:** If pre-revenue with design partners, recommend 90-day free pilot or founding customer discount (60-70% off) with locked rate

## Rules

- **Every output number must trace to an assumption.** If you can't show which blue cell drives a calculation, the model is broken.
- **Use realistic industry benchmarks.** Don't let founders model 0% churn, 50% MoM growth, or 95% gross margins without flagging it.
- **Always calculate runway.** This is the most important number for pre-revenue and early-stage companies.
- **Separate inputs from outputs.** The user should be able to change any assumption and understand how it ripples through the model.
- **Don't fabricate market data.** If you don't know a benchmark, say so and suggest where to find it.
- **Flag pilot pricing.** Design partners and first customers should not pay full price. Model the delayed revenue.
- **Use explicit cell references, not offset calculations.** When describing formulas, reference specific rows/cells. Non-linear layouts break index-based offsets.
- **Round appropriately.** Revenue to dollars, percentages to one decimal, ratios to one decimal.
- **18-month default timeframe.** Extend to 24 or 36 months only if the user asks or is modeling a fundraise beyond 18 months.

## What This Skill Does NOT Do

- Generate an actual Excel file (it produces the specification — use openpyxl or Google Sheets to build it)
- Replace a CFO or financial advisor for fundraising
- Provide tax advice or legal entity recommendations
- Build a cap table or model dilution from fundraising
- Create investor pitch decks or slide formatting
- Model non-SaaS business models (marketplace, e-commerce, services)
