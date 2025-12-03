---
name: beads-viewer
description: Analyze Beads issue tracker graphs for planning, prioritization, and execution insights. Use when the user asks about tasks, priorities, what to work on next, project planning, or mentions Beads issues. Provides graph-theoretic analysis (PageRank, critical path, bottlenecks) for intelligent prioritization.
---

# Beads Viewer Integration

## Overview

Beads Viewer (`bv`) provides structural analysis of issue tracker graphs (DAGs) stored in `.beads/beads.jsonl` files. It computes graph-theoretic metrics to identify bottlenecks, critical paths, and optimal execution sequences that traditional list-based trackers miss.

## When to Use This Skill

Invoke this skill when the user:
- Asks "what should I work on next?" or wants prioritization help
- Wants to understand project dependencies or blockers
- Needs execution planning or sequencing
- Asks about Beads issues, tasks, or project status
- Wants to see what's changed since a previous point in time
- Needs to identify bottlenecks or critical paths

## Available Commands

### Execution Planning
```bash
bv --robot-plan
```
Returns dependency-respecting execution plan:
- `tracks`: Independent work streams that can be parallelized
- `items`: Actionable issues sorted by priority within each track
- `unblocks`: Issues that become actionable when an item is done
- `summary.highest_impact`: The single most impactful item to work on

### Graph Insights
```bash
bv --robot-insights
```
Returns deep graph analysis:
- **PageRank**: Measures 'blocking power' - high score = fundamental dependency
- **Betweenness**: Measures 'bottleneck status' - high score = connects disparate clusters
- **CriticalPathScore**: Depth heuristic - high score = blocking long chain of work
- **Hubs/Authorities**: HITS algorithm for dependency relationships
- **Cycles**: Circular dependencies (unhealthy state)

### Priority Recommendations
```bash
bv --robot-priority
```
Suggests priority adjustments:
- `recommendations`: Sorted by confidence, then impact score
- `confidence`: 0-1 score indicating strength of recommendation
- `reasoning`: Human-readable explanations
- `direction`: 'increase' or 'decrease' priority

### Change Tracking
```bash
bv --diff-since HEAD~5 --robot-diff
```
Shows changes since a historical point:
- `new_issues`: Issues added since then
- `closed_issues`: Issues that were closed
- `modified_issues`: Issues with field changes
- `summary.health_trend`: 'improving', 'degrading', or 'stable'

### Available Recipes
```bash
bv --robot-recipes
```
Lists filtering/sorting presets: `default`, `actionable`, `recent`, `blocked`, `high-impact`, `stale`

## Workflow

### Standard Planning Query
1. Run `bv --robot-plan` to get execution plan
2. Parse JSON and identify `summary.highest_impact` issue
3. Present the recommended next action with context
4. If dependencies exist, show the unblock chain

### Deep Analysis Query
1. Run `bv --robot-insights` for graph metrics
2. Identify bottlenecks (high betweenness) and keystones (high PageRank)
3. Check for cycles (structural problems)
4. Provide strategic recommendations

### Priority Review
1. Run `bv --robot-priority`
2. Present high-confidence recommendations first
3. Include reasoning for each suggestion

## Multi-Repository Support

For workspaces with multiple Beads repos, use:
```bash
bv --workspace .bv/workspace.yaml
bv --workspace .bv/workspace.yaml --repo api  # Filter to specific repo
```

## Known Locations

The user has Beads repos in:
- `/Users/samuelz/Documents/LLM CONTEXT/.beads/` (root vault)
- `/Users/samuelz/Documents/LLM CONTEXT/1 - personal/.beads/` (personal)
- `/Users/samuelz/Documents/LLM CONTEXT/2 - work/DWA-PROJECT-HOME/.beads/` (DreamWorks)
- `/Users/samuelz/Documents/LLM CONTEXT/2 - work/COMCAST-PROJECT-HOME/.beads/` (Comcast)

## Output Interpretation

### PageRank Scores
- **High (>0.5)**: Foundational blocker - prioritize these
- **Medium (0.2-0.5)**: Important dependencies
- **Low (<0.2)**: Leaf nodes, can be parallelized

### Betweenness Centrality
- **High**: Bottleneck - completing this unblocks multiple paths
- **Low**: Not a critical junction

### Density
- **High (>0.3)**: Tightly coupled, may need simplification
- **Low (<0.1)**: Well-modularized or sparse dependencies

## Example Responses

When asked "What should I work on?":
1. Run `bv --robot-plan`
2. Extract highest impact item
3. Respond: "Based on dependency analysis, [ISSUE] has the highest impact. Completing it will unblock [N] other items."

When asked "Are there any bottlenecks?":
1. Run `bv --robot-insights`
2. Check Bottlenecks array
3. Respond with identified bottlenecks and their betweenness scores
