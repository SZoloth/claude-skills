---
name: beads-briefing
description: Executive briefing from beads task tracker. MANDATORY at session start. Shows overdue, due today, and blocked items. Use when user starts session, greets you, or asks about tasks/priorities.
---

# Beads Executive Briefing

## MANDATORY USAGE

**This skill MUST be invoked:**
1. At the START of every session (before any other work)
2. When user greets you (good morning, hey, let's go, etc.)
3. When user asks about tasks, priorities, or what to work on
4. Before ending a session (to confirm nothing was missed)

**DO NOT proceed with other work until this briefing is complete.**

## Purpose

Surface critical task information from beads (bd) so nothing falls through the cracks:
- Overdue items (priority 0 past due date)
- Due today (priority 0 items)
- Blocked items (waiting on others)
- This week's priorities

## Instructions

### Step 1: Get Ready Tasks

```bash
/Users/szolot431@cable.comcast.com/.local/bin/bd ready --json
```

### Step 2: Parse and Categorize

From the JSON output, categorize tasks:

**CRITICAL (Priority 0):**
- These are due TODAY or OVERDUE
- Surface these FIRST with urgency

**THIS WEEK (Priority 1):**
- Due within the week
- Show after critical items

**BLOCKED:**
- Status contains "BLOCKER" or "waiting" in description
- Call out who/what is blocking

### Step 3: Format Executive Briefing

Output format:

```
## TODAY - [Date]

### CRITICAL (Must Address Now)
| ID | Task | Status | Notes |
|----|------|--------|-------|
| xxx | Task name | OVERDUE/DUE TODAY | Context |

### BLOCKED (Needs Escalation)
| ID | Task | Blocker |
|----|------|---------|
| xxx | Task name | Who/what is blocking |

### THIS WEEK
| ID | Task | Due |
|----|------|-----|
| xxx | Task name | Target date |

---
**What do you want to tackle first?**
```

### Step 4: Push for Action

After showing the briefing:
1. Ask which item to start with
2. If user tries to ignore critical items, PUSH BACK
3. Update task status to `in_progress` when starting work
4. Mark `closed` when complete

## Enforcement Rules

1. **Never skip the briefing** - Even if user seems eager to start something else
2. **Call out ignored items** - If critical items aren't addressed by session end, flag them
3. **Update beads in real-time** - Mark in_progress/closed as work happens
4. **End-of-session check** - Before signing off, review what was/wasn't completed

## Integration with Other Skills

**With mission-control-session:**
- Run beads-briefing BEFORE mission-control-session start
- Or integrate beads data into session start

**With daily-reminders:**
- Beads-briefing replaces daily-reminders for task tracking
- daily-reminders still useful for relationship staleness

## Example Session

```
User: "hey"

Claude: [Runs bd ready --json]
Claude:
"## TODAY - Dec 3

### CRITICAL (Must Address Now)
| ID | Task | Status | Notes |
|----|------|--------|-------|
| 648 | Watch Galaxy demo recordings | OVERDUE | Carl shared Dec 2 |
| 8mm | Michelle meeting | TODAY | Validate process |
| 8f1 | Yao live demo | TODAY | EDI/ODIA demo |

### BLOCKED
| ID | Task | Blocker |
|----|------|---------|
| c9r | OSO access | Carl investigating |

### THIS WEEK
| ID | Task | Due |
|----|------|-----|
| a10 | Put test order through Galaxy | Dec 9 |
| 38s | Create UAT test scripts | Dec 6 |

---
**The demo recordings were supposed to be watched yesterday. What's the plan there?**"
```

## Commands Reference

```bash
# Get all ready tasks
/Users/szolot431@cable.comcast.com/.local/bin/bd ready --json

# Update task status
/Users/szolot431@cable.comcast.com/.local/bin/bd update <id> --status in_progress --json
/Users/szolot431@cable.comcast.com/.local/bin/bd close <id> --reason "Completed" --json

# Create new task
/Users/szolot431@cable.comcast.com/.local/bin/bd create "Task title" -t task -p 0 --json

# Sync at session end
/Users/szolot431@cable.comcast.com/.local/bin/bd sync
```

## Success Criteria

- No task goes unaddressed for >1 day without explicit acknowledgment
- Critical items are surfaced immediately at session start
- Blocked items get escalation plan
- End of session confirms task status updates
- User never asks "why didn't you remind me about X"
