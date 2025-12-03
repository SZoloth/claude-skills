---
name: carter-rituals
description: Track relationship rituals with Carter. Use when Sam mentions Carter, date nights, relationship maintenance, validating notes, flowers, or relationship rituals. Tracks weekly date, weekly note, and monthly flowers.
---

# Relationship Ritual Tracker

Keep Carter rituals consistent. These shouldn't fall through the cracks.

## Purpose

Track the three relationship rituals:
- 1 planned date per week
- 1 validating note per week
- Flowers monthly

## Data File

Read and write to: `/home/user/llm-context-personal/tools/data/carter-rituals-data.json`

Create if doesn't exist:
```json
{
  "rituals": []
}
```

Ritual entry:
```json
{
  "type": "date|note|flowers",
  "description": "Details",
  "timestamp": "ISO-8601",
  "week": "YYYY-MM-DD",
  "month": "YYYY-MM-01"
}
```

## Operations

### Show Status

1. Calculate current week (Monday) and month
2. Check for each ritual type this period
3. Display checklist

```
CARTER RITUALS

This Week (2025-11-18):
  [x] Planned date
  [ ] Validating note

This Month (2025-11):
  [x] Flowers

Recent:
  Nov 17: date - Dinner at Tavernetta
  Nov 15: flowers - Yellow roses

Still needed: validating note
```

### Log Date

When Sam mentions a date with Carter:
1. Create entry with type "date"
2. Include brief description
3. Show updated status

### Log Note

When Sam mentions writing Carter a note:
1. Create entry with type "note"
2. Include what was written
3. Show updated status

### Log Flowers

When Sam mentions flowers:
1. Create entry with type "flowers"
2. Show updated status

### Show History

Group recent rituals by week and show totals by type.

## Completion Messages

- **All complete**: "All rituals complete! Great relationship maintenance."
- **Partial**: "Still needed: [list missing]"

## Output Format

Keep it simple and checklist-focused. Small, consistent actions > grand gestures.

```
Logged: note
"Appreciated how you handled the conversation with your mom"

This Week:
  [x] Date
  [x] Note

This Month:
  [ ] Flowers (due soon)
```
