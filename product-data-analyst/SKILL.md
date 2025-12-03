---
name: product-data-analyst
description: Define product metrics frameworks (HEART, AARRR), create measurement plans, and quantify product improvements. Use when establishing success metrics, measuring feature impact, or building data-informed product culture.
---

# Product Data Analyst

## Overview

Design metrics frameworks, measurement plans, and analytics strategies to quantify product performance and inform decisions. Apply HEART, AARRR, and other product analytics frameworks.

## Core Frameworks

### HEART (Google)
- **Happiness:** User satisfaction, NPS
- **Engagement:** Usage frequency, session duration
- **Adoption:** New user activation
- **Retention:** Users returning over time
- **Task Success:** Completion rate, time-on-task, error rate

### AARRR (Pirate Metrics)
- **Acquisition:** How users find you
- **Activation:** First good experience
- **Retention:** Users come back
- **Revenue:** Monetization
- **Referral:** Users tell others

### North Star Metric
Single metric that best captures core value delivered to customers. Examples:
- Spotify: Time spent listening
- Airbnb: Nights booked
- Slack: Messages sent by teams

## Measurement Planning

### For each feature/initiative:
1. **Hypothesis:** What will improve and by how much?
2. **Success metrics:** How we'll measure impact
3. **Counter-metrics:** What we don't want to harm
4. **Instrumentation:** What data we need to collect
5. **Analysis plan:** How we'll interpret results

### Good vs bad metrics
**Good (actionable):**
- Time to find asset (can optimize this)
- Search abandonment rate (clear signal)
- Asset reuse rate (measures efficiency)

**Bad (vanity):**
- Total users (doesn't show value)
- Page views (doesn't indicate success)
- Features shipped (output, not outcome)

## Analytics Implementation

### Event tracking design
- Name events clearly (asset_search_completed, not event_42)
- Include context (search_type, result_count, time_to_first_click)
- Track both success and failure paths
- Capture user segments for analysis

### Dashboard principles
- Focus on decisions, not data
- Show trends over time, not just current state
- Include context (goals, benchmarks)
- Alert on anomalies automatically

## When to Use

- Defining success metrics for new features
- Measuring impact of product changes
- Building data-informed product culture
- Investigating performance issues
- Quantifying opportunity size

## Quality Checks

- [ ] Metrics directly relate to user/business value
- [ ] Instrumentation captures what's needed
- [ ] Counter-metrics defined (prevent gaming)
- [ ] Analysis plan clear before shipping
- [ ] Metrics accessible to whole team, not just analysts
