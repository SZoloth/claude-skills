---
name: cass
description: Search across all agent conversation history (Claude Code, Codex, Cursor, Gemini, Aider, ChatGPT). This skill should be used when looking for previous solutions, checking if a problem was solved before, or searching agent history. Triggers on "search history", "have I solved this before", "previous conversations", or "agent history".
---

# cass - Agent History Search

Search across all agent conversation histories to find previous solutions before solving problems from scratch.

## Critical Usage Rule

**Never run bare `cass`** - it launches an interactive TUI. Always use `--robot` or `--json` flags.

## Common Commands

```bash
# Check index health
cass health

# Search across all histories
cass search "authentication error" --robot --limit 5

# View specific result
cass view /path/to/session.jsonl -n 42 --json

# Expand context around a line
cass expand /path/to/session.jsonl -n 42 -C 3 --json

# Feature discovery
cass capabilities --json
cass robot-docs guide
```

## Key Flags

| Flag | Purpose |
|------|---------|
| `--robot` / `--json` | Machine-readable output (required!) |
| `--fields minimal` | Reduce payload size |
| `--limit N` | Cap result count |
| `--agent NAME` | Filter by agent (claude, codex, cursor, etc.) |
| `--days N` | Limit to recent N days |

## Output Convention

- stdout = data only
- stderr = diagnostics
- Exit 0 = success
