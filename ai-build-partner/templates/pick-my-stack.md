<template>
```markdown
# Stack Manifest — [PRODUCT NAME]

**Date:** [TODAY]
**Product type:** [Q1]
**Technical level:** [Q2]
**Audience at launch:** [Q3]
**Budget:** [Q4]
**Compliance:** [Q6]
**Integration preference:** [Q7]
**Scale shape:** [Q8]

---

## The 9-Category Stack

| Category | Primary pick | Alternative | Monthly cost at [Q3 volume] |
|---|---|---|---|
| Payment | [...] | [...] | [...] |
| ESP | [...] | [...] | [...] |
| Hosting | [...] | [...] | [...] |
| Landing page | [...] | [...] | [...] |
| Analytics | [...] | [...] | [...] |
| DB | [...] | [...] | [...] |
| Auth | [...] | [...] | [...] |
| Forms | [...] | [...] | [...] |
| Domain | [...] | [...] | [...] |
| **Total** | | | **$[X]/mo** |

**Budget check:** Q4 ceiling was [$Q4]; manifest comes in at [$X]. [If over: see swap options below.]

---

## Reasoning (Per Category)

### Payment
[Why this pick over alternatives — 2-3 sentences. What ceiling triggers a swap.]

### ESP
[...]

### Hosting
[...]

### Landing page
[...]

### Analytics
[...]

### DB
[...]

### Auth
[...]

### Forms
[...]

### Domain
[...]

---

## Setup Order

Wire in dependency order, NOT alphabetical. Day-by-day Day 11-13 of the sprint:

1. **Day 11 morning:** Domain (24-48h DNS propagation — kick this off first)
2. **Day 11 afternoon:** Hosting + Landing page placeholder
3. **Day 12 morning:** ESP (sender domain, DKIM/SPF, first automation sequence)
4. **Day 12 afternoon:** Analytics snippet + Forms (lead magnet form)
5. **Day 13 morning:** DB + Auth (if applicable)
6. **Day 13 afternoon:** Payment — LAST. Most-broken. Wire after everything else works.

---

## Migration Paths (When Each Pick Hits Its Ceiling)

- **[Pick]** → swap to [Alt] when [specific trigger: subscriber count / DB size / feature need]
- [...]

---

## Claude/MCP-Friendly Priorities

**Already MCP-ready (use today):**
- [...]

**MCP-able / API-friendly (good for future Kit-stack-wire plugins):**
- [...]

**No MCP / locked out (avoid if Q7 = Claude/MCP-friendly):**
- [...]

[If Q7 = Claude/MCP-friendly:]

### Future Kit-stack-wire Plugins (Run 6 Track C — coming)

When these ship, your stack becomes wireable in minutes instead of hours:
- `/kit-stripe-init` — wires Stripe payment links + webhooks
- `/kit-resend-init` — Resend domain, sender, first 4-email automation
- `/kit-vercel-deploy` — deploys landing page with env vars + domain
- `/kit-supabase-bootstrap` — Supabase project with Kit-recommended schema

Picking the MCP-friendly bias now is a forward-investment.

---

## Budget Swaps (If Manifest > Q4)

[Only shown if total > Q4 budget. Up to 3 swaps listed:]

| Swap | Saves | Tradeoff |
|---|---|---|
| [Pick A → Pick B] | $[X]/mo | [What you lose] |
| [...] | [...] | [...] |

Net new monthly cost after swaps: $[X]. [If still over: flag that Q4 budget may be too low for Q1 product type.]

---

## What's Next

Recommended: `/unstuck sprint` to lay out Day 11-13 wiring as a tracked sprint block.

Pair with:
- **T13 The Tech Stack** (kit reference card — generic-category baseline)
- **T14 The Build Vault** (where you save your wiring docs, env vars, webhook URLs)

---

*Built with the Unstuck Method — [unstuckwithmolly.com](https://unstuckwithmolly.com?ref=ai-build-partner&module=pick-my-stack)*
```
</template>
