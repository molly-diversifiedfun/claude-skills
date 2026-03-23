# Ask Me the Questions — Research Results

The optimal AI intake skill asks exactly **3 questions by default, never more than 5**, presents them one at a time (not as a batch), and follows a near-universal priority order: purpose, audience, then constraints. The evidence converges from UX form data, consulting methodology, and cognitive load research — and the most counterintuitive finding is that *how* you ask matters more than *how many* you ask. Multi-step presentation of identical questions converts **86% higher** than presenting them all at once.

Three tensions structure every design decision: thoroughness versus speed, personalization versus universality, and perceived effort versus actual effort.

---

## Q1: Four disciplines converge on the same opening move

**Consulting discovery (McKinsey/SCQA).** Barbara Minto's Situation-Complication-Question-Answer framework suggests asking first about the stable situation (baseline), then probing for the complication (what changed), which naturally surfaces the question. Hugo Sarrazin (McKinsey Senior Partner): "What are we trying to solve? What are the constraints? What are the dependencies?" Consultants attempt a "Day 1 answer" — a working hypothesis even after minimal information — then refine it. **3-5 structured exchanges** before switching to analysis.

**Design thinking (Stanford d.school/IDEO).** Canonical opening: "Tell me about the last time you..." Never ask binary questions, keep questions under ten words, ask one at a time, follow threads rather than scripts. The second question should always respond to what was actually said.

**Jobs-to-be-Done switch interview (Moesta/Spiek).** Start at the deliverable and work backward. Bob Moesta's "unbundle that" technique: when users say vague words like "professional" or "clean," probe what that means.

**AI/chatbot patterns.** Nielsen Norman Group (425 AI conversations): "funneling" pattern — user starts vague, AI adds constraints iteratively. ICLR 2025: standard RLHF training biases models against asking clarifying questions because single-turn preference labeling can't assess question value. A 2025 coding assistant uses a two-stage approach — an intent clarity classifier determines if input is under-specified before triggering clarification.

**Synthesis:** Open with a single broad question anchored on the deliverable. Adapt the second question by following whatever thread the user offered. Use "unbundle" probes when answers contain vague language. Switch to production after 3-5 exchanges, with a working hypothesis attempted as early as exchange 2.

**Confidence: High.**

---

## Q2: The cliff lives at five, but presentation shifts it dramatically

**HubSpot (40,000+ landing pages):** 3 fields optimal (~25% conversion), reducing from 4 to 3 increases conversions by nearly 50%. **Formstack:** each additional field reduces conversion by 5-10%. Steepest cliff between 3 and 6 fields: conversion drops from ~50% to ~20%.

**Chatbot-specific:** ShareChat dataset (142,808 conversations) found average 4.62 turns per LLM conversation. Most real-world AI interactions run 2-5 turns. Cowan's revised working memory capacity: **3-4 items**, not the popular 7±2.

**Critical counterpoint:** Context destroys these limits. WhatIsMyComfortZone.com achieved **53% completion on 30+ questions** when users expected a personalized result. **Multi-step forms convert 86% higher** than single-page equivalents with identical fields (Venture Harbour: 700% improvement). Pew Research: adaptive skip logic dropped abandonment from 23% to 9%.

**Adaptive questioning is essential.** Pew: adaptive sequencing trims effective survey length by 45%. Qualtrics 2024: personalized flows enhance perceived relevance by 58%. Hard ceiling should be task-dependent: 2-3 for simple tasks, 3-5 for medium, never exceeding 7.

**Confidence: High for form data, Medium for chatbot-specific.**

---

## Q3: Purpose and audience are universal; everything else is task-dependent

Every framework reviewed — creative briefs, requirements gathering, product requirements, prompt engineering guides — places **purpose/objective** and **audience/user** in the top two positions. Purpose partitions the largest solution space. Audience determines tone, complexity, format, and vocabulary simultaneously.

Below the top two, ordering is task-dependent: creative → format, technical → constraints, communication → tone. Default hierarchy: **Purpose → Audience → Constraints → Format → Tone**, with dynamic promotion of whichever dimension the user's input leaves most ambiguous.

**Confidence: Medium-High.** Top-two ordering robust across disciplines.

---

## Q4: Build standalone first, design for composability

Build standalone with a clean internal interface (question selection engine + context completeness detector + structured brief generator). Same core logic serves both direct users and programmatic callers. When invoked by another skill, it receives partial context, identifies what's missing, asks only the needed questions, returns a standardized context object.

Validated by Microsoft Azure guidance ("lowest complexity that meets requirements"), OpenAI's single-agent approach, and the Agent Skills Open Standard.

**Confidence: High on standalone-first. Medium on composability details.**

---

## Key design decisions

> **Default question count:** 3 questions default, hard ceiling of 5. HubSpot (40K pages), cognitive load research (3-4 items), average LLM conversation depth (4.62 turns) all converge.

> **Sequential vs. batched:** Always sequential, one at a time. Multi-step converts 86% higher.

> **Fixed script vs. adaptive:** Hybrid — follow universal priority (purpose → audience → constraints) but skip already-addressed dimensions and follow threads.

> **Transition signal:** Reflect back a one-sentence summary, state what you're about to produce, explicit "Should I go ahead?" checkpoint.

> **Complexity detection:** Yes — lightweight classifier on initial input. Simple tasks get 2 questions. Complex tasks get up to 5. Adaptive logic drops abandonment from 23% to 9%.

> **Architecture:** Standalone with composable interface (Option C).

---

## The universal intake protocol

**Opening move:** (1) Validate the request in one sentence, (2) Signal brevity — "Let me ask you a couple of quick questions so I can give you something actually useful," (3) Ask about purpose: "What's the main goal here — what do you need this to accomplish?"

**Adaptive middle:** Question 2 branches based on Q1. If purpose clear but audience ambiguous: "Who's going to read/use this?" If purpose implies known format, skip to constraints: "Any requirements — length, deadline, things to include or avoid?" If vague language detected, unbundle: "When you say 'professional,' what does that look like to you?" Internally tracks which of 5 dimensions (purpose, audience, constraints, format, tone) are resolved.

**Transition to production:** After 2-5 questions (adaptive): "Got it — so I'm making [deliverable] for [audience] that [key constraint]. Here's what I have..." Produces immediately. McKinsey "Day 1 answer" — complete working output from incomplete information, refined through iteration.

**Escape hatch:** User can say "just go" at any point. Skill detects when Q1 response is already rich enough to proceed. If someone writes two paragraphs of context, asking three more questions is insulting. The intake must always feel optional, never mandatory.
