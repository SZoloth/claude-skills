---
name: tmuxwatch
description: TUI dashboard for monitoring tmux sessions, useful for long-running agent tasks. This skill should be used when monitoring background processes, viewing tmux session output, or managing multiple terminal sessions. Triggers on "tmux sessions", "monitor background", "session dashboard", or "tmuxwatch".
---

# tmuxwatch - Session Monitor

TUI dashboard for monitoring tmux sessions - useful for long-running agent tasks.

## Launch

```bash
tmuxwatch
```

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| Tab / Shift+Arrow | Switch tabs |
| X | Kill session |
| / | Search |
| Ctrl+P | Command palette |

## When to Use

- Monitor output from background Claude Code sessions
- Track multiple long-running processes
- Quickly navigate between tmux sessions
- Kill stuck or completed sessions
