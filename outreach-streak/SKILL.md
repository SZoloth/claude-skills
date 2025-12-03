---
name: outreach-streak
description: Track job search outreach with weekly streak counter. Use when Sam mentions job outreach, applications, networking, job search progress, or wants to log a contact with a company. Target is 10 outreaches per week.
---

# Outreach Streak Tracker

Visual streak counter for the 10 outreaches/week target. Creates external accountability when internal motivation fails.

## Purpose

Job search has "pressure without motivation." This Skill creates momentum through visible streaks and progress tracking.

## Data Source: Unified Hub

**Primary Hub**: `.claude/skills/data/job_search_hub.json`

This skill reads from and writes to the unified job search hub, specifically:
- `hub.outreach[]` - Global outreach log
- `hub.metrics.weekly_outreach[]` - Weekly aggregates
- `hub.metrics.streak_count` - Consecutive weeks hitting target
- `hub.pipeline[company].emails_sent[]` - Per-company tracking

**CLI Tool**: Use `python scripts/job_search_hub_sync.py` for operations.

## Hub Data Structures

### Outreach Entry (in hub.outreach[])
```json
{
  "date": "2025-11-30",
  "type": "email",
  "contact": "John Doe",
  "company": "Stripe",
  "company_id": "stripe",
  "summary": "email to John Doe",
  "response_received": false,
  "follow_up_sent": false
}
```

### Weekly Aggregate (in hub.metrics.weekly_outreach[])
```json
{
  "week": "2025-11-25",
  "count": 6,
  "outreaches": ["Stripe:John Doe", "Figma:Jane Smith"]
}
```

## Operations

### Show This Week's Progress

```bash
python scripts/job_search_hub_sync.py --status
```

Or display inline:
1. Read hub.metrics.weekly_outreach for current week
2. Count against 10/week target
3. Display progress bar: `[OOOO......] 4/10`
4. Show:
   - Days left in week
   - Required daily pace to hit target
   - Today's outreach count
   - Recent outreaches (last 5)
   - Weekly streak from hub.metrics.streak_count

### Log an Outreach

When Sam mentions contacting a company:

```bash
python scripts/job_search_hub_sync.py --log-outreach "Company" "Contact Name" email
```

This automatically:
1. Adds to `hub.outreach[]`
2. Updates `hub.metrics.weekly_outreach[]`
3. Updates `hub.pipeline[company].emails_sent[]` if company in pipeline
4. Displays updated week progress

### Generate Scorecard

```bash
python scripts/job_search_hub_sync.py --generate-scorecard
```

Shows comprehensive view:
- Week progress bar
- Pipeline by status
- Response rate
- Streak count
- Stale items

## Week Calculation

Week starts Monday. Use: `week_start = current_date - days_since_monday`

## Progress Display

```
OUTREACH STREAK

This Week: [OOOOOO....] 6/10

Status: 4 more needed, 2 days remaining
Need 2/day to hit target

Today: 1 outreach

Recent:
- Nov 18: Stripe (email to John Doe)
- Nov 18: Figma (linkedin to Jane Smith)
- Nov 17: Canva (email to Recruiter)

Weekly Streak: 2 weeks hitting target
```

## Cross-Linking with Pipeline

When logging outreach for a company in the pipeline:

1. Find matching entry in `hub.pipeline[]`
2. Append to that entry's `emails_sent[]`
3. Update `last_action_date`
4. This keeps all company touchpoints unified

## Motivation Messages

- **On target (10+)**: "TARGET HIT! Week complete."
- **Close (7-9)**: "Almost there! X more to hit target."
- **Behind pace**: "Time to move! Need X/day remaining."
- **Wednesday+ and < 7**: "PACE WARNING: Behind on outreach!"

Be direct and numbers-focused. Create visible accountability.

## Integration with Other Skills

| Trigger | Action |
|---------|--------|
| gmail-manager sees job email sent | Offer to log as outreach |
| job-search-specialist processes application | Log as outreach automatically |
| executive-assistant weekly review | Pull streak data for scorecard |
