---
name: create-tag-based-funnel-system
description: Design tag-based email funnel state management systems that coordinate automation across multiple product tiers with purchase-based exits, timed progression, and reconciliation. Use when user mentions "email funnel," "tag system," "automation architecture," "sequence management," "purchase triggers," "email automation," "Mailchimp automation," "subscriber progression," "funnel automation," or needs to coordinate multi-product email sequences with conditional logic. Also trigger on "my emails keep sending after they buy," "how do I stop sales emails after purchase," "email sequence architecture," or any request to design email automation for a product ladder.
---

# Create Tag-Based Funnel System

## What This Skill Does

Designs a complete email funnel state management system using tags as the single source of truth for subscriber state. The output covers tag taxonomy, purchase handling, sequence architecture with conditional exits, timed progression between product tiers, and a daily reconciliation job that catches edge cases.

This solves the #1 email automation problem: sending sales emails to people who already bought. And the #2 problem: not knowing where a subscriber is in your funnel when things get complicated.

The architecture follows a three-layer separation: your automation tool (n8n, Zapier, Make) handles logic and state management, your email platform (Mailchimp, Kit, ActiveCampaign) handles email content and delivery, and tags are the coordination mechanism between them.

## Phase 1: Funnel Architecture Discovery

Ask these questions one at a time. Wait for the user's answer before moving to the next.

**If the user is stuck on any question:** Help them map out what they currently have, even if it's messy. Most people have some automation already — it's just not coordinated.

### The 7 Questions

**Q1: "What products do you sell, and in what order?"**
List every product/tier from cheapest to most expensive. What's the natural progression a customer takes through your product ladder? (e.g., free lead magnet → $17 tripwire → $97 core → $297/yr membership)

*If stuck, ask:* "What's free? What's your cheapest paid thing? What's your most expensive? Now put them in the order someone would encounter them."

**Q2: "What email platform are you using?"**
Mailchimp, Kit (ConvertKit), ActiveCampaign, Drip, Beehiiv, etc.? This affects what's possible — some platforms support conditional journey branching, others don't.

*If stuck, ask:* "Where do you send emails from today? Even if it's basic — that's your platform."

**Q3: "What payment processor(s) do you use?"**
Stripe, LemonSqueezy, Gumroad, Paddle, Shopify, Kit Commerce? Do you use multiple processors for different products? Each one sends different webhook formats.

*If stuck, ask:* "When someone buys from you, which service processes the payment? Check your bank statements if you're not sure."

**Q4: "What happens when someone buys — today?"**
Walk me through the current post-purchase experience. Do they get a delivery email? Are they removed from sales emails? Do they enter a new sequence? Or does nothing happen and they keep getting pitched?

*If stuck, ask:* "Buy your own product with a test email. What emails do you get in the next 7 days? That's your current post-purchase experience."

**Q5: "How long between product tiers?"**
After someone buys the tripwire, how many days should pass before you pitch the core product? What's the breathing room between each tier? Too soon feels pushy, too long loses momentum.

*If stuck, ask:* "After someone buys your cheapest product, when would it feel natural to mention the next one? A day? A week? A month?"

**Q6: "What emails does each pitch sequence have?"**
For each product you're selling via email: how many emails in the pitch sequence, and what's the general flow? (e.g., value → mechanism reveal → social proof → direct pitch → last chance)

*If stuck, ask:* "If you had to convince someone to buy [product] using 3-5 emails over a week, what would each email focus on?"

**Q7: "What automation tool handles the logic?"**
Do you use n8n, Zapier, Make (Integromat), or does your email platform handle everything natively? This determines where the state management lives — in an external tool or inside your email platform.

*If stuck, ask:* "Do you have any automations set up outside your email platform? If not, that's fine — we can design for your email platform's native capabilities."

## Phase 2: Generate the Funnel System

After gathering all 7 answers, generate a structured funnel system document with these 8 sections.

### Section 1: Tag Taxonomy

Design the complete tag system with consistent naming convention: `{tier}-{type}`

**Status Tags** (where the subscriber IS in the product ladder):
| Tag | Applied When | Meaning |
|-----|-------------|---------|
| lead-magnet-subscriber | Opts in | Has entered the funnel |
| tripwire-buyer | Purchases tripwire | Owns the tripwire product |
| core-buyer | Purchases core | Owns the core product |
| ... | ... | ... |

**Sequence Control Tags** (what's currently ACTIVE):
| Tag | Applied When | Removed When | Meaning |
|-----|-------------|-------------|---------|
| in-tripwire-sequence | Ready for tripwire pitch | Purchases tripwire OR sequence ends | Currently receiving tripwire sales emails |
| in-core-sequence | Ready for core pitch | Purchases core OR sequence ends | Currently receiving core sales emails |
| ... | ... | ... | ... |

**Delivery Confirmation Tags** (what's been SENT):
| Tag | Applied When | Meaning |
|-----|-------------|---------|
| tripwire-delivered | Product delivery email sent | Tripwire product has been delivered |
| core-delivered | Product delivery email sent | Core product has been delivered |
| ... | ... | ... |

**Naming Convention:** `{product-tier}-{tag-type}` — always lowercase, hyphen-separated. Examples: `tripwire-buyer`, `in-core-sequence`, `stack-delivered`.

### Section 2: State Machine Diagram

Show all possible states and transitions:

```
[Opt-In] → add: lead-magnet-subscriber
    ↓ (after 24hr wait + check not already buyer)
[Tripwire Sequence] → add: in-tripwire-sequence
    ↓ (purchase) → add: tripwire-buyer, remove: in-tripwire-sequence, add: tripwire-delivered
    ↓ (after N days)
[Core Sequence] → add: in-core-sequence
    ↓ (purchase) → add: core-buyer, remove: in-core-sequence, add: core-delivered
    ...
```

Include all entry points, transitions, and terminal states.

### Section 3: Opt-In Handler

The workflow that fires when someone subscribes:

1. **Receive webhook/form submission** — capture email and source
2. **Create or update contact** in email platform
3. **Add status tag:** `lead-magnet-subscriber`
4. **Wait 24 hours** — let them consume the lead magnet before pitching
5. **Check:** Does this person already have `tripwire-buyer` tag?
   - If YES: skip to next applicable sequence
   - If NO: **Add sequence tag:** `in-tripwire-sequence`

### Section 4: Universal Purchase Handler

Single handler for all purchases across all payment processors:

1. **Receive webhook** from payment processor
2. **Normalize data:** Extract email, product identifier, purchase date from processor-specific payload
   - LemonSqueezy: `data.attributes.user_email`, `data.attributes.product_id`
   - Gumroad: `purchaser_email`, `product_id`
   - Stripe: `customer.email`, `line_items[0].price.product`
3. **Route by product tier** using Switch/conditional logic
4. **For the matched tier:**
   - Add buyer status tag (e.g., `tripwire-buyer`)
   - Remove active sequence control tag (e.g., `in-tripwire-sequence`) — THIS STOPS SALES EMAILS
   - Update purchase date merge field (e.g., `TWPURCHASE = today`)
   - Add delivery confirmation tag (e.g., `tripwire-delivered`)
5. **Trigger product delivery** via email platform

### Section 5: Sequence Architecture

For each pitch sequence, design the email flow with conditional exits:

**[Product Name] Pitch Sequence**
- **Trigger:** `in-{tier}-sequence` tag added
- **Entry Filter:** Does NOT have `{tier}-buyer` tag (prevents re-entry after purchase)

```
Email 1: [Value/check-in — zero pitch]
  ↓
  If/Else: Has {tier}-buyer tag?
    → YES: Remove in-{tier}-sequence tag, EXIT
    → NO: Continue
  ↓
  Wait [N] days
  ↓
Email 2: [Problem agitation / mechanism reveal]
  ↓
  If/Else: Has {tier}-buyer tag?
    → YES: Remove in-{tier}-sequence tag, EXIT
    → NO: Continue
  ↓
  Wait [N] days
  ↓
Email 3: [Direct pitch with proof]
  ↓
  If/Else: Has {tier}-buyer tag?
    → YES: Remove in-{tier}-sequence tag, EXIT
    → NO: Continue
  ↓
  Wait [N] days
  ↓
Email 4: [Final chance / urgency]
  ↓
  Remove in-{tier}-sequence tag (end of sequence)
```

**Critical rule:** If/Else buyer check between EVERY email. Never assume the full sequence plays out.

**Between sequences:** Include a zero-pitch check-in email before starting the next tier's pitch. "How's [previous product] working for you?" — no mention of the next product. This resets relationship temperature.

### Section 6: Daily Reconciliation Job

Scheduled workflow (cron) that runs daily to catch edge cases:

**Schedule:** Daily at 9:00 AM (or preferred time)

**For each tier transition:**
1. Query all subscribers with `{tier}-buyer` tag AND without `in-{next-tier}-sequence` tag
2. Check: days since purchase ≥ threshold (e.g., 7 days for tripwire→core, 30 days for core→stack)
3. If threshold met: Add `in-{next-tier}-sequence` tag
4. Log all tag additions with subscriber email, tag added, and trigger reason

**Why this is not optional:** Real-time triggers miss edge cases:
- Someone buys two products simultaneously
- A webhook is delayed or fails
- Someone buys out of order (skips a tier)
- The automation tool was down when a purchase happened

The daily reconciliation catches all of these.

### Section 7: Edge Cases & Safety

Address each scenario:

**Someone buys two products at once:**
Purchase handler processes each webhook independently. First purchase removes current sequence, second purchase removes next sequence. Daily reconciliation starts the appropriate next sequence after timing threshold.

**Someone buys out of order (skips a tier):**
Add buyer tag for purchased tier. Daily reconciliation checks from highest tier down, so it starts the correct next sequence.

**Webhook delayed or fails:**
Daily reconciliation will catch it within 24 hours. Include webhook retry configuration for your processor.

**Subscriber unsubscribes mid-sequence:**
Respect the unsubscribe. Remove all sequence control tags. Do not re-add.

**Subscription renewal (if applicable):**
- Send pre-renewal notice 7 days before charge with visible cancel link
- Send post-renewal confirmation with refund window
- Handle failed payment with grace period and dunning sequence

### Section 8: Testing Protocol

**End-to-End Test Plan:**

| Test Case | Steps | Expected Result |
|-----------|-------|----------------|
| New opt-in | Subscribe with test email | Gets lead magnet, gets `lead-magnet-subscriber` tag, starts tripwire sequence after 24hr |
| Mid-sequence purchase | Buy while in tripwire sequence | Gets `tripwire-buyer` tag, `in-tripwire-sequence` removed, sales emails stop immediately |
| Timed progression | Wait N days after purchase | Daily reconciliation adds `in-core-sequence` tag, core pitch emails begin |
| Skip-tier purchase | Buy core without buying tripwire | Gets `core-buyer` tag, tripwire sequence stops, positioned correctly for next tier |
| Double purchase | Buy two products same day | Both buyer tags added, both sequence tags removed, reconciliation starts correct next sequence |

**Tag Verification Checklist:**
After each test, verify:
- [ ] Correct status tags present
- [ ] No conflicting sequence control tags
- [ ] Delivery confirmation tags match purchases
- [ ] Purchase date merge fields populated
- [ ] No sales emails sent after purchase

## Rules

- **Tags are the single source of truth.** Never rely on segment calculations or audience membership for real-time decisions. Tags change instantly; segments recalculate on delay.
- **Remove sequence control tags on purchase.** This is how you stop sales emails immediately. This is the #1 rule. If nothing else works right, this must work.
- **If/Else conditional check between EVERY email.** Never assume a multi-email sequence will play out uninterrupted. Purchases can happen at any point.
- **The Daily Reconciliation Job is not optional.** Real-time triggers miss edge cases. The cron catches them. Skipping this is how subscribers fall through the cracks.
- **Separate automation logic from email content.** Logic and state management live in your automation tool. Email templates and content editing live in your email platform. Don't mix them.
- **Consistent tag naming convention.** `{tier}-{type}` format: `tripwire-buyer`, `in-core-sequence`, `stack-delivered`. Inconsistent naming makes debugging impossible.
- **Zero-pitch check-in between sequences.** A pure-value email with no mention of the next product resets relationship temperature and prevents pitch fatigue.
- **Never send sales emails to someone who just bought.** This bears repeating. It's the fastest way to generate refund requests and destroy trust.
- **Merge fields for purchase dates.** Every purchase must set a date merge field. The daily reconciliation needs timestamps for timing calculations.
- **Test with real purchases.** Don't just test the happy path. Test mid-sequence purchases, out-of-order purchases, and simultaneous purchases.

## What This Skill Does NOT Do

- Write the actual email copy (it defines sequence structure, not content)
- Set up your email platform or automation tool (it produces the architecture to implement)
- Build webhook integrations (it specifies what they should do, not the code)
- Design landing pages or opt-in forms
- Create the product ladder itself (use design-offer-ladder for that)
- Handle email deliverability, domain setup, or sender reputation
