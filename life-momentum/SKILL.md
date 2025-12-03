---
name: life-momentum
description: Analyze and calculate momentum across life domains from personal documentation. Use when users want to understand their progress, identify areas needing attention, or track momentum across career, health, finances, relationships, and personal development.
---

# Life Momentum Analysis

This skill enables Claude to analyze momentum across different life domains by scanning personal documentation files and calculating energy scores, identifying synergies, and providing actionable next steps.

## When to Use

Use this skill when users ask about:
- Life momentum or progress tracking
- Areas where they're gaining or losing momentum
- Next actions across different life domains
- Synergies between life areas
- Overall life balance and priorities

## How It Works

The skill analyzes markdown files across seven life domains:
- **Marathon Training** (20% weight) - Physical fitness and endurance
- **Job Search** (25% weight) - Career development and opportunities
- **Nutrition & Cooking** (15% weight) - Health and meal planning
- **Financial Management** (15% weight) - Money and debt management
- **Relationships & CRM** (10% weight) - Personal and professional connections
- **Personal Development** (10% weight) - Growth and self-reflection
- **Vinalhaven Property** (5% weight) - Long-term planning

## Analysis Process

### 1. File Discovery
Scans for markdown files in each domain directory using specific patterns and activity rules.

### 2. Energy Calculation
Each domain receives an energy score (0-100%) based on:
- **Recency** (40%): How recently files were modified
- **Consistency** (35%): Regular activity patterns
- **Quality** (25%): Meaningful content indicators

### 3. Momentum Score
Overall momentum (0-10 scale) weighted by current life priorities.

### 4. Synergy Detection
Identifies when domains reinforce each other (e.g., training + nutrition synergy).

## Usage Examples

### Example 1: Quick Momentum Check
User: "What's my current life momentum?"
Claude should:
1. Run momentum analysis
2. Report overall score and domain breakdown
3. Highlight top priorities and concerns

### Example 2: Domain Focus
User: "How's my job search momentum?"
Claude should:
1. Analyze job search domain specifically
2. Provide detailed breakdown of activities
3. Suggest specific next actions

### Example 3: Momentum Trends
User: "Am I gaining or losing momentum?"
Claude should:
1. Compare current scores with historical snapshots
2. Identify trends (up/down/stable)
3. Explain what changed

## Skill Commands

### Calculate Current Momentum
```bash
# Quick method using the provided script
./calculate-momentum.sh

# Manual method
cd "/Users/samuelz/Documents/LLM CONTEXT/1 - personal/project_ideas/life-momentum"
npm run calculate
```

### Generate Daily Affirmations
```bash
# Quick method
./scripts/daily-affirmations.sh

# Manual method
cd "/Users/samuelz/Documents/LLM CONTEXT/1 - personal/personal_development"
node daily_affirmation_generator.js
```

### View Historical Trends
```bash
cd "/Users/samuelz/Documents/LLM CONTEXT/1 - personal/project_ideas/life-momentum"
ls .snapshots/
```

### Domain-Specific Analysis
The tool automatically analyzes all domains, but focus on specific domains when requested.

## Interpretation Guide

### Overall Momentum Scale (0-10)
- **9-10**: Exceptional momentum across all areas
- **8-9**: Strong performance with minor optimizations possible
- **7-8**: Good progress with some areas needing attention
- **6-7**: Steady state with opportunities for improvement
- **5-6**: Momentum slipping - time to refocus
- **4-5**: Multiple domains stalled - priority reset needed
- **0-4**: Rebuild mode - focus on one domain at a time

### Domain Energy Levels (0-100%)
- **80-100%**: Excellent activity and recent engagement
- **60-79%**: Good momentum and consistent progress
- **40-59%**: Moderate activity needing attention
- **0-39%**: Low energy requiring immediate focus

## Common Patterns

### High Momentum Indicators
- Recent file modifications across multiple domains
- Completed tasks and checkmarks in documentation
- Cross-references between related domains
- Consistent activity patterns

### Low Momentum Warning Signs
- Stale files (weeks without updates)
- Incomplete tasks and unchecked items
- Isolated activity in only one domain
- Inconsistent engagement patterns

## Customization

### Adjust Domain Weights
Edit `lib/domain-config.ts` to change importance of different life areas based on current priorities.

### Modify Activity Rules
Update quality indicators and file patterns to match your documentation style.

### Add New Domains
Extend the system to track additional life areas by adding new domain configurations.

## Integration Points

### Daily Planning
Use momentum scores to inform daily task prioritization and focus areas.

### Weekly Reviews
Compare momentum trends to assess progress and adjust strategies.

### Monthly Planning
Analyze long-term momentum patterns to set quarterly goals and priorities.

### Crisis Management
When momentum drops significantly, use the tool to identify specific intervention points.

## Best Practices

### Regular Check-ins
Run momentum analysis daily or weekly to maintain awareness of progress.

### Action-Oriented
Always follow momentum analysis with specific, actionable next steps.

### Holistic View
Consider synergies between domains rather than optimizing in isolation.

### Sustainable Pace
Balance high-priority domains while maintaining minimum activity in others.

## Troubleshooting

### "Cannot find module" errors
The script automatically handles dependency installation. If you run manually:
```bash
cd "/Users/samuelz/Documents/LLM CONTEXT/1 - personal/project_ideas/life-momentum"
npm install
```

### Permission denied on script
```bash
chmod +x calculate-momentum.sh
```

### No domains found
Check that PERSONAL_DOCS_PATH in .env.local points to the correct directory.

### Scores don't match reality
Adjust domain weights or activity rules to better reflect your priorities and work patterns.

## Technical Details

The skill executes a Node.js application that:
- Parses markdown files using custom parsers
- Analyzes file modification dates and content patterns
- Calculates weighted scores using configurable algorithms
- Generates human-readable reports with actionable insights
- Maintains historical snapshots for trend analysis

## Files and Resources

### Skill Files
- `SKILL.md` - This instruction file
- `calculate-momentum.sh` - Executable script for running analysis
- `README.md` - Quick reference and setup guide
- `examples.md` - Conversation examples and usage patterns

### Core Application (in project directory)
- `lib/index.ts` - Main orchestrator
- `lib/momentum-engine/calculator.ts` - Core algorithms
- `lib/domain-config.ts` - Domain definitions and weights
- `lib/parsers/markdown-parser.ts` - File analysis logic
- `.snapshots/` - Historical momentum data
- `README.md` - Complete technical documentation
