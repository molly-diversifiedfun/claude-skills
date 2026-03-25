---
name: extract-testimonial-stories
description: Turns raw customer success stories into formatted social proof assets — pull quotes, case studies, video scripts, ad copy, and landing page testimonials. Use when user wants to create testimonials, build social proof, capture customer stories, write case studies, or format success stories for marketing. Trigger on phrases like "I need testimonials," "customer success story," "social proof," "case study," "someone said something great about my product," "how do I use this testimonial," "I have customer feedback," "I need proof for my sales page," or any request to capture, format, or deploy customer stories. This is a FORCE MULTIPLIER skill — its output feeds into every other skill that needs proof. Pairs with brand-voice-router for surrounding copy voice and humanize-ai-writing for case study narratives.
---

# Extract Testimonial Stories

## What This Skill Does

Takes raw customer success stories — emails, DMs, call transcripts, reviews, casual texts, even vague "it was great" statements — and transforms them into a complete testimonial asset portfolio. Every story gets scored for depth, structured into a full SOAR case study, then reformatted into seven deployment-ready formats: pull quotes, social proof snippets, before/after cards, ad copy, email blocks, video scripts, and landing page testimonial blocks.

This skill does not just format quotes. It extracts the narrative structure hiding inside raw customer feedback, identifies gaps in story depth, and produces a placement map so every testimonial lands in the context where it hits hardest. It also builds a system for collecting stronger testimonials going forward — because the best social proof is a renewable resource, not a one-time harvest.

The output is designed to plug directly into other skills: build-irresistible-offer gets proof for value claims, funnel-ad-creator gets ad-ready testimonials, build-conversion-sales-letter gets testimonial sections, and design-launch-sequence gets social proof for every stage of the launch.

## Phase 1: Story Discovery Questions

Ask these questions one at a time. Wait for the user's answer before moving to the next.

**If the user is stuck on any question:** Don't just repeat it. Help them think through it — suggest where to look (inbox, DMs, text messages), offer examples of what a good answer looks like, or reframe the question. The goal is to get real material to work with, not placeholders.

**If the user truly can't answer one** (e.g., no direct quotes exist), note it as a gap and keep moving. Flag it in Section 5 of the portfolio.

### The 6 Questions

**Q1: "Tell me about the customer(s) whose story you want to capture."**
Name, business, what they bought from you, how long ago. The more context, the better the story.

*If stuck, ask:* "Start with your best success story. Who had the biggest transformation? If you can only think of one person, that's fine — we'll build from there."

**Q2: "What was their situation BEFORE working with you?"**
Specific details — the messier and more real, the better. What were they struggling with? What had they already tried that failed? How did the problem affect their daily life or business?

*If stuck, ask:* "Picture them the week before they found you. What was frustrating them? What had they already tried? How did they feel about the problem — stressed, overwhelmed, skeptical, desperate?"

**Q3: "What specific results did they achieve?"**
Numbers are gold: revenue increase, time saved, customers gained, cost reduced, conversion rate improvement. Emotional results matter just as much: confidence, clarity, relief, pride. Get both.

*If stuck, ask:* "What changed? Give me the before number and the after number. If it's not numerical, what's different about their daily life now? What can they do now that they couldn't before?"

**Q4: "Do you have their exact words — texts, emails, DMs, reviews, recorded calls?"**
Direct quotes are 10x more powerful than paraphrased stories. Paste them in raw — typos, emoji, casual language and all. That authenticity is the point.

*If stuck, ask:* "Check your inbox, DMs, Slack messages, or text messages. Customers often share wins in casual messages that are perfect testimonials. Even a 'holy crap this worked!' text is usable. Also check Google reviews, Trustpilot, or any review platform."

**Q5: "Where do you need to USE these testimonials?"**
Landing pages, sales emails, ad campaigns, social proof sections, presentations, proposals, webinars, social media posts. Be specific about which channels matter most.

*If stuck, ask:* "Where are you currently missing social proof? Where would a testimonial make the biggest difference right now — your sales page, your ads, your emails, or somewhere else?"

**Q6: "How many customer stories do you want to process?"**
A strong proof portfolio typically has 3-5 stories covering different customer personas and use cases. But even 1-2 strong stories are enough to start.

*If stuck, ask:* "Even 2-3 strong stories are enough to build a solid proof portfolio. Quality over quantity — one deep story beats five shallow ones. Start with however many you have."

## Phase 2: Generate the Testimonial Story Portfolio

After gathering all 6 answers, generate a structured portfolio with these 6 sections. Use the user's raw material — don't sanitize real customer language into corporate speak. Synthesize, structure, and fill gaps, but preserve the human voice.

### Section 1: Story Depth Score

For each customer story, score on the 4-Layer Testimonial Depth Model:

| Layer | Description | Present? | Content | Score |
|-------|-------------|----------|---------|-------|
| **Layer 1: Surface Statement** | Generic positive reaction ("It was great!") | Y/N | [the statement] | /10 |
| **Layer 2: Specific Result** | Measurable outcome ("Revenue increased 40%") | Y/N | [the metric/outcome] | /10 |
| **Layer 3: Emotional Transformation** | Feeling change ("I finally feel confident") | Y/N | [the feeling] | /10 |
| **Layer 4: Identity Shift** | New self-concept ("I see myself as a real business owner") | Y/N | [the new identity] | /10 |
| **Total Depth Score** | | | | **/40** |

**Scoring criteria:**
- **8-10:** Rich, specific, quotable material exists for this layer
- **5-7:** Material exists but is vague or could be stronger
- **1-4:** Barely present — implied but not stated
- **0:** Missing entirely

**For any story scoring below 25/40:** Flag it as needing depth reinforcement. Provide 2-3 specific follow-up questions the user can ask the customer to strengthen the weak layers.

**For missing layers:** Write the exact question to ask the customer. Examples:
- Missing Layer 2: "Can you put a number on it? How much time/money/effort did this save you compared to before?"
- Missing Layer 3: "How did it feel when [the result] happened? What changed emotionally?"
- Missing Layer 4: "Do you think about yourself or your business differently now? Has your identity or confidence shifted?"

### Section 2: SOAR Narrative (Full Case Study)

For each customer, write a complete case study using the SOAR framework:

**[Customer Name] — [One-Line Transformation Statement]**

**SITUATION:** 2-3 paragraphs painting the before state. Specific, detailed, empathetic. Use the Before-After-Bridge framework to make the reader feel the pain. Include what they had already tried that failed. This should read like the opening of a story, not a corporate brief.

**OBSTACLE:** The specific challenge that was blocking them. Not just "they needed help" — the real barrier. Was it knowledge, time, confidence, a broken system, bad advice from someone else? Name it.

**ACTION:** What they did — your solution, framed as THEIR journey. The customer is the hero (StoryBrand principle). Your product/service is the guide that gave them a plan. Describe the experience of working with you through their eyes.

**RESULT:** Measurable outcomes first (numbers, timelines, comparisons). Then emotional outcomes (confidence, relief, clarity). Then forward-looking impact (what's now possible that wasn't before). Include a timeline — when did results appear?

**Word count:** 400-600 words per case study. Long enough to tell a real story, short enough to hold attention.

### Section 3: Multi-Format Testimonial Assets

For each customer story, generate ALL seven of these formats:

**A. Pull Quote (1 line)**
The single most powerful sentence from their story. In their voice, with quotation marks. This should be the line that stops someone mid-scroll. Punchy, specific, emotional.

*If no direct quote exists, construct one from their story and mark it [CONSTRUCTED — get customer approval before using].*

**B. Social Proof Snippet (2-3 sentences)**
For embedding in sales pages, emails, or proposals. Result-focused. Opens with the transformation, closes with the specific outcome. Include customer name and relevant context (title, company, or situation descriptor).

**C. Before/After Card**

| Before | After |
|--------|-------|
| [specific painful state] | [specific transformed state] |
| [metric before] | [metric after] |
| [feeling before] | [feeling after] |

The contrast must be dramatic. If before and after look too similar, the card is not strong enough — flag it and recommend how to sharpen the contrast.

**D. Ad Copy Testimonial (for paid social)**
50-100 words. Hook line (the most surprising or relatable part of their story) + transformation + specific result. Formatted for Meta/Instagram ads. First line must stop the scroll.

**E. Email Testimonial Block**
A paragraph that can be dropped into any email sequence. Includes the customer's name, their situation before, and their result after. Written to feel like a natural aside in an email — not a bolted-on testimonial section.

**F. Video Testimonial Script (60-90 seconds)**
If the customer would record a video, provide a conversational script following SOAR structure:
- **Opening hook** (5-10 seconds): The most compelling single line from their story
- **Situation** (15-20 seconds): Where they were before
- **Turning point** (15-20 seconds): What they did and why they chose this solution
- **Result** (15-20 seconds): What changed — numbers and feelings
- **Advice to others** (10-15 seconds): What they'd say to someone in their old situation

Write it the way people actually talk — contractions, casual phrasing, natural pauses. Not a corporate script.

**G. Landing Page Testimonial Block**
A structured block ready for insertion into any landing page. Includes:
- The pull quote (large, prominent)
- Customer name, title/role, and company (or relevant descriptor)
- The key metric as a standalone callout (e.g., "40% revenue increase in 90 days")
- A 2-3 sentence supporting context paragraph
- Photo placeholder notation

Format as a semantic content block the user can hand to a designer or developer.

### Section 4: Testimonial Placement Map

Based on the user's answer to Q5, show where each format should be deployed:

| Asset Format | Where to Use | Which Customer Story | Why This Story Here |
|-------------|-------------|---------------------|-------------------|
| Pull Quote | [specific placement] | [Customer Name] | [reasoning — strongest line, most relevant persona, etc.] |
| Before/After Card | [specific placement] | [Customer Name] | [reasoning — most dramatic contrast] |
| Social Proof Snippet | [specific placement] | [Customer Name] | [reasoning — best for this context] |
| Ad Copy | [specific placement] | [Customer Name] | [reasoning — best specific result for ads] |
| Email Block | [specific placement] | [Customer Name] | [reasoning — most relatable for email audience] |
| Full Case Study | [specific placement] | [Customer Name] | [reasoning — most complete narrative] |
| Video Script | [specific placement] | [Customer Name] | [reasoning — most camera-ready story] |
| Landing Page Block | [specific placement] | [Customer Name] | [reasoning — strongest proof for conversion] |

**Matching rules:**
- Sales page hero section gets the single strongest pull quote
- Ad campaigns get the story with the most specific, surprising result
- Email sequences get the most relatable, conversational story
- Proposals and decks get the most credentialed or enterprise-relevant story
- Landing pages get the story with the strongest before/after contrast

### Section 5: Proof Gap Analysis

Audit the full testimonial portfolio against five dimensions:

**Missing Metrics**
Which stories lack specific numbers? For each, provide the exact follow-up question to ask the customer to get the metric. Example: "You mentioned things improved — can you estimate the percentage change? Even a rough number like 'about 2x' works."

**Missing Emotional Depth**
Which stories lack Layer 3 (emotional transformation) or Layer 4 (identity shift)? For each, provide a follow-up question. Example: "Beyond the business results, how did this change how you feel about [the domain]? Do you see yourself differently now?"

**Missing Diversity**
Do all stories come from similar customers? Map the testimonials by:
- Customer persona/segment
- Use case or product feature highlighted
- Result type (financial, time, emotional, operational)
- Business size/stage

Flag any personas or use cases from Q5 that lack representation. Recommend which type of customer story to collect next.

**Missing Formats**
Cross-reference Q5 deployment contexts against available assets. Flag any deployment context that does not have a matching, strong testimonial asset. Recommend which existing story could be reformatted, or whether a new story is needed.

**Freshness**
How old are the stories? Testimonials older than 12 months should be flagged for refresh. Recommend circling back to the customer for updated results — often the long-term results are even more impressive than the initial ones.

### Section 6: Testimonial Collection System

Provide a repeatable system for gathering strong testimonials going forward:

**When to Ask**
At the moment of peak satisfaction — right after a milestone is hit, after results are reported, after a positive interaction. Not at the end of a contract (too late, too formal). Map out 3-5 specific trigger moments in the user's customer journey where asking makes sense.

**How to Ask — 3 Scripts**

**Script 1: Email Ask**
A short, warm email template that makes it easy for the customer to say yes. Includes the 4 structured questions (SOAR format) so they can respond in writing.

**Script 2: DM/Text Ask**
A casual, 2-3 sentence message for platforms like Slack, Instagram DMs, or text. Low friction, high response rate. Designed to capture the win in the moment.

**Script 3: In-Person/Call Ask**
A conversational framework for asking during a call or meeting. Not a script to read — a sequence of prompts that guide the customer through their story naturally.

**The 4 SOAR Interview Questions**
A structured template the user can use in any format:
1. "What was your situation before we started working together?"
2. "What made you decide to work with us? What had you already tried?"
3. "What was the experience like? Walk me through it."
4. "What results have you seen? What's different now — in numbers and in how you feel?"

**Permission Template**
A simple, professional permission-to-use template that covers:
- What will be used (name, quote, photo, company name)
- Where it will be used (website, ads, email, social media)
- Right to edit for brevity (not meaning)
- Right to revoke at any time
- Signature/confirmation line

**Follow-Up Cadence**
- **Immediate:** Capture the win when it's reported (DM script)
- **1 week later:** Send the formal ask with SOAR questions (email script)
- **3 months later:** Circle back for updated results (often stronger)
- **12 months later:** Check for long-term transformation (identity shift stories live here)

## Rules

- **Never fabricate or embellish testimonials.** Every word attributed to a customer must be real. If a direct quote does not exist, construct one from their story and clearly mark it [CONSTRUCTED — get customer approval before using].
- **Customer's actual language beats polished corporate language.** "This saved my ass" is better than "This was extremely beneficial." Preserve slang, casual phrasing, and real voice. Only clean up obvious typos if the user requests it.
- **Every testimonial needs at least ONE specific detail.** A number, a timeline, a before/after comparison. "It was great" is not a testimonial — it's a starting point. Flag vague statements and provide follow-up questions to add specificity.
- **Pull quotes must be quotable.** Punchy, specific, and emotional. If a pull quote could describe any product or service, it's too generic. Rewrite or flag.
- **Before/After cards must show contrast.** If the before and after states look too similar, the testimonial is not strong enough. Flag it and recommend how to sharpen the gap.
- **Video scripts must sound conversational.** Write them the way people actually talk — contractions, natural phrasing, occasional filler words. If it sounds like a press release, rewrite it.
- **Stories scoring below 25/40 on the 4-Layer model must be flagged.** Provide specific follow-up questions to strengthen them. Do not present weak stories as deployment-ready without noting the gaps.
- **Testimonials must match the audience who will read them.** A testimonial from a Fortune 500 exec will not resonate with a solopreneur audience, and vice versa. Note audience fit in the placement map.
- **Always include a permission/consent reminder.** At the top of the portfolio, remind the user to get written permission before publishing any testimonial. Include the permission template in Section 6.
- **If brand-voice-router is active,** format the surrounding copy (section headers, analysis, recommendations) in brand voice. Never alter direct customer quotes to match brand voice.
- **If humanize-ai-writing is available,** apply to case study narratives in Section 2. Never apply to direct customer quotes — those must remain authentic.
- **If generate-persona-playbook exists,** cross-reference testimonial selection against persona profiles in the placement map. Ensure each key persona has at least one matching testimonial.

## What This Skill Does NOT Do

- **Conduct customer interviews.** Provides the framework, questions, and scripts — the user conducts the actual interview or collects the raw material.
- **Create the offer or product** the testimonial is about. The thing being praised must already exist.
- **Write sales pages or landing pages.** Provides testimonial BLOCKS for insertion into pages built by other skills or tools.
- **Design visual testimonial graphics or cards.** Outputs text-based content blocks, not visual designs.
- **Handle legal review of testimonial usage.** Provides a permission template, but the user is responsible for legal compliance (FTC guidelines, platform-specific rules, etc.).
- **Fabricate any customer data, results, or quotes.** If the raw material is thin, this skill flags the gaps and provides tools to fill them — it does not invent proof.
