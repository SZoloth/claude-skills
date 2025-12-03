---
name: opportunity-identifier
description: Execute Teresa Torres' systematic 7-step methodology to extract evidence-based opportunities from stakeholder interviews. Use when analyzing interview transcripts to identify product opportunities with proper source citations.
---

# Opportunity Identifier

## Overview

Apply Teresa Torres' rigorous 7-step process to extract opportunities from interview transcripts. Transform raw conversations into evidence-based product opportunities with full traceability to source material.

## When to Use

**Trigger opportunity-identifier when:**
- Just completed stakeholder or user interview
- Have raw transcript that needs systematic analysis
- Need to identify product opportunities with evidence
- Building opportunity solution tree
- Preparing for product prioritization decisions

## Teresa Torres' 7-Step Process

###1. Read entire transcript first

**Goal:** Understand full context before extracting

**Process:**
- Read from start to finish without taking notes
- Get sense of stakeholder's worldview
- Note major themes (mental bookmark only)
- Resist urge to jump to solutions

**Why:** Prevents cherry-picking quotes that support preconceptions. Full context reveals nuance.

### 2. Identify pain points and desired outcomes

**Goal:** Find specific moments where stakeholder struggled or expressed needs

**Look for:**
- Frustration stories ("I spent 2 hours...")
- Workarounds ("I usually just...")
- Time waste ("Every day I have to...")
- Desired outcomes ("I wish I could...")
- Comparison to better state ("Other tools let me...")

**Mark in transcript:** Highlight or tag these moments with line numbers.

### 3. Extract verbatim quotes

**Goal:** Capture exact language with full citation

**Format:**
```
> "Quote text here"
> — Stakeholder Name, Role (filename.md:line)
```

**Requirements:**
- Exact quote, not paraphrased
- Include speaker name and role
- File and line number citation
- Preserve context (enough to understand without reading full transcript)

**Example:**
> "I waste probably 30-40% of my time just searching for assets that I know exist somewhere."
> — Heidi Gilbert, Story TD (heidi-interview-2025-07-15.md:127)

### 4. Frame as opportunities (not solutions)

**Goal:** Describe user need without prescribing solution

**Template:** "Help [user] [accomplish outcome] so that [benefit]"

**Good (opportunity framing):**
- "Help story artists discover existing reference assets across productions"
- "Enable artists to identify the latest approved version of any asset"
- "Allow teams to see what reference material other productions have gathered"

**Bad (solution framing):**
- "Build semantic search"
- "Add version labels"
- "Create cross-production asset browser"

**Why:** Solutions are one possible answer. Opportunities leave space for creative solutions.

### 5. Group related opportunities

**Goal:** Organize opportunities into logical clusters

**Common groupings:**
- By workflow stage (planning → execution → review)
- By job-to-be-done (finding assets, organizing work, collaboration)
- By department or role
- By severity (daily pain vs occasional frustration)

**Example clustering:**
```
**Asset Discovery**
- Help artists find existing reference across productions
- Enable discovery of similar work from other shows
- Surface relevant assets without knowing exact search terms

**Version Control**
- Help artists identify latest approved versions
- Reduce confusion about which asset to use
- Prevent accidental use of outdated materials
```

### 6. Prioritize by evidence strength

**Goal:** Identify which opportunities have strongest support

**Evidence dimensions:**
- **Frequency:** Mentioned by X of Y interview stakeholders
- **Severity:** Impact on daily work (blocking vs annoying)
- **Specificity:** Concrete stories vs vague complaints
- **Consistency:** Same pain across different roles/departments

**Priority tiers:**
- **High confidence:** Multiple stakeholders, specific stories, clear impact
- **Medium confidence:** Mentioned by few, or impact unclear, or evidence thin
- **Low confidence:** Single mention, vague, or may be edge case

**Example:**
```
**High Priority**
1. Asset discovery across productions (5 of 5 stakeholders, daily impact)
2. Version identification (4 of 5 stakeholders, causes rework)

**Medium Priority**
3. Collaboration visibility (2 of 5 stakeholders, occasional need)
```

### 7. Map to outcome metrics

**Goal:** Connect opportunities to measurable business/user outcomes

**For each opportunity, identify:**
- **User outcome:** What improves for users? (time saved, quality increase, frustration reduction)
- **Business outcome:** What improves for organization? (efficiency, quality, collaboration)
- **Success metric:** How would we measure if solution works?

**Example:**
```
**Opportunity:** Help artists discover existing reference across productions

**User outcome:** Reduce time spent searching for assets (currently 30-40% of day)
**Business outcome:** Reduce asset duplication, increase reuse
**Success metric:**
- Time to find asset (reduce from 2hrs to <15min)
- Asset reuse rate (increase from 60% to 85%)
- Search abandonment (reduce from 40% to <10%)
```

## Output Template

Use `assets/opportunity-extraction-template.md`:

```markdown
# Opportunity Extraction: [Stakeholder Name]

**Date:** YYYY-MM-DD
**Stakeholder:** [Name, Role, Department]
**Source:** [transcript-filename.md]

## High-Priority Opportunities

### 1. [Opportunity name]

**Framing:** Help [user] [do what] so that [benefit]

**Evidence:**
- [Quote 1] (filename.md:line)
- [Quote 2] (filename.md:line)
- [Quote 3] (filename.md:line)

**Frequency:** Mentioned X times by Y stakeholders
**Severity:** [Daily blocker | Frequent frustration | Occasional pain]

**Desired outcomes:**
- User: [What improves for user]
- Business: [What improves for org]

**Potential success metrics:**
- [Metric 1]
- [Metric 2]

### 2. [Next opportunity...]
[Same structure]

## Medium-Priority Opportunities
[Opportunities with less evidence or lower impact]

## Questions for Validation
[What we still don't know that would change priority]
```

## Common Mistakes

**Avoid:**
1. **Jumping to solutions:** "Build search" instead of "Help users find assets"
2. **Cherry-picking:** Only noting quotes that support existing beliefs
3. **Vague opportunities:** "Improve user experience" (not specific enough)
4. **Missing citations:** Opportunities without source quotes
5. **Feature requests as opportunities:** User said "I want X" doesn't mean X is the opportunity

**Instead:**
1. Frame as user needs, not product features
2. Extract ALL pain points, even contradictory ones
3. Be specific about what user is trying to accomplish
4. Every opportunity backed by cited evidence
5. Dig beneath feature requests to underlying need

## Integration with Slash Commands

**Use existing slash command:**
```
/research:identify-opportunities "path/to/transcript.md" "Stakeholder Name" "Department"
```

This command executes the full 7-step process automatically.

## Resources

### references/
- `teresa-torres-opportunity-mapping.md` - Complete methodology with examples
- `opportunity-framing-examples.md` - Good vs bad opportunity statements

### assets/
- `opportunity-extraction-template.md` - Standard output format
- `evidence-strength-rubric.md` - How to assess confidence levels

### scripts/
- `extract_opportunities.py` - Automated opportunity extraction helper

## Quality Checks

Before finalizing opportunity extraction:
- [ ] Read full transcript (not just cherry-picked sections)
- [ ] All opportunities have verbatim quote citations
- [ ] Opportunities framed as needs, not solutions
- [ ] Evidence strength assessed honestly (not oversold)
- [ ] Related opportunities grouped logically
- [ ] Success metrics identified for high-priority opportunities
- [ ] Questions flagged for further validation
