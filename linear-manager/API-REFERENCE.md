# Linear SDK API Reference

This document provides detailed information about the Linear SDK capabilities beyond the basic CLI commands.

## LinearClient initialization

```javascript
import { LinearClient } from '@linear/sdk';

const client = new LinearClient({
  apiKey: process.env.LINEAR_API_KEY
});
```

## Common patterns

### Filtering issues

```javascript
// Get issues by status
const issues = await client.issues({
  filter: {
    state: { name: { eq: 'In Progress' } }
  }
});

// Get issues by assignee
const user = await client.viewer;
const myIssues = await client.issues({
  filter: {
    assignee: { id: { eq: user.id } }
  }
});

// Get issues by team
const issues = await client.issues({
  filter: {
    team: { key: { eq: 'PRVT' } }
  }
});

// Get issues by label
const issues = await client.issues({
  filter: {
    labels: { name: { eq: 'bug' } }
  }
});

// Combine filters
const issues = await client.issues({
  filter: {
    and: [
      { assignee: { id: { eq: user.id } } },
      { state: { name: { eq: 'In Progress' } } }
    ]
  }
});
```

### Updating issues

```javascript
// Update issue title
await client.updateIssue('issue-id', {
  title: 'New title'
});

// Update issue description
await client.updateIssue('issue-id', {
  description: 'New description'
});

// Change issue state
const states = await client.workflowStates();
const inProgressState = states.nodes.find(s => s.name === 'In Progress');
await client.updateIssue('issue-id', {
  stateId: inProgressState.id
});

// Assign issue
const user = await client.viewer;
await client.updateIssue('issue-id', {
  assigneeId: user.id
});

// Add labels
const labels = await client.issueLabels();
const bugLabel = labels.nodes.find(l => l.name === 'bug');
await client.updateIssue('issue-id', {
  labelIds: [bugLabel.id]
});

// Set priority (0=None, 1=Urgent, 2=High, 3=Medium, 4=Low)
await client.updateIssue('issue-id', {
  priority: 2
});

// Set estimate (in points)
await client.updateIssue('issue-id', {
  estimate: 5
});
```

### Working with comments

```javascript
// Add a comment
await client.createComment({
  issueId: 'issue-id',
  body: 'This is a comment'
});

// Get comments for an issue
const issue = await client.issue('issue-id');
const comments = await issue.comments();
for (const comment of comments.nodes) {
  console.log(`${comment.user.name}: ${comment.body}`);
}
```

### Working with projects

```javascript
// Create a project
const project = await client.createProject({
  name: 'Q4 Initiative',
  description: 'Main project for Q4',
  teamIds: ['team-id']
});

// Add issue to project
await client.updateIssue('issue-id', {
  projectId: project.project.id
});

// Get project issues
const project = await client.project('project-id');
const issues = await project.issues();
```

### Working with cycles

```javascript
// Get current cycle for a team
const team = await client.team('team-id');
const currentCycle = await team.activeCycle;

// Add issue to current cycle
await client.updateIssue('issue-id', {
  cycleId: currentCycle.id
});
```

### Searching

```javascript
// Search issues by text
const results = await client.issueSearch('authentication bug');
for (const issue of results.nodes) {
  console.log(`[${issue.identifier}] ${issue.title}`);
}
```

### Pagination

```javascript
// Get all issues with pagination
let allIssues = [];
let hasMore = true;
let cursor = undefined;

while (hasMore) {
  const response = await client.issues({
    first: 50,
    after: cursor
  });

  allIssues = allIssues.concat(response.nodes);
  hasMore = response.pageInfo.hasNextPage;
  cursor = response.pageInfo.endCursor;
}
```

## Advanced filtering operators

### Comparison operators
- `eq` - Equals
- `neq` - Not equals
- `gt` - Greater than
- `gte` - Greater than or equal
- `lt` - Less than
- `lte` - Less than or equal
- `in` - In array
- `nin` - Not in array

### Text operators
- `contains` - Contains substring
- `containsIgnoreCase` - Contains substring (case insensitive)
- `startsWith` - Starts with
- `endsWith` - Ends with

### Logical operators
- `and` - All conditions must be true
- `or` - At least one condition must be true

### Null checks
- `null: true` - Is null
- `null: false` - Is not null

## Issue states

Common workflow states:
- Triage
- Backlog
- Todo
- In Progress
- In Review
- Done
- Canceled

Get all states:
```javascript
const states = await client.workflowStates();
for (const state of states.nodes) {
  console.log(`${state.name} (${state.type})`);
}
```

## Issue priorities

Priority values:
- `0` - No priority
- `1` - Urgent
- `2` - High
- `3` - Medium
- `4` - Low

## Date handling

```javascript
// Filter by creation date
const issues = await client.issues({
  filter: {
    createdAt: {
      gte: new Date('2025-01-01')
    }
  }
});

// Filter by completion date
const issues = await client.issues({
  filter: {
    completedAt: {
      gte: new Date('2025-01-01')
    }
  }
});
```

## Webhooks and subscriptions

Note: Webhooks require server setup and are not available in the CLI.

## Error handling

```javascript
try {
  const issue = await client.issue('invalid-id');
} catch (error) {
  if (error.message.includes('not found')) {
    console.error('Issue not found');
  } else {
    console.error('Error:', error.message);
  }
}
```

## Rate limiting

The Linear API has rate limits:
- Check response headers for rate limit info
- Implement exponential backoff for retries
- Use pagination to avoid hitting limits

```javascript
// Good: Paginated requests
const response = await client.issues({ first: 50 });

// Bad: Requesting too much at once
const response = await client.issues({ first: 1000 });
```

## Best practices

1. **Always check for existence before updating**
   ```javascript
   const issue = await client.issue('id');
   if (issue) {
     await client.updateIssue(issue.id, { ... });
   }
   ```

2. **Use specific filters instead of fetching everything**
   ```javascript
   // Good
   const issues = await client.issues({
     filter: { team: { key: { eq: 'PRVT' } } }
   });

   // Bad
   const allIssues = await client.issues({ first: 1000 });
   const filtered = allIssues.nodes.filter(i => i.team.key === 'PRVT');
   ```

3. **Cache frequently accessed data**
   ```javascript
   // Cache teams, labels, states if using repeatedly
   const teams = await client.teams();
   const teamMap = new Map(teams.nodes.map(t => [t.key, t]));
   ```

4. **Handle async operations properly**
   ```javascript
   // When accessing nested data, await each step
   const issue = await client.issue('id');
   const state = await issue.state;
   const team = await issue.team;
   ```

## Common use cases

### Daily standup report
```javascript
const user = await client.viewer;
const yesterday = new Date();
yesterday.setDate(yesterday.getDate() - 1);

const completedIssues = await client.issues({
  filter: {
    assignee: { id: { eq: user.id } },
    completedAt: { gte: yesterday }
  }
});

const inProgressIssues = await client.issues({
  filter: {
    assignee: { id: { eq: user.id } },
    state: { name: { eq: 'In Progress' } }
  }
});
```

### Sprint planning
```javascript
const team = await client.team('team-id');
const backlogIssues = await client.issues({
  filter: {
    team: { id: { eq: team.id } },
    state: { name: { eq: 'Backlog' } }
  },
  orderBy: 'priority'
});
```

### Bug triage
```javascript
const labels = await client.issueLabels();
const bugLabel = labels.nodes.find(l => l.name === 'bug');

const untriagedBugs = await client.issues({
  filter: {
    labels: { id: { eq: bugLabel.id } },
    state: { name: { eq: 'Triage' } }
  }
});
```

## Resources

- [Linear API Documentation](https://developers.linear.app/docs)
- [Linear SDK on GitHub](https://github.com/linear/linear)
- [Linear API Explorer](https://studio.apollographql.com/public/Linear-API/variant/current/explorer)
