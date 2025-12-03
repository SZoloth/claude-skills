---
name: odi-outcome-generator
description: Convert JTBD insights and qualitative research into ODI (Outcome-Driven Innovation) desired outcome statements with proper syntax. Use when translating pain points, desires, or job steps into measurable, solution-agnostic outcome statements for prioritization and validation.
---

# ODI Outcome Generator

## Overview

Transform JTBD interview insights, qualitative research, or job map analysis into properly structured ODI desired outcome statements. Create measurable, controllable, solution-agnostic statements that can be quantified for importance and satisfaction.

## When to Use

- Converting JTBD four forces into outcome statements
- Transforming pain points into measurable outcomes
- Creating outcome statements from job map steps
- Preparing outcomes for quantitative research/prioritization
- Building opportunity landscapes for product strategy

## ODI Outcome Syntax

Every desired outcome follows this structure:

```
[Direction] + [Metric] + [Object] + [Context]
```

**Direction:** Minimize, Reduce, Increase, Maximize
**Metric:** time, likelihood, number of, probability that
**Object:** What is being controlled/measured
**Context:** When/where this matters (optional clarifier)

**Examples:**
- "Minimize **time** to locate the correct asset version **during turnover**"
- "Reduce **likelihood** that integration fails **on first attempt**"
- "Increase **probability** that updates propagate **across all shot instances**"

## Converting JTBD Forces to Outcomes

### Push (Pain) → Minimize/Reduce

**Pain:** "Can't find the right asset version during turnover"
**Outcome:** "Minimize time to locate correct asset version during handoff"

**Pain:** "Tool crashes with large files"
**Outcome:** "Reduce likelihood of application failure when handling files >5GB"

**Pain:** "Manual steps take 2 hours per shot"
**Outcome:** "Minimize time to complete [job step] per shot"

### Pull (Desire) → Increase/Maximize

**Desire:** "One-click propagation of updates"
**Outcome:** "Increase reliability of propagating updates across shot instances"

**Desire:** "See what's approved vs in-progress"
**Outcome:** "Increase visibility of asset approval status at any given time"

**Desire:** "Automatic version tracking"
**Outcome:** "Reduce manual effort to track version lineage across handoffs"

### Anxiety (Fear) → Reduce Risk/Uncertainty

**Anxiety:** "Worried about show pipeline integration"
**Outcome:** "Reduce integration complexity for show-specific pipelines"

**Anxiety:** "Concerns about learning curve during crunch"
**Outcome:** "Minimize time to achieve proficiency with new workflow"

**Anxiety:** "No rollback plan if it breaks"
**Outcome:** "Increase reliability of reverting to previous workflow state"

### Habit (Inertia) → Increase Compatibility/Preserve

**Habit:** "Scripts built around old format"
**Outcome:** "Increase compatibility with existing automation scripts"

**Habit:** "Templates in legacy format"
**Outcome:** "Reduce effort to migrate existing templates to new format"

**Habit:** "Team conventions assume old workflow"
**Outcome:** "Minimize disruption to established team conventions"

## Job Map to Outcomes

For each job step, generate 5-10 desired outcomes:

**Job Step:** Locate asset

**Outcomes:**
- Minimize time to locate the target asset
- Reduce likelihood of selecting wrong asset version
- Increase confidence that located asset meets requirements
- Minimize steps required to initiate asset search
- Reduce ambiguity in asset naming/metadata
- Increase relevance of search results
- Minimize false positive results in search
- Reduce time to verify asset is correct version

## Quality Criteria for Outcomes

**Good outcomes are:**
- **Measurable:** Can be quantified (time, likelihood, number)
- **Controllable:** Can be influenced by solution design
- **Solution-agnostic:** No mention of specific tools or features
- **Stable:** Doesn't change with technology
- **Specific:** Clear object and context
- **Actionable:** Suggests what to improve

**Avoid:**
- Vague metrics ("better," "easier," "faster" without units)
- Solution-embedded ("using the new tool...")
- Feature descriptions ("have a button that...")
- Unmeasurable desires ("feel confident")
- Multiple outcomes in one statement

## Outcome Quality Checklist

- [ ] Starts with direction (Minimize/Reduce/Increase/Maximize)
- [ ] Includes measurable metric (time/likelihood/number/probability)
- [ ] Clear object of control specified
- [ ] Context clarifies when/where (if needed)
- [ ] No solutions mentioned
- [ ] Actionable for solution design
- [ ] Unique (not duplicate of another outcome)

## From Outcomes to Prioritization

Once outcomes are generated:

1. **Quantify importance:** Survey users rating 1-5 importance
2. **Quantify satisfaction:** Rate how well current solution satisfies
3. **Calculate opportunity:** Importance + (Importance - Satisfaction)
4. **Rank outcomes:** Higher opportunity = higher priority

**Outcome opportunity score formula:**
```
Opportunity = Importance + max(Importance - Satisfaction, 0)
```

Scores >12 are typically underserved (high opportunity).

## Examples from DWA Context

**Story Department:**
- Minimize time to find correct sequence/panel across shows
- Increase preservation of dialogue metadata across handoffs
- Reduce manual steps to export boards for downstream departments

**Previz Department:**
- Minimize time to first assembled scene with correct versions
- Reduce rework from wrong version selection
- Minimize search time to first confident asset selection

**Final Layout:**
- Minimize time to install correct, approved assets for shot
- Reduce cognitive load during mode switching (assembly ↔ dressing)
- Increase persistence of collections across sessions

**Animation:**
- Minimize time to create reference playlists
- Reduce redundant work by surfacing available cycles
- Increase confidence in reference quality via context indicators

## Resources

### references/
- `outcome-syntax-guide.md` - Detailed syntax rules and examples
- `job-map-framework.md` - Universal job map for generating outcomes

### assets/
- `outcome-template.md` - Template for documenting outcomes with metadata
- `odi-examples-by-department.md` - DWA-specific outcome examples
