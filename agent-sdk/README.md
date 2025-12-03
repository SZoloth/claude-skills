# Anthropic Agent SDK Skill

Quick reference for creating and running autonomous agents using the Anthropic Agent SDK.

## Quick Start

### Create a New Agent

```bash
./.claude/skills/agent-sdk/create-agent.sh my-agent "Description of my agent"
```

This creates a new agent in `agents/my-agent/` with:
- TypeScript agent template
- Configuration files
- README with usage instructions
- Environment setup

### Install and Configure

```bash
cd agents/my-agent
npm install
echo "ANTHROPIC_API_KEY=your_key_here" > .env
```

### Run Your Agent

```bash
npm start "Your task description here"
```

## Common Agent Types

### Read-Only Research Agent

```typescript
allowedTools: ["Read", "Grep", "Glob"]
permissionMode: "ask"
```

Use for: Code exploration, documentation research, analysis

### Data Analysis Agent

```typescript
allowedTools: ["Read", "Bash"]
permissionMode: "acceptEdits"
```

Use for: Processing data files, running scripts, generating reports

### Development Agent

```typescript
allowedTools: ["Read", "Write", "Edit", "Bash", "Grep", "Glob"]
permissionMode: "acceptEdits"
```

Use for: Code generation, refactoring, automated development

## Basic Template

```typescript
import { query } from "@anthropic-ai/claude-agent-sdk";

const result = query({
  prompt: "Your task here",
  options: {
    systemPrompt: "You are a...",
    allowedTools: ["Read", "Grep", "Glob"],
    permissionMode: "ask"
  }
});

for await (const message of result) {
  console.log(message);
}
```

## Permission Modes

| Mode | Behavior | Use When |
|------|----------|----------|
| `ask` | Ask before every operation | Testing, sensitive tasks |
| `acceptEdits` | Auto-approve file edits | Trusted workflows |
| `acceptAll` | Auto-approve everything | Fully automated tasks |

## Available Tools

| Tool | Capability | Use For |
|------|------------|---------|
| `Read` | Read files | Viewing code, data |
| `Write` | Create files | Generating new content |
| `Edit` | Modify files | Updating existing code |
| `Grep` | Search content | Finding patterns |
| `Glob` | Find files | Locating files by name |
| `Bash` | Run commands | Executing scripts |
| `Task` | Launch agents | Complex workflows |

## Configuration Tips

### Effective System Prompts

```typescript
systemPrompt: `You are a [role] agent.

Your responsibilities:
- [Primary task]
- [Secondary task]
- [Constraints]

Guidelines:
- [Quality standard]
- [Behavior expectation]
- [Output format]`
```

### Tool Selection Strategy

1. **Start minimal**: Begin with read-only tools
2. **Add as needed**: Grant additional permissions when required
3. **Security first**: Review implications before adding powerful tools

## Common Use Cases

### Code Review

```bash
./.claude/skills/agent-sdk/create-agent.sh code-reviewer "Reviews code for best practices"
# Edit agent.ts with code review system prompt
# Run: npm start "Review the changes in src/components"
```

### Documentation Generator

```bash
./.claude/skills/agent-sdk/create-agent.sh doc-generator "Generates API documentation"
# Configure with Read, Write, Grep tools
# Run: npm start "Document all API endpoints"
```

### Test Writer

```bash
./.claude/skills/agent-sdk/create-agent.sh test-writer "Writes unit tests"
# Configure with Read, Write tools
# Run: npm start "Write tests for UserService"
```

### Data Analyzer

```bash
./.claude/skills/agent-sdk/create-agent.sh data-analyzer "Analyzes data files"
# Configure with Read, Bash tools
# Run: npm start "Analyze sales trends in data/sales.csv"
```

## Environment Variables

### Required

```bash
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

### Optional

```bash
ANTHROPIC_MODEL=claude-sonnet-4-5
AGENT_TIMEOUT=300000
```

## Troubleshooting

### API Key Issues

```bash
# Check .env file exists
cat agents/my-agent/.env

# Verify key format
grep ANTHROPIC_API_KEY agents/my-agent/.env
```

### Module Not Found

```bash
# Reinstall dependencies
cd agents/my-agent
rm -rf node_modules package-lock.json
npm install
```

### Permission Errors

1. Check `allowedTools` includes necessary tools
2. Verify `permissionMode` setting
3. Review security requirements

## Advanced Patterns

### Multi-Step Workflow

```typescript
// Step 1: Research
const research = query({
  prompt: "Research authentication patterns",
  options: { allowedTools: ["Read", "Grep"] }
});

// Step 2: Generate
const generate = query({
  prompt: `Based on research, generate improved code`,
  options: { allowedTools: ["Write", "Edit"] }
});
```

### Conditional Agent

```typescript
const task = process.argv[2];
const isReadOnly = process.argv.includes("--read-only");

const result = query({
  prompt: task,
  options: {
    allowedTools: isReadOnly
      ? ["Read", "Grep", "Glob"]
      : ["Read", "Write", "Edit", "Bash"],
    permissionMode: isReadOnly ? "ask" : "acceptEdits"
  }
});
```

## Resources

- **Full Documentation**: See `SKILL.md` for comprehensive guide
- **Examples**: See `examples.md` for detailed usage patterns
- **Official Docs**: https://docs.claude.com/en/docs/agent-sdk/overview
- **Demo Repository**: https://github.com/anthropics/claude-agent-sdk-demos

## Quick Reference

```bash
# Create agent
./.claude/skills/agent-sdk/create-agent.sh <name> <description>

# Setup agent
cd agents/<name>
npm install
echo "ANTHROPIC_API_KEY=your_key" > .env

# Run agent
npm start "task description"

# Development mode (watch)
npm run dev

# Run with custom prompt
npx tsx agent.ts "custom task here"
```

## Need Help?

1. Check `SKILL.md` for detailed documentation
2. Review `examples.md` for usage patterns
3. Visit official documentation
4. Check agent README in `agents/<name>/README.md`
