#!/bin/bash

# Life Momentum Calculator Script
# This script runs the momentum analysis for Claude

set -e  # Exit on any error

MOMENTUM_DIR="/Users/samuelz/Documents/LLM CONTEXT/1 - personal/project_ideas/life-momentum"

echo "🎯 Life.Momentum Calculator"
echo "📂 Navigating to: $MOMENTUM_DIR"
echo

# Change to the momentum directory
cd "$MOMENTUM_DIR"

# Check if dependencies are installed
if [ ! -d "node_modules" ]; then
    echo "📦 Installing dependencies..."
    npm install > /dev/null 2>&1
fi

# Run the momentum calculation
echo "🚀 Calculating current momentum..."
npm run calculate
