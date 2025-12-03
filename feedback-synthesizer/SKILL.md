---
name: feedback-synthesizer
description: Analyze user feedback from multiple sources (reviews, support tickets, interviews), identify patterns, and synthesize actionable insights for product prioritization. Use when customer feedback is scattered across channels and needs systematic analysis.
---

# Feedback Synthesizer

## Overview

Transform scattered user feedback from multiple channels into structured, actionable insights. Identify patterns across app reviews, support tickets, user interviews, and feature requests to inform product roadmap decisions.

## Core Capabilities

### 1. Multi-source aggregation

Collect and normalize feedback from diverse sources:
- App store reviews (iOS App Store, Google Play)
- Support tickets and customer service logs
- User interview transcripts
- Feature request databases
- Social media mentions
- NPS survey responses

**Output:** Unified feedback dataset with standardized structure (date, source, user segment, sentiment, category)

### 2. Pattern identification

Detect recurring themes and pain points:
- **Frequency analysis:** How often is each issue mentioned?
- **Sentiment correlation:** Which problems drive negative reviews?
- **Segment analysis:** Do patterns vary by user type (power user vs casual)?
- **Time trends:** Are issues growing or declining?

Reference `references/pattern-detection-methods.md` for systematic categorization approaches.

### 3. Theme categorization

Group feedback into actionable categories:
- **Feature requests:** What users want that doesn't exist
- **Usability issues:** Problems with existing features
- **Bugs and errors:** Technical problems
- **Performance complaints:** Speed, reliability, crashes
- **Delight moments:** What users love (preserve these!)

### 4. Impact scoring

Prioritize feedback by business impact:
- **Volume:** How many users mention this?
- **Intensity:** How strongly do they feel about it?
- **User value:** Does this affect high-value customer segments?
- **Trend:** Is this growing or stable?
- **Competitive gap:** Do competitors solve this better?

Use `assets/impact-scoring-template.md` for systematic evaluation.

### 5. Insight synthesis

Transform raw feedback into product recommendations:
- **Opportunity statements:** "Users need X because Y"
- **Evidence strength:** Supported by N mentions across M sources
- **Recommended actions:** What product should do about it
- **Success metrics:** How to measure if solution works

## When to Use This Skill

Trigger feedback-synthesizer when:
- Weekly/monthly feedback review cycles
- Planning product roadmap and need customer input
- Competing hypotheses about user needs exist
- Scattered feedback makes it hard to see patterns
- Stakeholders ask "what are users saying about X?"
- App store review score drops and need to understand why

## Analysis Workflow

### 1. Collect sources
Gather feedback from all available channels within time window (typically last 30-90 days).

### 2. Normalize data
Standardize format:
```
Date | Source | User Segment | Sentiment | Raw Feedback | Category
```

### 3. Initial categorization
Tag each piece of feedback with primary themes (can have multiple):
- Feature request
- Usability issue
- Bug/error
- Performance
- Positive feedback

### 4. Pattern detection
- Group similar feedback items
- Count frequency by category
- Identify correlations (e.g., Bug X often mentioned with Usability Issue Y)
- Track sentiment by category

### 5. Impact scoring
For each pattern, evaluate:
- Volume (how many mentions)
- User value (which segments affected)
- Intensity (mild annoyance vs showstopper)
- Trend (growing vs stable vs declining)

### 6. Synthesis and recommendations
Create structured insights:
- **Finding:** [Pattern description]
- **Evidence:** [N mentions across M sources]
- **Impact:** [Estimated user/business impact]
- **Recommendation:** [What to do about it]
- **Priority:** [High/Med/Low based on scoring]

## Output Formats

### Weekly feedback digest
```markdown
# Feedback Digest: [Date Range]

## Top Themes (by volume)
1. [Theme 1] - 47 mentions (↑ 23% vs last week)
2. [Theme 2] - 32 mentions (→ stable)
3. [Theme 3] - 28 mentions (↓ 15% vs last week)

## High-Priority Issues
[Issues requiring immediate attention]

## Feature Request Patterns
[Commonly requested capabilities]

## Positive Signals
[What users love - preserve this]
```

### Product roadmap input
```markdown
# Feedback-Driven Opportunities

## Opportunity 1: [Name]
**User need:** [What users are trying to accomplish]
**Evidence:** 47 mentions across app reviews, support tickets
**Impact:** High (affects power users, growing trend)
**Recommendation:** [Product response]
**Priority:** High

[Additional opportunities...]
```

## Resources

### references/
- `pattern-detection-methods.md` - Systematic approaches for identifying themes
- `sentiment-analysis-guide.md` - Interpreting emotional intensity in feedback

### assets/
- `impact-scoring-template.md` - Prioritization framework for feedback
- `weekly-digest-template.md` - Standard format for feedback summaries
- `feedback-database-schema.md` - Recommended structure for feedback tracking

## Quality Checks

Before finalizing synthesis:
- [ ] All major sources checked (not cherry-picking channels)
- [ ] Patterns supported by multiple mentions (not single anecdotes)
- [ ] Sentiment accurately captured (not just negative focus)
- [ ] User segments identified (power user vs casual feedback differs)
- [ ] Trends tracked over time (not just point-in-time snapshot)
- [ ] Positive feedback preserved (know what's working, not just broken)
