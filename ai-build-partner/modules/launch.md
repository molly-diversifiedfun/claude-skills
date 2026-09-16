<required_reading>
**Read these reference files NOW:**
1. references/core.md
</required_reading>

<process>

**Step 0 — Check User Context first (Mode 1 behavior)**

Before the Opening, scan `.unstuck/context.md`:
- Read **Section B** (the project) and **Section D.2** (T05 Scope) if present.
- If populated, DRAFT what you can: the project name, what it is, who it goes
  to, and any ship date already locked. Present the draft and ask them to
  correct it. Do not draft answers to the five below - those are theirs.
- If `.unstuck/context.md` is empty, use the Opening and run the five.

Don't ask what you can read. Don't invent what you can't.

---

**Step 0.5 — If they already have a One-Page Launch Plan, take it**

The free prompt at `theshipitsystem.com/launch-prompt` produces a One-Page
Launch Plan in whatever AI they were already using, and the fill-in page at
`theshipitsystem.com/launch-plan` produces the same thing as a form. People
arrive here holding one. Asking them five questions they answered twenty
minutes ago is the fastest way to lose them.

So before the Opening, ask ONCE, in one line, whether they have a plan to
paste. Yes or no, not an essay. **If no - fall through to the Opening below,
completely unchanged.**

If they paste one, it maps ONE TO ONE onto the five sections below, because all
three artifacts now ask the same five. Take each answer into its section and
skip that section's questions.

| What the plan says | Section |
|---|---|
| The one action someone takes when it works | 1 |
| The first real person, by name | 2 |
| Everything that has to be true first | 3 |
| What that person would notice missing - V1 | 4 |
| The day, the hours, and whether they agree | 5 |
| Three moves, with done-whens | The closing block |
| The context block (`## B. The project`) | Straight into `.unstuck/context.md` |

Four rules, all load-bearing:

1. **A tagged field is not an answer.** The prompt marks its own guesses
   `[MY CALL]` and its gaps `[STILL FUZZY]`. Those tags exist precisely because
   the user never answered. Ingesting one untagged launders another AI's guess
   into their decision, and every module downstream then reads it as fact. Ask
   every tagged field in this module's own wording, as if the plan had left it
   blank.

2. **Read it back before you use it.** Section by section: what you extracted
   and where it landed. Ask them to confirm or correct. Show a blank as a blank
   - never fill one from another section, from the project's shape, or from
   what a plan like this usually says.

3. **Do not re-cut V1.** That V1 came out of an item-by-item pass where the
   user made every cut themselves, under a rule that said once something was
   out it stayed out. Section 4 below still runs for someone starting cold -
   **it does not run on an ingested V1.** Take it as given.

4. **An older plan may carry a price.** Plans made before the artifacts moved
   off the money-first seven have a price field in them. Write it down in their
   words if they mention it, put it in `.unstuck/context.md` where pricing
   belongs, and ask nothing further. It is not part of this exercise.

Then run only the sections the plan did not fill. Say one line up front naming
which ones you're skipping and why, then skip them without further comment.

---

**Opening (output verbatim):**

> "Let's get you a plan you could defend to someone who asked why.
>
> Five questions. We're not going to plan the whole thing - we're going to find
> the first real person who sees it and work backwards from them.
>
> **One ground rule:** if you don't know an answer, you have three ways out:
> - Type **`hint`** - I'll show another worked example
> - Type **`guide me`** - I'll interview you to your answer, then synthesize
> - Type **`draft it`** - paste whatever rough version you have; I'll polish it
>
> Ready?"

One at a time. Ask, then STOP and wait. Do not answer for them, do not invent
their side, and do not produce the plan until they have actually answered. If
they invoke hint / guide me / draft it, fire the matching sub-flow from
`references/core.md` `<answer_assistance>`.

**Money is not part of this.** Not the scope, not the date, not the moves. Don't
ask for a price, don't ask whether they'd charge later, and don't ask which tool
they'd use - from the other side of the screen that last one reads exactly like
the price question. A first subscriber, member, reader or reply counts here
exactly the same as a first customer. If they raise a price themselves, write it
down in their words and move on.

**Quotes only.** If you turn a vague answer into something precise, show the
conversion and tag it `[MY CALL]`. This bites hardest on quantities: "a couple
of evenings, bit at the weekend" is not ten hours until you've shown them you
read "a couple" as four and they agreed.

---

**Section 1: What does someone DO when it works?**

**What we're writing:** One action, by one person.

"When this works, what does someone actually DO? Not what you ship - what they
do. One action."

**Example of a 5/5 answer:**
> "A gallery owner replies to my email and asks to see more work."

"It's live" is not an action - that's something you did. Push once,
specifically. If what they want is invisible - "she reads it" - keep it as the
action and note one visible sign underneath. Don't swap their goal for a metric
you find easier to verify.

→ Next: **Section 2** - one real person, by name

---

**Section 2: Who's the first real person you'll send it to?**

**What we're writing:** A name.

"Who's the first real person you'll send this to? Not a type of person. One
name."

**Example of a 5/5 answer:**
> "Priya. She runs the print studio on Bow Street and asked what I'd been
> working on in July. I never answered because I had nothing to send."

"People who might hire me" is not a name. **If they genuinely cannot name one,
stop the module here** - finding one person who wants this is the whole week,
and that IS their plan. Make that the three moves and skip to the closing block.

→ Next: **Section 3** - the dump

---

**Section 3: What has to be true first?**

**What we're writing:** Everything, unedited.

"What has to be true before you'd send it to her? Everything. Don't trim it,
don't tell me whether you really need it - that's the next question's job."

**Example of a 5/5 answer:**
> "Pick twelve pieces. Scan the older ones. Write a line for each. Decide on a
> name. Buy the domain. Build the site. Write an about page. Get a proper
> headshot. Set up a contact form. Figure out the newsletter."

Don't help. Don't trim. Don't ask "do you really need that?" Let it get long -
a short list means they edited themselves, so push once for more.

→ Next: **the one question worth more than the list**

---

**BEFORE SECTION 4 - THE VEHICLE**

Do this the moment the list is on the table, BEFORE going through it item by
item. If the vehicle is wrong, working through ten items is ten questions about
a thing they are not going to build.

They've been at this for months, so its shape stopped being a choice long ago -
it's now just what they assume the thing IS. **Most lists are long because the
VEHICLE is too big, not because the list is badly pruned.**

So look at the action from Section 1, and the weight of what they just listed,
and ask: what is the smallest thing in the world that produces that action?
Then say whether it's what they described.

> "She replies about work" - does that need a website, or three images and a
> way to reply?
> "Someone reads it" - does that need a site with an archive, or an email you
> send from your own address?
> "Illustrators give each other real feedback" - does that need a platform with
> billing and a directory, or eight people in a group chat?

If the smaller route is genuinely the same outcome, PUT IT TO THEM AS AN
EITHER/OR and stop. Name what it costs, what it gives up, and how it gets the
same action. It's a swap they accept or refuse, not a correction.

Expect a flinch. Months went into the big version and the small one can feel
like losing. Say the one true thing - the big version can still exist after the
small one has already got them the thing - and then let it go.

**One proposal, freely refused.** If they say no, say "your call", carry on with
theirs, and never mention it again - not as an aside, not as a note in the plan.

If they TAKE the swap, ask them to dump the small thing's list, and do NOT run
Section 4 on it. They just built that list from scratch against the action, with
the small version in front of them. Ask once instead: "anything on that list
she wouldn't actually notice?" Take the answer and move on.

---

**Section 4: What would THEY notice missing? - ONLY when they keep the original**

**What we're writing:** V1.

That list was built without the action in mind, so it's the one that needs going
through. Item by item. Name the item, ask whether that one person would notice
it missing, wait for the answer, then the next one. Every item gets asked.

**You may not cut an item yourself.** You may not say "and the rest of these are
out." You may not argue them out of one.

If they answer YES and give a reason - they said why she'd notice - it stays. **A
reason attached to a NO is a cut with an explanation on it, not a keep.** "I'd
notice, she wouldn't" means OUT. Read what the reason argues FOR, not that a
reason was given.

What survives is V1. What doesn't is out of this plan - not "later", not "phase
two". Don't offer a future date to soften the cut, and once something is out it
does not come back, by their hand or yours.

The cut has to be theirs. A scope they agreed to is one they'll keep; a scope
you handed them is one they'll renegotiate at midnight.

→ Next: **Section 5** - the date, and whether it's true

---

**Section 5: What day does she get it - and is that true?**

**What we're writing:** A date, the hours, and the arithmetic between them.

Ask both together: what day does that person get it, and roughly how many hours
will they actually have between now and then. Offer a pick on the hours - "a
couple of evenings, five a week, most of a weekend?" - because they won't know
the number cold.

**Read the hours back in DAILY terms before using them.** "Sixty a week is eight
and a half hours every day for sixteen days, weekends included. Is that the real
number?" People inflate this without meaning to lie, and a weekly total hides
it. If they confirm an implausible number, use it and tag the verdict
`[MY CALL]` so they can see whose optimism it was.

If they give no hours at all, don't invent one and don't treat unbounded time as
a pass. Say what you're assuming and tag it.

Then do the arithmetic out loud - "three weeks at five hours is fifteen hours" -
and say in one line whether V1 fits.

If it doesn't fit, say so ONCE, plainly: the scope and the date can't both be
true, and one of them will give. Then stop. Do not move the date, do not quietly
redefine V1 so the arithmetic works, and do not start a second round of cutting
here - that's `/unstuck scope`, and it's a different sitting. Shrinking what an
item means until it fits is moving the date where they won't notice.

"It'll be tight" is not a finding. Give them the number.

→ Next: **the closing block**

---

**The closing block**

1. One line: "You'd send this to <name> on <date>."
2. Three moves for this week, each with what makes it done - built from their
   own words where they exist, tagged `[MY CALL]` where they don't. Don't ask
   for these first; write them, then ask them to confirm or swap one.
3. Ask what's the smallest piece of move one they could finish today, under an
   hour.
4. One last question, once: they see it and nothing happens - what do you do?
   Don't answer it for them. Don't soften it. Ask, and write down what they say.

**A punt is not a confirmation.** "They look fine, whatever you think" at the
end of a long conversation is the likeliest place someone gives up, and it's the
one artifact they walk away with. Tag it and say so.

→ Next: **Present**

---

**Present the Launch Plan**

Use the template at templates/launch-plan.md. Five headings, their answers
under each, readable in thirty seconds. Mark anything unresolved
`[STILL FUZZY]` and anything you decided `[MY CALL]`.

→ Next: **Save**

---

**Save artifact**

Save to `.unstuck/launch-YYYY-MM-DD.md` using the Write tool. Use today's date.

→ Next: **Update context**

---

**Update context**

Append to `.unstuck/context.md` under **Section D.6** (Launch Plan):
- Project name + one-line description
- The one action, and the first person by name
- V1 (what survived) and what was cut
- Ship date, hours available, and whether V1 fit
- Date locked

---

**What's next**

The plan says what they're doing. It doesn't get them doing it - and the two
things this module deliberately stops short of both have homes:

> **BRANCHING EXIT - pick the path that fits:**
>
> - **V1 didn't fit the hours:** run `/unstuck scope`. That's the second cut,
>   done properly, with each item sized - which is the part this module refuses
>   to do in the same sitting.
> - **V1 fit, and the date is more than two weeks out:** run
>   `/unstuck roadmap`. It turns the hours into actual sessions on actual days,
>   which is the difference between a date and a plan.
> - **No validation yet - nobody has said they want this:** run
>   `/unstuck validate` before building anything.
>
↩ Come back to `/unstuck launch` when: the plan is stale, or you're launching
something new.

</process>

<success_criteria>
This module is complete when:
- [ ] All five sections filled in with specific answers
- [ ] The one action is something the OTHER person does, not something they ship
- [ ] Section 2 is a name, or the module stopped and made finding one the plan
- [ ] The vehicle question was asked before Section 4, and asked once
- [ ] Every V1 cut was theirs - no item cut, argued away, or restored by you
- [ ] The hours were read back in daily terms and the arithmetic was shown
- [ ] Money appears nowhere: no price asked, no "first sale", no tooling question
- [ ] Three moves, each with what makes it done
- [ ] The last question asked and their answer written down, not supplied
- [ ] Launch Plan artifact delivered and saved to `.unstuck/launch-YYYY-MM-DD.md`
- [ ] Context updated in `.unstuck/context.md` Section D.6
- [ ] If a plan was pasted: every `[MY CALL]` / `[STILL FUZZY]` field re-asked,
      the extraction read back and confirmed, and V1 taken as given
- [ ] Next module recommended
</success_criteria>
