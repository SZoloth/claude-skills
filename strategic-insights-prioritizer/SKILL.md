---
name: strategic-insights-prioritizer
description: Synthesize multiple research sources into strategic insights with value-risk prioritization framework. Use when planning product roadmaps, evaluating competing opportunities, or making high-stakes decisions with limited resources.
---

# Strategic Insights Prioritizer

## Overview

Transform scattered research, stakeholder input, competitive analysis, and market data into prioritized strategic recommendations. Apply systematic scoring to identify highest-value opportunities while managing risk and resource constraints.

## Core Problem

**Challenge:** Multiple competing opportunities, limited resources, unclear how to prioritize.

**Symptoms:**
- Stakeholders advocate for different priorities
- Every opportunity seems important
- Analysis paralysis from too many options
- Unclear how to compare apples and oranges (e.g., new feature vs technical debt)

**Solution:** Systematic multi-factor scoring that makes tradeoffs explicit and defensible.

## Prioritization Framework

### Value dimensions (positive scoring)

**Business impact (+3 max):**
- Revenue potential (new customers, upsell, retention)
- Cost reduction (operational efficiency, support burden)
- Strategic positioning (competitive differentiation, market expansion)

**User impact (+3 max):**
- Problem severity (how painful is current state?)
- User coverage (how many affected?)
- Frequency (how often does pain occur?)

**Confidence (+2 max):**
- Evidence strength (validated with users vs assumption)
- Clarity of requirements (well-defined vs fuzzy)
- Precedent (done before vs novel)

**Leverage (+2 max):**
- Platform value (benefits multiple use cases)
- Reusability (applicable across departments/products)
- Network effects (value increases with adoption)

### Risk dimensions (negative scoring)

**Effort (-3 max):**
- Development time (weeks/months)
- Team size required
- Technical complexity

**Risk (-2 max):**
- Technical feasibility (proven vs experimental)
- Dependency complexity (standalone vs tightly coupled)
- Reversibility (easy to back out vs permanent)

**Adoption friction (-2 max):**
- Change magnitude (minor vs workflow overhaul)
- Training required
- Stakeholder buy-in difficulty

### Scoring formula

```
Priority Score = (Business + User + Confidence + Leverage) - (Effort + Risk + Adoption)

Theoretical range: -7 to +10
Practical range: -3 to +8
```

**Interpretation:**
- **+6 to +10:** Clear priority - high value, manageable risk
- **+3 to +5:** Strong candidate - evaluate capacity
- **0 to +2:** Marginal - likely defer unless strategic
- **Negative:** Avoid or redesign to improve fundamentals

## Workflow

### 1. Gather inputs (go wide)

Collect research from all relevant sources:
- User interviews and feedback
- Stakeholder priorities
- Competitive analysis
- Technical constraints
- Business goals and metrics

**Output:** Comprehensive view of landscape before narrowing.

### 2. Extract opportunities

From each source, identify distinct opportunities:
- What problem would this solve?
- Who benefits and by how much?
- What's the evidence strength?

Reference `references/opportunity-extraction-guide.md` for systematic identification.

### 3. Score systematically

For each opportunity, evaluate all dimensions:
- Use scoring rubrics consistently (see `references/scoring-rubrics.md`)
- Document rationale for each score
- Note uncertainties and assumptions
- Identify what validation would increase confidence

Use `assets/scoring-template.md` for structured evaluation.

### 4. Rank and calibrate

Sort by total score and sanity-check:
- Does rank order feel right intuitively?
- Are there outliers that need re-examination?
- Should scoring weights be adjusted for context?

### 5. Create decision framework

Present top opportunities with:
- Clear recommendation (what to do first, second, third)
- Supporting rationale (why this order)
- Tradeoffs made explicit (what we're not doing and why)
- Validation needs (what could change priority)

## Output Format

### Strategic roadmap recommendations

```markdown
# Q4 2025 Roadmap Priorities

## Recommended Focus

### 1. [Opportunity name] (Score: +7)
**Problem:** [What pain this solves]
**Evidence:** [Research sources + confidence level]
**Impact:** [Business + user value]
**Effort:** [Time/resource estimate]
**Why first:** [Rationale vs alternatives]
**Success metric:** [How we'll know it worked]

### 2. [Opportunity name] (Score: +5)
[Same structure]

### 3. [Opportunity name] (Score: +4)
[Same structure]

## Not Now (But Worth Revisiting)

### [Opportunity] (Score: +2)
**Why deferred:** [Effort too high, unclear requirements, etc.]
**What would change priority:** [Validation that would increase score]
```

### Scoring comparison table

| Opportunity | Business | User | Confidence | Leverage | Effort | Risk | Adoption | **Total** |
|------------|----------|------|------------|----------|--------|------|----------|-----------|
| Previz installer | +2 | +3 | +2 | +1 | -2 | -1 | -1 | **+7** |
| Collections mgmt | +3 | +3 | +2 | +2 | -3 | -1 | -2 | **+4** |
| FLO migration | +1 | +1 | +1 | +1 | -2 | -2 | -1 | **-1** |

## When to Use This Skill

Trigger strategic-insights-prioritizer when:
- Planning quarterly or annual product roadmaps
- Multiple stakeholders propose competing priorities
- Need to defend prioritization decisions with systematic rationale
- Resources are constrained and tradeoffs are unavoidable
- Previous ad-hoc prioritization led to regret or disputes
- Executive asks "why are we doing X before Y?"

## Common Patterns

### Quarterly planning
Evaluate all proposed initiatives systematically before committing capacity.

### Stakeholder alignment
Use scoring to make implicit preferences explicit and negotiable.

### Portfolio management
Balance quick wins (high score, low effort) with strategic bets (high value, higher risk).

### Validation planning
Identify which uncertainties, if resolved, would most change priorities.

## Resources

### references/
- `opportunity-extraction-guide.md` - How to identify opportunities from research
- `scoring-rubrics.md` - Detailed criteria for each dimension
- `calibration-examples.md` - Reference scores across different opportunity types

### assets/
- `scoring-template.md` - Structured template for evaluating opportunities
- `roadmap-presentation-template.md` - Executive-ready prioritization summary

## Quality Checks

Before finalizing prioritization:
- [ ] All major opportunities evaluated (not cherry-picked subset)
- [ ] Scoring consistent across opportunities (same rubric applied)
- [ ] Assumptions and uncertainties documented
- [ ] Validation paths identified (what evidence would change ranking)
- [ ] Stakeholder perspectives represented
- [ ] Recommendation includes clear "why this order" rationale
