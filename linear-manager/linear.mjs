#!/usr/bin/env node

import { LinearClient } from '@linear/sdk';
import dotenv from 'dotenv';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

// Load .env file from project root
const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const projectRoot = join(__dirname, '..');
dotenv.config({ path: join(projectRoot, '.env') });

const apiKey = process.env.LINEAR_API_KEY;
if (!apiKey) {
  console.error('ERROR: LINEAR_API_KEY environment variable is required');
  console.error('Please set it in .env file or export LINEAR_API_KEY=your_key');
  process.exit(1);
}

const client = new LinearClient({ apiKey });

const commands = {
  async viewer() {
    const user = await client.viewer;
    console.log('Authenticated User:');
    console.log(`  Name: ${user.name}`);
    console.log(`  Email: ${user.email}`);
    console.log(`  ID: ${user.id}`);
    console.log(`  Admin: ${user.admin}`);
  },

  async teams() {
    const teams = await client.teams();
    console.log(`Teams (${teams.nodes.length}):`);
    for (const team of teams.nodes) {
      console.log(`  - ${team.name} (${team.key})`);
    }
  },

  async issues(args) {
    const limit = args[0] ? parseInt(args[0]) : 10;
    const issues = await client.issues({ first: limit });
    console.log(`Recent Issues (${limit}):`);
    for (const issue of issues.nodes) {
      const team = await issue.team;
      console.log(`  [${team?.key}-${issue.number}] ${issue.title}`);
      console.log(`    Status: ${(await issue.state)?.name || 'Unknown'}`);
      console.log(`    URL: ${issue.url}`);
    }
  },

  async 'my-issues'(args) {
    const user = await client.viewer;
    const limit = args[0] ? parseInt(args[0]) : 20;
    const issues = await client.issues({
      filter: { assignee: { id: { eq: user.id } } },
      first: limit,
    });
    console.log(`My Assigned Issues (${issues.nodes.length}):`);
    for (const issue of issues.nodes) {
      const team = await issue.team;
      const state = await issue.state;
      console.log(`  [${team?.key}-${issue.number}] ${issue.title}`);
      console.log(`    Status: ${state?.name || 'Unknown'}`);
      console.log(`    URL: ${issue.url}`);
    }
  },

  async projects() {
    const projects = await client.projects();
    console.log(`Projects (${projects.nodes.length}):`);
    for (const project of projects.nodes) {
      console.log(`  - ${project.name}`);
      console.log(`    Status: ${project.state}`);
      if (project.description) {
        console.log(`    Description: ${project.description.substring(0, 100)}...`);
      }
    }
  },

  async 'create-issue'(args) {
    if (args.length < 2) {
      console.error('Usage: create-issue <team-key> <title> [description]');
      process.exit(1);
    }
    const [teamKey, title, ...descriptionParts] = args;
    const description = descriptionParts.join(' ');

    const teams = await client.teams({ filter: { key: { eq: teamKey } } });
    if (teams.nodes.length === 0) {
      console.error(`Team with key "${teamKey}" not found`);
      process.exit(1);
    }

    const issue = await client.createIssue({
      teamId: teams.nodes[0].id,
      title,
      description,
    });

    console.log('Issue created successfully:');
    console.log(`  URL: ${issue.issue?.url}`);
  },

  async labels() {
    const labels = await client.issueLabels();
    console.log(`Labels (${labels.nodes.length}):`);
    for (const label of labels.nodes) {
      console.log(`  - ${label.name}`);
    }
  },

  async help() {
    console.log('Linear CLI - Built with @linear/sdk\n');
    console.log('Available commands:');
    console.log('  viewer              Show authenticated user info');
    console.log('  teams               List all teams');
    console.log('  issues [limit]      List recent issues (default: 10)');
    console.log('  my-issues [limit]   List your assigned issues (default: 20)');
    console.log('  projects            List all projects');
    console.log('  labels              List all labels');
    console.log('  create-issue <team-key> <title> [description]');
    console.log('  help                Show this help message');
    console.log('\nEnvironment Variables:');
    console.log('  LINEAR_API_KEY      Required: Your Linear API key');
  },
};

const command = process.argv[2] || 'help';
const args = process.argv.slice(3);

if (!commands[command]) {
  console.error(`Unknown command: ${command}`);
  console.error('Run "linear help" for available commands');
  process.exit(1);
}

try {
  await commands[command](args);
} catch (error) {
  console.error('Error:', error.message);
  process.exit(1);
}
