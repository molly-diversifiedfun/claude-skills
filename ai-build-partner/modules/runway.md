<required_reading>
**Read these reference files NOW:**
1. references/core.md
</required_reading>

<process>

**Step 0 — Check User Context first**

Read `.unstuck/context.md`:
- **Section A** (day-job role, company stage — for salary estimate)
- **Section B.2** (hours/week — correlates with how much side-project time they have)
- **Section E.5** (price — for revenue projections)
- **Section G.3** (PMF score, if exists — for growth rate estimate)

---

**Opening (output verbatim):**

> "Runway calculator. Five numbers, ten minutes. You'll know exactly:
> 1. How many months of runway you have right now
> 2. What monthly revenue makes the side project self-sustaining
> 3. What monthly revenue lets you quit — safely
> 4. How many sales/month that means at your price
> 5. At current growth, when you'd hit that number
>
> **Disclaimer:** I'm a calculator, not a financial advisor. These numbers inform your thinking — they don't replace an accountant for tax planning or a financial advisor for investment decisions.
>
> Ready?"

---

**Step 1 — Monthly expenses (the burn)**

> "What's your total monthly household expenses? Include rent/mortgage, food, insurance, utilities, subscriptions, debt payments, childcare — everything that has to get paid every month. Round to the nearest $500. Don't include savings or investments — just the non-negotiable burn."

If they hesitate: "Check your bank statement for last month. Total outflows minus one-time purchases. Most people are within $500 of $4,000-$8,000."

Lock the number: **Monthly burn = $___**

→ Next: **Step 2** — current income + savings

---

**Step 2 — Current financial state**

Three numbers:

> "1. What's your current take-home pay per month? (After taxes, after 401K, the number that hits your bank account.)
> 2. How much liquid savings do you have? (Checking + savings + money market. NOT retirement accounts, NOT home equity, NOT stock you'd have to sell.)
> 3. Does your household have a second income? (Partner's take-home, if relevant. $0 if solo.)"

Lock: **Take-home = $___** | **Savings = $___** | **Partner income = $___**

→ Next: **Step 3** — calculate runway + targets

---

**Step 3 — The math (output as a table)**

Calculate and present:

```
RUNWAY CALCULATOR — [Date]

YOUR NUMBERS:
Monthly burn:           $[X]
Day-job take-home:      $[Y]
Partner income:         $[Z]
Liquid savings:         $[S]

RUNWAY (if you quit today with $0 side income):
Months of runway = Savings ÷ (Burn - Partner income)
                 = $[S] ÷ ($[X] - $[Z])
                 = [N] months

BREAK-EVEN (side project covers its own costs):
Side-project costs/mo:  $[estimate: hosting + tools + email platform]
Sales needed at $[price]: [costs ÷ price] = [N] sales/month
→ You're profitable after [N] sales/month. Most digital products hit this in month 1-2.

SELF-SUSTAINING (side income replaces day-job contribution):
Gap to fill = Burn - Partner income = $[X] - $[Z] = $[G]/month
Sales needed at $[price]: [G ÷ price] = [N] sales/month

THE QUIT NUMBER (safe to resign):
Quit when ALL THREE are true:
1. Side MRR ≥ $[G] (covers the gap) for 3+ consecutive months
2. Liquid savings ≥ $[G × 6] (6-month emergency fund post-quit)
3. Growth rate is flat or positive (not a launch spike declining)

At $[price], that's [G ÷ price] sales/month sustained for 3 months.
```

→ Next: **Step 4** — growth projection

---

**Step 4 — When do you hit the quit number?**

If they have sales data (from Phase 6-7):

> "How many sales did you make last month? And the month before?"

Calculate simple growth rate and project:

```
GROWTH PROJECTION:
Month 1 sales: [N1]
Month 2 sales: [N2]  
Growth rate: ([N2] - [N1]) / [N1] = [X]%

At [X]% monthly growth:
Month 3: [projected]
Month 6: [projected]
Month 12: [projected]

Quit number ([N] sales/mo) reached in: ~[M] months

⚠️ Growth rates rarely stay linear. This is a directional estimate,
not a prediction. Re-run this calculator quarterly.
```

If they don't have sales data yet:

> "You haven't launched yet — no projection possible. Come back after Phase 5 (first sales) with real numbers. For now, the break-even and quit numbers above are your targets."

→ Next: **Step 5** — the decision framework

---

**Step 5 — The real conversation**

> "Here's what the numbers actually say:"

Present one of four verdicts based on the math:

**STAY (most common):** Side MRR < 30% of gap, or < 3 months of data
> "Keep the day job. Optimize the 10-hour week. The side project is an investment, not an income replacement yet. Re-run this calculator quarterly."

**NEGOTIATE:** Side MRR 30-60% of gap, stable or growing
> "Your side income is meaningful but not replacement-level. Consider: reduced hours at work? Remote-only arrangement? Four-day week? Most senior tech employees get a 'yes' they assumed was a 'no.' The conversation costs nothing."

**PLAN THE EXIT:** Side MRR 60-90% of gap, growing, 3+ months data
> "You're approaching the quit number. Pick a date 90-180 days out. Build the bridge: save aggressively, start the accountant conversation (tax implications of leaving W-2), tell your partner the timeline."

**QUIT (rare at this stage):** Side MRR ≥ gap for 3+ consecutive months AND 6-month emergency fund
> "The math says you can quit. But math isn't the whole picture. Three conversations first: (1) Partner — are they aligned? (2) Accountant — healthcare, taxes, retirement gap? (3) Boss — 2-week or longer notice? Don't resign on a Friday night high. Sleep on it. If Monday morning the math still works and you still want it — go."

→ Next: **Step 6** — save artifact

---

**Step 6 — Output artifact**

Save the full calculator output (Steps 3-5) to `.unstuck/runway-YYYY-MM-DD.md`.

Update `.unstuck/context.md` Section G with:
- Monthly burn
- Runway months
- Quit number (sales/month)
- Current verdict (STAY / NEGOTIATE / PLAN / QUIT)

> "Calculator saved. Re-run quarterly, or anytime your expenses, income, or sales change significantly. Fire `/unstuck day-job-decision` when you need the full decision framework (conversations, timeline, risk assessment) — not just the math."

</process>

<success_criteria>
This module is complete when:
- [ ] Monthly burn locked
- [ ] Take-home, savings, partner income locked
- [ ] Runway months calculated
- [ ] Break-even sales/month calculated
- [ ] Quit number (sales/month × 3 consecutive months + 6-month fund) calculated
- [ ] Growth projection run (if sales data exists)
- [ ] Verdict delivered (STAY / NEGOTIATE / PLAN / QUIT)
- [ ] Artifact saved
- [ ] Context updated with financial state
</success_criteria>
