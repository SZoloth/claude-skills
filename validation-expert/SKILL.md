---
name: validation-expert
description: Design UX validation methodologies, research protocols, and test planning to validate assumptions before building. Use when planning validation studies, designing experiments, or testing risky product assumptions.
---

# Validation Expert

## Overview

Design rigorous validation approaches to test product assumptions before committing to full build. Reduce risk through systematic experimentation and evidence gathering.

## Validation Hierarchy

### Least to most rigorous (and expensive):

1. **Customer interviews** - Understand problem depth
2. **Concept tests** - Show mockups, gauge reaction
3. **Prototype tests** - Interactive prototype, observe usage
4. **Concierge MVP** - Manually deliver service, learn workflow
5. **Wizard of Oz** - Fake automation, real user experience
6. **Alpha/Beta** - Real product, limited audience
7. **Full launch** - Real product, real scale

**Principle:** Start cheap, increase fidelity only when needed.

## Assumption Testing

### For each risky assumption:
1. **State assumption clearly**
   - "Artists will use semantic search daily"
   - "Version labeling will reduce rework by 20%"

2. **Identify risk type**
   - Value: Will they use it?
   - Usability: Can they use it?
   - Feasibility: Can we build it?
   - Viability: Does business model work?

3. **Design cheapest test**
   - Value: Interviews, fake door test
   - Usability: Prototype test
   - Feasibility: Technical spike
   - Viability: Pricing survey, mock sales calls

4. **Define success criteria**
   - "6 of 8 reference customers commit to using it"
   - "Users complete task in under 2 minutes"
   - "Technical spike proves latency under 100ms"

5. **Execute and learn**
   - Run test
   - Document results
   - Update confidence level
   - Decide: proceed, pivot, or stop

## Validation Methods

### Usability testing
**Setup:** 5-8 participants, task-based scenarios, think-aloud protocol
**Output:** Friction points, confusion moments, success/failure rates
**Cost:** Low (1-2 days)

### Fake door test
**Setup:** Show feature in UI, track clicks, explain "coming soon"
**Output:** Interest level, click-through rate
**Cost:** Very low (hours to implement)

### Concierge MVP
**Setup:** Manually deliver service to small group
**Output:** Workflow understanding, value confirmation
**Cost:** Medium (time-intensive but low tech investment)

### Landing page test
**Setup:** Marketing page for non-existent product, track signups
**Output:** Market demand signal
**Cost:** Low (day to build)

## Test Planning Template

```markdown
## Assumption to Test
[Clear statement of what we're testing]

## Risk Type
[Value | Usability | Feasibility | Viability]

## Why This Matters
[What happens if we're wrong]

## Test Approach
[Which validation method and why]

## Success Criteria
[Specific, measurable threshold]

## Participants
[Who we need to test with]

## Timeline
[How long to run test]

## Next Decision
[What we'll decide after results]
```

## When to Use

- Before committing to large development effort
- When assumptions are high-risk
- Stakeholders want "proof" before investment
- Multiple solution paths possible
- User behavior uncertain

## Quality Checks

- [ ] Riskiest assumptions identified first
- [ ] Test method matches risk level
- [ ] Success criteria defined before running test
- [ ] Participants representative of target users
- [ ] Results actionable (tells us proceed/pivot/stop)
- [ ] Learning documented and shared
