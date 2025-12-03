# MCP Server Requirements

This document lists the MCP (Model Context Protocol) servers that skills in this repository depend on.

## Required MCP Servers

### Things 3 (macOS only)
**Used by:** `executive-assistant`, `morning-kickstart`, `beads-viewer`

**Tools:** `mcp__things__get_today`, `mcp__things__get_projects`, `mcp__things__add_todo`, etc.

**Setup:**
```json
// Add to ~/.claude/settings.json under "mcpServers"
"things": {
  "command": "npx",
  "args": ["-y", "@anthropic/mcp-server-things"]
}
```

### Gmail
**Used by:** `gmail-manager`, `executive-assistant`, `morning-kickstart`

**Tools:** `mcp__gmail__search_emails`, `mcp__gmail__read_email`, `mcp__gmail__send_email`, etc.

**Setup:**
```json
"gmail": {
  "command": "npx",
  "args": ["@gongrzhe/server-gmail-autoauth-mcp"]
}
```

### Google Calendar
**Used by:** `executive-assistant`, `morning-kickstart`, `calendar-manager`

**Tools:** `mcp__google-calendar__list-events`, `mcp__google-calendar__create-event`, etc.

**Setup:**
```json
"google-calendar": {
  "command": "npx",
  "args": ["-y", "@anthropic/mcp-server-google-calendar"],
  "env": {
    "GOOGLE_CLIENT_ID": "your-client-id",
    "GOOGLE_CLIENT_SECRET": "your-client-secret"
  }
}
```

### Strava
**Used by:** `morning-kickstart`

**Tools:** `mcp__strava-mcp__get-athlete-profile`, `mcp__strava-mcp__get-recent-activities`, etc.

**Setup:**
```json
"strava-mcp": {
  "command": "npx",
  "args": ["-y", "@anthropic/mcp-server-strava"],
  "env": {
    "STRAVA_CLIENT_ID": "your-client-id",
    "STRAVA_CLIENT_SECRET": "your-client-secret",
    "STRAVA_REFRESH_TOKEN": "your-refresh-token"
  }
}
```

### Linear (optional)
**Used by:** `linear-manager`

**Tools:** `mcp__linear__*`

**Setup:**
```json
"linear": {
  "command": "npx",
  "args": ["-y", "@anthropic/mcp-server-linear"],
  "env": {
    "LINEAR_API_KEY": "your-api-key"
  }
}
```

## Minimal Setup

If you only need basic skills, you can skip MCP servers entirely. The following skills work without any MCP servers:

- `think-first` - Cognitive engagement coaching
- `upskilling-coach` - Learning acceleration
- `monodraw-diagrams` - ASCII diagram creation
- `communication-optimizer` - Document optimization
- `marty-cagan-coach` - Product coaching
- `product-transformation-coach` - Organizational transformation
- `research-expert` - Research methodology
- `validation-expert` - UX validation
- `stakeholder-analyst` - Stakeholder communication
- `jtbd-*` - Jobs-to-be-Done skills
- `odi-outcome-generator` - ODI statements
- `fact-checker-investigator` - Claim verification
- `rodbt-coach` - RO-DBT therapy (uses local files)

## Permission Configuration

Add skill permissions to your project's `.claude/settings.local.json`:

```json
{
  "permissions": {
    "allow": [
      "Skill(morning-kickstart)",
      "Skill(executive-assistant)",
      "Skill(upskilling-coach)",
      "Skill(rodbt-coach)",
      "mcp__things__get_today",
      "mcp__things__add_todo",
      "mcp__gmail__search_emails"
    ]
  }
}
```

## Troubleshooting

### MCP Server Won't Start
1. Check that Node.js is installed: `node --version`
2. Try running the npx command directly to see errors
3. Check environment variables are set correctly

### Skills Not Available
1. Verify symlink exists: `ls -la ~/.claude/skills`
2. Check skill has SKILL.md file with proper frontmatter
3. Restart Claude Code after setup

### Authentication Issues
For Gmail and Google Calendar:
1. You may need to re-authenticate periodically
2. Use `mcp-troubleshoot` skill for guided troubleshooting
