---
name: systems-thinking-coach
description: Apply systems thinking frameworks to understand complex problems, identify leverage points, and design sustainable interventions. Use when facing recurring issues, unintended consequences, or problems where obvious solutions keep failing.
---

# Systems Thinking Coach

## Overview

Analyze complex problems through a systems lens using Donella Meadows' frameworks. Identify feedback loops, delays, leverage points, and systemic structures that drive behavior. Design interventions that address root causes rather than symptoms.

## When to Use Systems Thinking

**Strong signals:**
- Same problem keeps recurring despite multiple "fixes"
- Solutions create new problems (unintended consequences)
- Different stakeholders see completely different problems
- Everyone agrees on symptoms but disagrees on causes
- Simple interventions produce unexpected resistance
- Problem involves multiple reinforcing factors

**Examples:**
- "We keep missing deadlines despite adding more people"
- "Every process improvement creates new bottlenecks"
- "Users keep requesting features we've already built"

## Core Systems Concepts

### 1. Feedback loops

**Reinforcing loops (amplification):**
- Success breeds success, failure breeds failure
- Virtuous cycles and vicious cycles
- Exponential growth or collapse

**Example:** Good tool adoption → More users → More feature requests → Better tool → More adoption

**Balancing loops (stabilization):**
- System seeks equilibrium
- Goal-seeking behavior
- Resistance to change

**Example:** Add developers → More code → More bugs → More time fixing → Less new development

### 2. Delays

Time gaps between action and consequence cause oscillation and overshoot.

**Example:** Hire more people (action) → 3 months onboarding (delay) → Productivity dip before improvement → Management panics and hires even more → Chaos.

### 3. System structure determines behavior

People respond rationally to system incentives. "Bad" outcomes usually stem from system design, not bad actors.

**Example:** Artists duplicate work not because they're careless, but because the search system makes discovery harder than recreation.

## Donella Meadows' Leverage Points

Ranked from least to most effective (counterintuitively, high-leverage points are often subtle):

**12. Parameters** (Weakest)
- Tweaking numbers (budgets, timelines, targets)
- Common but rarely transformative

**11. Buffer sizes**
- Stabilizers that prevent overshooting
- Example: Caching to smooth load spikes

**10. System structure**
- Physical infrastructure and flows
- Example: Network bandwidth, storage capacity

**9. Delays**
- Reduce time between action and feedback
- Example: Ship smaller increments for faster learning

**8. Balancing loops**
- Negative feedback that prevents runaway
- Example: Automated tests catch bugs before shipping

**7. Reinforcing loops**
- Positive feedback that amplifies change
- Example: Network effects, word-of-mouth growth

**6. Information flows**
- Make consequences visible to decision-makers
- Example: Show developers production errors in real-time

**5. Rules**
- Incentives, constraints, permissions
- Example: Change promotion criteria to value quality over features

**4. Self-organization**
- System's ability to evolve new structures
- Example: Let teams form around problems vs assigned

**3. Goals**
- System purpose drives all behavior
- Example: Shift from "ship features" to "solve user problems"

**2. Paradigm**
- Mental models and assumptions
- Example: From "users are the problem" to "system design is the problem"

**1. Transcending paradigms** (Strongest)
- Ability to shift between multiple paradigms
- Recognizing all models are incomplete

See `references/leverage-points-detailed.md` for deep dive on each level.

## Analysis Workflow

### 1. Identify the problem behavior

What pattern keeps recurring? Describe observable symptoms without diagnosis.

**Good:** "Sprint velocity drops every time we onboard new developers"
**Avoid:** "We need better onboarding" (already jumped to solution)

### 2. Map the system

Identify key elements:
- **Variables:** What changes over time? (team size, bug count, velocity)
- **Connections:** What affects what? (more code → more bugs)
- **Feedback loops:** What reinforces or balances?
- **Delays:** Where are time gaps between cause and effect?

Use causal loop diagrams (see `assets/causal-loop-template.md`).

### 3. Find the structure

What systemic patterns produce this behavior?

**Common archetypes:**
- **Fixes that fail:** Solution has unintended consequences
- **Shifting the burden:** Symptomatic fix prevents addressing root cause
- **Tragedy of the commons:** Individual optimization degrades shared resource
- **Success to the successful:** Winner gets advantages that ensure continued winning

Reference `references/system-archetypes.md` for pattern library.

### 4. Identify leverage points

Where can small changes produce disproportionate impact?

**Questions:**
- What information is invisible to decision-makers?
- What delays prevent fast feedback?
- What rules create perverse incentives?
- What goals are driving unwanted behavior?

### 5. Design intervention

**High-leverage approaches:**
- Make consequences visible (information flows)
- Reduce delays (faster feedback)
- Change incentives (rules)
- Shift goals or paradigms

**Test for:**
- Does this address structure or just symptoms?
- Will this create new problems elsewhere?
- Can system self-correct once started?

## Example Analysis

### Problem: Artists spend too much time searching for assets

**Symptom-level solution:** Build better search UI

**Systems analysis:**

**Variables:** Time spent searching, asset count, search quality, duplication

**Reinforcing loop (vicious cycle):**
```
Poor search → Can't find assets → Recreate from scratch → More assets → Harder to search → Worse
 search
```

**Balancing loop (resistance):**
- Better search tools require time to build
- Building takes time away from creating assets
- Leadership sees "low productivity" and demands less tool-building

**Leverage points:**
1. **Information flow** (high leverage): Show leadership total hours lost to search vs hours to build tool
2. **Rules** (high leverage): Make asset reuse a team metric, not just individual output
3. **Parameters** (low leverage): Add more search filters (doesn't address duplication cycle)

**Recommended intervention:**
- Measure and visualize cost of poor search (information flow)
- Change incentives to reward asset reuse over creation (rules)
- This breaks reinforcing loop without requiring immediate tool perfection

## Resources

### references/
- `leverage-points-detailed.md` - Complete guide to Meadows' 12 leverage points with examples
- `system-archetypes.md` - Common patterns and how to recognize them
- `causal-loop-guide.md` - How to draw and interpret feedback loop diagrams

### assets/
- `causal-loop-template.md` - Structure for creating system maps
- `analysis-worksheet.md` - Step-by-step problem analysis template

## Quality Checks

Before finalizing systems analysis:
- [ ] Identified at least one reinforcing and one balancing loop
- [ ] Mapped key delays between cause and effect
- [ ] Intervention addresses structure not just symptoms
- [ ] Considered unintended consequences in other parts of system
- [ ] Identified metrics to track whether intervention works
- [ ] Solutions target leverage points above "parameters" (more than tweaking numbers)
