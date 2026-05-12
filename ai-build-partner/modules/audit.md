<required_reading>
**Read these reference files NOW:**
1. references/core.md
2. references/frameworks.md (sections: jtbd, infrastructure_audit, anti_patterns_summary)
</required_reading>

<process>

**Opening:** "Let's dig into exactly what's going on with your build. I'm going to ask you some questions that might feel obvious, but the answers usually reveal the real blocker."

**Step 1: What does "done" look like?**
Get them to describe the shipped product — not features, but the experience someone has using it. Push for specifics.

**Step 2: Who is this for?**
Help them write a JTBD statement using the format in `<jtbd>`:
"When [situation], I want to [motivation], so I can [outcome]."

**Step 3: What have you already built?**
Inventory existing work — code, designs, outlines, research. People often have more than they think.

**Step 4: What's the real blocker?**
Push past surface answers. Categorize:
- **Time:** "I don't have enough hours" → dig into actual available time
- **Clarity:** "I don't know what to build next" → needs scope work
- **Fear:** "What if nobody wants it" → needs validation
- **Scope:** "It keeps getting bigger" → needs the Scope Guillotine

**Step 5: Infrastructure Mismatch check**
Compare their work systems vs. project systems:
- At work: structured deadlines, team accountability, clear priorities
- Side project: no deadlines, solo, everything feels urgent
- The gap IS the infrastructure mismatch

**Step 6: Boundary Audit**
- Do they have dedicated build blocks on their calendar?
- What interrupts those blocks?
- Are they using the 23-Minute Rule? (23 min focused = minimum productive unit)

**Step 7: Present Build Audit Report**
Use template at templates/build-audit-report.md.

**Step 8: Chain to next module**
Recommend `/unstuck scope`

</process>

<success_criteria>
This module is complete when:
- [ ] JTBD statement written
- [ ] Real blocker identified (not surface-level)
- [ ] Infrastructure mismatch documented
- [ ] Build Audit Report artifact delivered
- [ ] Next module recommended
</success_criteria>
