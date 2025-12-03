---
name: linear-manager
description: Manage Linear issues, projects, and teams. Use when the user mentions Linear, wants to create/view/update issues, check project status, or manage their Linear workflow. Provides comprehensive Linear API access through the @linear/sdk.
---

# Linear Manager

A comprehensive skill for managing Linear issues, projects, teams, and workflows using the Linear API.

## When to use this skill

Use this skill whenever the user:
- Mentions Linear or Linear issues
- Wants to create, view, update, or search for issues
- Needs to check their assigned tasks or team's workload
- Wants to manage projects or view project status
- Needs to interact with Linear's workflow (teams, labels, states, etc.)

## Prerequisites

This skill requires:
1. The `@linear/sdk` npm package (should be installed in the project)
2. A `LINEAR_API_KEY` environment variable or `.env` file with the API key
3. The `linear.mjs` script located at `scripts/linear.mjs`

## Available commands

The Linear CLI script provides these commands:

### View user information
```bash
npm run linear viewer
```
Shows authenticated user details (name, email, ID, admin status).

### List teams
```bash
npm run linear teams
```
Lists all teams with their names and keys (e.g., PRVT, DWA).

### View recent issues
```bash
npm run linear issues [limit]
```
Shows recent issues across all teams. Optional limit parameter (default: 10).

Example:
```bash
npm run linear issues 25  # Show 25 most recent issues
```

### View assigned issues
```bash
npm run linear my-issues [limit]
```
Shows issues assigned to the authenticated user. Optional limit parameter (default: 20).

Example:
```bash
npm run linear my-issues 10  # Show my 10 most recent issues
```

### List projects
```bash
npm run linear projects
```
Shows all projects with their names, status, and descriptions.

### List labels
```bash
npm run linear labels
```
Shows all available issue labels.

### Create an issue
```bash
npm run linear create-issue <team-key> <title> [description]
```
Creates a new issue in the specified team.

Example:
```bash
npm run linear create-issue PRVT "Buy groceries" "Need milk and eggs"
```

### Get help
```bash
npm run linear help
```
Shows all available commands and usage instructions.

## Best practices

### When creating issues
1. Always verify the team key first by running `npm run linear teams`
2. Use clear, descriptive titles
3. Include relevant context in the description
4. Confirm the issue was created by checking the returned URL

### When querying issues
1. Start with a reasonable limit (10-20) to avoid overwhelming output
2. If the user wants to see specific issues, consider filtering by team or status
3. Always show the issue URL so the user can easily access it in their browser

### Error handling
- If the LINEAR_API_KEY is not set, the script will show a clear error message
- If a team key is not found, the script will list available teams
- Network errors will be caught and displayed with helpful messages

## Examples

### Example 1: Check what's on your plate
```bash
npm run linear my-issues 5
```

Claude should:
1. Run the command
2. Parse the output to show a clean summary
3. Highlight any urgent or blocked issues
4. Offer to help with any issues if needed

### Example 2: Create a new task
```bash
# First verify the team key
npm run linear teams

# Then create the issue
npm run linear create-issue PRVT "Prepare Q4 presentation" "Create slides for quarterly review meeting"
```

Claude should:
1. Confirm the team key exists
2. Create the issue with appropriate title and description
3. Report the success and provide the URL
4. Optionally ask if the user wants to add labels or assign it

### Example 3: Check team workload
```bash
npm run linear issues 20
```

Claude should:
1. Run the command
2. Analyze the output to identify patterns (which team has most issues, common states)
3. Provide insights about the team's current focus
4. Suggest next actions if appropriate

## Advanced usage

### Direct script execution
If npm scripts are not available, the script can be run directly:
```bash
cd "/Users/samuelz/Documents/LLM CONTEXT"
node scripts/linear.mjs <command> [args]
```

### Environment variables
The script automatically loads `.env` from the project root. Alternatively, set the environment variable directly:
```bash
LINEAR_API_KEY=your_key_here npm run linear viewer
```

## Extending functionality

The `linear.mjs` script can be extended with additional commands. To add new functionality:

1. Open `scripts/linear.mjs`
2. Add a new command to the `commands` object
3. Follow the existing patterns for error handling and output formatting
4. Update the help command with the new command documentation
5. Update this SKILL.md file with the new command details

## Troubleshooting

### "LINEAR_API_KEY environment variable is required"
- Ensure `.env` file exists in `/Users/samuelz/Documents/LLM CONTEXT/`
- Verify the file contains: `LINEAR_API_KEY=lin_api_...`
- Check that `.env` is not in `.gitignore` (it should be for security)

### "@linear/sdk not found"
- Run: `npm install @linear/sdk` in the project directory

### "Team with key X not found"
- Run `npm run linear teams` to see valid team keys
- Team keys are case-sensitive (e.g., PRVT, DWA)

### Script not found
- Verify `scripts/linear.mjs` exists
- Check that the script is executable: `chmod +x scripts/linear.mjs`

## Security notes

- The LINEAR_API_KEY grants full access to your Linear workspace
- Never commit the `.env` file to version control
- The `.env` file is automatically added to `.gitignore`
- API keys should be treated as sensitive credentials

## Integration tips

This skill works well with:
- Daily standup routines (check my-issues at start of day)
- Project planning (create multiple issues in sequence)
- Status reporting (analyze recent issues for updates)
- Task management workflows (create, update, track issues)
- Team coordination (check team workload and assignments)
