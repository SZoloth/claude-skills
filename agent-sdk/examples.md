# Agent SDK Examples

Detailed examples and conversation patterns for using the Anthropic Agent SDK skill.

## Example 1: Creating a Code Review Agent

### User Request
"I want to create an agent that reviews pull requests for security issues and code quality."

### Claude's Response

I'll help you create a code review agent using the Anthropic Agent SDK.

**Step 1: Create the agent**
```bash
./.claude/skills/agent-sdk/create-agent.sh code-reviewer "Reviews code for security and quality"
```

**Step 2: Install dependencies**
```bash
cd agents/code-reviewer
npm install
```

**Step 3: Configure the agent**

I'll customize the `agent.ts` file with a specialized system prompt:

```typescript
const AGENT_CONFIG = {
  systemPrompt: `You are a security-focused code review expert.

Your responsibilities:
- Identify security vulnerabilities (SQL injection, XSS, CSRF, etc.)
- Check for code quality issues
- Verify error handling and edge cases
- Review for performance concerns
- Ensure best practices are followed

Guidelines:
- Prioritize security issues by severity (Critical, High, Medium, Low)
- Provide specific code suggestions for fixes
- Reference security standards (OWASP, CWE)
- Be constructive and educational in feedback
- Include code examples in recommendations`,

  allowedTools: [
    "Read",
    "Grep",
    "Glob"
  ],

  permissionMode: "ask" as const
};
```

**Step 4: Run the agent**
```bash
npm start "Review the authentication code in src/auth/ for security issues"
```

### Expected Behavior
The agent will:
1. Search for authentication-related files
2. Analyze code for common vulnerabilities
3. Provide detailed security recommendations
4. Suggest specific improvements with code examples

---

## Example 2: Data Analysis Agent

### User Request
"Create an agent that can analyze CSV files and generate insights."

### Claude's Response

I'll create a data analysis agent for you.

**Step 1: Create the agent**
```bash
./.claude/skills/agent-sdk/create-agent.sh data-analyzer "Analyzes data files and generates insights"
```

**Step 2: Configure for data analysis**

Edit `agent.ts` with this configuration:

```typescript
const AGENT_CONFIG = {
  systemPrompt: `You are a data analysis expert specializing in CSV data.

Your capabilities:
- Load and parse CSV files
- Calculate statistics (mean, median, mode, std dev)
- Identify trends and patterns
- Generate visualizations when helpful
- Detect outliers and anomalies
- Provide actionable insights

Analysis approach:
1. Load and validate the data
2. Provide summary statistics
3. Identify key trends
4. Highlight notable patterns or concerns
5. Suggest next steps or deeper analysis`,

  allowedTools: [
    "Read",
    "Bash",  // For running data processing scripts
    "Write"  // For generating reports
  ],

  permissionMode: "acceptEdits" as const
};
```

**Step 3: Usage example**
```bash
npm start "Analyze data/sales.csv and identify trends in Q4 sales"
```

### Sample Output
```
Loading data/sales.csv...

Summary Statistics:
- Total records: 1,247
- Date range: 2024-10-01 to 2024-12-31
- Total revenue: $2,456,789
- Average transaction: $1,968

Key Findings:
1. Sales increased 23% in December vs October
2. Weekend sales 35% higher than weekdays
3. Product category "Electronics" shows strongest growth
4. Peak sales time: 2-4 PM EST

Recommendations:
- Increase weekend inventory
- Focus marketing on electronics
- Consider afternoon promotions
```

---

## Example 3: Documentation Generator

### User Request
"I need an agent to document my REST API endpoints."

### Claude's Response

I'll create a documentation generator agent.

**Setup**
```bash
./.claude/skills/agent-sdk/create-agent.sh api-documenter "Generates API documentation"
cd agents/api-documenter
npm install
```

**Configuration**
```typescript
const AGENT_CONFIG = {
  systemPrompt: `You are a technical documentation expert for REST APIs.

Documentation requirements:
- Endpoint URL and HTTP method
- Request parameters (query, path, body)
- Request/response examples with real data
- Authentication requirements
- Error responses and status codes
- Rate limiting information

Format:
Use clear markdown with:
- Table of contents
- Organized by resource
- Code examples in multiple languages
- Common use cases
- Troubleshooting tips`,

  allowedTools: [
    "Read",
    "Grep",
    "Glob",
    "Write"
  ],

  permissionMode: "acceptEdits" as const
};
```

**Run the agent**
```bash
npm start "Document all API endpoints in src/api/routes/"
```

---

## Example 4: Test Generation Agent

### User Request
"Create an agent that writes unit tests for my TypeScript code."

### Claude's Response

**Create the agent**
```bash
./.claude/skills/agent-sdk/create-agent.sh test-writer "Writes comprehensive unit tests"
```

**Configuration**
```typescript
const AGENT_CONFIG = {
  systemPrompt: `You are a testing expert specializing in TypeScript/Jest.

Test requirements:
- Cover all public methods and functions
- Test happy paths and edge cases
- Include error handling tests
- Mock external dependencies
- Use descriptive test names
- Follow AAA pattern (Arrange, Act, Assert)

Coverage goals:
- Aim for 90%+ code coverage
- Test all branches and conditions
- Include integration tests where appropriate
- Add performance tests for critical paths

Best practices:
- Tests should be independent and isolated
- Use factories or fixtures for test data
- Keep tests focused and single-purpose
- Include setup and teardown as needed`,

  allowedTools: [
    "Read",
    "Write",
    "Grep",
    "Glob"
  ],

  permissionMode: "acceptEdits" as const
};
```

**Usage**
```bash
npm start "Write comprehensive tests for src/services/UserService.ts"
```

---

## Example 5: Refactoring Agent

### User Request
"I want an agent to refactor my legacy code to use modern patterns."

### Claude's Response

**Setup**
```bash
./.claude/skills/agent-sdk/create-agent.sh refactoring-expert "Modernizes and refactors code"
cd agents/refactoring-expert
npm install
```

**Configuration**
```typescript
const AGENT_CONFIG = {
  systemPrompt: `You are a refactoring expert specializing in code modernization.

Refactoring priorities:
1. Preserve existing functionality (add tests first if needed)
2. Improve code organization and structure
3. Apply SOLID principles
4. Add type safety (TypeScript)
5. Remove code smells
6. Modernize syntax and patterns

Approach:
- Make small, incremental changes
- Test after each refactoring
- Document breaking changes
- Explain the reasoning behind each change
- Suggest further improvements

Patterns to apply:
- Dependency injection
- Factory patterns
- Strategy pattern
- Promise-based async/await
- Modern ES6+ syntax`,

  allowedTools: [
    "Read",
    "Edit",
    "Bash",  // For running tests
    "Grep",
    "Glob"
  ],

  permissionMode: "ask" as const  // Ask permission for each change
};
```

---

## Example 6: Multi-Agent Workflow

### User Request
"Can I chain multiple agents together for a complex workflow?"

### Claude's Response

Yes! Here's an example of chaining agents for a complete code review and improvement workflow:

**Create the agents**
```bash
# Agent 1: Analyzer
./.claude/skills/agent-sdk/create-agent.sh code-analyzer "Analyzes code for issues"

# Agent 2: Test Generator
./.claude/skills/agent-sdk/create-agent.sh test-generator "Generates tests"

# Agent 3: Documenter
./.claude/skills/agent-sdk/create-agent.sh documenter "Creates documentation"
```

**Create workflow script**

Create `agents/workflow.ts`:
```typescript
import { query } from "@anthropic-ai/claude-agent-sdk";

async function complexWorkflow(targetFile: string) {
  console.log("=== Step 1: Analyze Code ===\n");

  // Agent 1: Analyze the code
  const analyzeResult = query({
    prompt: `Analyze ${targetFile} for code quality, security, and potential improvements`,
    options: {
      systemPrompt: "You are a code analysis expert.",
      allowedTools: ["Read", "Grep"],
      permissionMode: "ask"
    }
  });

  let analysisReport = "";
  for await (const message of analyzeResult) {
    console.log(message);
    analysisReport += message.content || "";
  }

  console.log("\n=== Step 2: Generate Tests ===\n");

  // Agent 2: Generate tests based on analysis
  const testResult = query({
    prompt: `Based on this analysis:\n${analysisReport}\n\nGenerate comprehensive tests for ${targetFile}`,
    options: {
      systemPrompt: "You are a testing expert.",
      allowedTools: ["Read", "Write"],
      permissionMode: "acceptEdits"
    }
  });

  for await (const message of testResult) {
    console.log(message);
  }

  console.log("\n=== Step 3: Generate Documentation ===\n");

  // Agent 3: Create documentation
  const docResult = query({
    prompt: `Document ${targetFile} with API reference and usage examples`,
    options: {
      systemPrompt: "You are a technical writer.",
      allowedTools: ["Read", "Write"],
      permissionMode: "acceptEdits"
    }
  });

  for await (const message of docResult) {
    console.log(message);
  }

  console.log("\n=== Workflow Complete! ===");
}

// Run workflow
const targetFile = process.argv[2] || "src/main.ts";
complexWorkflow(targetFile);
```

**Run the workflow**
```bash
npx tsx agents/workflow.ts src/services/PaymentService.ts
```

---

## Example 7: Research Agent

### User Request
"Create an agent that researches and documents architectural patterns in my codebase."

### Configuration
```typescript
const AGENT_CONFIG = {
  systemPrompt: `You are a software architecture researcher.

Research methodology:
1. Identify architectural patterns in use
2. Document design decisions and rationale
3. Map component relationships
4. Identify consistency and inconsistencies
5. Suggest architectural improvements

Analysis areas:
- File and folder structure
- Module boundaries
- Data flow patterns
- State management approach
- API design patterns
- Error handling strategies

Deliverables:
- Architecture diagram (mermaid format)
- Pattern inventory
- Consistency report
- Improvement recommendations`,

  allowedTools: [
    "Read",
    "Grep",
    "Glob",
    "Write"
  ],

  permissionMode: "acceptEdits" as const
};
```

**Usage**
```bash
npm start "Research and document the architecture of our frontend application in src/"
```

---

## Example 8: CI/CD Integration

### User Request
"How can I use agents in my CI/CD pipeline?"

### Claude's Response

You can integrate agents into your CI/CD pipeline for automated checks:

**GitHub Actions Example**
```yaml
name: Agent Code Review

on:
  pull_request:
    branches: [main]

jobs:
  agent-review:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Setup Node
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Install Agent
        run: |
          cd agents/code-reviewer
          npm install

      - name: Run Code Review Agent
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          cd agents/code-reviewer
          npm start "Review all changes in this PR for security and quality" > review.txt

      - name: Post Review Comment
        uses: actions/github-script@v6
        with:
          script: |
            const fs = require('fs');
            const review = fs.readFileSync('agents/code-reviewer/review.txt', 'utf8');
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: `## 🤖 Agent Code Review\n\n${review}`
            });
```

**Pre-commit Hook Example**
```bash
#!/bin/bash
# .git/hooks/pre-commit

echo "Running agent code quality check..."

cd agents/quality-checker
npm start "Check staged files for quality issues" --read-only

if [ $? -ne 0 ]; then
    echo "❌ Quality check failed. Fix issues before committing."
    exit 1
fi

echo "✅ Quality check passed!"
```

---

## Example 9: Scheduled Agent Tasks

### User Request
"Can I run agents on a schedule?"

### Claude's Response

Yes! Here's how to set up scheduled agent tasks:

**Cron Job Example**
```bash
# Edit crontab
crontab -e

# Run daily report agent at 9 AM
0 9 * * * cd /path/to/project/agents/daily-reporter && npm start "Generate daily summary"

# Run weekly cleanup agent on Sundays at 2 AM
0 2 * * 0 cd /path/to/project/agents/cleanup && npm start "Identify and report unused code"
```

**Node.js Scheduler**
```typescript
import { query } from "@anthropic-ai/claude-agent-sdk";
import cron from "node-cron";

// Run every day at 9 AM
cron.schedule('0 9 * * *', async () => {
  console.log('Running daily report agent...');

  const result = query({
    prompt: "Generate daily project status report",
    options: {
      systemPrompt: "You are a project reporting agent.",
      allowedTools: ["Read", "Grep", "Bash", "Write"],
      permissionMode: "acceptAll"
    }
  });

  for await (const message of result) {
    console.log(message);
  }
});
```

---

## Example 10: Debugging Assistant Agent

### Configuration
```typescript
const AGENT_CONFIG = {
  systemPrompt: `You are a debugging assistant.

Debugging approach:
1. Reproduce the issue from description
2. Analyze error messages and stack traces
3. Review relevant code sections
4. Identify root cause
5. Suggest fixes with explanations
6. Provide prevention strategies

Investigation steps:
- Check logs and error output
- Review recent code changes
- Verify configuration
- Test edge cases
- Validate assumptions

Output format:
- Root cause analysis
- Step-by-step fix instructions
- Code examples
- Prevention tips`,

  allowedTools: [
    "Read",
    "Grep",
    "Glob",
    "Bash"  // For running diagnostic commands
  ],

  permissionMode: "ask" as const
};
```

**Usage**
```bash
npm start "Debug why user authentication is failing intermittently"
```

---

## Tips for Effective Agent Usage

### 1. Start Simple
Begin with basic tasks and gradually increase complexity:
```bash
# Start: Simple read task
npm start "Read and summarize src/config.ts"

# Progress: Analysis task
npm start "Analyze authentication flow"

# Advanced: Complex workflow
npm start "Refactor authentication with proper error handling"
```

### 2. Iterate on System Prompts
Refine prompts based on agent behavior:
```typescript
// Initial (too vague)
systemPrompt: "You are a helpful coding assistant."

// Better (specific role)
systemPrompt: "You are a React expert focusing on hooks and performance."

// Best (detailed instructions)
systemPrompt: `You are a React expert specializing in:
- Hooks best practices
- Performance optimization
- Component composition
- State management patterns

Always:
- Explain your reasoning
- Provide code examples
- Reference React documentation
- Consider edge cases`
```

### 3. Use Appropriate Permission Modes
Match permission mode to task risk level:
```typescript
// High risk: Ask permission
permissionMode: "ask"  // Deleting files, running commands

// Medium risk: Accept edits
permissionMode: "acceptEdits"  // Writing tests, documentation

// Low risk: Accept all
permissionMode: "acceptAll"  // Read-only analysis, research
```

### 4. Monitor and Log
Track agent behavior for improvement:
```typescript
let operationCount = 0;

for await (const message of result) {
  operationCount++;
  console.log(`[${operationCount}]`, message);

  if (message.type === "tool_use") {
    console.log(`Tool used: ${message.tool}`);
  }
}

console.log(`Total operations: ${operationCount}`);
```

---

## Common Patterns Summary

| Pattern | Use Case | Tools | Permission |
|---------|----------|-------|------------|
| Read-Only | Research, Analysis | Read, Grep, Glob | ask |
| Data Processing | Analysis, Reports | Read, Bash, Write | acceptEdits |
| Code Generation | New features | All tools | acceptEdits |
| Code Review | Security, Quality | Read, Grep, Glob | ask |
| Refactoring | Modernization | Read, Edit, Bash | ask |
| Testing | Test generation | Read, Write, Grep | acceptEdits |
| Documentation | API docs | Read, Grep, Write | acceptEdits |
| Debugging | Issue resolution | Read, Grep, Bash | ask |

---

## Next Steps

1. Start with the examples that match your use case
2. Customize system prompts for your specific needs
3. Test with simple tasks before complex workflows
4. Iterate based on agent performance
5. Build libraries of reusable agents

For more details, see:
- `SKILL.md` - Comprehensive documentation
- `README.md` - Quick reference guide
