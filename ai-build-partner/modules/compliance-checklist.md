<required_reading>
**Read these reference files NOW:**
1. references/core.md
</required_reading>

<process>

**Step 0 — Check User Context first**

Read `.unstuck/context.md`:
- **Section B.1** (project type — app / course / template kit / service / newsletter / community / physical product)
- **Section E.5** (price — affects refund policy complexity)
- **Section D.8** (landing page — if it exists, compliance pages link from it)

If no project type is set, ask: "What are you selling? Digital download / SaaS app / service / course / community / physical product?"

---

**Opening (output verbatim):**

> "Compliance checklist. The legal minimum before you take someone's money.
>
> This is NOT legal advice — I'm generating templates and a checklist based on your product type. For anything beyond a simple digital product, consult a lawyer in your state. The goal: get the basics live in 30 minutes so legal gaps don't block your launch.
>
> Product type detected: **[from context]**. Price: **$[from context]**.
>
> Ready?"

---

**Step 1 — Privacy Policy (everyone needs this)**

> "If you collect ANY data — email addresses, payment info, analytics, cookies — you need a privacy policy. Not optional. GDPR (EU) and CCPA (California) have real fines."

Generate a privacy policy template based on their product type:

**All products:**
- What data you collect (email, name, payment info)
- How you use it (deliver product, send updates, improve service)
- Third parties who process data (Stripe, your email platform, analytics)
- How users can request data deletion
- Contact email for privacy questions

**SaaS / apps additionally:**
- Cookie policy (what cookies, why, how to opt out)
- Data retention period
- Data processing agreement reference (if B2B)

**Output:** Paste-ready privacy policy. Tell the buyer: "Put this on your site at /privacy. Link it from your checkout page footer."

→ Next: **Step 2** — Terms of Service

---

**Step 2 — Terms of Service**

Generate based on product type:

**Digital downloads (PDFs, templates, kits):**
- License: personal use, non-transferable, no resale
- Delivery: digital, immediate after payment
- No warranty: provided "as-is"
- Limitation of liability
- Governing law (buyer's state)

**SaaS / apps:**
- Above + acceptable use policy
- Account termination rights
- Service availability (no SLA for solo products)
- Data ownership (user owns their data)

**Services (consulting, coaching):**
- Scope of engagement
- Payment terms
- Cancellation policy
- No guarantee of results (important for coaching/consulting)
- Confidentiality

**Courses:**
- Access period (lifetime / time-limited)
- No guarantee of outcomes
- Intellectual property (course content is yours, not theirs to resell)

**Output:** Paste-ready terms. "Put this at /terms. Link from checkout footer."

→ Next: **Step 3** — Refund Policy

---

**Step 3 — Refund Policy**

> "Three options. Pick one based on your risk tolerance and product type."

| Policy | Best for | Language |
|--------|----------|----------|
| **30-day no-questions** | Digital products, courses, templates. Builds trust. Refund rate is usually <5%. | "Not happy? Email [you] within 30 days for a full refund. No questions asked." |
| **14-day conditional** | Services, higher-priced products. | "Request a refund within 14 days if you've completed [specific action] and it didn't work. Email [you] with what you tried." |
| **No refunds** | Low-price digital downloads ($9-19). Clear before purchase. | "All sales final. This is a digital product delivered immediately — no refunds." |

Push for the 30-day option:

> "Most solo builders pick 'no refunds' out of fear. The data says the opposite: generous refund policies INCREASE sales more than they increase refunds. A 30-day guarantee on a $149 kit will net you more revenue than a no-refund policy. The refund rate on digital products is typically 2-5%."

**Output:** Paste-ready refund policy. "Put this on your sales page AND checkout page. Visible before they click buy."

→ Next: **Step 4** — Product-type specific requirements

---

**Step 4 — Product-type specific additions**

Only fire the relevant ones:

**If collecting emails (everyone):**
- [ ] Unsubscribe link in every email (CAN-SPAM, required by law)
- [ ] Double opt-in recommended (not legally required in US, required in EU)
- [ ] Physical mailing address in email footer (CAN-SPAM requirement — use a PO Box or virtual address if working from home)

**If SaaS / app:**
- [ ] Cookie consent banner (required in EU, best practice everywhere)
- [ ] Accessibility statement (recommended, not yet required for most small businesses)

**If handling sensitive data (health, finance, children):**
- [ ] STOP. Consult a lawyer before launch. HIPAA / COPPA / SOC 2 compliance is not template-able.

**If service business:**
- [ ] Service agreement template (scope, deliverables, timeline, payment terms, cancellation)
- [ ] Professional liability insurance consideration (see `/unstuck business-setup`)

→ Next: **Step 5** — The checklist artifact

---

**Step 5 — Output the compliance checklist**

```
COMPLIANCE CHECKLIST — [Product Name] — [Date]
Product type: [paste]
Price: $[paste]

BEFORE LAUNCH:
- [ ] Privacy policy live at /privacy
- [ ] Terms of service live at /terms  
- [ ] Refund policy on sales page + checkout page
- [ ] Unsubscribe link in all emails
- [ ] Physical address in email footer (PO Box OK)
- [ ] Cookie consent banner (if SaaS/app or EU audience)

AFTER FIRST SALE:
- [ ] Business bank account (separate from personal)
- [ ] Basic bookkeeping started (even a spreadsheet)

AT $1K REVENUE:
- [ ] LLC formed (liability protection)
- [ ] EIN obtained (free from IRS, takes 5 min online)

AT $5K REVENUE:
- [ ] Accountant consulted (quarterly estimates, deductions, sales tax)

Templates generated:
- Privacy policy: [paste or link]
- Terms of service: [paste or link]
- Refund policy: [paste]

⚠️ This is not legal advice. Templates are starting points.
For anything complex (SaaS with user data, services with liability,
health/finance/children), consult a lawyer in your state.

Built with the Unstuck Method — unstuckwithmolly.com
```

Save to `.unstuck/compliance-checklist-YYYY-MM-DD.md`.

<mcp_actions>
**With Notion MCP detected:**
- OFFER: "Want me to create Privacy Policy and Terms of Service pages in your Notion workspace?"
- If yes → `notion-create-pages` — two pages:
  - Page 1: "[Product name] — Privacy Policy" with the generated privacy policy content
  - Page 2: "[Product name] — Terms of Service" with the generated terms content
- Also offer: "Want me to add the compliance checklist as a Notion page too?" → third page with the checklist as toggleable checkboxes
**Without Notion MCP:** paste-ready templates in the artifact (default path above)
</mcp_actions>

---

**Step 6 — Exit and route**

> "Compliance basics done. You have privacy + terms + refund ready to paste. The legal templates will cover 95% of solo digital product businesses.
>
> **Next:** If you haven't wired payment yet, run `/unstuck pick-my-stack` to choose your payment processor. If payment is wired, you're clear to launch.
>
> **Comeback triggers:**
> - You change product type (digital → SaaS → service)
> - You expand to EU audience (GDPR gets stricter)
> - You cross $5K revenue (accountant time)
> - You handle sensitive data (lawyer time)"

</process>

<success_criteria>
This module is complete when:
- [ ] Product type identified
- [ ] Privacy policy generated (paste-ready)
- [ ] Terms of service generated (paste-ready)
- [ ] Refund policy chosen and written
- [ ] Product-type specific items checked
- [ ] Compliance checklist artifact saved
- [ ] Revenue-trigger milestones communicated ($1K LLC, $5K accountant)
</success_criteria>
