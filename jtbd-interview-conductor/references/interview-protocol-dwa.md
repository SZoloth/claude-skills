# DWA JTBD Interview Protocol

Complete question set for conducting Jobs-to-be-Done interviews at DreamWorks Animation, adapted for internal tool/workflow adoption decisions.

## Purpose

Reveal actual adoption timelines and causal triggers (Push, Pull, Anxiety, Habit) across roles (artists, supervisors, TDs, production, tech leadership). Surface blockers and enablers to produce ODI-ready desired outcomes.

## Interview Structure (30-45 minutes)

1. **Framing** (2 min)
2. **Start at decision moment, work backwards** (15-20 min)
3. **Fill gaps, four forces at each stage** (10-15 min)
4. **Wrap with counterfactuals + artifact links** (3-5 min)

---

## Opening (Reduce Pressure)

Use "documentary mode" opener:

> "We're documenting how teams adopt tools here. Anything you remember helps; there are no wrong answers. We'll work backward from the moment you decided to adopt/use [capability]."

**First anchor question:**
> "Why did you decide to adopt/use [capability/workflow] and where were you when you made that decision?"

---

## Timeline Anchors (Work Backwards)

### Decision Moment

- "What was the exact moment you first used [capability] on real work?"
- "What day/week was that?"
- "What sequence/shot/asset was it?"
- "Where were you when you made that decision?"

### Just Before First Use

- "What happened just before that?"
- "Were there any approvals, exceptions, tickets, enablement steps?"
- "Who had to sign off or help enable this?"

### When Did You First Consider It?

- "When did you first think about using [capability]?"
- "What prompted that thought?"
- "What was happening in your work at that time?"

### Time Wall

- "Was there a deadline or milestone that made this 'now' instead of 'later'?"
- "What would have happened if you waited another sprint/week/milestone?"

---

## Environmental Cues (DWA-Specific)

Use these to help participants locate timeline:

### Show Cadence
- "Was this before or after show award?"
- "Before or after kickoff?"
- "During turnover to animation?"
- "Before temp delivery?"
- "During a freeze window?"
- "Before or after final delivery?"

### Operational Events
- "Was there an outage that affected your work?"
- "Did you hit a storage quota or render limit?"
- "Was there a performance issue with existing tools?"
- "Did a tool get deprecated or sunset?"
- "Was there a policy or security change?"

### Communication Channels
- "Did you see this in a Slack thread? Which channel?"
- "Was there a Confluence page about it?"
- "Did someone demo it in a meeting?"
- "Was it mentioned in dailies or a weekly?"
- "Did you see it at a show-and-tell?"

---

## Artifacts to Request

Concrete evidence that helps verify timeline:

- "Do you remember the Jira or ShotGrid ticket number?"
- "Can you find the Slack thread where this was discussed?"
- "Was there a Confluence page with instructions?"
- "What was the version tag or asset ID you used?"
- "Do you have the email where you requested access?"

---

## Four Forces Prompts (Per Stage)

### Push (Pain of Status Quo)

- "What made the current way unacceptable?"
- "When did that pain spike?"
- "What broke or took too long?"
- "How did it show up in your day/week?"
- "What would have happened if you kept doing it the old way?"
- "How did this affect your team/sequences deliverables?"

### Pull (Attraction to New Way)

- "What did you hope this would let you do that you couldn't before?"
- "Which moment or example convinced you it was worth trying?"
- "What did you see others doing that looked appealing?"
- "What promise or capability attracted you?"
- "What did the demo or documentation show that interested you?"

### Anxiety (Fears/Unknowns)

- "What risks or unknowns almost stopped you?"
- "Who was worried and about what?"
- "What would have made this feel safe sooner?"
- "What could have gone wrong?"
- "What did you not understand yet?"
- "Were there concerns about show impact, deadlines, or deliverables?"
- "Did anyone push back or hesitate?"

### Habit (Inertia/Installed Base)

- "What would you have done if nothing changed?"
- "Who prefers the old path and why?"
- "What ties you to existing tools/checkpoints?"
  - Templates in old format?
  - Scripts that automate old workflow?
  - Muscle memory from years of use?
  - Team conventions or standards?
- "How much training/ramp-up would the new way require?"
- "What existing work would need to be redone or migrated?"

---

## Role and Stakeholder Mapping

### Decision Distribution

- "Who initially pushed for trying this?"
- "Who was hesitant or skeptical?"
- "Who had to approve it?"
- "Who had to enable it technically?" (TD, platform, security)
- "If you said 'yes,' who else needed to agree?"
- "Were there any silent veto points?" (Someone who could block but didn't speak up)

### Stakeholder Concerns

- "What did your supervisor think?"
- "What did production say?"
- "What did the TD team need to do?"
- "Were there security or policy concerns?"
- "Did other teams have opinions?"

---

## Alternatives Considered

### Comparison Set

- "What else did you look at or consider?"
- "What did you rule out and why?"
- "If [capability] wasn't available, what would you have done?"
- "Did you try any workarounds first?"
- "Were there other teams doing something different?"

### Why This Won

- "What made this option better than the alternatives?"
- "What was the deciding factor?"
- "What would have made you choose differently?"

---

## Counterfactuals and Time Walls

### Testing Causality

- "If [milestone/outage/deprecation] hadn't happened, would you have adopted anyway?"
- "What deadline made this go from 'someday' to 'now'?"
- "If you had two more weeks, would you have done it differently?"
- "What would have delayed this by a month?"

### Alternate Scenarios

- "If the legacy tool still worked fine, would you have switched?"
- "If integration took a week instead of a day, would you have tried it?"
- "If your lead hadn't supported it, would it have happened?"

---

## Probing for Specifics

When answers are vague, drill down:

### Vague → Specific

**Vague:** "It was faster"
**Probe:** "How much faster? Can you give me an example task?"

**Vague:** "Everyone wanted it"
**Probe:** "Who specifically? Walk me through who said what."

**Vague:** "It didn't work well"
**Probe:** "What failed? When? What did you try to fix it?"

**Vague:** "We heard about it"
**Probe:** "Where? From whom? Show me the Slack message or demo."

### Finding Inconsistencies

**Contrast questions:**
- "Earlier you said X was the problem, but just now you said Y was fine. Which one actually caused you to switch?"
- "You mentioned the demo was in May, but you also said kickoff was in June. Can we nail down the order?"

---

## Quality Signals

### Good Interview Flow

- Participant recalls names, dates, assets, and people quickly
- Inconsistencies surface and get resolved naturally
- Clear time wall or trigger emerges
- Story has causality ("because," "when," "after")
- Specific artifacts can be linked/verified

### Needs Course Correction

- Too many hypotheticals ("we would probably...")
- Vague timelines without anchors
- Feature brainstorming instead of reconstruction
- No clear trigger or time wall
- Can't recall key people or decisions
- Episode older than 18 months and fuzzy

---

## Closing Questions

### Verify Understanding

- "Let me play back what I heard... Does that sound right?"
- "Is there anything important I missed?"
- "Who else should I talk to about this decision?"

### Artifacts and Follow-Up

- "Can you send me links to those tickets/threads/pages?"
- "Would you be open to a short follow-up if I have clarifying questions?"
- "Can I reach out if I need to verify a date or detail?"

---

## DWA-Specific Context Tips

### Show Calendar Language

When participants reference show milestones, understand the sequence:
1. Award (show greenlit)
2. Kickoff (production starts)
3. Turnover (handoff between departments)
4. Temp delivery (work-in-progress review)
5. Rough/Final (completion stages)
6. Freeze windows (no changes allowed)

### Department Rhythms

Different departments have different cycles:
- **Story:** Editorial, panel reviews, screenings
- **Previz:** Shot assembly, camera blocking, rough animation
- **Animation:** Performance, cycles, curves, character acting
- **Final Layout (FLO):** Set dressing, asset placement, optimization
- **Lookdev/Lighting:** Material development, rendering, final pixel

Adapt questions to match their workflow vocabulary.

### Technical Stakeholders

When adoption requires technical enablement:
- **TDs (Technical Directors):** Integration, tools, pipeline
- **Platform team:** Infrastructure, permissions, deployment
- **Security:** Compliance, access control, data governance
- **Production:** Scheduling, resource allocation, risk assessment

Always ask who enabled the adoption technically.

---

## Post-Interview: Immediate Synthesis

Within 10 minutes of interview end:

1. **Complete timeline template** - All stages with four forces
2. **Extract 3-5 verbatim quotes** - Positioning, not just description
3. **Classify adoption path** - Drip→trigger or Deep dive→unlock
4. **Tag trigger type** - Milestone, outage, policy, pilot, peer proof
5. **Log all artifacts** - Tickets, threads, pages, assets
6. **Measure enablement lag** - Request date → first success date

If template can't be completed, schedule 15-min follow-up immediately.

---

## Practice Before Large Research

Do 2-3 dry-run interviews before launching major research:
- Pick recent, non-mandated workflow changes
- Avoid top-down decrees (no organic causality)
- Swap roles and critique each other
- Refine question flow and timing
- Calibrate on what "good specifics" look like

Skills atrophy - refresh before each research round.
