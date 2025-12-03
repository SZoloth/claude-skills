---
name: agent-sdk
description: Create and run autonomous agents using the Anthropic Agent SDK. Use when the user wants to build custom AI agents, automate workflows with Claude's capabilities, or execute complex multi-step tasks programmatically.
---

# Anthropic Agent SDK

A comprehensive skill for creating, configuring, and running autonomous agents using the Anthropic Agent SDK (formerly Claude Code SDK).

## When to Use

Use this skill whenever the user:
- Wants to create a custom AI agent
- Needs to automate complex workflows with Claude
- Wants to build agents that can read files, execute code, or interact with systems
- Needs programmatic access to Claude's agentic capabilities
- Wants to create specialized agents for specific tasks (data analysis, code review, research, etc.)

## Overview

The Anthropic Agent SDK enables you to programmatically build AI agents with Claude Code's capabilities to create autonomous agents that can:
- Understand and navigate codebases
- Read and edit files
- Run commands and scripts
- Execute complex workflows
- Make decisions based on context
- Use tools and integrations

## Installation

The SDK is available as an npm package:

```bash
npm install @anthropic-ai/claude-agent-sdk
```

## Core Concepts

### The `query()` Function

The primary function for creating agents is `query()`, which:
- Takes a prompt and optional configuration
- Returns an AsyncIterator that streams agent responses
- Supports custom system prompts, tool permissions, and more

### Basic Usage Pattern

```typescript
import { query } from "@anthropic-ai/claude-agent-sdk";

async function main() {
  const result = query({
    prompt: "Your task description here",
    options: {
      systemPrompt: "You are a specialized agent for...",
      allowedTools: ["Read", "Write", "Bash"],
      permissionMode: "acceptEdits"
    }
  });

  for await (const message of result) {
    console.log(message);
  }
}

main();
```

## Configuration Options

### System Prompt
Defines the agent's role, behavior, and expertise:
```typescript
systemPrompt: "You are a data analysis agent that specializes in..."
```

### Allowed Tools
Restrict which tools the agent can use:
```typescript
allowedTools: ["Read", "Grep", "Glob", "Bash"]
```

Common tool combinations:
- **Read-only agent**: `["Read", "Grep", "Glob"]`
- **Analysis agent**: `["Read", "Grep", "Glob", "Bash"]`
- **Development agent**: `["Read", "Write", "Edit", "Bash", "Grep", "Glob"]`

### Permission Mode
Controls how the agent handles operations:
- `"ask"`: Ask before each operation (default)
- `"acceptEdits"`: Auto-approve file edits, ask for commands
- `"acceptAll"`: Auto-approve all operations (use carefully!)

### Setting Sources
Control which settings to load:
```typescript
settingSources: ['project']  // Load project-specific settings
```

## Common Agent Patterns

### Data Analysis Agent

```typescript
const result = query({
  prompt: "Analyze the sales data in data/sales.csv and generate insights",
  options: {
    systemPrompt: `You are a data analysis expert. Analyze data files and:
    - Calculate key statistics
    - Identify trends and patterns
    - Generate visualizations when helpful
    - Provide actionable insights`,
    allowedTools: ["Read", "Bash", "Write"],
    permissionMode: "acceptEdits"
  }
});
```

### Code Review Agent

```typescript
const result = query({
  prompt: "Review the changes in src/components for best practices",
  options: {
    systemPrompt: `You are a code review expert. Review code for:
    - Security vulnerabilities
    - Performance issues
    - Code style and consistency
    - Best practices adherence`,
    allowedTools: ["Read", "Grep", "Glob"],
    permissionMode: "ask"
  }
});
```

### Research Agent

```typescript
const result = query({
  prompt: "Research how authentication is implemented in this codebase",
  options: {
    systemPrompt: `You are a codebase researcher. When researching:
    - Search systematically through relevant files
    - Document patterns and architectures
    - Create summaries of findings
    - Provide code examples`,
    allowedTools: ["Read", "Grep", "Glob"],
    permissionMode: "ask"
  }
});
```

### Automation Agent

```typescript
const result = query({
  prompt: "Set up a new React component with tests and styles",
  options: {
    systemPrompt: `You are an automation expert. When creating components:
    - Follow project conventions
    - Include comprehensive tests
    - Add proper documentation
    - Handle edge cases`,
    allowedTools: ["Read", "Write", "Edit", "Bash", "Grep", "Glob"],
    permissionMode: "acceptEdits"
  }
});
```

## Using the Skill

### Quick Agent Creation

Use the provided scaffold script to create a new agent:

```bash
./.claude/skills/agent-sdk/create-agent.sh <agent-name> <description>
```

This creates a new agent template in `agents/<agent-name>/` with:
- Main agent script
- Configuration file
- README with usage instructions

### Manual Agent Creation

1. **Create agent directory:**
```bash
mkdir -p agents/my-agent
cd agents/my-agent
npm init -y
npm install @anthropic-ai/claude-agent-sdk
```

2. **Create agent script (`agent.ts`):**
```typescript
import { query } from "@anthropic-ai/claude-agent-sdk";

async function runAgent() {
  const result = query({
    prompt: process.argv[2] || "Default task",
    options: {
      systemPrompt: "Your agent's role and instructions",
      allowedTools: ["Read", "Grep", "Glob"],
      permissionMode: "ask"
    }
  });

  for await (const message of result) {
    console.log(message);
  }
}

runAgent().catch(console.error);
```

3. **Run the agent:**
```bash
npx tsx agent.ts "Your task here"
```

## Environment Setup

### Required Environment Variables

```bash
# Required: Anthropic API key
ANTHROPIC_API_KEY=your_api_key_here

# Optional: Model selection (defaults to sonnet-4-5)
ANTHROPIC_MODEL=claude-sonnet-4-5

# Optional: Timeout settings
AGENT_TIMEOUT=300000
```

### .env File Setup

Create a `.env` file in your agent directory:
```bash
ANTHROPIC_API_KEY=sk-ant-...
ANTHROPIC_MODEL=claude-sonnet-4-5
```

## Best Practices

### Agent Design

1. **Clear Purpose**: Give each agent a specific, well-defined role
2. **Appropriate Tools**: Only grant tools the agent actually needs
3. **Safety First**: Use `"ask"` permission mode for sensitive operations
4. **Good Prompts**: Provide clear context and expected outcomes

### System Prompts

Write effective system prompts by:
- Defining the agent's role and expertise
- Listing specific capabilities and limitations
- Including quality guidelines and best practices
- Providing examples of desired behavior

Example:
```typescript
systemPrompt: `You are a security audit agent specializing in Node.js applications.

Your responsibilities:
- Identify security vulnerabilities in code
- Check for common OWASP Top 10 issues
- Verify authentication and authorization patterns
- Review dependency security

Guidelines:
- Always explain the security impact of findings
- Provide specific remediation steps
- Prioritize findings by severity
- Reference security standards when applicable`
```

### Error Handling

Always handle errors gracefully:
```typescript
async function runAgent() {
  try {
    const result = query({...});

    for await (const message of result) {
      console.log(message);
    }
  } catch (error) {
    console.error("Agent error:", error);
    process.exit(1);
  }
}
```

### Streaming Output

Process agent responses as they stream:
```typescript
for await (const message of result) {
  if (message.type === "text") {
    console.log(message.content);
  } else if (message.type === "tool_use") {
    console.log(`Using tool: ${message.tool}`);
  }
}
```

## Advanced Usage

### Custom Tool Configuration

Create agents with specific tool combinations:

```typescript
// Read-only research agent
allowedTools: ["Read", "Grep", "Glob"]

// Data processing agent
allowedTools: ["Read", "Write", "Bash"]

// Full development agent
allowedTools: ["Read", "Write", "Edit", "Bash", "Grep", "Glob", "Task"]
```

### Multi-Step Workflows

Chain multiple agent queries for complex workflows:

```typescript
async function complexWorkflow() {
  // Step 1: Research
  const research = query({
    prompt: "Research the authentication patterns in this codebase",
    options: { allowedTools: ["Read", "Grep", "Glob"] }
  });

  let findings = "";
  for await (const message of research) {
    findings += message.content;
  }

  // Step 2: Generate improvements
  const improvements = query({
    prompt: `Based on these findings:\n${findings}\n\nGenerate improved authentication code`,
    options: { allowedTools: ["Write", "Edit"] }
  });

  for await (const message of improvements) {
    console.log(message);
  }
}
```

### Agent Communication

Build agents that work together:

```typescript
// Analyzer agent finds issues
const analyzer = query({
  prompt: "Analyze code quality in src/",
  options: { systemPrompt: "You are a code quality analyzer" }
});

// Fixer agent resolves issues
const fixer = query({
  prompt: `Fix the following issues: ${issues}`,
  options: { systemPrompt: "You are a code improvement specialist" }
});
```

## Example Use Cases

### Use Case 1: Automated Testing Agent

**Goal**: Create an agent that writes tests for existing code

```typescript
const result = query({
  prompt: "Write comprehensive tests for the UserService class",
  options: {
    systemPrompt: `You are a testing expert. When writing tests:
    - Cover all public methods
    - Test edge cases and error conditions
    - Use appropriate assertions
    - Follow testing best practices
    - Include setup and teardown`,
    allowedTools: ["Read", "Write", "Grep"],
    permissionMode: "acceptEdits"
  }
});
```

### Use Case 2: Documentation Generator

**Goal**: Agent that generates documentation from code

```typescript
const result = query({
  prompt: "Generate API documentation for all endpoints in src/api/",
  options: {
    systemPrompt: `You are a technical writer. Generate documentation that:
    - Describes each endpoint's purpose
    - Lists all parameters and types
    - Shows example requests and responses
    - Documents error cases
    - Includes authentication requirements`,
    allowedTools: ["Read", "Write", "Grep", "Glob"],
    permissionMode: "acceptEdits"
  }
});
```

### Use Case 3: Refactoring Agent

**Goal**: Agent that refactors code for better patterns

```typescript
const result = query({
  prompt: "Refactor the legacy code in src/legacy/ to use modern patterns",
  options: {
    systemPrompt: `You are a refactoring expert. When refactoring:
    - Preserve existing functionality
    - Improve code organization
    - Apply SOLID principles
    - Add type safety
    - Update tests accordingly`,
    allowedTools: ["Read", "Edit", "Bash", "Grep"],
    permissionMode: "acceptEdits"
  }
});
```

## Troubleshooting

### "ANTHROPIC_API_KEY not found"
- Ensure your `.env` file contains `ANTHROPIC_API_KEY=your_key`
- Load environment variables: `source .env` or use `dotenv`

### "Module not found: @anthropic-ai/claude-agent-sdk"
- Install the SDK: `npm install @anthropic-ai/claude-agent-sdk`
- Check your `package.json` includes the dependency

### Agent not responding
- Check your API key is valid
- Verify you have API credits available
- Ensure your network connection is stable

### Permission denied errors
- Adjust `permissionMode` to grant necessary permissions
- Review `allowedTools` to include required tools
- Consider security implications before changing modes

### Unexpected agent behavior
- Review and refine your system prompt
- Add more specific instructions and constraints
- Test with simpler tasks first
- Check that allowed tools match the task requirements

## Security Considerations

### API Key Safety
- Never commit API keys to version control
- Use environment variables or secret management
- Rotate keys regularly
- Restrict key permissions to minimum needed

### Permission Modes
- Use `"ask"` mode for sensitive operations
- Review all operations before auto-approval
- Audit agent actions regularly
- Consider workspace isolation for risky operations

### Tool Restrictions
- Only grant necessary tools for the task
- Be cautious with `Write`, `Edit`, and `Bash` tools
- Consider read-only agents for analysis tasks
- Review generated code before execution

## Integration Tips

### CI/CD Integration
Run agents as part of your pipeline:
```bash
npx tsx agents/code-review/agent.ts "Review PR changes"
```

### Git Hooks
Use agents in pre-commit or pre-push hooks:
```bash
#!/bin/bash
npx tsx agents/linter/agent.ts "Check code quality"
```

### Scheduled Tasks
Run agents on a schedule with cron:
```bash
0 9 * * * cd /path/to/project && npx tsx agents/daily-report/agent.ts
```

### IDE Integration
Create IDE tasks that invoke agents:
```json
{
  "label": "Run Code Review Agent",
  "type": "shell",
  "command": "npx tsx agents/review/agent.ts '${input:reviewPrompt}'"
}
```

## Resources

### Official Documentation
- [Agent SDK Overview](https://docs.claude.com/en/docs/agent-sdk/overview)
- [TypeScript SDK Reference](https://docs.claude.com/en/api/agent-sdk/typescript)
- [Migration Guide](https://docs.claude.com/en/docs/claude-code/sdk/migration-guide)

### Community Resources
- [Demo Repository](https://github.com/anthropics/claude-agent-sdk-demos)
- [Python SDK](https://github.com/anthropics/claude-agent-sdk-python)
- [TypeScript SDK](https://github.com/anthropics/claude-agent-sdk-typescript)

### Blog Posts
- [Building Agents with Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)
- [Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) ⭐ **New pattern for 95%+ token savings**

## Code Execution with MCP (Advanced Pattern)

### Overview

Instead of preloading all MCP tool definitions into an agent's system prompt (which wastes context), agents can **write Python code** that calls MCP tools programmatically. This achieves:
- **95-98% reduction in token usage**
- **Progressive disclosure** - load only tools needed
- **Better data processing** - filter/aggregate in code, not in context
- **State persistence** - build up results across operations

### The Problem with Direct MCP Tool Calls

Traditional approach (wasteful):
```typescript
// System prompt lists ALL tools (3,000+ tokens)
systemPrompt: `
Available tools:
- mcp__things__get-today: Get today's tasks
- mcp__things__create-todo: Create new task
- mcp__google_calendar__list_events: List calendar events
- mcp__gmail__list_messages: List emails
[... 50+ more tool definitions ...]
`

// Every data fetch passes through context
const tasks = call_tool('mcp__things__get-today')  // 2,000 tokens for 20 tasks
const events = call_tool('mcp__google_calendar__list_events')  // 1,000 tokens for 5 events
const emails = call_tool('mcp__gmail__list_messages')  // 3,500 tokens for 30 emails
// Total: ~10,800 tokens just for data!
```

### Code Execution Approach (Efficient)

New approach with 95% savings:
```python
#!/usr/bin/env python3
import sys
sys.path.append('/home/user/llm-context-personal/scripts')

from mcp_tools import things, calendar, gmail

# Fetch data via MCP
tasks = things.get_today()
events = calendar.list_events_today()
emails = gmail.get_unread(limit=50)

# Process locally (NOT in Claude's context!)
p1_tasks = [t for t in tasks if t.get('priority') == 'P1']
urgent_emails = [e for e in emails if 'urgent' in e['subject'].lower()]
conflicts = detect_conflicts(tasks, events)

# Return only summary (~300 tokens vs 10,800 tokens)
print(f"""
Daily Summary:
- {len(p1_tasks)} P1 tasks requiring attention
- {len(urgent_emails)} urgent emails
- {len(conflicts)} calendar conflicts
""")
```

### Python MCP Tools Package

Located at `scripts/mcp_tools/`, provides wrappers for:

**Things 3 (`things`)**:
- `things.get_today()` - Today's tasks
- `things.create_todo(title, notes, tags, deadline)` - Create task
- `things.update_todo(id, completed=True)` - Update task

**Google Calendar (`calendar`)**:
- `calendar.list_events_today()` - Today's events
- `calendar.create_event(title, start, end)` - Create event
- `calendar.get_free_busy(start, end)` - Check availability

**Gmail (`gmail`)**:
- `gmail.get_unread(limit=50)` - Unread messages
- `gmail.send_message(to, subject, body)` - Send email
- `gmail.search_messages(query)` - Search emails

**Full documentation**: See `scripts/mcp_tools/README.md`

### Example: Daily Planning Agent

**Old approach** (10,800 tokens):
```typescript
const result = query({
  prompt: "Generate my daily plan",
  options: {
    systemPrompt: `
    # You have access to:
    - Things 3 MCP tools: get-today, create-todo, update-todo, ...
    - Calendar MCP tools: list_events, create_event, ...
    - Gmail MCP tools: list_messages, send_message, ...
    [Detailed tool descriptions... 3,000+ tokens]
    `,
    allowedTools: ["mcp__things__get-today", "mcp__google_calendar__list_events", ...]
  }
});
// Agent calls each tool directly, all data passes through context
```

**New approach** (500 tokens):
```typescript
const result = query({
  prompt: "Generate my daily plan",
  options: {
    systemPrompt: `
    Write Python code using mcp_tools package to:
    1. Fetch data from Things, Calendar, Gmail
    2. Process locally (filter P1 tasks, detect conflicts, categorize emails)
    3. Return concise summary only

    Template:
    from mcp_tools import things, calendar, gmail
    # ... fetch and process ...
    print(f"Summary: {p1_count} P1 tasks, {urgent_count} urgent emails")

    Example: scripts/mcp_tools/examples/daily_plan.py
    `,
    allowedTools: ["Bash", "Read", "Write"]
  }
});
// Agent writes code, executes locally, returns only summary
```

### When to Use Code Execution

✅ **Use code execution when**:
- Fetching large datasets from MCP tools
- Need to filter/aggregate/process data
- Performing repeated operations (loops)
- Building up state across multiple calls
- Want to minimize context usage

❌ **Use direct tool calls when**:
- Single, simple tool invocation
- Result is small and needs to stay in context
- No processing needed (just fetch and display)

### Setting Up Code Execution Agents

1. **Configure MCP servers** in `.mcp.json`:
```json
{
  "mcpServers": {
    "things": {"command": "node", "args": ["/path/to/things-mcp/index.js"]},
    "google-calendar": {"command": "node", "args": ["/path/to/calendar-mcp/index.js"]},
    "gmail": {"command": "node", "args": ["/path/to/gmail-mcp/index.js"]}
  }
}
```

2. **Write agent with code execution instructions**:
```typescript
const result = query({
  prompt: userPrompt,
  options: {
    systemPrompt: `
    You have access to MCP tools via Python code execution.

    Import from mcp_tools package:
    - things: Things 3 task management
    - calendar: Google Calendar
    - gmail: Gmail email management

    Always:
    1. Fetch data first
    2. Process/filter in Python
    3. Return only concise summary

    See: scripts/mcp_tools/README.md and examples/
    `,
    allowedTools: ["Bash", "Read", "Write", "Grep", "Glob"]
  }
});
```

3. **Example complete agent**:
See `agents/executive-assistant/` or `.claude/skills/executive-assistant/SKILL.md` for production implementation.

### Benefits Summary

| Aspect | Direct Tool Calls | Code Execution | Savings |
|--------|------------------|----------------|---------|
| Token usage | ~10,800 tokens | ~500 tokens | 95% |
| Context efficiency | Low (all data in context) | High (only summaries) | Massive |
| Data processing | Limited (in Claude) | Full Python capabilities | Much better |
| State persistence | None | Full Python state | Significant |
| Tool discovery | Preload all | Progressive disclosure | Efficient |

### See Also

- **Full documentation**: `docs/CODE_EXECUTION_WITH_MCP.md`
- **Python package**: `scripts/mcp_tools/README.md`
- **Examples**: `scripts/mcp_tools/examples/daily_plan.py`
- **Live implementation**: `.claude/skills/executive-assistant/SKILL.md`

## Extending This Skill

### Adding New Agent Templates

1. Create new template in `templates/`
2. Add template variables for customization
3. Update scaffold script to support new template
4. Document the new template in examples

### Creating Agent Libraries

Build reusable agent functions:
```typescript
// lib/agents/code-review.ts
export function createCodeReviewAgent(options) {
  return query({
    prompt: options.prompt,
    options: {
      systemPrompt: "You are a code review expert...",
      ...options
    }
  });
}
```

### Agent Composition

Combine multiple agents for complex workflows:
```typescript
import { analyzerAgent } from "./lib/agents/analyzer";
import { reporterAgent } from "./lib/agents/reporter";

async function fullAudit() {
  const analysis = await analyzerAgent("Audit codebase");
  const report = await reporterAgent(analysis);
  return report;
}
```

## Skill Files

- `SKILL.md` - This comprehensive guide
- `README.md` - Quick reference and setup
- `create-agent.sh` - Scaffold script for new agents
- `templates/` - Agent templates for common use cases
- `examples.md` - Detailed usage examples and patterns
