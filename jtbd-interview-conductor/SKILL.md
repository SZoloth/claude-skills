---
name: jtbd-interview-conductor
description: Prepare for and conduct Jobs-to-be-Done interviews to understand tool/workflow adoption decisions. Use when planning JTBD interviews, creating interview guides, or conducting adoption research at DreamWorks Animation or similar organizations. Focuses on reconstructing real adoption episodes using the four forces framework.
---

# JTBD Interview Conductor

## Overview

Conduct ethnographic Jobs-to-be-Done interviews that reconstruct real adoption decisions for tools and workflows. Extract the four forces (Push, Pull, Anxiety, Habit) across decision stages to understand causality and predict future adoption patterns.

## When to Use

Use this skill when:
- Planning JTBD interviews about tool/workflow adoption
- Preparing interview guides for specific departments or contexts
- Conducting interviews to understand adoption decisions
- Training others on JTBD interview methodology
- Scheduling and framing adoption research sessions

## Interview Preparation Workflow

### 1. Identify Target Episodes

Select recent, organic adoption decisions to reconstruct:

**Recency guidelines:**
- Prefer decisions within last 6 months
- Stretch to 6-18 months only as skills mature
- Avoid older than 18 months unless unusually salient (major outage, show-wide migration)

**Target clear decision moments:**
- Tool trial start
- First time a sequence/team used the capability
- Policy exception granted
- Pilot go/no-go decision
- Migration off legacy tool
- Expansion to second sequence/team

**Interview multiple roles:**
- The person who used the capability (doer)
- Supervisor/lead who sponsored (decider)
- TD/integrator who enabled (enabler)
- Production/ops who approved (approver)

### 2. Gather Pre-Interview Context

Collect anchors before the interview:
- Adoption telemetry timestamps (if available)
- Jira/ShotGrid tickets related to request
- Confluence pages or documentation
- Slack threads about the decision
- Show/sequence identifiers
- Relevant milestone dates

**Pre-interview checklist (10 minutes):**
- [ ] Look up adoption telemetry (first-use timestamp)
- [ ] Find related tickets/threads/docs
- [ ] Prepare blank timeline template with four forces
- [ ] Decide stopping condition (30-45 minutes)
- [ ] Determine who drives follow-ups
- [ ] Request recording consent if needed

### 3. Pair Up for Interview

Run interviews with two people:
- **Lead interviewer:** Tracks the story, asks questions
- **Partner:** Watches for inconsistencies, timestamps, missing anchors

Pairing prevents cognitive overload and captures richer detail.

### 4. Frame the Interview

Open with "documentary mode" to reduce pressure:

> "We're documenting how teams adopt tools here. Anything you remember helps; there are no wrong answers. We'll work backward from the moment you decided to adopt/use [capability]."

**First anchor question:**
"Why did you decide to adopt/use [capability/workflow] and where were you when you made that decision?"

## Interview Execution

### Working Backwards from Decision Moment

Start at the adoption moment and work backwards through stages:

**Timeline stages to reconstruct:**
1. First thought ("We can't track X reliably during turnover")
2. Passive looking (watching demo, reading docs, seeing show-and-tell)
3. Active looking (requesting access, spike, pilot thread)
4. Decision ("Let's run this on sequence ABC in week 6")
5. First use (first successful asset/shot through new path)
6. Ongoing use/switch (expanding or backing out)

### Making Recall Concrete

Ask for specifics every time:

**Names/IDs:**
- Sequence, shot, show, sprint
- Jira ticket, Confluence page, Slack thread
- Version tag, asset name

**Environmental cues for DWA context:**
- Was this pre-kickoff or during delivery?
- Before animation turnover?
- During a freeze?
- After a vendor drop?
- Day/night? On site or remote?

**People:**
- Who was in the room/Zoom?
- Who pushed for this?
- Who hesitated?
- Who had to sign off?

**Use DWA-native milestones to locate timeline:**
- Show: award, kickoff, turnover, temp delivery, rough/final, freeze windows
- Operational: outage, tool deprecation, security change, render limits, quota hits
- Routine: sprint boundaries, department weeklies, WBR, rollups

**Request artifacts:**
- Jira/ShotGrid tickets
- Confluence links
- Slack threads
- Version tags/asset IDs

### Extracting Four Forces Per Stage

For each timeline stage, probe gently for the four forces:

**Push (pain of status quo):**
- "What made the current way unacceptable?"
- "When did that pain spike?"
- "What broke or took too long?"
- "How did it show up in your day/week?"

**Pull (attraction to new way):**
- "What did you hope this would let you do that you couldn't before?"
- "Which moment or example convinced you it was worth trying?"

**Anxiety (fears/unknowns):**
- "What risks or unknowns almost stopped you?"
- "Who was worried and about what?"
- "What would have made this feel safe sooner?"

**Habit (inertia/installed base):**
- "What would you have done if nothing changed?"
- "Who prefers the old path and why?"
- "What ties you to existing tools/checkpoints?" (templates, scripts, automation, muscle memory)

### Surfacing Causality Without Pushing

Use gentle probes to reveal true drivers:

**Contrast questions:**
"You said versioning pain was the driver, but earlier you said reviews were fine. Which one actually tipped the scales?"

**Counterfactuals:**
"If [milestone/outage/deprecation] hadn't happened, would you have adopted?"

**Time wall checks:**
"What deadline or event made this go from 'someday' to 'now'?"

### Mapping Roles and Stakeholders

Understand decision distribution:
- "Who pushed for adoption?"
- "Who hesitated?"
- "Who had to approve or enable?"
- "If one person said 'yes,' who else needed to agree?"
- "Any silent veto points?"

### Exploring Alternatives

Understand the consideration set:
- "What else did you look at?"
- "What did you rule out and why?"
- "If this wasn't available, what would you have done?"

## Quality Signals During Interview

**Interview is going well when:**
- Specifics appear quickly (names, dates, assets, links, people)
- Inconsistencies get resolved with gentle contrast questions
- Clear time wall or deciding event emerges
- Participant reconstructs causality naturally

**Interview needs adjustment when:**
- Getting hypotheticals instead of real episodes
- Vague, tool-led talk without concrete anchors
- Episodes too old or details fuzzy
- Pushing too hard on causality (causing defensiveness)

## Anti-Patterns to Avoid

- **Brainstorming features** - Stay anchored to actual adoption story
- **"What" without "why now"** - Over-indexing on what happened without probing timing
- **Org chart assumptions** - Letting org charts stand in for real decision paths
- **Hypotheticals** - Accepting "we would probably..." instead of "we did..."
- **Solution talk** - Letting interview drift into feature requests

## After-Interview Synthesis (10 Minutes)

Immediately after each interview:

1. **Complete timeline template** with four forces per stage
2. **Extract 3-5 verbatim quotes** that signal positioning (why they said it, not just what)
3. **Classify adoption path:**
   - Drip→trigger: Cadence of demos/docs, then specific trigger
   - Deep dive→unlock: Binge learning, hit gated step, request access
4. **Tag trigger type:**
   - Milestone (show calendar gates)
   - Outage/deprecation
   - Policy change
   - Pilot window
   - Peer proof
5. **Log artifacts** (tickets, threads, links)
6. **Measure enablement lag** (request → first success)

**If template can't be completed:** Interview missed anchors. Schedule short follow-up while details fresh.

## Practice Before Going Live

Do 2-3 dry runs internally before large research push:
- Pick recent, non-mandated workflow change
- Avoid pure impulses or top-down decrees
- Seek organic decision causality
- Swap roles and critique after
- Refresh skills before each round

## Scheduling Template

Use when inviting participants:

**Subject:** 30 min — help us understand how [capability] got adopted

**Body:**
```
Hi [Name],

We're documenting how teams adopt tools/workflows so we can remove friction and invest where it matters. It's a 30-45 min conversation where we work backward from when you decided to use [capability]. No prep needed, there are no wrong answers. Anything you remember helps.

[Suggest 2-3 time slots]

Thanks!
```

## Resources

### references/
- `interview-protocol-dwa.md` - Full DWA-specific interview protocol with all questions
- `four-forces-framework.md` - Deep dive on Push, Pull, Anxiety, Habit
- `dwa-adoption-patterns.md` - Common DWA-specific adoption paths and triggers

### assets/
- `timeline-template.md` - Four forces timeline template to fill during/after interview
- `synthesis-checklist.md` - Post-interview synthesis checklist
