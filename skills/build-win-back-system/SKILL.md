---
name: build-win-back-system
description: Design the complete system for recovering churned customers and re-engaging cold leads — segmentation, 3-phase win-back sequences, 9-word re-engagement emails, dunning flows, and proactive churn prevention triggers. Use when user mentions "win back customers," "churned customers," "customer recovery," "re-engagement," "cold leads," "inactive subscribers," "lapsed customers," "churn prevention," "dunning sequence," "breakup email," "sunset email," "we miss you email," "win-back sequence," "customer reactivation," "reduce churn," "churn rate," or "lost customers." Also trigger on "customers stopped buying," "people aren't coming back," "how do I get old customers back," "my list is dead," "inactive users," "failed payments," "involuntary churn," "voluntary churn," "customer health score," or any request to recover revenue from customers who left.
---

# Build Win-Back System

## What This Skill Does

Designs the complete system for recovering churned customers and re-engaging cold leads — the most cost-effective growth channel most businesses ignore. Winning back a churned customer costs 5-7x less than acquiring a new one, yet most businesses have no structured process for it. This skill builds the segmentation strategy, email sequences, proactive triggers, and metrics framework that turn customer loss into a recoverable revenue stream.

This skill encodes frameworks from Dean Jackson (9-Word Email, Before/During/After Unit), Klaviyo and ActiveCampaign (3-Phase Win-Back Sequence), Gainsight and ChurnZero (Customer Health Scoring), and Kahneman & Tversky (Loss Aversion). It segments your churned customers by recency, value, and churn reason, then designs tailored recovery approaches for each segment — from automated email sequences to personal outreach plays. The 3-Phase Win-Back Sequence (reconnection, offer, breakup) recovers 15-30% of churned customers. The 9-Word Email generates 10-25% reply rates from cold lists that traditional marketing emails cannot reach.

Most businesses over-invest in the "During Unit" (doing the work) and under-invest in the "After Unit" (retention, referrals, win-back, lifetime value). This skill builds the After Unit infrastructure that captures revenue you are currently leaving on the table — without spending a dollar on new customer acquisition.

## Phase 1: Win-Back Discovery Questions

Ask these questions one at a time. Wait for the user's answer before moving to the next.

**If the user is stuck on any question:** Use the helper prompt to reframe. Most businesses have churned customers they can recover — they just haven't thought systematically about who left, why, and what would bring them back.

### The 7 Questions

**Q1: "What product/service did these customers buy, and how long have they been gone?"**
Understanding what they originally purchased and how long ago they left determines the entire recovery approach. A customer who left last month is fundamentally different from one who left a year ago — different emotional state, different memory of your brand, different likelihood of return.

*If stuck, ask:* "Tell me about the customers who left. What did they originally buy? When did they stop engaging? Are we talking about people who cancelled a subscription, stopped reordering, or just went silent?"

**Q2: "Why do customers typically leave?"**
The reason for departure dictates the win-back message. Price-sensitive churns need value reinforcement. Disappointed churns need proof that things have changed. Life-change churns need a gentle door left open. Competitive churns need differentiation. Common reasons: price, didn't see results, found an alternative, life circumstances changed, poor experience, outgrew the product, payment failure.

*If stuck, ask:* "Have you ever asked someone who left why they left? What did they say? If not, what's your best guess? Think about the last 5 customers who stopped buying — what do you think happened?"

**Q3: "What does your current win-back process look like?"**
Most businesses answer "nothing" — and that is a valid answer. Some have a single email, a discount code, or an ad campaign. Understanding the baseline reveals how much infrastructure needs to be built from scratch versus refined.

*If stuck, ask:* "What happens right now when a customer stops buying or engaging? Is there an automated email? A manual check-in? A discount offer? Be honest — 'nothing' is the most common answer and the best starting point."

**Q4: "What's the value of a recovered customer vs. acquiring a new one?"**
This question establishes the economic case for win-back investment. If a recovered customer has higher LTV, higher repeat purchase rate, and lower acquisition cost than a new customer, the win-back system pays for itself many times over.

*If stuck, ask:* "How much does it cost you to get a new customer? How much does a typical customer spend over their lifetime? Do customers who come back tend to be more loyal the second time around, or less?"

**Q5: "What would make a churned customer come back?"**
This shapes the win-back offer and messaging. Some customers need to see that you fixed the problem. Others need a financial incentive. Others just need to be reminded you exist. The answer here becomes the core of Email 2 in the win-back sequence.

*If stuck, ask:* "If you could say ONE thing to a customer who left, what would it be? What would make them say 'hm, maybe I should give it another shot'? Is it a new feature, a fixed problem, a better price, or just personal attention?"

**Q6: "Do you have separate segments of churned customers?"**
Not all churns are equal. Recent churns are warm and recoverable. Ancient churns may not remember you. High-value churns deserve personal outreach. Involuntary churns (payment failure) need a completely different approach than voluntary churns. Segmentation is the difference between a win-back system and a mass blast.

*If stuck, ask:* "Is someone who left last month different from someone who left a year ago? Are there high-value customers you'd especially want back? Did some people leave because their credit card expired versus actively deciding to cancel?"

**Q7: "What data do you have on churned customers?"**
The system is only as good as the data behind it. Email addresses are the minimum. Purchase history, engagement data, last interaction date, churn reason, and customer health indicators enable increasingly sophisticated segmentation and personalization.

*If stuck, ask:* "Can you email them? Do you know what they bought and when they stopped? Do you have any data on their engagement before they left — like login frequency, support tickets, or usage patterns?"

## Phase 2: Generate the Win-Back System

After gathering all 7 answers, generate a complete win-back system with these 7 sections.

### Section 1: Churn Segmentation

Based on Q2 and Q6, segment churned customers into actionable groups. Each segment gets a tailored recovery approach.

| Segment | Description | Size Estimate | Win-Back Approach | Priority |
|---------|------------|---------------|-------------------|----------|
| Recent Churns (0-30 days) | Just left, still remember you, emotional residue is fresh | [Estimate from Q1] | 3-Phase Win-Back Sequence — reconnection, offer, breakup | HIGH |
| Warm Churns (30-90 days) | Fading but reachable, may have tried alternatives | [Estimate] | 9-Word Email to re-open conversation, then win-back offer | HIGH |
| Cold Churns (90-365 days) | Mostly forgotten you, settled into new habits | [Estimate] | Story-driven re-engagement, then 9-Word Email | MEDIUM |
| Dead List (365+ days) | May not remember you at all | [Estimate] | 9-Word Email only — low investment, test for signs of life | LOW |
| High-Value Churns | Spent significantly above average, then left | [Estimate] | Personal outreach — phone call, DM, handwritten note + dedicated offer | CRITICAL |
| Involuntary Churns | Payment failed, card expired, billing error | [Estimate] | Dunning sequence — technical recovery, not re-selling | HIGH |

**Segment-Specific Notes:**
For each segment, add 2-3 sentences explaining the psychology of that group and why the chosen approach fits. Reference specific answers from Q2 (why they leave) and Q5 (what would bring them back) to customize the approach.

**Prioritization Matrix:**

| Factor | Weight | How to Score |
|--------|--------|-------------|
| Recency of churn | 30% | More recent = higher score |
| Historical LTV | 25% | Higher spend = higher score |
| Churn reason | 20% | Fixable reason = higher score |
| Engagement before churn | 15% | Higher prior engagement = higher score |
| Data quality | 10% | More data available = higher score |

### Section 2: 3-Phase Win-Back Email Sequence

Design the core automated sequence for recent and warm churns. This is the industry-standard 3-email arc refined by Klaviyo and ActiveCampaign that recovers 15-30% of churned customers.

**Sequence Flow:**
```
Email 1 (Day 1)          Email 2 (Day 3-5)         Email 3 (Day 7-10)
Reconnection             Win-Back Offer             Breakup/Sunset
"We miss you"            "Come back and get X"      "Click to stay or we remove you"
NO discount              Incentive + urgency         Loss aversion trigger
Warm, not desperate      Direct, valuable            Clear, final
     │                        │                           │
     ▼                        ▼                           ▼
[Opened? ──Yes──►]      [Clicked? ──Yes──►]        [Clicked? ──Yes──► RECOVERED]
     │                        │                           │
     No                       No                          No
     │                        │                           │
     ▼                        ▼                           ▼
  Send E2                  Send E3                  REMOVE from list
```

**Email 1 — Reconnection (Day 1)**

- **Purpose:** Re-establish the relationship. Show what has changed or improved since they left. Build emotional warmth. NO discount, NO offer — reconnection only.
- **Subject line options** (3, customized to their business from Q1):
  1. [Curiosity + personal — e.g., "A few things have changed since you left"]
  2. [Update-driven — e.g., "You might not recognize us anymore"]
  3. [Warm + direct — e.g., "[Name], it's been a while"]
- **Key message:** "Things have changed since you left." Reference specific improvements, new features, or resolved issues based on Q2 (why they leave) and Q5 (what would bring them back).
- **Tone:** Warm, genuine, not desperate. No guilt. No "we've been crying into our pillows." Confident and inviting.
- **CTA:** Soft — "See what's new" or "Reply and tell us what happened." No purchase link.
- **Word count target:** 200-350 words

**Email 2 — Win-Back Offer (Day 3-5)**

- **Purpose:** Give them a concrete, time-limited reason to return. This is where the incentive lives.
- **Subject line options** (3, customized):
  1. [Offer-forward — e.g., "A comeback offer just for you"]
  2. [Curiosity + value — e.g., "I set something aside for you"]
  3. [Direct — e.g., "Come back and get [specific incentive]"]
- **The offer:** Based on Q5, design the specific incentive — discount, extended trial, bonus content, exclusive access, free shipping, account credit, or upgraded tier. State the exact offer clearly.
- **Key message:** "We want to make it right." Acknowledge the gap. Present the incentive as a bridge back.
- **Urgency:** Time-limited — 7 days. State the expiration clearly. Open-ended offers have no urgency and convert poorly.
- **CTA:** Direct — "Come back and get [incentive]" with link. Repeat CTA 2x (top and bottom of email).
- **Word count target:** 200-300 words

**Email 3 — Breakup/Sunset (Day 7-10)**

- **Purpose:** Last chance. Trigger loss aversion. Clean the list.
- **Subject line options** (3, using loss aversion):
  1. [Loss-framed — e.g., "We're removing your account"]
  2. [Final — e.g., "Last email from us (unless you click)"]
  3. [Direct — e.g., "Should I remove you?"]
- **Key message:** "We're removing you from our list unless you click to stay." This is the highest-converting email in the sequence because loss aversion makes people feel losses ~2x more intensely than equivalent gains (Kahneman & Tversky).
- **The psychology:** "You're about to lose access" is more motivating than "Come back and gain access." The breakup email leverages this directly.
- **CTA:** Two options — "Click to stay" (primary) and "Remove me" (secondary). Both are clear actions.
- **Critical rule:** This is a REAL action. If they do not click, actually remove them. Fake breakup emails destroy trust and harm deliverability. The secondary benefit of a real sunset: cleaning your list improves deliverability scores for everyone who stays.
- **Word count target:** 100-200 words (short, direct, no storytelling)

### Section 3: The 9-Word Re-Engagement Email

Customized for their business using Dean Jackson's framework. This is the single most effective tool for re-engaging cold leads and ghosted prospects.

**Why This Works:**
The 9-Word Email looks like a personal email from a real human. No images, no formatting, no sales pitch. It bypasses every marketing filter — both the email client's spam filter and the reader's mental spam filter. It triggers a conversational response instead of a transactional one.

**The Template:**
- **Subject:** [Customer's first name — nothing else]
- **Body:** "[Are you still looking for / interested in / working on] [specific thing]?"
- **Formatting rules:** Plain text ONLY. No images. No HTML formatting. No bold, no italic, no colored text. No signature block. No logo. No unsubscribe link in the body (keep it in the footer where required by law, but do not draw attention to it). It must look indistinguishable from a personal email sent from a real person's inbox.

**Customized 9-Word Variations:**
Generate 3-5 variations tailored to their specific business based on Q1 (what they sell) and Q2 (why they leave):

| Variation | The 9-Word Email | Best Used For |
|-----------|-----------------|---------------|
| 1 | "[Are you still looking for [specific outcome]?]" | Cold leads who showed interest but never bought |
| 2 | "[Are you still interested in [specific solution]?]" | Customers who cancelled but didn't give a reason |
| 3 | "[Are you still working on [specific goal]?]" | Customers who churned due to lack of results |
| 4 | "[Did you ever find a solution for [specific problem]?]" | Customers who left for a competitor |
| 5 | "[Are you still thinking about [specific transformation]?]" | Leads who went silent mid-conversation |

**When to Use:**
- Cold list re-engagement (60+ days inactive)
- Leads who showed interest but never bought
- Customers who ghosted without cancelling
- Re-opening conversations after a long gap

**Expected Performance:**
- Reply rate: 10-25% (vs. 1-3% for typical marketing emails)
- Goal: Get a REPLY. That is the only metric. The reply re-starts the conversation. Do not try to sell in this email.

**Follow-Up Protocol:**
When someone replies to the 9-Word Email:
1. Respond personally within 24 hours
2. Ask about their current situation (do not pitch immediately)
3. Listen for their needs, then connect to relevant offer
4. If high-value: schedule a call. If standard: send relevant resource.

### Section 4: Involuntary Churn Prevention (Dunning)

Design the dunning sequence for payment failures. Involuntary churn (failed payments, expired cards) is NOT the same as voluntary churn — these customers did not decide to leave. They have a billing problem, not a satisfaction problem. Treat them accordingly.

**If not applicable** (non-subscription, non-recurring business): Skip this section and note that involuntary churn does not apply to their model.

**Pre-Dunning (Before Failure):**

| Trigger | Timing | Message | Channel |
|---------|--------|---------|---------|
| Card expiring soon | 30 days before expiration | "Your card ending in XXXX expires soon. Update it to avoid interruption." | Email |
| Card expiring soon | 7 days before expiration | "Your payment method expires in 7 days. Update now to keep your access." | Email + in-app |
| Card expiring soon | 1 day before expiration | "Last chance to update your card before tomorrow's charge." | Email + SMS (if opted in) |

**Post-Failure Dunning Sequence:**

| Step | Timing | Message | Tone |
|------|--------|---------|------|
| 1 — Immediate notification | Within 1 hour of failure | "Your payment didn't go through. This happens — click here to update your card." | Helpful, no alarm |
| 2 — Gentle reminder | Day 3 | "We tried charging your card again but it didn't work. Your access is still active — update your payment method to keep it that way." | Reassuring |
| 3 — Urgency | Day 7 | "We've tried [X] times but your payment keeps failing. Your access will be paused in 48 hours unless you update your card." | Direct, clear consequences |
| 4 — Final notice | Day 10-14 | "Your access will be removed tomorrow. Click here to update your payment and keep everything you've built." | Loss aversion, finality |

**Retry Schedule:**
- Retry 1: Day 1 (immediately after failure)
- Retry 2: Day 3 (after first reminder)
- Retry 3: Day 5 (before urgency email)
- Retry 4: Day 7 (with urgency email)

**Recovery Tactics:**
- Offer alternative payment methods (different card, PayPal, bank transfer)
- If repeated failures: offer to pause subscription instead of cancel
- For high-value accounts: personal outreach from support team

### Section 5: Proactive Churn Prevention Triggers

Based on Q2 (why they leave), design early warning systems that catch at-risk customers BEFORE they churn. Prevention is cheaper than recovery.

| Warning Signal | What It Means | Intervention | Timing |
|---------------|--------------|-------------|--------|
| [Behavior based on Q2] | [Interpretation] | [Specific action to take] | [When to trigger] |

**Build 6-10 warning signals** customized to their business. Common patterns include:

| Warning Signal | What It Means | Intervention | Timing |
|---------------|--------------|-------------|--------|
| Login frequency drops 50%+ | Losing interest or finding alternatives | Personal check-in email: "Everything okay?" | Within 7 days of drop |
| Support ticket filed + no resolution | Frustration building | Escalate to senior support + follow-up call | Within 24 hours |
| Downgrade or feature reduction | Testing whether they need you | Value demonstration: show ROI of full plan | Same day |
| No engagement with new features | Not growing with the product | Targeted tutorial or onboarding for new features | Within 14 days of feature launch |
| Competitor research detected | Actively evaluating alternatives | Proactive outreach with differentiation + exclusive offer | Within 48 hours |
| Usage plateau after initial ramp | Hit a ceiling, not seeing new value | Advanced use case content or strategy session | When plateau exceeds 30 days |

**Customer Health Score Framework:**
If they have sufficient data (Q7), design a composite health score:

| Factor | Weight | Healthy | At-Risk | Critical |
|--------|--------|---------|---------|----------|
| Usage frequency | 30% | [Define threshold] | [Define threshold] | [Define threshold] |
| Feature adoption | 20% | [Define] | [Define] | [Define] |
| Support interactions | 15% | [Define] | [Define] | [Define] |
| Payment history | 15% | [Define] | [Define] | [Define] |
| Engagement (emails, content) | 10% | [Define] | [Define] | [Define] |
| Time since last activity | 10% | [Define] | [Define] | [Define] |

**Intervention Playbook by Risk Tier:**
- **Healthy (score 70-100):** Standard nurture. Upsell opportunities. Referral requests.
- **At-Risk (score 40-69):** Proactive check-in. Value reinforcement. Usage tips. Dedicated support.
- **Critical (score 0-39):** Immediate personal outreach. Executive-level attention for high-value accounts. Retention offer. Exit interview if recovery fails.

### Section 6: Win-Back Metrics and Goals

Define success metrics for the entire system.

| Metric | Target | How to Measure | Review Cadence |
|--------|--------|---------------|----------------|
| Win-back rate (3-Phase Sequence) | 15-30% | Churned customers who return after receiving the sequence | Monthly |
| 9-Word Email reply rate | 10-25% | Replies received / emails sent | Per campaign |
| Breakup email save rate | 20-40% | "Click to stay" / emails sent | Per campaign |
| Re-activated customer LTV | [Based on Q4] | Revenue from recovered customers over 12 months | Quarterly |
| Involuntary churn recovery rate | 50-70% | Failed payments recovered via dunning | Monthly |
| Time to re-activation | [Target based on Q1] | Days from first win-back email to return purchase | Monthly |
| List hygiene improvement | Remove 100% of non-responders after sunset | Unresponsive contacts removed / total sunset emails sent | Per campaign |
| Churn prediction accuracy | 70%+ | Customers flagged at-risk who actually churn within 90 days | Quarterly |
| Prevention intervention success | 30-50% | At-risk customers who return to healthy after intervention | Monthly |

**Revenue Impact Projection:**
Based on Q4 (customer value) and segment sizes from Section 1, calculate:
- **Recoverable revenue** = (Number of churned customers) x (Win-back rate target) x (Average recovered customer LTV)
- **Cost of system** = Email platform costs + time investment + incentive costs
- **ROI** = (Recoverable revenue - Cost of system) / Cost of system

### Section 7: System Gaps and Recommendations

Audit the complete win-back system and identify what is missing, weak, or could be improved.

**Data Gaps:**
Based on Q7, what customer data is missing that would improve win-back effectiveness? Common gaps: churn reason tracking, engagement scoring before churn, customer satisfaction data, competitive intelligence, usage analytics.

**Timing Gaps:**
Based on Q1 and Q3, are they waiting too long to intervene? The first 72 hours after churn are the highest-recovery window. Every week of delay reduces win-back probability by roughly 10-15%.

**Segmentation Gaps:**
Based on Q6, are they treating all churns the same? A one-size-fits-all win-back email to every churned customer wastes the high-value segment and under-invests in recoverable segments.

**Feedback Gaps:**
Based on Q2, are they systematically learning WHY people leave? Recommend: exit survey at cancellation, 30-day post-churn check-in, quarterly churn analysis review.

**Re-Onboarding Gap:**
Returning customers need a different onboarding than new customers. They already know the basics but may need to learn what has changed. Design a re-onboarding checklist:
- Welcome back message (acknowledge they left and returned)
- What's new since they left (feature updates, improvements)
- Quick-start for returning users (skip basics, show advanced features)
- Dedicated support contact for first 30 days
- If design-onboarding-sequence output exists, adapt its structure for returning customers

**Prevention vs. Recovery:**
Based on Q2 and Q5, would investing in better onboarding, support, or product experience reduce the need for win-back entirely? Sometimes the best win-back system is a better retention system. Flag specific upstream fixes that would reduce churn at the source.

**Companion Skill Recommendations:**
- If churn is driven by poor onboarding: chain to **design-onboarding-sequence** for re-onboarding flow
- If email content needs story-driven engagement: pair with **build-email-story-engine**
- If messaging needs voice consistency: activate **brand-voice-router**
- If AI-generated copy needs humanizing: run through **humanize-ai-writing**
- If win-back messaging needs persona alignment: reference **generate-persona-playbook**

## Rules

- The 9-Word Email must be PLAIN TEXT — no images, no formatting, no HTML, no signature block. It must look like a personal email from a human, not a marketing message.
- Never use guilt, shame, or desperation in win-back messaging. "We miss you" is warm. "You're missing out" is acceptable. "Don't you care about your business?" is manipulative and off-limits.
- The breakup/sunset email is a REAL action — if they do not click, actually remove them from the active list. Do not send fake breakup emails. Fake sunsets destroy trust and harm deliverability.
- Win-back offers must be time-limited (7-14 days) — open-ended offers have no urgency and convert at a fraction of the rate.
- Involuntary churn (payment failure) is NOT the same as voluntary churn — never send a "we miss you" email to someone whose card expired. Send a "let's fix your payment" email instead.
- High-value churns deserve personal outreach (phone call, DM, handwritten note), not just automated emails. Flag any high-value segment that is only receiving automated sequences.
- The first win-back email must NEVER include a discount or offer — reconnect first, offer second. Leading with a discount trains customers to churn for discounts.
- Loss aversion is the most powerful tool in the system — "You're about to lose X" beats "Come back and get X" every time. Use it in the breakup email and dunning sequence.
- If design-onboarding-sequence output exists, design a re-onboarding flow specifically for returning customers — do not put them through the new customer onboarding.
- If generate-persona-playbook output exists, match win-back messaging to persona psychology, language patterns, and emotional triggers.
- If brand-voice-router is active, apply its voice profile to all generated copy across every email in the system.
- Apply humanize-ai-writing to all email copy before finalizing — win-back emails that sound like AI-generated marketing will not recover anyone.
- Never fabricate testimonials, results, or data in win-back copy — flag where real proof is needed and leave a placeholder.
- Segment before sending — a single win-back email blasted to the entire churned list is not a system, it is spam.

## What This Skill Does NOT Do

- Fix the underlying product, service, or experience problems that caused churn in the first place — this skill recovers customers, it does not solve the root cause of their departure
- Build the email automation infrastructure, set up ESP integrations, or configure triggers and workflows (use create-tag-based-funnel-system for automation architecture)
- Handle billing, payment recovery technology, or subscription management platform setup — this skill designs the messaging and strategy, not the payment infrastructure
- Conduct customer exit interviews — this skill provides the framework and questions, but the actual interviews require human execution
- Design the full re-onboarding experience in detail (use design-onboarding-sequence for that) — this skill flags the gap and provides a checklist, not a complete onboarding flow
- Create retargeting ads or paid media campaigns aimed at churned customers
- Build the offer or incentive structure from scratch (use build-irresistible-offer for that) — this skill deploys an existing offer within the win-back sequence
- Replace a proper customer success or account management function — automated win-back supplements but does not replace human relationship management
