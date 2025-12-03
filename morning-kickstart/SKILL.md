---
name: morning-kickstart
description: Enhanced morning ritual with bi-directional integration between Things MCP (tasks), Strava MCP (training), and existing trackers. Use when Sam mentions morning routine, starting the day, daily planning, morning kickstart, or wants an overview. Provides intelligent cross-domain insights where data sources inform each other.
---

# Morning Kickstart (Enhanced)

Start your day with intentionality. Combines Things, Strava, and existing trackers with **bi-directional integration** for intelligent insights.

## Purpose

Quick morning ritual (~2 minutes) that:
1. Suggests needle-mover from Things P1 tasks (energy-aware)
2. Shows job search momentum with Things task alignment
3. Displays training status with energy level for task planning
4. Provides ritual checks with cross-domain context
5. Detects avoidance patterns

**Key Innovation**: Data sources actively inform each other - Things P1 tasks become needle-mover suggestions, Strava training load influences challenge timing, energy levels shape task recommendations.

## Data Sources (Bi-directional Integration)

### MCP Sources (via code execution - 95% token savings)
- **Things MCP**: Today's tasks, P1/P2 priorities, upcoming 3 days
- **Strava MCP**: Recent activities, athlete stats, weekly training data

### Local Files
- `/Users/samuelz/Documents/LLM CONTEXT/.claude/skills/data/needle-mover-data.json`
- `/Users/samuelz/Documents/LLM CONTEXT/.claude/skills/data/outreach-streak-data.json`
- `/Users/samuelz/Documents/LLM CONTEXT/.claude/skills/data/carter-rituals-data.json`
- `/Users/samuelz/Documents/LLM CONTEXT/.claude/skills/data/denver-connect-data.json`
- `/Users/samuelz/Documents/LLM CONTEXT/.claude/skills/data/workout-plan-metadata.json`

### Integration Examples
- **Things P1 → Needle-mover**: Most uncomfortable P1 task suggested
- **Strava energy → Task selection**: HIGH energy = hard tasks, LOW = easier tasks
- **Workout plan → Denver**: "Long run Saturday → try run club!"
- **Things tags → Outreach**: "#job-search tasks → log to tracker"

## Output Structure (Enhanced with Integration)

### 1. Today's Needle Mover (with Things + Strava context)
- **Suggested action** from Things P1 tasks
- **From Things**: How many P1 tasks, why this one chosen
- **Training context**: Energy level (HIGH/MEDIUM/LOW) from Strava
- **Outreach alignment**: How it helps weekly goal
- **Current streak**: Days consecutive
- **Avoidance check**: Pattern detection ("Uncomfortable = important" or "⚠️ Architect pattern?")

### 2. Job Search Momentum (with Things + Energy context)
- **Progress bar**: Visual [OOOOOO....] X/10 for week
- **Remaining**: How many more needed
- **Things Context**:
  - Count of #job-search tagged tasks
  - Top 3 tasks listed
  - Reminder to log completions
- **Energy suggestion**: Based on training (e.g., "High energy → 2-3 quality outreaches")
- **Weekly streak**: Weeks hitting 10/week target

### 3. Quick Checks (with cross-domain context)
**Carter Rituals**:
- This Week: [ ] Date [ ] Note
- This Month: [ ] Flowers
- **Things integration**: "Planned in Things: Date night"

**Denver Connection**:
- Current challenge
- Status
- **Training tie-in**: "Saturday long run → try run club!"

### 4. Today's Training (NEW - Strava + Workout Plan)
- **Current phase**: "Phase 2, Week 2: Ski Prep Build"
- **Phase dates**: (2025-11-18 to 2025-12-15)
- **Today's workout**: From weekly template
- **This week**:
  - Volume: X/Y miles (on track / behind)
  - Time: Hours trained
  - Workouts completed: Checkboxes
- **Energy Level**: HIGH/MEDIUM/LOW
  - HIGH → "Good for uncomfortable/hard tasks"
  - LOW → "Save energy for training"

### 5. Remember (context-aware)
- Energy-specific reminder (if HIGH: "Do hard things first")
- "Uncomfortable = probably important"
- "Job search is 90-day priority"

## Implementation Notes

### Code Execution Pattern (95% Token Savings)
Instead of calling Things/Strava MCP tools directly (~10,000 tokens), the skill uses Python code execution:

```python
#!/usr/bin/env python3
import sys
sys.path.append('/Users/samuelz/Documents/LLM CONTEXT/scripts')
sys.path.append('/Users/samuelz/Documents/LLM CONTEXT/.claude/skills/morning-kickstart')

from mcp_tools import things, strava
from kickstart_engine import generate_morning_summary

# Fetch and process data locally (happens in Python, not in context!)
summary = generate_morning_summary()

# Return only concise summary (~300-500 tokens)
print(summary)
```

**Result**: ~500 tokens total vs ~10,000+ tokens with direct MCP calls (95% savings)

### Graceful Degradation
- If Things MCP unavailable → uses tracker data only
- If Strava MCP unavailable → uses workout plan for energy estimate
- If workout metadata stale → auto-refreshes from markdown
- If all MCPs fail → falls back to legacy mode

### Manual Overrides
- Needle-mover: User can override AI suggestion (accept by default)
- Workout metadata: Manual update when plan changes (every 2-8 weeks)
- Energy level: Falls back to workout plan if no Strava data

---

## Full Output Example

```
════════════════════════════════════════════════════════════
MORNING KICKSTART - Wednesday, November 20
════════════════════════════════════════════════════════════

1. TODAY'S NEEDLE MOVER
────────────────────────────────────────────────────────────
[JOB_SEARCH] Personalized outreach to Stripe hiring manager

From Things: 3 P1 tasks today, this one is most uncomfortable
Training: High energy (rest day) → good for hard work
Outreach: Need 4 more this week → this gets you closer

Streak: 4 days

AVOIDANCE CHECK: Uncomfortable = important. Do it first.

────────────────────────────────────────────────────────────
2. JOB SEARCH MOMENTUM
────────────────────────────────────────────────────────────
This Week: [OOOOOO....] 6/10
Need 2/day remaining (Thu, Fri) to hit target

Things Context:
  - 3 tasks tagged #job-search today
  - "Apply to Figma PM role" marked P1
  - When complete, log to outreach tracker

Energy: High (rest day) → aim for 2-3 quality outreaches today

Weekly Streak: 2 weeks hitting 10

────────────────────────────────────────────────────────────
3. QUICK CHECKS
────────────────────────────────────────────────────────────
Carter Rituals:
  This Week: [x] Date [ ] Note
  This Month: [x] Flowers
  Still needed: Validating note (write tonight)

Denver Connection:
  Challenge: Go to a local event alone and talk to 1 person
  Status: PENDING
  Training tie-in: Saturday long run → try run club!

────────────────────────────────────────────────────────────
4. TODAY'S TRAINING
────────────────────────────────────────────────────────────
Phase 2, Week 1: Ski Prep Build (Nov 18 - Dec 15)
Today: REST (recovery from Tuesday's tempo run)

This Week:
  - Volume: 18/24 mi (on track)
  - Workouts: ✓ Tempo ✓ Strength □ Easy □ Long
  - Next: Easy 5 mi tomorrow

Energy Level: HIGH (rest day) → good for uncomfortable work

════════════════════════════════════════════════════════════
REMEMBER:
  - After rest day: Energy available, do hard things first
  - Uncomfortable = probably important
  - Job search is 90-day priority
════════════════════════════════════════════════════════════
```

**Notice the integration**:
- "From Things: 3 P1 tasks, this one is most uncomfortable" ← Things informs needle-mover
- "Training: High energy → good for hard work" ← Strava informs task selection
- "3 tasks tagged #job-search → log to tracker" ← Things aligns with outreach
- "Saturday long run → try run club!" ← Workout plan informs Denver challenge

## Important

This is a 2-minute ritual, not a 20-minute planning session. Show the info, prompt for action, done. The goal is clarity and intentionality, not another planning loop.
