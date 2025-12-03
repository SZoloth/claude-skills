#!/bin/bash
# setup.sh - Configure Claude Code skills for this machine
# Usage: ./setup.sh [--force]

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_SKILLS_DIR="$HOME/.claude/skills"
CLAUDE_DIR="$HOME/.claude"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "========================================"
echo "Claude Code Skills Setup"
echo "========================================"
echo ""

# Create ~/.claude if it doesn't exist
if [ ! -d "$CLAUDE_DIR" ]; then
    echo -e "${YELLOW}Creating $CLAUDE_DIR...${NC}"
    mkdir -p "$CLAUDE_DIR"
fi

# Check if skills symlink already exists
if [ -L "$CLAUDE_SKILLS_DIR" ]; then
    CURRENT_TARGET=$(readlink "$CLAUDE_SKILLS_DIR")
    if [ "$CURRENT_TARGET" = "$SCRIPT_DIR" ]; then
        echo -e "${GREEN}Skills already configured correctly!${NC}"
        echo "Symlink: $CLAUDE_SKILLS_DIR -> $SCRIPT_DIR"
        exit 0
    else
        echo -e "${YELLOW}Existing symlink found pointing to: $CURRENT_TARGET${NC}"
        if [ "$1" = "--force" ]; then
            echo "Removing existing symlink (--force flag used)..."
            rm "$CLAUDE_SKILLS_DIR"
        else
            echo ""
            echo -e "${RED}WARNING: A different skills directory is already configured.${NC}"
            echo "Current: $CURRENT_TARGET"
            echo "New:     $SCRIPT_DIR"
            echo ""
            read -p "Replace existing symlink? (y/N) " -n 1 -r
            echo
            if [[ $REPLY =~ ^[Yy]$ ]]; then
                rm "$CLAUDE_SKILLS_DIR"
            else
                echo "Aborted."
                exit 1
            fi
        fi
    fi
elif [ -d "$CLAUDE_SKILLS_DIR" ]; then
    echo -e "${YELLOW}WARNING: $CLAUDE_SKILLS_DIR exists as a regular directory${NC}"
    echo "This may contain existing skills."
    if [ "$1" = "--force" ]; then
        echo "Backing up to ${CLAUDE_SKILLS_DIR}.backup..."
        mv "$CLAUDE_SKILLS_DIR" "${CLAUDE_SKILLS_DIR}.backup"
    else
        echo ""
        read -p "Back up and replace? (y/N) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            mv "$CLAUDE_SKILLS_DIR" "${CLAUDE_SKILLS_DIR}.backup"
            echo "Backed up to ${CLAUDE_SKILLS_DIR}.backup"
        else
            echo "Aborted."
            exit 1
        fi
    fi
fi

# Create the symlink
echo -e "${GREEN}Creating symlink...${NC}"
ln -s "$SCRIPT_DIR" "$CLAUDE_SKILLS_DIR"
echo "Created: $CLAUDE_SKILLS_DIR -> $SCRIPT_DIR"

# Create data directory if it doesn't exist (for tracking files)
if [ ! -d "$SCRIPT_DIR/data" ]; then
    mkdir -p "$SCRIPT_DIR/data"
    echo '{}' > "$SCRIPT_DIR/data/.gitkeep.json"
    echo "Created: $SCRIPT_DIR/data/ (for tracking files)"
fi

echo ""
echo -e "${GREEN}========================================"
echo "Setup Complete!"
echo "========================================${NC}"
echo ""
echo "The following skills are now available globally:"
echo ""
ls -1 "$SCRIPT_DIR" | grep -v -E '^\.|^README|^setup|^data$|\.sh$|\.md$' | head -20
SKILL_COUNT=$(ls -1 "$SCRIPT_DIR" | grep -v -E '^\.|^README|^setup|^data$|\.sh$|\.md$' | wc -l | xargs)
echo "... ($SKILL_COUNT total skills)"
echo ""

# Print MCP server requirements
echo "========================================"
echo "MCP Server Requirements"
echo "========================================"
echo ""
echo "Some skills require MCP servers. Add these to ~/.claude/settings.json:"
echo ""
echo "  things     - Task management (morning-kickstart, executive-assistant)"
echo "  gmail      - Email access (gmail-manager, executive-assistant)"
echo "  google-calendar - Calendar access (executive-assistant, morning-kickstart)"
echo "  strava-mcp - Fitness data (morning-kickstart)"
echo ""
echo "See MCP-REQUIREMENTS.md for setup instructions."
echo ""
