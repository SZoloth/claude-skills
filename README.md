# Claude Code Skills

Shared skills for Claude Code that work across all projects.

## Quick Start

### As Git Submodule (Recommended)

```bash
# In your project root
git submodule add https://github.com/SZoloth/claude-skills.git .claude/shared-skills
git submodule update --init

# Run setup
.claude/shared-skills/setup.sh
```

### Standalone Installation

```bash
git clone https://github.com/SZoloth/claude-skills.git ~/.claude-skills
~/.claude-skills/setup.sh
```

## What This Does

The setup script creates a symlink:
```
~/.claude/skills → (this directory)
```

This makes all skills available globally to Claude Code on your machine.

## Skills Included

### Productivity & Life Management
- `executive-assistant` - Daily planning, weekly reviews, task management
- `morning-kickstart` - Morning ritual with bi-directional integrations
- `holistic-life-coach` - Cross-domain life coaching and synthesis

### Product & Strategy
- `marty-cagan-coach` - SVPG product leadership principles
- `product-transformation-coach` - Feature factory to product-led transformation
- `product-coaching` - Evidence-based product skills development
- `research-expert` - Teresa Torres continuous discovery
- `validation-expert` - UX research and validation

### Learning & Development
- `upskilling-coach` - Deliberate practice and skill building
- `think-first` - Cognitive engagement ("Think First, AI Second")

### Specialized Tools
- `monodraw-diagrams` - ASCII architecture diagrams
- `communication-optimizer` - BLUF, Minto Pyramid, SCR frameworks
- `fact-checker-investigator` - Claim verification and source checking
- `rodbt-coach` - RO-DBT therapy coaching
- `job-search-specialist` - Never Search Alone methodology

### Utilities
- `gmail-manager` - Email management
- `calendar-manager` - Calendar operations
- `beads-viewer` - Issue tracker analysis
- `skill-creator` - Create new skills

## MCP Server Requirements

Some skills require MCP servers for full functionality. See [MCP-REQUIREMENTS.md](./MCP-REQUIREMENTS.md) for setup instructions.

**No MCP required:** `think-first`, `upskilling-coach`, `monodraw-diagrams`, `marty-cagan-coach`, `product-coaching`, `research-expert`, `validation-expert`, `communication-optimizer`, `rodbt-coach`

**MCP required:** `executive-assistant`, `morning-kickstart`, `gmail-manager` (Gmail, Calendar, Things)

## Project-Specific Skills

This repo contains **shared** skills. Projects can have their own skills in `.claude/skills/` which take precedence.

## Architecture

```
~/.claude/skills (symlink) → (this repo or submodule)
    ├── skill-name/
    │   ├── SKILL.md          # Main skill definition (required)
    │   ├── references/       # Supporting documentation
    │   ├── agents/           # TypeScript Agent SDK workflows
    │   └── scripts/          # Python/shell helpers
    └── data/                 # Tracking files (local only)
```

See [README-ARCHITECTURE.md](./README-ARCHITECTURE.md) for detailed documentation.

## Updating

### As Submodule
```bash
cd .claude/shared-skills
git pull origin main
```

### Standalone
```bash
cd ~/.claude-skills
git pull origin main
```
