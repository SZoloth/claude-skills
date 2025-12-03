# Linear Manager Skill

A comprehensive Agent Skill for managing Linear issues, projects, and teams through Claude Code.

## Installation

This skill is installed in `~/.claude/skills/linear-manager/` for global access across all Claude Code projects.

## Usage

The skill is automatically triggered when you mention Linear or Linear-related tasks. Examples:

- "Show me my Linear issues"
- "Create a Linear issue for buying groceries"
- "What's on the PRVT team's plate?"
- "List all my projects in Linear"

## Files

- `SKILL.md` - Main skill instructions (loaded when triggered)
- `API-REFERENCE.md` - Detailed Linear SDK documentation (loaded as needed)
- `linear.mjs` - CLI script for Linear operations
- `README.md` - This file

## Requirements

The skill requires:
1. Node.js and npm installed
2. `@linear/sdk` package installed in your project
3. `LINEAR_API_KEY` environment variable set (via `.env` or export)

## Project setup

In any project where you want to use Linear:

1. Install the Linear SDK:
   ```bash
   npm install @linear/sdk dotenv
   ```

2. Create a `.env` file with your API key:
   ```bash
   echo "LINEAR_API_KEY=your_key_here" > .env
   ```

3. Add `.env` to `.gitignore`:
   ```bash
   echo ".env" >> .gitignore
   ```

4. Copy the linear.mjs script to your project:
   ```bash
   mkdir -p scripts
   cp ~/.claude/skills/linear-manager/linear.mjs scripts/
   ```

5. Add npm script to `package.json`:
   ```json
   {
     "scripts": {
       "linear": "node scripts/linear.mjs"
     }
   }
   ```

## Commands

Once set up, you can use these commands:

```bash
npm run linear viewer          # Show user info
npm run linear teams           # List teams
npm run linear issues [N]      # Show recent issues
npm run linear my-issues [N]   # Show assigned issues
npm run linear projects        # List projects
npm run linear labels          # List labels
npm run linear create-issue <team> <title> [desc]
npm run linear help            # Show all commands
```

## Extending

To add new functionality:

1. Edit `~/.claude/skills/linear-manager/linear.mjs`
2. Add new command to the `commands` object
3. Update `SKILL.md` documentation
4. Optionally update `API-REFERENCE.md` with new SDK patterns

## Architecture

This skill follows the Agent Skills architecture:

- **Level 1 (Metadata)**: Name and description always loaded (~100 tokens)
- **Level 2 (Instructions)**: SKILL.md loaded when triggered (~5k tokens)
- **Level 3 (Resources)**: API-REFERENCE.md and linear.mjs loaded as needed

## Version

Created: 2025-11-07
Linear SDK: v63.2.0
