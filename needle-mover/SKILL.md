---
name: needle-mover
description: Track and manage daily high-impact actions. Use when Sam mentions today's priority, daily action, needle mover, what to focus on, or needs help deciding the ONE thing to do today. Fights the pattern of scattered goals by forcing focus on a single action.
---

# Needle Mover Daily

One high-impact action per day. No planning paralysis. Just ONE thing.

## Purpose

This Skill fights Sam's "architect systems, avoid needle-movers" pattern by forcing focus on a single high-impact action instead of 12 scattered goals.

## Data File

Read and write to: `/home/user/llm-context-personal/tools/data/needle-mover-data.json`

Create the file if it doesn't exist with this structure:
```json
{
  "entries": [],
  "streak": 0,
  "last_completed": null
}
```

Entry structure:
```json
{
  "date": "YYYY-MM-DD",
  "category": "job_search|creation|social|relationship|vision",
  "action": "The specific action",
  "completed": false,
  "set_at": "HH:MM",
  "completed_at": "HH:MM"
}
```

## Operations

### Show Today's Needle Mover

1. Read the data file
2. Check for today's entry (use current date in YYYY-MM-DD format)
3. If exists: Show action and status (PENDING or DONE)
4. If not exists: Suggest a needle mover based on 90-day focus
5. Calculate and show current streak (consecutive completed days)
6. Include avoidance check reminder

### Set Needle Mover

When Sam provides an action:
1. Determine category from keywords:
   - friend/denver/social/event/meet → social
   - carter/date/relationship/note → relationship
   - build/ship/create/code/app/prototype → creation
   - vision/2030/future/want → vision
   - Default → job_search (90-day priority)
2. Create entry with current date
3. Remind: "Now go do it. No more planning."

### Mark Complete

1. Find today's entry
2. Set `completed: true` and `completed_at` to current time (HH:MM)
3. Calculate new streak
4. Celebrate based on streak length

### Calculate Streak

Count consecutive days with completed entries, starting from today going backwards.

## Suggestions by Category

Weight suggestions toward job_search (50%), creation (20%), social (15%), relationship (10%), vision (5%).

**job_search** (primary 90-day focus):
- Send 1 personalized outreach email to a hiring manager
- Apply to 1 stretch role you feel underqualified for
- Have 1 informational conversation with someone in target industry
- Follow up with 1 person you haven't heard back from
- Practice STAR response for your weakest case story

**creation**:
- Build 1 small feature for your app (not research, BUILD)
- Ship 1 public prototype demonstrating a skill
- Write 1 post sharing something you learned

**social**:
- Message 1 potential Denver friend to meet up
- Go to 1 local event alone and talk to someone new
- Invite someone to do an activity with you this week

**relationship**:
- Write Carter a validating note about something specific
- Plan a specific date for this week
- Share 1 vulnerable feeling without trying to fix it

**vision**:
- Spend 30 minutes on your 2025-2030 vision (not organizing, DECIDING)
- Answer: What would you do if money/status didn't matter?
- Draft 1 paragraph describing your life in 2030

## Output Format

Always include:
1. Today's date
2. The needle mover (existing or suggested)
3. Status (pending/complete)
4. Current streak
5. Avoidance check reminder:

```
AVOIDANCE CHECK:
- Uncomfortable but important? → DO IT
- Comfortable but low-impact? → THIS IS AVOIDANCE
```

Be direct and action-oriented. No fluff. The goal is to get Sam moving on ONE thing.
