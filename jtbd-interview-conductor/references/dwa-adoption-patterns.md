# DWA Adoption Patterns

Common patterns observed in tool/workflow adoption at DreamWorks Animation and similar animation studios. Use these patterns to recognize adoption paths during interviews and design interventions.

## Two Primary Adoption Paths

### Path A: Drip → Trigger

**Pattern:**
1. Passive exposure over time (demos, docs, peer mentions)
2. Series-like learning journey forms
3. Specific trigger/time wall causes adoption

**Characteristics:**
- Long consideration period (weeks/months)
- Multiple touchpoints before decision
- Knowledge accumulates gradually
- Trigger creates urgency

**Example DWA scenario:**
> Artist sees three different Slack posts about asset library over 2 months. Attends optional demo. Reads Confluence page. Then during turnover crunch, can't find asset version quickly, remembers the library, requests TD access, adopts within days.

**Intervention opportunities:**
- **Increase drip cadence:** Regular show-and-tells, #channel updates
- **Create series content:** Multi-part tutorials, progressive demos
- **Time trigger visibility:** Announce upcoming milestones, deprecations
- **Make triggers predictable:** Known pilot windows, scheduled enablement

### Path B: Deep Dive → Unlock

**Pattern:**
1. User discovers capability and binge-learns (reads all docs, shadows workflow end-to-end)
2. Hits gated step requiring enablement (TD integration, permission, approval)
3. Requests unlock
4. Adopts quickly after gate opens

**Characteristics:**
- Short, intense consideration
- Comprehensive learning in one session
- Blocked by access/integration, not knowledge
- Rapid adoption post-unlock

**Example DWA scenario:**
> Supervisor hears about workflow in standup, reads entire Confluence space in one afternoon, tries to use it but hits security gate. Requests TD enablement, gets approval in 2 days, sequence adopts the following week.

**Intervention opportunities:**
- **Reduce unlock friction:** Pre-approved access, streamlined TD process
- **Make gating explicit:** Clear "request access" CTA in docs
- **Fast-track enablement:** SLA for integration requests (<2 days)
- **Comprehensive onboarding:** Single "complete guide" for deep divers

## DWA-Specific Time Walls

Time walls convert "someday" to "now." Common at DWA:

### Show Calendar Gates

**Kickoff**
- Teams starting fresh, open to new workflows
- Less risk than mid-production changes
- Opportunity: "Adopt before kickoff" campaigns

**Turnover**
- Handoff between departments (Story→Previz→Animation→Layout)
- Pain points surface acutely
- Opportunity: Just-in-time enablement before turnover windows

**Freeze Windows**
- No changes allowed, creates pre-freeze urgency
- Teams rush to adopt before freeze
- Opportunity: Announce capabilities 2-3 weeks before freeze

**Temp/Final Delivery**
- Quality bar increases, existing pain intolerable
- Too late for risky changes
- Opportunity: Enable early enough (6-8 weeks before)

### Operational Events

**Outage/Performance Degradation**
- Legacy tool breaks or slows critically
- Creates immediate Push, reduces Habit
- Opportunity: Have alternatives ready to recommend

**Quota/Limit Hit**
- Storage, render slots, API limits exceeded
- Forces evaluation of alternatives
- Opportunity: Efficient solutions get attention

**Deprecation Announcement**
- Legacy tool sunset date announced
- Creates known deadline
- Opportunity: Migration path with plenty of lead time

**Policy/Security Change**
- Compliance requirement, security tightening
- Forces workflow changes
- Opportunity: Compliant solutions ready

### Pilot/Access Windows

**Limited Enablement Slots**
- TD bandwidth constrained
- Creates FOMO (fear of missing out)
- Opportunity: Publicize limited pilot availability

**Sequence Selection**
- Production chooses sequences for pilots
- Creates competitive pressure
- Opportunity: Highlight pilot successes to non-selected teams

**Show Expansion**
- Capability proven on Show A, expanding to Show B
- Reduces Anxiety (proof exists)
- Opportunity: Cross-show learning sessions

## Studio-Specific Friction Points

### Integration Friction

**Symptom:** High interest, low adoption despite demand

**Root causes:**
- TD enablement backlog (weeks-long queue)
- Show-specific pipeline complications
- Security review bottleneck
- Vendor compatibility unknowns

**Indicators in interviews:**
- "We wanted it but couldn't get it enabled"
- "TD said they'd get to it eventually"
- "Not sure if security would approve"
- "Works great on Show X but not configured for us"

**Solutions:**
- Pre-integrate for common show pipelines
- TD self-service enablement (automation)
- Security pre-approvals for standard tools
- Vendor compatibility matrix published

### Discovery Friction

**Symptom:** Low awareness despite capability existing

**Root causes:**
- Capability not discoverable
- No marketing/communication
- Siloed knowledge in single team
- Documentation scattered or hidden

**Indicators in interviews:**
- "I didn't know this existed until..."
- "Wish I'd known about this 6 months ago"
- "Heard about it by accident in standup"
- "Only found out because colleague mentioned it"

**Solutions:**
- Regular show-and-tells
- Department newsletter highlights
- Searchable capability catalog
- Peer testimonial library

### Learning Friction

**Symptom:** Try once, abandon after failure

**Root causes:**
- Insufficient onboarding
- First-run failure with no help
- Expectation mismatch
- Missing context for workflow

**Indicators in interviews:**
- "Tried it once, didn't work, gave up"
- "Not sure I was doing it right"
- "Worked for them but not for me"
- "Too complicated for quick learning"

**Solutions:**
- Progressive onboarding (hello world → advanced)
- Error messages that teach
- Context-specific examples (per department/show)
- Office hours / live help available

### Social Proof Friction

**Symptom:** "Wait and see" attitude, slow adoption

**Root causes:**
- No visible peer success
- Risk-averse culture
- Failure stories more visible than success
- Unclear which teams/shows are using it

**Indicators in interviews:**
- "Waiting to see if others succeed"
- "Don't want to be first"
- "Heard it didn't work well for Team X"
- "Which shows are actually using this?"

**Solutions:**
- Public success stories with metrics
- Adoption dashboard (X teams using it)
- Peer testimonials in channels
- Case studies per department/show

## Stakeholder Dynamics

### Doer (Artist) Dynamics

**Characteristics:**
- Feels pain directly
- Wants quick fix
- Time-constrained
- May lack authority to adopt

**Interview focus:**
- Pain timing and intensity (Push)
- What they've tried (workarounds)
- Who they need permission from
- What would make it safe

### Decider (Supervisor/Lead) Dynamics

**Characteristics:**
- Balances team productivity vs risk
- Cares about show delivery
- Has authority but limited time
- Needs proof before committing team

**Interview focus:**
- What convinced them (Pull)
- Risk assessment (Anxiety)
- Alternative evaluation
- Team readiness

### Enabler (TD) Dynamics

**Characteristics:**
- Gatekeeps technical integration
- Concerned with pipeline stability
- Backlog of requests
- Show-specific complications

**Interview focus:**
- Integration complexity
- Priority/urgency drivers
- Blockers encountered
- Enablement timeline

### Approver (Production/Ops) Dynamics

**Characteristics:**
- Manages schedule and budget
- Risk-averse during crunch
- Needs clear ROI
- Coordinates across shows

**Interview focus:**
- Schedule impact (risk)
- Resource allocation
- Show priorities
- Approval timeline

## Cross-Department Patterns

### Story → Previz Handoff

**Common pain:** Boards don't translate cleanly to 3D

**Adoption pattern:**
- Story exports in format Previz can't use
- Previz manually recreates
- Push intensifies at turnover
- Adoption: tools that preserve panels/timing

**Time wall:** Previz sequence start

### Previz → Animation Handoff

**Common pain:** Camera/blocking changes after turnover

**Adoption pattern:**
- Animation receives incomplete info
- Back-and-forth inefficiency
- Push spikes when retakes required
- Adoption: locked camera approvals

**Time wall:** Animation kickoff

### Animation → Layout Handoff

**Common pain:** Rig changes break Layout work

**Adoption pattern:**
- Layout rebuilds after rig updates
- Lost work frustration
- Push increases near delivery
- Adoption: version locking tools

**Time wall:** Layout shot start

### Cross-Show Learning

**Pattern:**
- Show A pilots capability
- Show B watches, waits for proof
- Success stories trigger Show B adoption
- Failure stories delay/prevent adoption

**Acceleration:**
- Document Show A learnings
- Share metrics (time saved, quality improved)
- Provide Show B-specific guidance
- Assign peer mentors cross-show

## Instrumentation for Pattern Recognition

Track these signals to identify patterns:

### Adoption Metrics
- Request date → first use date (enablement lag)
- First use → regular use (adoption success)
- One team → multiple teams (expansion)
- Pilot → production (graduation)

### Path Indicators
- Number of exposures before request (drip count)
- Time from awareness to request (consideration length)
- Documentation read pattern (deep dive vs drip)
- Request urgency language (time wall signals)

### Friction Indicators
- Abandoned trials (tried once, didn't return)
- Request backlog (asked but not enabled)
- Repeat questions (discovery/learning friction)
- Churn (adopted then reverted)

### Success Indicators
- Peer referrals (social proof forming)
- Expansion requests (success breeding success)
- Proactive asks (seeking not pushed)
- Cross-show adoption (pattern spreading)

## Using Patterns in Interviews

### Pattern Recognition

Listen for pattern language:
- "I saw several people mention this over time" → Drip→Trigger
- "I read everything in one sitting" → Deep Dive→Unlock
- "We had a deadline coming up" → Time wall
- "Waited to see if Team X succeeded" → Social proof friction

### Pattern-Specific Questions

**For Drip→Trigger:**
- "How many times did you see this before trying it?"
- "What was the series of exposures?"
- "What finally made you act?"

**For Deep Dive→Unlock:**
- "When did you go from casual interest to comprehensive learning?"
- "What gate did you hit?"
- "How long did unlock take?"

**For Time Walls:**
- "What deadline or event made this urgent?"
- "What would have happened if you waited?"

**For Friction:**
- "What almost stopped you?"
- "What took longer than expected?"
- "What confusion or failure did you hit?"

## Converting Patterns to Strategy

### For Drip→Trigger Path

**Strategy:** Increase touchpoints and trigger visibility

**Tactics:**
- Regular show-and-tells
- Consistent channel updates
- Pre-announce time walls (freezes, deprecations)
- Series content (Part 1, 2, 3 tutorials)

### For Deep Dive→Unlock Path

**Strategy:** Remove unlock friction and advertise comprehensiveness

**Tactics:**
- Streamline enablement (self-service or fast TD SLA)
- "Complete guide" documentation
- Clear "request access" CTAs
- Fast-track pilot applications

### For Time Wall Conversion

**Strategy:** Make time walls visible and preparation easy

**Tactics:**
- Announce upcoming milestones in advance
- Pre-integrate before freeze windows
- Deprecation timelines public
- Pre-freeze adoption campaigns

### For Friction Reduction

**Strategy:** Instrument, identify, eliminate

**Tactics:**
- Track abandoned trials → improve first-run success
- Monitor enablement lag → speed up or self-serve
- Collect "didn't know it existed" → improve discovery
- Analyze failure modes → better error messages

## WBR Integration

Report patterns in weekly business review:

**Adoption Path Distribution**
- X% Drip→Trigger, Y% Deep Dive→Unlock
- Trend over time

**Time Wall Effectiveness**
- Adoption spike before freeze: +N%
- Conversion after deprecation announcement: N teams

**Friction Identification**
- Enablement lag average: N days (target: <2)
- First-run success rate: X% (target: >80%)
- Discovery lag: N weeks from launch to awareness

**Pattern-Based Predictions**
- "Increasing drip touchpoints should convert N passive lookers by next milestone"
- "Reducing unlock time to <2 days should increase Deep Dive conversions by X%"

Test predictions with small experiments, measure, iterate.
