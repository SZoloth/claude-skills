# Gmail & Calendar Manager Skills

**Created:** 2025-11-15
**Pattern:** Code Execution with MCP (95%+ token savings)
**Purpose:** Job search communication and scheduling workflows

## What Was Built

Two new Claude Code Skills that use the **Code Execution pattern** for token-efficient email and calendar management:

1. **gmail-manager** - Email operations (search, send, draft, manage inbox)
2. **calendar-manager** - Calendar operations (schedule, search, find free time)

### Why These Skills?

Based on your job search workflow analysis:
- **High-frequency need**: Checking recruiting emails, scheduling interviews, sending follow-ups
- **Token efficiency**: 95%+ savings vs. always-on MCP tools
- **Job-search optimized**: Commands and examples tailored to PM job search

## Architecture

```
User request → Claude invokes skill → Skill executes Python code → Python calls MCP server → Result returned
```

**Key benefit**: MCP tool schemas aren't loaded into every conversation. Code executes on-demand only when skills are used.

## Files Created

### Skills
- `.claude/skills/gmail-manager/SKILL.md` - Gmail skill documentation
- `.claude/skills/calendar-manager/SKILL.md` - Calendar skill documentation

### CLI Scripts
- `scripts/gmail_cli.py` - Gmail command-line interface
- `scripts/calendar_cli.py` - Calendar command-line interface

### Supporting Infrastructure (already existed)
- `scripts/mcp_tools/gmail.py` - Gmail Python wrapper
- `scripts/mcp_tools/calendar.py` - Calendar Python wrapper
- `scripts/mcp_tools/client.py` - Base MCP client
- `scripts/mcp_tools/config.py` - Configuration loader

## Setup Required

### Step 1: Install MCP Servers

You need to add Gmail and Google Calendar MCP servers to `.mcp.json`.

**Option A: Use official Google MCP servers (if available)**

Check if these exist:
```bash
npx -y @modelcontextprotocol/server-gmail --help
npx -y @modelcontextprotocol/server-google-calendar --help
```

**Option B: Build custom MCP servers**

Create simple MCP servers that wrap the Gmail and Google Calendar APIs using the MCP SDK.

### Step 2: Configure `.mcp.json`

Add to `1 - personal/.mcp.json`:

```json
{
  "mcpServers": {
    "gmail": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-gmail"],
      "env": {
        "GOOGLE_API_CREDENTIALS": "path/to/credentials.json"
      }
    },
    "google-calendar": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-google-calendar"],
      "env": {
        "GOOGLE_API_CREDENTIALS": "path/to/credentials.json"
      }
    },
    "eight_sleep": { ... existing ... },
    "readwise": { ... existing ... }
  }
}
```

**Note**: Exact configuration depends on which MCP servers you use. Adjust `command`, `args`, and `env` accordingly.

### Step 3: Google API Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or use existing)
3. Enable APIs:
   - Gmail API
   - Google Calendar API
4. Create OAuth 2.0 credentials
5. Download credentials JSON
6. Set up OAuth consent screen (if needed)
7. Authenticate the first time (will open browser)

### Step 4: Test MCP Servers

Verify the MCP servers work:

```bash
# Test from Python
cd "/Users/samuelz/Documents/LLM CONTEXT"
python scripts/mcp_tools/examples/daily_plan.py
```

If this works, the MCP infrastructure is set up correctly!

### Step 5: Test CLI Scripts

```bash
# Test Gmail CLI
python scripts/gmail_cli.py unread 5

# Test Calendar CLI
python scripts/calendar_cli.py today
```

## Usage Examples

### Job Search Workflows

#### 1. Morning Email Check
```bash
# Check unread recruiting emails
python scripts/gmail_cli.py search "recruiter OR interview OR application" 10
```

**In Claude Code:**
> "Check my recruiting emails from the last few days"

Claude will invoke the gmail-manager skill and execute the search.

#### 2. Schedule Interview
```bash
# Find free time
python scripts/calendar_cli.py free "2025-11-20T09:00:00" "2025-11-20T17:00:00"

# Schedule interview
python scripts/calendar_cli.py quick "Gusto PM Interview - Round 2" 5 14 1
```

**In Claude Code:**
> "I have a Gusto interview next Wednesday at 2pm. Can you schedule it?"

Claude will find free time and create the event.

#### 3. Follow-up Email Workflow
```bash
# Search for original email
python scripts/gmail_cli.py search "from:recruiter@davita.com interview"

# Get specific email
python scripts/gmail_cli.py get <message-id>

# Create draft follow-up
python scripts/gmail_cli.py draft "recruiter@davita.com" "Follow-up: PM Role Interview" "Thank you for the opportunity..."
```

**In Claude Code:**
> "Draft a follow-up email to the DaVita recruiter thanking them for the interview"

Claude will search for the original email, draft a professional follow-up, and create it in your Gmail drafts for review.

#### 4. Interview Prep Schedule
```bash
# Check this week's calendar
python scripts/calendar_cli.py week

# Schedule prep time before interview
python scripts/calendar_cli.py quick "Prep: Atlassian Interview" 3 12 2
```

**In Claude Code:**
> "I have an Atlassian interview on Thursday. Block 2 hours on Wednesday afternoon for prep"

## Token Savings Breakdown

### Old Approach (Always-On MCP Tools)
Every conversation includes:
- Gmail MCP tool definitions: ~3,500 tokens
- Calendar MCP tool definitions: ~2,800 tokens
- Things MCP tool definitions: ~2,500 tokens
- **Total overhead**: ~8,800 tokens per conversation

### New Approach (Code Execution Pattern)
- Skills load on-demand: ~0 tokens when not used
- When invoked: ~200-500 tokens (just the summary)
- **Total overhead**: ~200-500 tokens only when skills are used

**Savings: 95-97%** when skills aren't active, **still 94%** even when they are!

## Best Practices

### Email Management
1. **Always search first** - Don't browse unread, use specific queries
2. **Create drafts for important emails** - Review before sending
3. **Use Gmail search syntax** - `from:`, `subject:`, `is:unread`, `after:YYYY/MM/DD`
4. **Archive processed emails** - Keep inbox clean

### Calendar Management
1. **Check conflicts first** - Use `free` command before scheduling
2. **Use descriptive titles** - Include company name and role
3. **Add preparation buffers** - Schedule prep time before interviews
4. **Quick command for simple events** - Faster than full ISO datetimes

### Integration with Other Skills
- **job-search-specialist**: Coordinate application tracking with email/calendar
- **executive-assistant**: Daily planning uses both email and calendar
- **linear-manager**: Create Linear tasks from recruiting emails

## Troubleshooting

### "Gmail MCP server not configured"
- Check `.mcp.json` has `"gmail"` entry
- Verify MCP server is installed and accessible
- Test with `python scripts/mcp_tools/examples/daily_plan.py`

### "Google API authentication failed"
- Verify credentials.json path is correct
- Check OAuth consent screen is configured
- Re-authenticate: delete token file and run again
- Ensure Gmail API is enabled in Google Cloud Console

### "Command not found: npx"
- Install Node.js: `brew install node`
- Verify: `npx --version`

### Skills not auto-invoking in Claude Code
- Check skill names in frontmatter match directory names
- Verify `SKILL.md` files exist and have proper frontmatter
- Restart Claude Code to reload skills

## Next Steps

1. **Set up Google API credentials** (Step 3 above)
2. **Install Gmail & Calendar MCP servers** (Step 1-2)
3. **Test the CLI scripts** (Step 4-5)
4. **Try the job search workflows** in Claude Code

Once set up, you can use natural language in Claude Code:
- "Check my recruiting emails"
- "Schedule a coffee chat with [name] next week"
- "What's on my calendar today?"
- "Draft a follow-up to [company] recruiter"

Claude will automatically invoke the appropriate skills and execute the operations!

## Related Skills

- **executive-assistant**: Uses gmail + calendar for daily planning
- **job-search-specialist**: Tracks applications and interviews
- **linear-manager**: Task management for job search projects

## References

- [Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) - 95% token savings pattern
- [Claude Code Skills](https://claude.com/blog/skills) - Skill system documentation
- MCP Protocol: Model Context Protocol for tool integration
