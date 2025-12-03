---
name: mcp-troubleshoot
description: Troubleshoot MCP server connection issues, re-authenticate Gmail MCP, and manage server configurations. This skill should be used when MCP tools fail, servers won't connect, Gmail MCP needs re-authentication, or managing MCP server settings. Triggers on "MCP not working", "Gmail MCP", "MCP error", "server won't connect", or "re-authenticate MCP".
---

# MCP Troubleshoot

Diagnose and fix MCP server connection issues.

## Active Servers Reference

| Server | Tools | Purpose |
|--------|-------|---------|
| peekaboo | 21 | macOS GUI automation |
| things | 22 | Task management |
| strava-mcp | 18 | Fitness tracking |
| playwright | 22 | Browser automation |
| pencil | 20 | Design tool |
| google-calendar | 15 | Calendar (personal) |
| google-calendar-dreamworks | 15 | Calendar (work) |
| gmail | ~10 | Email management |

## Gmail MCP Re-authentication

If Gmail MCP fails to connect:

```bash
npx @gongrzhe/server-gmail-autoauth-mcp auth
# Then restart Claude Code
```

**Credentials location:**
- OAuth config: `~/.gmail-mcp/gcp-oauth.keys.json`
- Auth tokens: `~/.gmail-mcp/credentials.json`

**Config in `~/.claude/settings.json`:**
```json
"gmail": {
  "command": "npx",
  "args": ["@gongrzhe/server-gmail-autoauth-mcp"]
}
```

## General Troubleshooting

1. **Server not appearing**: Check `~/.claude/settings.json` for correct config
2. **Tools timing out**: Restart Claude Code to reconnect MCP servers
3. **Token overhead**: Each server adds ~50-200 tokens/tool. Disable unused servers to reduce context cost

## Disable/Enable Servers

Edit `~/.claude/settings.json` and add/remove server entries from the `mcpServers` object.
