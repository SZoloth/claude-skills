---
name: mcporter
description: Discover, inspect, and call MCP servers directly from CLI without needing Claude. This skill should be used when listing available MCP tools, calling MCP tools directly, viewing tool schemas, or generating standalone CLIs from MCP servers. Triggers on "list MCP", "call MCP tool", "MCP schema", or "generate CLI from MCP".
---

# mcporter - MCP Discovery & Direct CLI

Discover, call, and generate CLIs from MCP servers without needing Claude in the loop.

## Common Commands

```bash
# List all discovered MCP servers
mcporter list

# View tool documentation and schema
mcporter list things --schema

# Call MCP tools directly
mcporter call things.get_today
mcporter call strava-mcp.get-recent-activities perPage:5

# Generate standalone CLI from MCP server
mcporter generate-cli --server things --compile ./things-cli
```

## When to Use

- Inspect what tools an MCP server provides
- Call MCP tools directly without Claude overhead
- Generate standalone CLI binaries for frequent operations
- Debug MCP server configurations

## Configuration

Config location: `~/config/mcporter.json`

Auto-imports configurations from Claude and Cursor config files.
