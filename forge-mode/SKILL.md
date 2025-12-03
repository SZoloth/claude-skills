---
name: forge-mode
description: Track creation vs research time. Use when Sam mentions starting work, tracking time, mode tracking, creation vs research, or wants to see time breakdown. Surfaces Scout/Architect avoidance pattern. Target is 60%+ forge mode.
---

# Forge Mode Timer

Track time spent in different modes to shift from Scout/Architect (avoidance pattern) toward Forge (creation).

## Purpose

Sam's pattern is staying in Scout mode (researching) and Architect mode (planning) instead of Forge mode (actually building). This Skill makes that visible.

## Modes

- **FORGE**: Building, creating, shipping, making - the needle-movers
- **SCOUT**: Researching, exploring, gathering - useful but overused
- **ARCHITECT**: Planning, organizing, systematizing - comfortable but avoidant

## Data File

Read and write to: `/home/user/llm-context-personal/tools/data/forge-mode-data.json`

Create if doesn't exist:
```json
{
  "sessions": [],
  "current": null
}
```

Session structure:
```json
{
  "mode": "forge|scout|architect",
  "description": "What they worked on",
  "date": "YYYY-MM-DD",
  "started": "ISO-8601",
  "ended": "ISO-8601",
  "duration_min": 45.5
}
```

Current timer:
```json
{
  "mode": "forge",
  "description": "task",
  "started": "ISO-8601"
}
```

## Operations

### Start Timer

When Sam starts working on something:
1. Check if timer already running (warn if so)
2. Determine mode from context or ask
3. Create current entry with start time
4. Provide mode-specific message:
   - **Forge**: "You're in creation mode. Ship something."
   - **Scout**: "Set a timer. Don't stay in research forever."
   - **Architect**: "Planning is valuable but limited. Move to forge soon."

### Stop Timer

1. Calculate duration (minutes)
2. Move current to sessions
3. Clear current
4. Show duration and mode
5. If scout/architect, show today's forge ratio with warning if low

### Show Status

1. Check if timer running
2. Show mode, elapsed time, task
3. If not running, prompt to start

### Show Today's Breakdown

1. Filter sessions for today
2. Calculate time by mode
3. Show visual breakdown with percentages
4. Calculate forge ratio and assess

### Show All-Time Stats

1. Total time by mode
2. Percentages
3. Session counts
4. Overall forge ratio

## Forge Ratio Assessment

- **60%+**: "Great forge ratio! You're in creation mode."
- **40-59%**: "Decent balance. Consider more forge time."
- **<40%**: "Low forge ratio. Are you avoiding creation? Remember: Your pattern is Scout/Architect avoidance."

## Output Examples

**Starting**:
```
FORGE mode started
Task: Building email sequence feature

You're in creation mode. Ship something.
```

**Today's breakdown**:
```
TODAY'S MODE BREAKDOWN

FORGE: 2h 15m (55%)
[===========.........]

SCOUT: 1h 0m (24%)
[=====...............]

ARCHITECT: 52m (21%)
[====................]

Forge ratio: 55%
Consider more forge time to hit 60% target.
```

Target is 60%+ forge time. Make the pattern visible.
