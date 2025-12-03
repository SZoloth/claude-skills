# Life Momentum Skill

This Claude Skill enables analysis of life momentum across multiple domains by scanning personal documentation and calculating energy scores.

## Quick Start

```bash
# Run momentum analysis
./calculate-momentum.sh
```

## What It Does

Analyzes your personal documentation system to provide:
- **Overall momentum score** (0-10 scale)
- **Domain-by-domain breakdown** with energy levels
- **Next action recommendations**
- **Synergy detection** between related areas
- **Historical trend tracking**

## Domains Analyzed

- **Marathon Training** (20%) - Fitness and endurance goals
- **Job Search** (25%) - Career development and opportunities
- **Nutrition & Cooking** (15%) - Health and meal planning
- **Financial Management** (15%) - Money and debt management
- **Relationships & CRM** (10%) - Personal and professional connections
- **Personal Development** (10%) - Growth and self-reflection
- **Vinalhaven Property** (5%) - Long-term planning

## Example Output

```
🚀 Overall Momentum: 5.5/10

🏃 Marathon Training         65%  ██████░░░░
💼 Job Search                88%  ████████░░
🍳 Nutrition & Cooking       21%  ██░░░░░░░░
💰 Financial Management      67%  ██████░░░░
🤝 Relationships & CRM       29%  ██░░░░░░░░
📝 Personal Development      34%  ███░░░░░░░
🏝️ Vinalhaven Property       16%  █░░░░░░░░░

⚡ SYNERGIES DETECTED
   Training + Nutrition coordination
   Bonus: +15%
```

## Customization

Edit the core application in `1 - personal/project_ideas/life-momentum/` to:
- Adjust domain weights based on current priorities
- Modify activity detection rules
- Add new domains to track
- Change scoring algorithms

## Integration

Use this skill when you want to:
- Check overall life momentum
- Identify areas needing attention
- Track progress over time
- Get specific next action recommendations
- Understand synergies between life domains
