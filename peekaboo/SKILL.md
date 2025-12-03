---
name: peekaboo
description: Invoke Peekaboo-powered autonomous agents for visual GUI tasks. This skill should be used when the task requires visual understanding, GUI automation, design QA comparison, UI testing, or user research recording. Triggers on requests like "compare this design to the implementation", "test this UI flow", "automate clicking through this app", or "record this user session".
---

# Peekaboo Agents

Autonomous Agent SDK applications that use Peekaboo's MCP server for visual understanding and GUI control. Located at `~/Projects/peekaboo-agents`.

## Prerequisites

Ensure Peekaboo MCP server is running before invoking any agent. If visual tools are not available, inform user to start Peekaboo.

## Available Agents

### 1. Computer Use Agent
**General-purpose GUI automation**

**When to use:**
- General GUI automation ("open Safari and go to github.com")
- Multi-step computer tasks ("create a note and fill it with meeting notes")
- Single actions ("take a screenshot", "click that button")
- Any visual task not covered by specialized agents

**Invocation:**
```bash
cd ~/Projects/peekaboo-agents/computer-use-agent && npm start -- "TASK_DESCRIPTION"
```

**Example:**
```bash
cd ~/Projects/peekaboo-agents/computer-use-agent && npm start -- "Open System Preferences and enable Dark Mode"
```

---

### 2. Design QA Validator
**Visual design comparison - mockup vs implementation**

**When to use:**
- Comparing Figma/Sketch designs to live implementations
- Checking pixel-perfect alignment, colors, typography
- Design system compliance validation
- Pre-release visual QA

**Invocation:**
```bash
cd ~/Projects/peekaboo-agents/design-qa-validator && npm start -- "DESIGN_URL" "IMPLEMENTATION_URL"
```

**Example:**
```bash
cd ~/Projects/peekaboo-agents/design-qa-validator && npm start -- "https://figma.com/file/abc123" "http://localhost:3000/dashboard"
```

**Output:** Generates detailed QA report with measurements, discrepancies, and CSS fix suggestions.

---

### 3. Smart QA Agent
**Natural language UI testing**

**When to use:**
- End-to-end testing without brittle selectors
- Exploratory testing automation
- User flow validation
- Testing described in plain English

**Invocation:**
```bash
cd ~/Projects/peekaboo-agents/smart-qa-agent && npm start -- "TEST_SCENARIO"
```

**Example:**
```bash
cd ~/Projects/peekaboo-agents/smart-qa-agent && npm start -- "Navigate to the login page, enter invalid credentials, verify error message appears"
```

**Output:** Test report with screenshot evidence at each step.

---

### 4. User Research Recorder
**Session recording with JTBD analysis**

**When to use:**
- Recording user research sessions
- Capturing user behavior with timeline documentation
- Detecting events (errors, success, confusion, discovery)
- Post-session analysis and insight extraction

**Invocation:**
```bash
cd ~/Projects/peekaboo-agents/user-research-recorder && npm start -- "SESSION_NAME" "DURATION_MINUTES"
```

**Example:**
```bash
cd ~/Projects/peekaboo-agents/user-research-recorder && npm start -- "onboarding-test-p01" "30"
```

**Output:** Session recording with timestamped screenshots and event annotations.

## Routing Logic

When user requests visual/GUI task, route to appropriate agent:

| Request Pattern | Agent |
|----------------|-------|
| "Compare design to implementation" | Design QA Validator |
| "Test this flow/feature" | Smart QA Agent |
| "Record user session" | User Research Recorder |
| General GUI automation | Computer Use Agent |

## Important Notes

1. **Run in background** - These agents can take several minutes. Consider running with `&` or in a separate terminal.
2. **Peekaboo required** - All agents depend on Peekaboo MCP server for visual understanding.
3. **Reports generated** - Each agent creates reports/screenshots in its directory under `reports/` or `sessions/`.
4. **First run** - May need `npm install` in each agent directory first.
