---
name: gemini-context
description: Use Gemini CLI for analyzing large codebases that exceed Claude's context limits. This skill should be used when context is too large, analyzing entire codebases, comparing many files, or verifying implementation across a whole project. Triggers on "context too large", "analyze whole codebase", "gemini for large files", or "exceeds context".
---

# gemini-context - Large Codebase Analysis

When files exceed Claude's context limits, use Gemini CLI with its massive context window.

## Basic Syntax

Use `@` syntax to include files/directories. Paths are relative to current directory.

```bash
# Single file
gemini -p "@src/main.py Explain this file's purpose"

# Multiple files
gemini -p "@package.json @src/index.js Analyze dependencies"

# Entire directory
gemini -p "@src/ Summarize the architecture"

# Multiple directories
gemini -p "@src/ @tests/ Analyze test coverage"

# Entire project
gemini -p "@./ Give me an overview"
# Or:
gemini --all_files -p "Analyze project structure"
```

## Implementation Verification Examples

```bash
# Check if feature exists
gemini -p "@src/ @lib/ Has dark mode been implemented?"

# Verify authentication
gemini -p "@src/ @middleware/ Is JWT auth implemented?"

# Find patterns
gemini -p "@src/ Are there React hooks handling WebSocket?"

# Check error handling
gemini -p "@src/ @api/ Is proper error handling implemented?"

# Security audit
gemini -p "@src/ @api/ Are SQL injection protections in place?"

# Test coverage
gemini -p "@src/payment/ @tests/ Is payment module fully tested?"
```

## When to Use

- Files total >100KB
- Need project-wide pattern analysis
- Current Claude context insufficient
- Verifying implementation across entire codebase
- Comparing multiple large files

## Notes

- Paths in `@` are relative to where you run `gemini`
- No `--yolo` flag needed for read-only analysis
- Be specific about what you're looking for
