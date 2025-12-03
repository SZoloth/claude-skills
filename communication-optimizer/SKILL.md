---
name: communication-optimizer
description: Transform verbose, lengthy documents into clear, concise, actionable communications using proven frameworks (BLUF, Minto Pyramid, SCR). Use when stakeholders aren't reading lengthy docs or when critical messages get lost in detail.
---

# Communication Optimizer

## Overview

Transform verbose documents into crisp communications that stakeholders actually read and act upon. Apply proven frameworks to create information hierarchy that prioritizes key messages and makes documents skimmable.

## Core Problem

**Symptoms:**
- Stakeholders ignore lengthy documents
- Critical decisions buried in page 47
- Teammates ask questions answered in the doc
- Writing takes hours but gets 30 seconds of attention

**Root cause:** Information architecture optimized for comprehensive coverage, not reader comprehension.

## Frameworks

### BLUF (Bottom Line Up Front)

Lead with the conclusion or recommendation. Bury nothing important.

**Structure:**
1. **Bottom line** (1-2 sentences): The answer/decision/recommendation
2. **Key supporting points** (3-5 bullets): Why this is the answer
3. **Details** (if needed): Full context for those who want it

**Example transformation:**

**Before (buried lead):**
> Over the past 6 weeks we conducted interviews with 12 story artists across 3 productions. We asked about their workflow challenges, particularly around reference collections. Several themes emerged including search difficulty, version control confusion, and collaboration friction. Based on this research, we recommend prioritizing collections management.

**After (BLUF):**
> **Recommendation:** Prioritize collections management feature
>
> **Why:**
> - Story artists lose 30-40% of time searching for assets (12 of 12 interviews)
> - Current folder structure fails at scale (500TB across productions)
> - High confidence: pain validated across all productions and seniority levels
>
> [Full research synthesis: story-research.md]

### Minto Pyramid Principle

Structure arguments from conclusion → key arguments → supporting evidence.

**Rules:**
1. Ideas at any level must summarize ideas grouped below
2. Ideas in each grouping must be same kind of idea
3. Ideas in each grouping must be logically ordered

**Application:**
- Start with governing thought (the answer)
- Support with 3-5 major arguments
- Each argument supported by specific evidence
- Reader can stop at any level and get complete picture

Reference `references/minto-pyramid-detailed.md` for complex restructuring.

### SCR (Situation-Complication-Resolution)

Narrative framework for proposals or recommendations.

**Structure:**
1. **Situation:** Current state (uncontroversial facts)
2. **Complication:** What changed or why situation is problematic
3. **Resolution:** Your proposal/recommendation

**When to use:** Proposing change, making recommendations, requesting decisions.

**Example:**

**Situation:** Story department manages 500TB of reference imagery using shared network folders.

**Complication:** Artists lose 30-40% of work time searching for assets. Current folder structure doesn't scale to production size. Teams duplicate work because they can't find existing references.

**Resolution:** Implement semantic search + collections management to reduce search time by 50% and enable cross-team asset discovery.

## Transformation Workflow

### 1. Identify core message
What is the single most important thing the reader must know? If they read nothing else, what should they walk away with?

### 2. Extract key support
What 3-5 points support the core message? Rank by importance.

### 3. Restructure
- Lead with core message (BLUF)
- Support with key points in descending importance
- Move detailed evidence to appendices or linked docs
- Add clear headers and visual hierarchy

### 4. Apply readability test
- Can reader skim in under 2 minutes?
- Is core message in first paragraph?
- Are headers clear without reading body text?
- Could executive summary stand alone?

### 5. Reduce word count
Target 50% reduction from original. Cut:
- Hedging language ("perhaps," "might," "could")
- Redundant phrasing ("in order to" → "to")
- Obvious context the reader already knows
- Details that belong in linked references

## Common Patterns

### Executive summaries
Use BLUF + SCR:
- Bottom line: The recommendation
- Situation: Where we are
- Complication: The problem
- Resolution: Your proposal
- Key evidence: 3-5 supporting bullets
- Link to full analysis

### Research reports
Use Pyramid:
- Conclusion: What we learned
- Major findings (3-5)
  - Each finding supported by evidence
  - Each finding leads to implication
- Full transcript/data in appendix

### Stakeholder memos
Use BLUF + clear asks:
- Decision needed (what, by when)
- Recommendation with rationale
- Options considered (brief)
- Next steps if approved
- Link to full analysis

## Resources

### references/
- `minto-pyramid-detailed.md` - Complete guide to pyramid principle with examples
- `bluf-examples.md` - Before/after transformations across document types
- `stakeholder-communication-patterns.md` - Adapting style for different audiences

### assets/
- `executive-summary-template.md` - BLUF-structured summary template
- `one-pager-template.md` - Single-page decision memo format
- `research-brief-template.md` - SCR-structured research summary

## Quality Checks

Before sending optimized doc:
- [ ] Core message in first 2 sentences
- [ ] Document skimmable in under 2 minutes
- [ ] Headers tell the story without reading body
- [ ] Critical information not buried
- [ ] Clear next steps or decisions needed
- [ ] 50%+ shorter than original while preserving all key content
