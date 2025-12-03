# Executive Assistant Skill

This skill provides comprehensive EA/PM capabilities that automatically activate when relevant topics are discussed.

## How It Works

This is a **Claude Code Skill** that automatically activates when you discuss:
- Daily planning and morning rituals
- Weekly reviews and strategic planning
- Calendar management and scheduling
- Email triage and inbox management
- Task prioritization and Things 3 integration
- Cross-domain life coordination
- Synthesis freshness checks

## Usage

Simply talk naturally about these topics. For example:

```
"Generate my daily plan for today"
"Check my calendar and help me schedule time for P1 tasks"
"Triage my inbox and categorize by domain"
"Run my weekly review"
"Check my synthesis freshness"
"What should I focus on today?"
```

No `npm start` needed! Claude automatically uses this skill when relevant.

## Key Features

- **Morning Planning** (7-12 min): Pull Things tasks, check calendar, triage email
- **Evening Reflection** (7-8 min): Self-enquiry, task updates, tomorrow prep
- **Weekly Reviews** (15 min): Aggregate data, generate insights, Big Three
- **Synthesis Monitoring**: Automatic freshness checks, update suggestions
- **Calendar Integration**: Google Calendar and Apple Calendar via MCP
- **Email Management**: Gmail integration for triage and organization
- **Cross-Domain Coordination**: Manage 7 life domains strategically

## MCP Tools Available

### Things 3
- `mcp__things__get-today`, `mcp__things__get-upcoming`, `mcp__things__get-projects`
- `mcp__things__create-todo`, `mcp__things__update-todo`

### Google Calendar
- `mcp__google_calendar__list_events`, `mcp__google_calendar__create_event`
- `mcp__google_calendar__update_event`, `mcp__google_calendar__delete_event`
- `mcp__google_calendar__get_free_busy`, `mcp__google_calendar__search_events`

### Gmail
- `mcp__gmail__list_messages`, `mcp__gmail__get_message`
- `mcp__gmail__send_message`, `mcp__gmail__reply_to_message`
- `mcp__gmail__create_draft`, `mcp__gmail__modify_labels`
- `mcp__gmail__mark_as_read`, `mcp__gmail__search_messages`

## Setup

See `agents/MCP_INTEGRATION_GUIDE.md` for complete setup instructions for Calendar and Email MCP integrations.

## Related Documentation

- Main README: `agents/AGENTS_README.md`
- MCP Setup Guide: `agents/MCP_INTEGRATION_GUIDE.md`
- Daily Planning System: `1 - personal/strategic_planning/daily_planning/daily_planning_system.md`
- Synthesis Document: `1 - personal/about_sam/synthesis-frameworks.md`
