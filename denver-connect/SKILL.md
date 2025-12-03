---
name: denver-connect
description: Weekly micro-action challenges for building Denver friendships. Use when Sam mentions local friends, Denver social life, loneliness, social anxiety, making friends, or connecting with people locally. Addresses the pattern of zero local friends after 2+ years.
---

# Denver Connection Challenge

Build local friendships through consistent micro-actions. One small action per week.

## Purpose

Sam has been in Denver 2+ years with zero local close friends. Social anxiety leads to avoidance. This Skill provides small, manageable weekly challenges to build comfort and connection.

## Data File

Read and write to: `/home/user/llm-context-personal/tools/data/denver-connect-data.json`

Create if doesn't exist:
```json
{
  "challenges": [],
  "current_level": 1,
  "consecutive_skips": 0
}
```

Challenge entry:
```json
{
  "week": "YYYY-MM-DD",
  "challenge": "The challenge text",
  "assigned": "ISO-8601",
  "completed": false,
  "what_happened": "Description",
  "completed_at": "ISO-8601",
  "skipped": false
}
```

## Challenge Levels

**Level 1 - Low Stakes**:
- Have a real conversation with a barista or cafe regular (not just ordering)
- Compliment someone at the gym/coffee shop on something specific
- Ask someone at a coffee shop what they're working on
- Make eye contact and smile at 3 strangers today
- Say hi to a neighbor you've never talked to

**Level 2 - Small Talk**:
- Go to a local event alone and talk to at least 1 person
- Join a Meetup group and attend one event
- Ask someone at a coffee shop if you can sit at their table
- Strike up a conversation with someone at a run club/gym class

**Level 3 - Taking Initiative**:
- Message someone you've met once to get coffee
- Invite someone from a Meetup/class to hang out separately
- Ask a coworker/acquaintance to grab lunch
- Follow up with someone you exchanged numbers with

**Level 4 - Vulnerability**:
- Tell someone new you're trying to build more local friendships
- Admit to someone that you find making friends hard
- Invite someone to do something you're nervous about
- Share something personal with an acquaintance

## Operations

### Get This Week's Challenge

1. Calculate current week (Monday)
2. Check for existing challenge
3. If exists: Show with status
4. If not: Assign new one from current level
5. Show: challenge, level, completed count, streak
6. Reminder: "Zero local friends after 2+ years is the pattern."

### Log Completion

When Sam says they did the challenge:
1. Get description of what happened
2. Mark completed
3. Reset consecutive skips
4. Check for level up (every 3 completions)
5. Show streak and encouragement

### Skip Week

1. Mark skipped
2. Increment consecutive_skips
3. Provide accountability:
   - 1 skip: "Skipped. Don't let it become a pattern."
   - 2 skips: "2 in a row. The discomfort is the growth."
   - 3+ skips: "3+ consecutive. Social anxiety wins by you not showing up."

### Show Ideas

List all challenges by level.

## Level Up Logic

Every 3 completions → advance to next level (max 4)

## Output Format

```
DENVER CONNECTION CHALLENGE

This Week's Challenge:
  Go to a local event alone and talk to at least 1 person

Level: 2/4
Completed: 5
Weekly Streak: 2

Remember: Zero local friends after 2+ years is the pattern.
One micro-action per week breaks it.
```

The discomfort is the point—that's where growth happens.
