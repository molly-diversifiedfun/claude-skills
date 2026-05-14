<required_reading>
**Read these reference files NOW:**
1. references/core.md
</required_reading>

<process>

**Step 0 — Check User Context first (Mode 1 behavior)**

This skill locks the refund policy + drafts the 12 canned support responses BEFORE launch. Day 23 of the sprint, alongside T23 wiring. Before the Opening, scan:

- **Section B.1** (product, audience, persona)
- **Section D.2** (V1 features + price)
- **Section D.3** (locked price)
- **Section A** (voice / register — keep canned responses sounding like the buyer, not corporate)

If price > $500 and the buyer hasn't decided on a refund policy → push toward Policy C (strict). If price < $100 → push toward Policy A (generous). If mid → Policy B (conditional with light gate).

Don't ask what you can read. Anchor the policy recommendation in the locked price + product type before asking the buyer.

---

**Opening (output verbatim to the buyer):**

> "Pre-write 12 canned responses + lock the refund policy BEFORE launch. The first refund request lands within 14 days for ~all products. Winging it = bad refund. Pre-decided = clean refund.
>
> Three jobs in this skill:
> 1. **Pick a refund policy** (A generous / B conditional / C strict) — anchored to your price + product type
> 2. **Draft 12 canned responses** in your voice — pre-purchase / post-purchase / refund-and-dispute
> 3. **Set the response-time promise** + inbox routing
>
> **One ground rule:** buyers remember the refund more than the purchase. Make it easy. The 4-paragraph fight email never converts the regret-buyer back to advocate. The clean refund sometimes does. I'm going to push back on Policy C if it doesn't match your price tier.
>
> Ready?"

---

**Step 1 — Lock the refund policy**

Based on User Context price + format:

| Price | Format | Recommended | Why |
|---|---|---|---|
| < $100 digital | Course / template / guide | **Policy A — Generous** (14-30 day no-questions-asked) | Trust signal at checkout matters more than 3-8% refund rate |
| $99-$499 | Mid-priced product | **Policy B — Conditional** (7-14 day with light gate) | Filter impulse-buy-regret without being hostile |
| $500+ | High-touch / cohort / coaching | **Policy C — Strict** (no-refunds OR completion-gate) | Refunds cannibalize completion-paid revenue |

Output the recommended policy with sample wording:

**Policy A — Generous:**
> "If this isn't right for you within [N] days, send one email and you'll get a full refund. No questions, no forms, no hassle. We'd rather have your money back in your pocket than your frustration in our inbox."

**Policy B — Conditional:**
> "Try [PRODUCT] for [N] days. If the [templates / framework / lessons] aren't moving you forward, send us a one-paragraph note about what you tried and we'll refund you in full. We read every note — it's how we make the next version better."

**Policy C — Strict:**
> "We don't offer refunds because this is a high-touch [cohort / engagement], and pulling a seat after starting affects the other [members / clients]. Before you buy, [talk to us / take the assessment / read the FAQ] — we'd rather have you skip the wrong fit than refund a bad fit."

If the buyer picks a policy that doesn't match their price tier, push back:

> "You picked Policy C at a $97 price point. That signals 'don't trust me' to a buyer scanning your landing page. At your price, the refund cost is the trust signal — Policy A or B works better economically AND for conversion. Want to keep Policy C anyway? Tell me why."

Lock the policy + window length + where it's documented.

---

**Step 2 — Draft the 12 canned responses**

Pull from User Context Section A (voice). Each ≤ 100 words. Smart-friend tone, not corporate.

### Pre-purchase questions

> **Q1 — "Is this for me if I'm [persona variant — not technical / a beginner / advanced]?"**
> Honest yes/no + the ONE signal that decides. "If you can [X], yes. If you can't, no — try [alternative] first."

> **Q2 — "What's the time commitment?"**
> Specific hours + cadence. Don't say "as little as you want." "[N] hrs total over [N] days. Most people do [pattern]."

> **Q3 — "What format is the product?"**
> "[PDF / Notion / video / live cohort] + [companion]. Delivered via [link / email / Stripe portal]."

> **Q4 — "Can I get a discount?"**
> Either yes (and when — "first 25 buyers" / "launch week") or no (and what kind of buyer gets a different deal — "team seats: yes, 30% off at 5+").

### Post-purchase questions

> **Q5 — "I didn't get my delivery email"**
> Check spam. If not there: check ESP log for the address. Resend manually. Apologize specifically.

> **Q6 — "I lost my access link"**
> Send a fresh one. Don't make them re-purchase.

> **Q7 — "Can I share this with my team?"**
> Refer to license. Honest: most digital products are "single-buyer" license; selling team seats is a different SKU. Don't say "feel free" if you mean "no please."

> **Q8 — "I'd like to upgrade / add [X]"**
> Either sell it (point at it) or note for V1.1 backlog. Don't promise an upgrade you won't ship in 90 days.

### Refund + dispute questions

> **Q9 — "I'd like a refund — [reason]"**
> Reply within 24 hrs. Refund per Step 1 policy. Ask ONE optional question about what they wished was different. Don't argue.

> **Q10 — "My payment got declined"**
> Forward processor error. Suggest: try different card, check international block, contact bank. Don't debug their bank.

> **Q11 — "I bought twice by accident"**
> Refund the duplicate. Apologize. Verify in Stripe FIRST — most "double charge" reports are actually a pending auth + final charge.

> **Q12 — "I want to chargeback / I disputed this"**
> Reply within 6 hrs. Offer refund directly + ask them to withdraw the chargeback. Chargebacks cost $15-25 + reputation; refunds don't.

For each, draft the actual response customized to:

- The buyer's product name + price + format (from User Context)
- The buyer's voice (smart-friend tone, no "thanks for reaching out," no "let me know if you have any other questions")
- One specific detail that proves the email was read (not a form letter)

Label each `[T24-Q1]` through `[T24-Q12]` for saving as canned responses in Gmail / Help Scout / Front / Intercom.

---

**Step 3 — Set the response-time promise**

| Promise | Use when |
|---|---|
| **Within 24 hrs (business days)** | Solo founder, V1 launch, < 100 customers |
| **Within 12 hrs (business days)** | Team of 2+, monitoring shared inbox |
| **Within 1 hr (business hours)** | Premium product ($500+), B2B SaaS, paying SLA |

Anchor to buyer's reality:

- If User Context shows solo founder + < 100 customers → 24 hrs default
- If price > $500 and buyer claimed 1-hr — push back: "Can you actually sustain 1-hr response without burning out? If not, promise 12 hrs and beat it."

Document at: purchase email + landing-page footer.

---

**Step 4 — Inbox routing checklist**

- [ ] Create `support@[yourproduct].com` OR forward `hello@` to a real inbox
- [ ] Save 12 canned responses in email tool (label `[T24-Q1]` through `[T24-Q12]`)
- [ ] Set up the status macro: "Acknowledged — investigating, back within 24h"
- [ ] Save the refund-flow link from your payment processor in 1Password
- [ ] Add support email to T14 Build Vault

---

**Step 5 — Output the Support / Refund artifact**

```
SECTION D.7.5 — T24 Support / Refund Playbook
Locked: [Date — Day 23]
Source: /unstuck support-refund

REFUND POLICY: Policy [A / B / C]
- Window: ___ days
- Documented at: [landing page URL] · [purchase email]
- Sample wording (pasted on landing page): [paste]

RESPONSE PROMISE: within [X] hrs (business days)
- Documented at: [purchase email + landing page footer]

INBOX ROUTING:
- Support email: ___
- Tool: ___
- 12 canned responses saved: [tool + folder/label]

12 CANNED RESPONSES (Q1-Q12): drafted, labeled [T24-Q1] through [T24-Q12]

RUNNING METRICS (update weekly):
- Refund rate: [%]
- Most-asked question: [Q#]
- Response-time average: [hrs]

Built with the Unstuck Method — unstuckwithmolly.com
```

---

**Step 6 — Chain to next module**

- "Support locked. After launch, watch your refund rate — if > 8%, it's a fit problem, not a pricing problem. If 3+ customers ask the same question that's NOT in the 12, add it to your landing-page FAQ AND your purchase email; support volume = doc gap. At Day 38, refund rate feeds `/unstuck pricing-iteration` — if it's > 10%, hold the price and investigate fit."

</process>

<success_criteria>
This module is complete when:
- [ ] Refund policy locked (A / B / C) matching price tier (push-back applied if mismatched)
- [ ] Policy window length set + documented locations identified (landing + purchase email)
- [ ] All 12 canned responses drafted in buyer's voice, ≤ 100 words each
- [ ] Each canned response labeled [T24-Q1] through [T24-Q12]
- [ ] Response-time promise locked + sustainable (push-back applied if aspirational)
- [ ] Inbox routing checklist run (support email + canned responses saved + status macro + refund-link in 1Password)
- [ ] Section D.7.5 paste block delivered
- [ ] Running-metrics tracker initialized
</success_criteria>
