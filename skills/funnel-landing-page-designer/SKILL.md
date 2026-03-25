---
name: funnel-landing-page-designer
description: Generate complete, deployable HTML/CSS landing pages optimized for conversion. Use when user wants to build, create, or ship a landing page — mentions opt-in page, sales page, webinar registration, thank you page, tripwire, or application page. Also use when user says "I need a page for my offer," "build me a landing page," "create a signup page," "I need a page that converts," or any request involving a deployable web page for a funnel. This is the ONLY skill that produces shipped code — a complete HTML file someone can open in a browser and deploy immediately. Every other skill produces strategy or architecture. This one produces the actual page. Works for any brand — pairs with build-irresistible-offer for offer details, generate-persona-playbook for audience targeting, and extract-testimonial-stories for social proof.
---

# Funnel Landing Page Designer

## What This Skill Does

Takes an offer, a persona, and a page type, then generates a complete, self-contained HTML/CSS landing page ready to deploy. No frameworks. No CDN links. No JavaScript dependencies. One file, opens in a browser, works on mobile, converts visitors.

This is not strategy. This is not architecture. This is shipped code.

Every section is conversion-optimized using the AIDA structure (Attention, Interest, Desire, Action). Every CTA is backed by social proof. Every pixel serves the single goal of the page.

If the user has output from build-irresistible-offer, generate-persona-playbook, extract-testimonial-stories, or design-pricing-architecture, this skill consumes that output and turns it into a real page.

## Phase 1: Landing Page Discovery

Ask these questions one at a time. Wait for the user's answer before moving to the next.

**If the user is stuck on any question:** Don't just repeat it. Help them think through it — suggest options based on what they've already told you, offer examples from common patterns, or reframe the question. The goal is to get a real answer, not a placeholder.

**If the user has output from companion skills** (build-irresistible-offer, generate-persona-playbook, extract-testimonial-stories), reference that output instead of making them repeat themselves.

### The 7 Questions

**Q1: "What type of landing page do you need?"**
The page type determines the entire structure. Each type has a different layout, length, and conversion goal.

Options:
- **Opt-in / Lead Magnet Page** — Minimal. Headline, benefit bullets, email capture.
- **Sales Page (Long-form)** — Full AIDA structure with all sections. For paid offers.
- **Webinar Registration Page** — Event details, speaker bio, what they'll learn, countdown.
- **Thank You / Confirmation Page** — Next steps, order bump, social share.
- **Tripwire / Low-ticket Offer Page** — Short sales page with urgency. Usually under $50.
- **Application / High-ticket Page** — Qualification-focused. Book a call CTA.

*If stuck, ask:* "What's the ONE thing you want the visitor to do on this page? Give their email? Buy something? Register for an event? Apply for a call? That tells me the page type."

**Q2: "What's the offer?"**
What are they getting? What's the price (if applicable)? What's the headline promise?

If they've already run build-irresistible-offer, pull the offer name, transformation, value stack, and guarantee from that output.

*If stuck, ask:* "Complete this sentence: 'Get [specific result] by [your method] in [timeframe].' That's your offer in one line."

**Q3: "Who is the visitor? What's their awareness level?"**
The copy tone, length, and proof requirements all depend on who lands on this page and how much they already know.

If they've already run generate-persona-playbook or map-awareness-to-messaging, reference that output.

- **Cold traffic** (never heard of you) — needs more proof, longer page, education before CTA.
- **Warm traffic** (on your list, referred, saw your content) — shorter page, faster to CTA, assumes some trust.
- **Hot traffic** (ready to buy, returning visitors) — minimal friction, direct CTA.

*If stuck, ask:* "Is the person landing on this page cold (never heard of you), warm (already on your list or referred by someone), or hot (already decided and just needs the link)?"

**Q4: "What proof do you have?"**
Testimonials, case studies, client logos, stats, credentials, media mentions, certifications. List everything available.

If they've already run extract-testimonial-stories, use those formatted testimonials directly.

*If stuck, ask:* "Even one or two testimonials help. Do you have any client quotes, results, screenshots, or before/after stories? If you've used extract-testimonial-stories, share that output."

**Q5: "What's your brand style?"**
This determines the visual design of the page.

Need:
- **Colors**: Primary, secondary, accent (CTA button color)
- **Fonts**: Preferred fonts or general style
- **Vibe**: Clean/minimal, bold/energetic, warm/friendly, professional/corporate
- **Logo**: URL or description (will be a placeholder if not provided)

*If stuck, ask:* "Give me 2-3 websites whose look you like. Or just pick one: minimal, bold, warm, or corporate. I'll handle the rest."

**Q6: "What's the CTA?"**
What does the button say? Where does it go?

- Button text: "Get Started," "Buy Now," "Book Your Call," "Download Free Guide," etc.
- Destination: Form submission, checkout URL, calendar link, external URL

*If stuck, ask:* "What do you want the button to say? And when someone clicks it, what happens — do they fill out a form on this page, go to a checkout, or book a call?"

**Q7: "Any specific sections you want included or excluded?"**
The default structure depends on page type. But you might want to add or remove:

- Countdown timer placeholder
- Video embed placeholder
- Comparison table (us vs. them)
- Pricing table
- FAQ section
- Guarantee badge
- Speaker/author bio section
- "As seen in" logo bar

*If stuck, ask:* "I'll include the standard sections for your page type. Want to add anything special (video, countdown, comparison table) or remove anything?"

## Phase 2: Complete Landing Page

After gathering all answers, produce four sections in order.

### Section 1: Page Architecture

Before writing any code, show the page structure as a text wireframe. This lets the user approve or adjust the layout before you build it.

Format the wireframe based on the page type selected. Example for a long-form sales page:

```
[HEADER] Logo (left) | Optional nav link (right)
─────────────────────────────────────────────────
[HERO] Headline | Subheadline | CTA Button | Hero Image Placeholder
─────────────────────────────────────────────────
[PROBLEM] 3 pain points | "Sound familiar?"
─────────────────────────────────────────────────
[SOLUTION] Your approach | How it works (3 steps)
─────────────────────────────────────────────────
[SOCIAL PROOF] 2-3 testimonials | Trust badges
─────────────────────────────────────────────────
[BENEFITS] Feature/benefit grid (4-6 items)
─────────────────────────────────────────────────
[VALUE STACK] What's included | Perceived value table
─────────────────────────────────────────────────
[FAQ] 4-6 questions with answers
─────────────────────────────────────────────────
[FINAL CTA] Restate offer | CTA Button | Guarantee
─────────────────────────────────────────────────
[FOOTER] Copyright | Privacy link | Terms link
```

Adjust the wireframe per page type:
- **Opt-in page**: Header, Hero (with form), Social Proof, Footer
- **Webinar page**: Header, Hero (with date/time), What You'll Learn, Speaker Bio, Social Proof, Registration Form, Footer
- **Thank you page**: Header, Confirmation Message, Next Steps, Order Bump (optional), Social Share, Footer
- **Tripwire page**: Header, Hero, Problem, Solution, Social Proof, Offer + Price, CTA, Footer
- **Application page**: Header, Hero, Who This Is For, Process, Social Proof, Application Form/Book Call CTA, Footer

### Section 2: The HTML/CSS Page

Generate a COMPLETE, self-contained HTML file. The file must work immediately when opened in a browser. No external dependencies of any kind.

**HTML requirements:**
- Semantic HTML5 (`<header>`, `<main>`, `<section>`, `<footer>`)
- Proper `<meta>` viewport tag for mobile
- Descriptive `<title>` tag
- Form elements with proper `<label>` elements (not just placeholders)
- Accessible markup: alt text on images, ARIA labels where needed, logical heading hierarchy
- Smooth scroll behavior for anchor links
- Placeholder images with descriptive comments: `<!-- Replace with: product mockup, 800x600 -->`

**CSS requirements:**
- All CSS embedded in `<style>` within the `<head>` — no external stylesheets
- CSS custom properties at `:root` for all colors, fonts, and spacing — easy to customize
- Mobile-first media queries with breakpoints at 768px and 1024px
- BEM-like class naming for clarity (e.g., `.hero__headline`, `.cta__button`)
- Fluid typography using `clamp()` for headlines and body text
- System font stack with readable fallbacks
- WCAG AA contrast ratios for all text
- CTA buttons: large tap targets (min 48px height), high-contrast color, clear hover/focus states
- No CSS frameworks — pure CSS only

**CSS custom properties example:**
```css
:root {
  --color-primary: #2563eb;
  --color-secondary: #1e293b;
  --color-accent: #f59e0b;
  --color-bg: #ffffff;
  --color-bg-alt: #f8fafc;
  --color-text: #334155;
  --color-text-light: #64748b;
  --color-cta: #2563eb;
  --color-cta-hover: #1d4ed8;
  --color-cta-text: #ffffff;
  --font-heading: system-ui, -apple-system, sans-serif;
  --font-body: system-ui, -apple-system, sans-serif;
  --spacing-section: clamp(3rem, 8vw, 6rem);
  --max-width: 1200px;
}
```

**Conversion design principles baked in:**
- F-pattern reading flow
- CTA button appears at LEAST 3 times on long-form pages (hero, mid-page, footer)
- Social proof positioned near every CTA
- Whitespace prioritized over clutter
- Above-the-fold contains: headline, value proposition, CTA
- Single-column layout for readability on all devices

**Copy rules:**
- Never use lorem ipsum — write real copy based on the offer and persona provided
- If build-irresistible-offer output exists, use the value stack and guarantee verbatim
- If extract-testimonial-stories output exists, use the formatted testimonials
- If generate-persona-playbook output exists, match the copy to the persona's language
- If brand-voice-router is active, apply that voice to all copy blocks
- Apply humanize-ai-writing principles to all copy — no corporate filler, no buzzwords, real human language

Save the file as `landing-page.html` or name it after the offer (e.g., `6-week-accelerator-landing-page.html`).

### Section 3: Customization Guide

Provide a quick-reference table so the user can tweak the page without reading all the CSS:

**Colors:**
| What to change | CSS variable | Current value |
|---------------|-------------|---------------|
| Primary brand color | `--color-primary` | #value |
| CTA button color | `--color-cta` | #value |
| Background | `--color-bg` | #value |
| Text color | `--color-text` | #value |

**Fonts:**
- Heading font: change `--font-heading` in `:root`
- Body font: change `--font-body` in `:root`
- To use Google Fonts: add `<link>` in `<head>` and update the variable

**Images to replace:**
List every placeholder with its location and recommended dimensions:
- Hero image: line ~XX, recommended 800x600 or 1200x800
- Testimonial headshots: line ~XX, recommended 80x80, circular
- Logo: line ~XX, recommended 200x60

**Copy blocks to update:**
- Headline: line ~XX
- Subheadline: line ~XX
- Testimonial quotes: lines ~XX-XX
- FAQ answers: lines ~XX-XX

**CTA button:**
- Button text: search for `class="cta__button"` — update the inner text
- Button link: update the `href` attribute on the same element

### Section 4: Conversion Optimization Checklist

Score the generated page against conversion best practices:

| Element | Present | Notes |
|---------|---------|-------|
| Headline above the fold | /  | |
| Clear value prop in under 5 seconds | /  | |
| Single CTA (repeated) | /  | How many times it appears |
| Social proof near CTA | /  | Which sections |
| Mobile responsive | /  | Tested at 375px, 768px, 1024px |
| Fast load (no external deps) | /  | Single file, no CDN |
| CTA button contrast | /  | Contrast ratio |
| FAQ handles top objections | /  | Number of FAQs |
| Urgency/scarcity (if real) | /  | Only if genuine |
| Accessible forms (labels, not just placeholders) | /  | |
| WCAG AA text contrast | /  | |
| Logical heading hierarchy (h1 > h2 > h3) | /  | |

Mark any missing elements with a note explaining why (e.g., "No urgency — user has no real deadline. Don't fake it.").

## Rules

- Output must be a COMPLETE, self-contained HTML file — no external CSS, no CDN links, no JavaScript frameworks
- Mobile-first responsive design is non-negotiable — most landing page traffic is mobile
- One page, one goal, one CTA — never mix multiple offers on one page
- CTA button must appear at LEAST 3 times on a long-form page (hero, mid-page, footer)
- Social proof must appear NEAR every CTA — proof and action go together
- Never use lorem ipsum — write real copy based on the offer and persona information provided
- Placeholder images must have descriptive comments: `<!-- Replace with: product mockup, 800x600 -->`
- Colors must meet WCAG AA contrast ratios for text readability
- Forms must have proper `<label>` elements, not just placeholders (accessibility)
- The hero section must communicate the value proposition in under 5 seconds of reading
- If build-irresistible-offer output exists, use the value stack and guarantee from it
- If extract-testimonial-stories output exists, use the formatted testimonials from it
- If generate-persona-playbook output exists, match copy to the persona's language patterns
- If brand-voice-router is active, apply that brand voice to all copy blocks
- Apply humanize-ai-writing principles to all copy — no corporate jargon, no filler, real language
- File should be saved as `landing-page.html` or named after the offer
- Ask Phase 1 questions ONE AT A TIME — do not dump all seven at once

## What This Skill Does NOT Do

- **Set up hosting, domains, or DNS** — this produces the file, not the infrastructure
- **Create backend form processing** — provides the HTML form, not the server handler (use Formspree, Netlify Forms, or your own backend)
- **Write JavaScript-heavy interactions** — keeps it simple, fast, and accessible
- **Design email sequences** that drive traffic to the page — use build-email-story-engine
- **Build the offer itself** — use build-irresistible-offer to architect the offer first
- **Handle A/B testing setup** — deploy the page, then use your testing tool
- **Create animations or complex interactions** — speed and clarity beat flash
- **Generate traffic** — this builds the destination, not the journey to it

## Companion Skills

**Chains FROM (use their output as input):**
- build-irresistible-offer — the offer details, value stack, guarantee
- build-conversion-sales-letter — copy architecture and messaging hierarchy
- extract-testimonial-stories — formatted social proof
- generate-persona-playbook — audience language and awareness level
- design-pricing-architecture — pricing tables and tier structures
- map-awareness-to-messaging — headline and copy angle by awareness stage

**Chains TO (this page feeds into):**
- design-launch-sequence — orchestrate the traffic driving to this page
- build-email-story-engine — post-conversion email sequences
- funnel-ad-creator — ads that point to this page
