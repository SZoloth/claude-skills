#!/bin/bash

# Create Agent Script
# Creates a new agent using the Anthropic Agent SDK with a pre-configured template

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if agent name is provided
if [ -z "$1" ]; then
    echo -e "${RED}Error: Agent name is required${NC}"
    echo "Usage: $0 <agent-name> [description]"
    echo ""
    echo "Example:"
    echo "  $0 code-reviewer 'An agent that reviews code for best practices'"
    exit 1
fi

AGENT_NAME="$1"
DESCRIPTION="${2:-An agent created with the Anthropic Agent SDK}"
AGENT_DIR="agents/${AGENT_NAME}"

# Check if agent already exists
if [ -d "$AGENT_DIR" ]; then
    echo -e "${RED}Error: Agent '${AGENT_NAME}' already exists at ${AGENT_DIR}${NC}"
    exit 1
fi

echo -e "${GREEN}Creating agent: ${AGENT_NAME}${NC}"
echo -e "Description: ${DESCRIPTION}"
echo ""

# Create directory structure
echo "Creating directory structure..."
mkdir -p "$AGENT_DIR"

# Create package.json
echo "Creating package.json..."
cat > "$AGENT_DIR/package.json" << EOF
{
  "name": "${AGENT_NAME}",
  "version": "1.0.0",
  "description": "${DESCRIPTION}",
  "type": "module",
  "main": "agent.ts",
  "scripts": {
    "start": "tsx agent.ts",
    "dev": "tsx watch agent.ts"
  },
  "dependencies": {
    "@anthropic-ai/claude-agent-sdk": "^1.0.0"
  },
  "devDependencies": {
    "tsx": "^4.0.0",
    "typescript": "^5.0.0",
    "@types/node": "^20.0.0"
  }
}
EOF

# Create tsconfig.json
echo "Creating tsconfig.json..."
cat > "$AGENT_DIR/tsconfig.json" << EOF
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ES2022",
    "moduleResolution": "node",
    "esModuleInterop": true,
    "strict": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "outDir": "dist"
  },
  "include": ["*.ts"],
  "exclude": ["node_modules", "dist"]
}
EOF

# Create main agent file
echo "Creating agent.ts..."
cat > "$AGENT_DIR/agent.ts" << 'EOF'
import { query } from "@anthropic-ai/claude-agent-sdk";

/**
 * Configuration for the agent
 */
const AGENT_CONFIG = {
  systemPrompt: `You are a helpful AI agent.

Your responsibilities:
- Follow user instructions carefully
- Provide clear and accurate responses
- Ask for clarification when needed

Guidelines:
- Be concise but thorough
- Explain your reasoning
- Handle errors gracefully`,

  allowedTools: [
    "Read",
    "Grep",
    "Glob",
    // Uncomment additional tools as needed:
    // "Write",
    // "Edit",
    // "Bash",
  ],

  permissionMode: "ask" as const, // Options: "ask", "acceptEdits", "acceptAll"

  settingSources: ["project"],
};

/**
 * Main agent function
 */
async function runAgent() {
  // Get task from command line or use default
  const task = process.argv.slice(2).join(" ") || "Hello! What can I help you with?";

  console.log("Starting agent...");
  console.log(`Task: ${task}\n`);

  try {
    const result = query({
      prompt: task,
      options: {
        systemPrompt: AGENT_CONFIG.systemPrompt,
        allowedTools: AGENT_CONFIG.allowedTools,
        permissionMode: AGENT_CONFIG.permissionMode,
        settingSources: AGENT_CONFIG.settingSources,
      },
    });

    // Stream and display agent responses
    for await (const message of result) {
      console.log(message);
    }

    console.log("\nAgent completed successfully!");
  } catch (error) {
    console.error("Agent error:", error);
    process.exit(1);
  }
}

// Run the agent
runAgent().catch((error) => {
  console.error("Fatal error:", error);
  process.exit(1);
});
EOF

# Create .env.example
echo "Creating .env.example..."
cat > "$AGENT_DIR/.env.example" << EOF
# Anthropic API Key (required)
ANTHROPIC_API_KEY=your_api_key_here

# Optional: Model selection (defaults to claude-sonnet-4-5)
ANTHROPIC_MODEL=claude-sonnet-4-5

# Optional: Timeout in milliseconds
AGENT_TIMEOUT=300000
EOF

# Create .env if it doesn't exist
if [ ! -f "$AGENT_DIR/.env" ]; then
    cp "$AGENT_DIR/.env.example" "$AGENT_DIR/.env"
    echo -e "${YELLOW}Created .env file - remember to add your ANTHROPIC_API_KEY${NC}"
fi

# Create .gitignore
echo "Creating .gitignore..."
cat > "$AGENT_DIR/.gitignore" << EOF
# Dependencies
node_modules/
package-lock.json
yarn.lock

# Environment variables
.env
.env.local

# Build output
dist/
*.js
*.js.map

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
EOF

# Create README.md
echo "Creating README.md..."
cat > "$AGENT_DIR/README.md" << EOF
# ${AGENT_NAME}

${DESCRIPTION}

## Setup

1. Install dependencies:
\`\`\`bash
npm install
\`\`\`

2. Configure environment variables:
\`\`\`bash
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
\`\`\`

## Usage

Run the agent with a task:

\`\`\`bash
npm start "Your task description here"
\`\`\`

Or run directly with tsx:

\`\`\`bash
npx tsx agent.ts "Your task description here"
\`\`\`

## Configuration

Edit \`agent.ts\` to customize:

- **System Prompt**: Define the agent's role and behavior
- **Allowed Tools**: Specify which tools the agent can use
- **Permission Mode**: Control auto-approval settings

### System Prompt

The system prompt defines the agent's personality and capabilities. Edit the \`systemPrompt\` in \`AGENT_CONFIG\`.

### Allowed Tools

Available tools:
- \`Read\`: Read files
- \`Write\`: Create new files
- \`Edit\`: Modify existing files
- \`Grep\`: Search file contents
- \`Glob\`: Find files by pattern
- \`Bash\`: Execute shell commands
- \`Task\`: Launch sub-agents

### Permission Modes

- \`ask\`: Ask before each operation (safest)
- \`acceptEdits\`: Auto-approve file edits, ask for commands
- \`acceptAll\`: Auto-approve all operations (use carefully!)

## Examples

### Example 1: Research Task

\`\`\`bash
npm start "Research how authentication is implemented in this codebase"
\`\`\`

### Example 2: Code Analysis

\`\`\`bash
npm start "Analyze the performance of our database queries"
\`\`\`

### Example 3: Documentation

\`\`\`bash
npm start "Generate documentation for the API endpoints"
\`\`\`

## Development

Run in watch mode for development:

\`\`\`bash
npm run dev
\`\`\`

## Troubleshooting

### API Key Error

If you see "ANTHROPIC_API_KEY not found":
1. Check that \`.env\` file exists
2. Verify the API key is set correctly
3. Restart the agent after updating \`.env\`

### Module Not Found

If you see module errors:
\`\`\`bash
npm install
\`\`\`

### Permission Denied

If operations are blocked:
1. Check \`permissionMode\` setting
2. Verify \`allowedTools\` includes necessary tools
3. Review security implications before changing

## Next Steps

1. Customize the system prompt for your specific use case
2. Adjust allowed tools based on required capabilities
3. Set appropriate permission mode for your security needs
4. Test with simple tasks before complex operations

## Resources

- [Agent SDK Documentation](https://docs.claude.com/en/docs/agent-sdk/overview)
- [TypeScript SDK Reference](https://docs.claude.com/en/api/agent-sdk/typescript)
- [Example Agents](https://github.com/anthropics/claude-agent-sdk-demos)
EOF

echo ""
echo -e "${GREEN}Agent created successfully!${NC}"
echo ""
echo "Next steps:"
echo "  1. cd $AGENT_DIR"
echo "  2. npm install"
echo "  3. Edit .env and add your ANTHROPIC_API_KEY"
echo "  4. Customize agent.ts for your use case"
echo "  5. Run: npm start \"Your task here\""
echo ""
echo -e "${YELLOW}Don't forget to add your ANTHROPIC_API_KEY to ${AGENT_DIR}/.env${NC}"
