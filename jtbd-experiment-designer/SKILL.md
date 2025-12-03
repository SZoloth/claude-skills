---
name: jtbd-experiment-designer
description: Design PDSA (Plan-Do-Study-Act) experiments to test JTBD/ODI hypotheses about adoption, measure outcome movement, and iterate based on results. Use when converting insights into testable interventions for Weekly Business Review (WBR) tracking.
---

# JTBD Experiment Designer

## Overview

Convert JTBD insights and ODI outcomes into testable experiments using PDSA methodology. Design lightweight interventions that produce measurable signals within 1-2 sprint/milestone cycles.

## When to Use

- Converting JTBD patterns into testable hypotheses
- Designing interventions to improve adoption
- Planning WBR (Weekly Business Review) experiments
- Validating assumptions about adoption barriers
- Testing whether outcome metrics move as predicted

## Experiment Design Framework

Every experiment follows this structure:

**Prediction (If-Then):**
"If we [intervention], then we expect [behavior/metric change] because [causal mechanism]"

**Success metric:**
Single measurable outcome (not multiple)

**Guardrails:**
What would make us stop/pivot

**Timeframe:**
1-2 sprints/milestones (fast feedback)

**Next-step trigger:**
What result causes what action

## Converting JTBD Patterns to Experiments

### Pattern: Drip→Trigger Adoption Path

**Insight:** Artists see multiple exposures before adopting; time walls trigger action

**Prediction:**
"If we increase touchpoint cadence to weekly #channel updates + monthly show-and-tells, then passive lookers will convert 2x faster because drip exposure reduces Anxiety and strengthens Pull"

**Success metric:** Time from first exposure to adoption request (target: <4 weeks)

**Guardrails:** If no conversion improvement after 3 cycles, try different channels

**Timeframe:** 6 weeks (2 milestone cycles)

### Pattern: Deep Dive→Unlock Path

**Insight:** Users binge-learn but get blocked by TD enablement gates

**Prediction:**
"If we reduce TD enablement SLA to <2 days, then Deep Dive adopters will convert before next milestone (instead of stalling) because unlock friction is removed"

**Success metric:** % of enablement requests converted to active use within 1 week

**Guardrails:** If TD capacity can't sustain <2 days, build self-service enablement

**Timeframe:** 4 weeks (1 milestone cycle)

### Pattern: Integration Friction

**Insight:** High interest but weeks-long TD enablement queues block adoption

**Prediction:**
"If we pre-integrate for top 3 show pipelines, then adoption requests will convert 3x faster because TD enablement becomes instant"

**Success metric:** Enablement lag (request → first use) drops from 14 days to <2 days

**Guardrails:** If <50% of requests fit pre-integrated shows, expand coverage

**Timeframe:** 8 weeks (implementation + 1 cycle validation)

### Pattern: Social Proof Friction

**Insight:** Teams wait to see peer success before adopting

**Prediction:**
"If we publish success stories with metrics in #channel after each pilot, then adoption requests will increase by 30% because social proof reduces Anxiety"

**Success metric:** Adoption requests per week (baseline vs intervention)

**Guardrails:** If no lift after 3 success stories, investigate message clarity

**Timeframe:** 6 weeks (3 pilot completions)

## Experiment Design Process

### 1. State the Pattern

From JTBD analysis:
- What adoption pattern was observed?
- How many interviews showed this?
- What forces drive/block adoption?

**Example:** "5 of 8 Previz interviews showed Drip→Trigger path; time wall was turnover milestone"

### 2. Form Hypothesis

If-then-because structure:
- **If** (intervention)
- **Then** (expected behavior/metric change)
- **Because** (causal mechanism from four forces)

**Example:** "If we announce pilot windows 4 weeks before turnover, then Previz sequences will request adoption 2x more because explicit time wall converts passive lookers"

### 3. Define Success Metric

Single, measurable outcome:
- What specific metric will move?
- What is current baseline?
- What target indicates success?

**Example:**
- Metric: Adoption requests per turnover cycle
- Baseline: 2 sequences/turnover
- Target: 4+ sequences/turnover

### 4. Set Guardrails

What would make you stop or pivot:
- Negative side effects to watch for
- Resource constraints
- Risk thresholds

**Example:**
- If adoption requests spike but enablement fails >50%, TD capacity is bottleneck
- If announcements create noise complaints, try different channels

### 5. Choose Timeframe

How long to run experiment:
- Fast feedback (1-2 cycles preferred)
- Long enough to see signal
- Short enough to iterate

**Example:** 2 turnover cycles (6 weeks each) = 12 weeks total

### 6. Plan Next Steps

What result triggers what action:
- Success → Scale to more departments
- Partial success → Refine and repeat
- Failure → Pivot to different intervention

**Example:**
- If 4+ sequences: Scale to Animation department
- If 3 sequences: Extend announcement lead time to 6 weeks
- If ≤2 sequences: Interview non-adopters for blockers

## Experiment Types

### Increase Exposure (Drip Path)

**Interventions:**
- Regular channel updates
- Show-and-tells cadence
- Documentation series
- Demo recordings

**Metrics:** Exposure count before request, time to first request

### Reduce Unlock Friction (Unlock Path)

**Interventions:**
- Faster TD SLA
- Self-service enablement
- Pre-integration
- Auto-approvals

**Metrics:** Enablement lag (days), conversion rate (request → use)

### Create Time Walls

**Interventions:**
- Announce deprecations
- Publicize pilot windows
- Pre-freeze campaigns
- Milestone reminders

**Metrics:** Requests per time wall event, conversion timing

### Amplify Social Proof

**Interventions:**
- Success story publishing
- Peer testimonials
- Adoption dashboards
- Cross-team learning sessions

**Metrics:** Requests after each story, referral sources

## Instrumentation

Track these to validate experiments:

**Adoption funnel:**
- Exposures (views, demo attendance)
- Requests (access, enablement asks)
- First use (telemetry timestamp)
- Regular use (7+ days active)

**Enablement:**
- Request date
- Approval date
- First use date
- Lags at each stage

**Outcomes:**
- Time saved (self-reported or measured)
- Error reduction (before/after comparison)
- Satisfaction (quick pulse survey)

## WBR (Weekly Business Review) Format

Report experiments weekly:

**This week:**
- Experiments running: [Name + week N of M]
- New signals: [Metric movement]
- Decisions made: [Scale/refine/pivot]

**Next week:**
- Experiments starting: [Name + prediction]
- Experiments completing: [Name + decision criteria]

Keep concise, metric-focused.

## Common Pitfalls

**Avoid:**
- Too many metrics (focus on one primary)
- Too long timeframe (>2 cycles)
- Vague predictions ("will be better")
- No baseline (can't measure change)
- No guardrails (don't know when to stop)
- Complex interventions (can't isolate cause)

**Prefer:**
- Single metric
- Fast feedback (1-2 cycles)
- Specific prediction (2x, +30%, <2 days)
- Known baseline
- Clear guardrails
- Simple interventions

## Example Experiments from DWA Context

### Experiment: Pre-Turnover Pilot Windows

**Pattern:** Previz adoption spikes before turnover milestones

**Prediction:** If we announce 3-week pilot windows before each turnover, then adoption requests will increase by 50% because explicit time wall converts passive lookers

**Metric:** Requests per turnover cycle (baseline: 3, target: 5+)

**Guardrails:** If TD enablement can't keep up, automate or add capacity

**Timeframe:** 2 turnover cycles (12 weeks)

**Next steps:**
- 5+ requests → Scale to Animation
- 4 requests → Extend window to 4 weeks
- ≤3 requests → Interview non-adopters

### Experiment: Success Story Amplification

**Pattern:** Teams cite peer success as Pull factor

**Prediction:** If we publish detailed success stories (metrics + quotes) after each pilot, then subsequent adoption requests will increase 30% because social proof reduces Anxiety

**Metric:** Requests per week (baseline: 2, target: 3+)

**Guardrails:** If engagement low, try different formats (video, Slack, demo)

**Timeframe:** 6 weeks (3 success stories)

**Next steps:**
- 3+ requests/week → Systematize story pipeline
- 2-3 requests/week → A/B test story formats
- <2 requests/week → Investigate channel/timing

## Resources

### assets/
- `experiment-template.md` - PDSA experiment design template
- `wbr-update-template.md` - Weekly business review format
