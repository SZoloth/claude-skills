---
name: calendar-manager
description: Manage Google Calendar events for job search scheduling. Use when the user wants to check their calendar, schedule interviews, create events, find free time, or manage their schedule. Optimized for job search coordination.
---

# Calendar Manager

A skill for managing Google Calendar events with a focus on job search scheduling using the Code Execution pattern for token efficiency.

## When to use this skill

Use this skill whenever the user:
- Wants to check their calendar (today, this week, specific dates)
- Needs to schedule interviews or coffee chats
- Wants to find free time slots for meetings
- Needs to create, update, or delete calendar events
- Wants to search for specific events
- Mentions "calendar", "schedule", "interview time", "meeting", or calendar tasks

## Prerequisites

This skill requires:
1. Google Calendar MCP server configured in `.mcp.json` (in `1 - personal/.mcp.json`)
2. Python environment with the MCP client modules
3. Google Calendar API credentials properly configured in the MCP server

## Available operations

All operations use the Python CLI at `scripts/calendar_cli.py`.

### Check today's events
```bash
python scripts/calendar_cli.py today
```
Shows all events for today.

### Check this week's events
```bash
python scripts/calendar_cli.py week
```
Shows all events for the next 7 days.

### List events in date range
```bash
python scripts/calendar_cli.py list <start-date> <end-date>
```
Lists events between two dates (YYYY-MM-DD format).

Example:
```bash
python scripts/calendar_cli.py list 2025-11-15 2025-11-22
```

### Search events
```bash
python scripts/calendar_cli.py search <query>
```
Search for events by title, location, or description.

Example:
```bash
python scripts/calendar_cli.py search "interview"
python scripts/calendar_cli.py search "Gusto"
```

### Create event
```bash
python scripts/calendar_cli.py create <title> <start-datetime> <end-datetime> [location] [description]
```
Create a new calendar event (datetimes in ISO format).

Example:
```bash
python scripts/calendar_cli.py create "Interview with Gusto" "2025-11-20T14:00:00" "2025-11-20T15:00:00" "Zoom" "PM role discussion"
```

### Create quick event (relative time)
```bash
python scripts/calendar_cli.py quick <title> <days-from-now> <hour> <duration-hours>
```
Create event with relative scheduling.

Example:
```bash
python scripts/calendar_cli.py quick "Coffee chat" 2 10 1
# Creates 1-hour event in 2 days at 10am
```

### Update event
```bash
python scripts/calendar_cli.py update <event-id> [title] [start] [end] [location]
```
Update an existing event (provide only fields to change).

### Delete event
```bash
python scripts/calendar_cli.py delete <event-id>
```
Delete a calendar event.

### Find free slots
```bash
python scripts/calendar_cli.py free <start-datetime> <end-datetime>
```
Find free time slots in a date range.

Example:
```bash
python scripts/calendar_cli.py free "2025-11-20T09:00:00" "2025-11-20T17:00:00"
# Shows free slots during business hours
```

## Job search use cases

### Check interview schedule
```bash
python scripts/calendar_cli.py search "interview"
```

### Schedule interview
```bash
# Find free time first
python scripts/calendar_cli.py free "2025-11-20T09:00:00" "2025-11-20T17:00:00"

# Create interview event
python scripts/calendar_cli.py quick "Gusto PM Interview" 3 14 1
```

### View upcoming week
```bash
python scripts/calendar_cli.py week
```
See all scheduled interviews, networking events, and deadlines.

### Schedule coffee chat
```bash
python scripts/calendar_cli.py quick "Coffee with [Name]" 5 10 1
```

## Best practices

### When creating events
1. Use descriptive titles including company name
2. Always add location (Zoom link, address, phone)
3. Include relevant details in description (role, interviewer name, preparation notes)
4. Check for conflicts using `free` command first

### When scheduling interviews
1. Search for existing company events first
2. Add travel time buffers for in-person interviews
3. Include preparation time before interviews
4. Set reminders (usually handled by Google Calendar defaults)

### Time format tips
- Use ISO format for exact times: `2025-11-20T14:30:00`
- Use `quick` command for simple relative scheduling
- Check timezone handling (default uses your local timezone)
- Business hours typically: 9am-5pm (09:00-17:00)

## Token efficiency

This skill uses the Code Execution pattern:
- No persistent MCP tools loaded in every conversation
- Python code executes on-demand when skill is invoked
- 95%+ token savings compared to always-on MCP tools
- Clean separation between orchestration (skill) and execution (Python)

## Job Search Hub Integration

**Primary Hub**: `.claude/skills/data/job_search_hub.json`

When checking calendar events, cross-reference with the job search hub for interview detection and prep status.

### Interview Detection Protocol

When checking calendar for interviews:

```python
import json
from pathlib import Path
from datetime import datetime, timedelta

hub_path = Path.home() / "Documents/LLM CONTEXT/.claude/skills/data/job_search_hub.json"
hub = json.loads(hub_path.read_text())

today = datetime.now().date()
soon = today + timedelta(days=3)

# Get pipeline company names
pipeline_companies = {e['company'].lower(): e for e in hub['pipeline']}

# Check each upcoming event
for event in calendar_events:
    title = event.get('summary', '').lower()
    event_date = event.get('start', {}).get('dateTime', '')[:10]

    # Detect interview events
    is_interview = 'interview' in title
    matched_company = next((c for c in pipeline_companies if c in title), None)

    if is_interview or matched_company:
        if event_date <= soon.isoformat():
            entry = pipeline_companies.get(matched_company)
            if entry and not entry.get('prep_complete', False):
                print(f"⚠️ INTERVIEW in {(datetime.fromisoformat(event_date).date() - today).days} days!")
                print(f"   Company: {matched_company}")
                print(f"   Prep complete: ❌")
                print(f"   → Run interview prep workflow?")
```

### Prep Incomplete Alert

When an interview is detected within 3 days AND `hub.pipeline[company].prep_complete == false`:

1. **Display warning**: "Interview with [Company] in X days - prep not complete!"
2. **Offer action**: "Run interview prep? (creates Things task + triggers prep workflow)"
3. **If yes**:
   - Create Things task: "Interview prep: [Company] - [Date]"
   - Update hub: `python scripts/job_search_hub_sync.py --update-pipeline company prep_complete true`

### After Scheduling Interview

When an interview is added to calendar:

**Prompt**: "Add this interview to [Company] in pipeline?"

If yes:
```bash
# Add to pipeline interviews list
python scripts/job_search_hub_sync.py --update-pipeline company status interviewing
```

### Calendar Scan on Morning Planning

When executive-assistant runs morning planning:
1. Get next 3 days of events
2. Detect any interviews
3. Cross-reference with hub.pipeline for prep status
4. Flag any prep_complete=false as action item

## Integration with job search

This skill works well with:
- **gmail-manager**: Check interview invites from emails, then schedule them
- **job-search-specialist**: Coordinate application deadlines and interview schedules
- **executive-assistant**: Manage overall calendar and priorities
- **Hub integration**: Cross-reference interviews with pipeline prep status
