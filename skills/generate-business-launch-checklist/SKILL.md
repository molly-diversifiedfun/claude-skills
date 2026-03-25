---
name: generate-business-launch-checklist
description: Generate comprehensive, prioritized business launch checklists tailored to your specific startup context. Use when founder has built MVP but needs clarity on everything required to launch — mentions "what do I need to launch," "launch checklist," "am I ready to launch," "what am I missing," "compliance requirements," "legal setup for startup," "business formation," or any request about preparing a product or business for real customers. Works for any industry — automatically tailors to regulatory environment, tech stack, and business model.
---

# Generate Business Launch Checklist

## What This Skill Does

Takes a specific startup context — your product, your customers, your regulatory environment, your budget — and produces a comprehensive, prioritized launch checklist covering everything from legal entity formation to customer onboarding. Every item is tagged by priority (blocker, important, nice-to-have), includes cost and time estimates, and identifies dependencies.

This is not a generic "10 things every startup needs" list. It's a tailored action plan that accounts for your data handling requirements, your geographic location, your integration dependencies, and your fundraising plans. The output ends with a "First 2 Weeks Sprint" — the 10-15 most critical actions in priority order so you know exactly what to do Monday morning.

## Phase 1: Business Context Questions

Ask these questions one at a time. Wait for the user's answer before moving to the next.

**If the user is stuck on any question:** Help them think through it — suggest common answers for their industry, ask clarifying follow-ups, or reframe. The goal is specific enough context to produce a tailored checklist, not a generic one.

**If the user truly can't answer one** (e.g., they haven't thought about insurance yet), note it and include recommendations in the checklist.

### The 8 Questions

**Q1: "What does your product/business do, and who are your first customers?"**
Not the vision pitch. The specific thing you're launching and who's paying for it first. Are they consumers or businesses? How many first customers do you have lined up?

*If stuck, ask:* "If someone asked 'what do you sell and to whom?' — what's the one-sentence answer?"

**Q2: "What's your current stage?"**
Is the product built? Prototype? MVP live with bugs? Feature-complete? What works and what doesn't yet? Have you had any real users touch it?

*If stuck, ask:* "Could a customer use your product today and get value from it, or are there things that need to be built/fixed first?"

**Q3: "What data do you handle?"**
This determines your compliance requirements. Do you touch any of: customer PII (names, emails, phone numbers), payment/financial data, health records (HIPAA), location data, OAuth tokens or API keys, children's data (COPPA)? Be exhaustive.

*If stuck, ask:* "Walk me through what happens when a customer signs up and starts using your product. What information do you collect, store, or process along the way?"

**Q4: "Where are you located, and where are your customers?"**
State and country for you (determines entity formation and tax obligations). State/country for your customers (determines privacy law compliance — CCPA, GDPR, etc.). If your customers are nationwide or global, say so.

*If stuck, ask:* "Where is your home base, and are your customers primarily local, national, or international?"

**Q5: "What's your business model and pricing?"**
How do customers pay? Subscription (monthly/annual), one-time purchase, usage-based, freemium? What are your planned price points? Have you validated pricing with anyone?

*If stuck, ask:* "How will money move from the customer to you? And roughly how much per customer per month or per transaction?"

**Q6: "What third-party integrations or partnerships do you depend on?"**
APIs you need to connect to, partner programs you need approval from, platform certifications required. These often have multi-week approval processes that gate your entire launch timeline.

*If stuck, ask:* "Does your product need to connect to any other system to work? Payment processors, data sources, marketplaces, partner APIs?"

**Q7: "What's your budget and timeline for launch?"**
How much can you allocate to legal, compliance, insurance, and operational setup? When do you need to be live with paying customers? Is the timeline flexible or fixed?

*If stuck, ask:* "Roughly how much could you spend on lawyers, incorporation, insurance, and setup? And is there a hard date you need to launch by?"

**Q8: "Are you planning to raise funding?"**
If yes: what type (SAFE, convertible note, priced round), how much, at what valuation, and when? This affects entity structure decisions (LLC vs C-Corp, state of incorporation) and changes the urgency of several checklist items.

*If stuck, ask:* "Are you self-funding this, or do you plan to bring in outside money at some point? If raising, is that in the next 3 months or the next 12?"

## Phase 2: Generate the Launch Checklist

After gathering all 8 answers, generate a structured checklist with these 10 categories. Tailor every item to the user's specific context — no generic advice.

### Priority Tags

Every item gets one tag:
- **🔴 BLOCKER** — Customers literally cannot go live without this. Legal requirements, compliance items, integration approvals that gate launch.
- **🟡 IMPORTANT** — Should happen within first 90 days. Needed for sustainable operations but doesn't block day-one launch.
- **🟢 NICE-TO-HAVE** — Valuable but can defer. Won't hurt you in the first quarter if missing.

### Category 1: Legal Entity Formation

- Entity type recommendation with reasoning (LLC vs C-Corp vs S-Corp; state of incorporation)
- EIN application
- Operating agreement or bylaws
- Registered agent setup
- State-specific requirements (California Statement of Information, Delaware franchise tax, etc.)

Include cost estimates and timeline for each item.

### Category 2: Contracts & Agreements

- Customer terms of service / SaaS agreement
- Design partner or pilot agreements (if applicable)
- Contractor/employee agreements (if applicable)
- NDA template
- Partnership agreements (if integrations require them)

### Category 3: Data Privacy & Compliance

Tailored to the data types from Q3 and geography from Q4:
- Privacy policy (must cover specific data types handled)
- Data Processing Agreement (DPA) if B2B
- Cookie consent / tracking disclosure
- CCPA compliance (if California customers)
- GDPR compliance (if EU customers)
- HIPAA (if health data)
- SOC 2 readiness assessment (usually 🟢 for early stage unless enterprise customers require it)
- Data retention and deletion policy
- Consent management implementation

### Category 4: Insurance

- Cyber liability / data breach insurance
- Errors & Omissions (E&O) / Professional Liability
- General liability
- Directors & Officers (D&O) — if raising funding

Include typical cost ranges for startups at this stage.

### Category 5: Financial Setup

- Business bank account
- Accounting system (QuickBooks, Xero, etc.)
- Payment processing setup (Stripe, etc.)
- Sales tax registration / nexus obligations
- Bookkeeping arrangement
- Financial controls (dual authorization, expense tracking)

### Category 6: Integration Partnerships

Tailored to Q6 — for each integration dependency:
- Partner program application process
- API access requirements
- Approval timeline estimate
- Technical requirements (sandbox, certification testing)
- **Flag the critical path** — identify the longest-timeline dependency and mark it as day-1 priority

### Category 7: Customer Onboarding

- Onboarding flow / setup wizard
- Welcome email sequence
- Support channel setup (email, chat, phone)
- Help documentation / knowledge base
- Feedback collection mechanism
- Success metrics definition

### Category 8: Product Readiness

- Error monitoring and alerting
- Data backup and recovery
- Security hardening (HTTPS, input validation, auth)
- Rate limiting on APIs
- Load testing / performance baseline
- Logging and audit trail
- Environment separation (dev/staging/production)

### Category 9: Brand & IP

- Trademark search and filing
- Domain registration and protection (common misspellings, .com/.io/.co)
- Social media account reservation
- Brand guidelines (if not already established)
- Logo and visual assets

### Category 10: Fundraising Readiness (if applicable)

Only include if user answered yes to Q8:
- Entity structure aligned with funding type
- SAFE or convertible note templates
- Data room setup (financial model, cap table, product metrics)
- Pitch deck requirements
- Legal counsel for fundraise

### First 2 Weeks Sprint

Extract the 10-15 most critical actions from the full checklist, ordered by priority:
1. Start with the critical path item (longest external dependency)
2. Then legal blockers
3. Then compliance blockers
4. Then financial setup
5. Then product readiness items

For each sprint item, include: what to do, estimated time, estimated cost, and any dependencies.

### Cost Summary

Total estimated costs across all categories:
| Category | Estimated Range |
|----------|----------------|
| Legal Entity | $X - $X |
| Contracts | $X - $X |
| Compliance | $X - $X |
| Insurance | $X - $X |
| ... | ... |
| **Total** | **$X - $X** |

## Rules

- **Never give generic advice.** Every item must be tailored to the specific business, industry, and regulatory environment described in Phase 1.
- **Priority tags must reflect real launch dependencies.** 🔴 BLOCKER means customers cannot legally or technically go live without it — not "it would be nice to have."
- **Always identify the critical path.** The longest-timeline external dependency (partner approvals, compliance certifications) determines launch speed and must be started immediately.
- **Cost estimates must be realistic ranges.** Use actual market rates for lawyers ($200-$500/hr), incorporation services ($500-$2,000), insurance ($500-$3,000/yr for startups), etc. Don't make up numbers.
- **Flag where the founder needs a lawyer vs. can DIY.** Terms of service templates exist, but DPAs for enterprise customers need legal review. Be specific.
- **Don't recommend SOC 2 as a blocker** for pre-revenue startups unless their customers explicitly require it. It's a 6+ month, $20K+ process.
- **Include state-specific requirements** when the user's location is known. California has different requirements than Delaware, Texas, or New York.
- **Integration dependencies must include timeline estimates.** "Apply to Toast partner program" without "4-8 week approval process" is useless.
- **Pilot pricing belongs in the checklist.** If launching with first customers, include a note about founding customer pricing (90-day free pilot or 60-70% discount) rather than assuming full-price from day one.

## What This Skill Does NOT Do

- File legal paperwork (it tells you what to file and provides guidance, but you need a lawyer or service for execution)
- Write your terms of service or privacy policy (it tells you what they need to cover)
- Build your product or fix bugs
- Create your pitch deck or financial model (use generate-saas-financial-model for that)
- Provide tax advice (consult a CPA)
- Set up your actual payment processing or accounting tools
