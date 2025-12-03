#!/usr/bin/env python3
"""
RO-DBT Exercise Generator

Generates personalized RO-DBT exercises based on identified patterns from journal analysis
or session notes. Simpler than full agent - primarily templates and recommends exercises.

Usage:
    python exercise-generator.py --patterns "withdrawal,perfectionism"
    python exercise-generator.py --from-analysis journal-analysis_2025-11-27.md
    python exercise-generator.py --interactive
"""

import json
import argparse
from pathlib import Path
from typing import List, Dict, Optional
from datetime import datetime

# Pattern definitions and exercise mappings
PATTERN_EXERCISES = {
    "withdrawal": {
        "name": "Withdrawal When Hurt",
        "edge_question": "What would happen if I shared the hurt instead of retreating?",
        "exercises": [
            {
                "type": "Self-Disclosure Practice",
                "description": "When you notice withdrawal starting, pause and use 'I' statements",
                "steps": [
                    "Notice the urge to withdraw",
                    "Name the feeling: 'I feel hurt/unappreciated/misunderstood'",
                    "Share impact: 'When [event], I felt [emotion]'",
                    "Stay present for the response (don't retreat)"
                ],
                "difficulty": "moderate",
                "duration": "5-10 minutes"
            },
            {
                "type": "Opposite Action",
                "description": "Do the opposite of withdrawal - move toward connection",
                "steps": [
                    "When hurt, instead of going silent, reach out",
                    "Send a simple message: 'Can we talk about what happened?'",
                    "Stay engaged even if uncomfortable",
                    "Observe outcomes without judgment"
                ],
                "difficulty": "challenging",
                "duration": "Varies"
            },
            {
                "type": "Curiosity Questions",
                "description": "Question assumptions about what withdrawal protects",
                "steps": [
                    "Ask: 'What am I protecting by withdrawing?'",
                    "Ask: 'What might I gain by staying engaged?'",
                    "Ask: 'How has withdrawal served me? How has it limited me?'",
                    "Journal responses without judging"
                ],
                "difficulty": "easy",
                "duration": "10-15 minutes"
            }
        ]
    },
    "perfectionism": {
        "name": "Perfectionism in Relationships",
        "edge_question": "Could 'good enough' create more connection than 'perfect'?",
        "exercises": [
            {
                "type": "Flexible Mind Practice",
                "description": "Intentionally lower standards in low-stakes situations",
                "steps": [
                    "Identify one area where you hold high standards",
                    "Set a 'good enough' threshold instead of 'perfect'",
                    "Notice the discomfort when accepting 'good enough'",
                    "Observe: Does connection increase?"
                ],
                "difficulty": "moderate",
                "duration": "Ongoing practice"
            },
            {
                "type": "Appreciation Over Critique",
                "description": "Practice noticing effort rather than outcome",
                "steps": [
                    "When you notice critique arising, pause",
                    "Find one thing to appreciate about the effort",
                    "Express appreciation verbally",
                    "Notice impact on relationship"
                ],
                "difficulty": "easy",
                "duration": "Daily moments"
            },
            {
                "type": "Imperfection Experiment",
                "description": "Intentionally show imperfection to safe people",
                "steps": [
                    "Choose something you'd normally perfect before sharing",
                    "Share it 'imperfect' with a trusted person",
                    "Notice: Does it damage the relationship or deepen it?",
                    "Reflect on what you learned"
                ],
                "difficulty": "challenging",
                "duration": "Weekly experiment"
            }
        ]
    },
    "strategic_avoidance": {
        "name": "Strategic Avoidance",
        "edge_question": "What if the discomfort is information, not danger?",
        "exercises": [
            {
                "type": "Willingness Practice",
                "description": "Move toward discomfort with awareness",
                "steps": [
                    "Identify the task you're avoiding",
                    "Name the emotion you're avoiding: 'I'm avoiding feeling...'",
                    "Set timer for 5 minutes of facing the avoided task",
                    "Notice: Is the discomfort dangerous or just uncomfortable?"
                ],
                "difficulty": "moderate",
                "duration": "5 minutes"
            },
            {
                "type": "Small Brave Steps",
                "description": "Break avoided task into tiny actions",
                "steps": [
                    "Identify what you're avoiding (job outreach, difficult conversation)",
                    "Break into smallest possible first step",
                    "Do just that one step",
                    "Observe: Did facing it build momentum?"
                ],
                "difficulty": "easy",
                "duration": "2-5 minutes"
            },
            {
                "type": "Pattern Recognition",
                "description": "Notice when you're optimizing instead of acting",
                "steps": [
                    "When planning/optimizing, pause and ask: 'Am I avoiding something?'",
                    "Name what you're avoiding",
                    "Choose: Continue optimizing OR face the avoided thing",
                    "Track pattern in journal"
                ],
                "difficulty": "easy",
                "duration": "Ongoing awareness"
            }
        ]
    },
    "low_self_disclosure": {
        "name": "Low Self-Disclosure",
        "edge_question": "Could vulnerability deepen trust rather than damage it?",
        "exercises": [
            {
                "type": "Graduated Vulnerability",
                "description": "Share inner experience in low-stakes situations first",
                "steps": [
                    "Choose safe person (Carter, therapist, trusted friend)",
                    "Share one authentic feeling you'd normally keep private",
                    "Notice their response - did they judge or connect?",
                    "Gradually increase vulnerability with positive outcomes"
                ],
                "difficulty": "moderate",
                "duration": "Weekly practice"
            },
            {
                "type": "Internal State Sharing",
                "description": "Name your emotions as they happen",
                "steps": [
                    "When feeling something, pause",
                    "Say aloud: 'I'm feeling [emotion] right now'",
                    "Don't explain or justify, just name",
                    "Notice: Does naming create relief or connection?"
                ],
                "difficulty": "easy",
                "duration": "Daily moments"
            },
            {
                "type": "Asking for Support",
                "description": "Practice requesting help instead of handling alone",
                "steps": [
                    "Identify something you're struggling with",
                    "Ask one person: 'Could you help me with...'",
                    "Receive help without minimizing need",
                    "Reflect: Did asking damage the relationship?"
                ],
                "difficulty": "challenging",
                "duration": "Weekly experiment"
            }
        ]
    },
    "detail_focused": {
        "name": "Detail-Focused Processing",
        "edge_question": "What if acting with incomplete information is better than perfect planning?",
        "exercises": [
            {
                "type": "Big Picture Practice",
                "description": "Intentionally zoom out from details",
                "steps": [
                    "When lost in details, pause",
                    "Ask: 'What's the big picture goal?'",
                    "Ask: 'What decision would I make if I only had 5 minutes?'",
                    "Make that decision and move forward"
                ],
                "difficulty": "moderate",
                "duration": "5 minutes"
            },
            {
                "type": "Time-Boxed Decisions",
                "description": "Set deadline for deciding regardless of information",
                "steps": [
                    "Set timer for decision deadline (10 minutes, 1 hour, 1 day)",
                    "Gather info only until deadline",
                    "Decide at deadline with available information",
                    "Observe: Was 'complete' information actually necessary?"
                ],
                "difficulty": "moderate",
                "duration": "Varies"
            },
            {
                "type": "Intuition Check-In",
                "description": "Practice trusting gut alongside analysis",
                "steps": [
                    "Before deep analysis, ask: 'What does my gut say?'",
                    "Note the intuitive response",
                    "Do your analysis",
                    "Compare: Did analysis change the intuitive answer?"
                ],
                "difficulty": "easy",
                "duration": "10 minutes"
            }
        ]
    },
    "compulsive_envy": {
        "name": "Compulsive Envy",
        "edge_question": "Could celebrating others' wins actually increase my own joy?",
        "exercises": [
            {
                "type": "Loving Kindness Practice",
                "description": "Genuinely wish others well",
                "steps": [
                    "When hearing good news, pause before automatic comparison",
                    "Silently say: 'May you experience continued success'",
                    "Notice if wishing them well shifts your feeling",
                    "Practice daily with small wins"
                ],
                "difficulty": "moderate",
                "duration": "2 minutes per instance"
            },
            {
                "type": "Abundance Gratitude",
                "description": "Notice your own wins to counter scarcity thinking",
                "steps": [
                    "When envy arises, name it: 'I'm feeling envious'",
                    "List 3 things going well in your own life",
                    "Ask: 'Can both of us be successful?'",
                    "Return to celebrating their win"
                ],
                "difficulty": "easy",
                "duration": "5 minutes"
            },
            {
                "type": "Active Celebration",
                "description": "Express joy for others' success out loud",
                "steps": [
                    "When someone shares good news, notice envy if it arises",
                    "Choose to celebrate anyway",
                    "Say: 'That's amazing! Tell me more!'",
                    "Observe: Does expressing joy shift your feeling?"
                ],
                "difficulty": "challenging",
                "duration": "In the moment"
            }
        ]
    },
    "emotional_inhibition": {
        "name": "Emotional Inhibition",
        "edge_question": "What if expressing emotions in small doses prevents larger eruptions?",
        "exercises": [
            {
                "type": "Emotion Labeling",
                "description": "Name feelings as they arise",
                "steps": [
                    "Set hourly reminder to check: 'What am I feeling right now?'",
                    "Name the emotion (even if subtle)",
                    "Notice where you feel it in your body",
                    "Don't judge or change it, just name it"
                ],
                "difficulty": "easy",
                "duration": "1 minute per check"
            },
            {
                "type": "Somatic Awareness",
                "description": "Track emotions in your body",
                "steps": [
                    "Notice physical sensations: tension, tightness, warmth",
                    "Ask: 'What emotion might this sensation indicate?'",
                    "Breathe into the sensation",
                    "Name the emotion connection"
                ],
                "difficulty": "moderate",
                "duration": "5 minutes daily"
            },
            {
                "type": "Gradual Expression",
                "description": "Share feelings in low-stakes situations",
                "steps": [
                    "Choose very safe person/situation",
                    "Share one small feeling: 'I felt a little frustrated when...'",
                    "Notice: Did expressing it help or hurt?",
                    "Gradually increase with positive results"
                ],
                "difficulty": "moderate",
                "duration": "Weekly practice"
            }
        ]
    },
    "rigid_thinking": {
        "name": "Rigid Thinking",
        "edge_question": "Could embracing paradox make life richer?",
        "exercises": [
            {
                "type": "Dialectical Practice",
                "description": "Hold opposites simultaneously",
                "steps": [
                    "Notice absolute thinking: 'always', 'never', 'must'",
                    "Ask: 'What's the opposite truth?'",
                    "Practice saying: 'Both X and Y can be true'",
                    "Sit with the discomfort of paradox"
                ],
                "difficulty": "moderate",
                "duration": "Daily awareness"
            },
            {
                "type": "Both/And Language",
                "description": "Replace either/or with both/and",
                "steps": [
                    "Catch yourself thinking 'either/or'",
                    "Reframe: 'both/and'",
                    "Example: 'I can be productive AND rest'",
                    "Notice if flexibility increases"
                ],
                "difficulty": "easy",
                "duration": "Ongoing practice"
            },
            {
                "type": "Rule Breaking Experiments",
                "description": "Intentionally break minor personal rules",
                "steps": [
                    "Identify one rigid rule you hold",
                    "Intentionally break it in low-stakes situation",
                    "Observe: Does everything fall apart?",
                    "Reflect on what you learned"
                ],
                "difficulty": "challenging",
                "duration": "Weekly experiment"
            }
        ]
    }
}


class ExerciseGenerator:
    def __init__(self, patterns: List[str]):
        self.patterns = patterns
        self.exercises = []

    def generate_exercises(self) -> Dict:
        """Generate exercise plan based on identified patterns"""

        result = {
            "generated_at": datetime.now().isoformat(),
            "patterns_addressed": self.patterns,
            "exercise_plan": {},
            "weekly_schedule": self.create_weekly_schedule(),
            "getting_started": self.create_getting_started_guide()
        }

        for pattern in self.patterns:
            if pattern in PATTERN_EXERCISES:
                result["exercise_plan"][pattern] = PATTERN_EXERCISES[pattern]

        return result

    def create_weekly_schedule(self) -> Dict:
        """Suggest a weekly practice schedule"""
        return {
            "monday": {
                "type": "Self-Enquiry",
                "duration": "10 minutes",
                "focus": "Notice patterns without judgment"
            },
            "tuesday": {
                "type": "Easy Exercise",
                "duration": "5-10 minutes",
                "focus": "Practice one 'easy' difficulty exercise"
            },
            "wednesday": {
                "type": "Edge Question",
                "duration": "15 minutes",
                "focus": "Journal on one edge question"
            },
            "thursday": {
                "type": "Moderate Exercise",
                "duration": "10-15 minutes",
                "focus": "Practice one 'moderate' difficulty exercise"
            },
            "friday": {
                "type": "Pattern Tracking",
                "duration": "10 minutes",
                "focus": "Review week, track progress in rodbt-progress.json"
            },
            "saturday": {
                "type": "Challenging Exercise",
                "duration": "Varies",
                "focus": "Attempt one 'challenging' difficulty exercise"
            },
            "sunday": {
                "type": "Reflection",
                "duration": "20 minutes",
                "focus": "Weekly review: What worked? What to try next?"
            }
        }

    def create_getting_started_guide(self) -> Dict:
        """Guide for beginning practice"""
        return {
            "week_1": "Choose ONE easy exercise and practice daily. Focus on noticing, not changing.",
            "week_2": "Add journaling about the edge question. What discomfort arises?",
            "week_3": "Introduce ONE moderate exercise. Notice outcomes without judgment.",
            "week_4": "Review progress. What patterns are shifting? What needs more practice?",
            "ongoing": "Gradually increase difficulty. Remember: discomfort is information, not danger."
        }

    def format_as_markdown(self, exercises_data: Dict) -> str:
        """Format exercise plan as markdown"""

        md = f"""# RO-DBT Exercise Plan

**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M")}
**Patterns Addressed:** {', '.join(self.patterns)}

---

## 🎯 Getting Started

**Week 1:** {exercises_data['getting_started']['week_1']}

**Week 2:** {exercises_data['getting_started']['week_2']}

**Week 3:** {exercises_data['getting_started']['week_3']}

**Week 4:** {exercises_data['getting_started']['week_4']}

**Ongoing:** {exercises_data['getting_started']['ongoing']}

---

## 📅 Suggested Weekly Schedule

"""

        for day, details in exercises_data['weekly_schedule'].items():
            md += f"**{day.title()}:** {details['type']} ({details['duration']})\n"
            md += f"- {details['focus']}\n\n"

        md += "\n---\n\n## 🛠️ Exercises by Pattern\n\n"

        for pattern, data in exercises_data['exercise_plan'].items():
            md += f"### {data['name']}\n\n"
            md += f"**Edge Question:** _{data['edge_question']}_\n\n"

            for i, exercise in enumerate(data['exercises'], 1):
                md += f"#### Exercise {i}: {exercise['type']}\n\n"
                md += f"**Description:** {exercise['description']}\n\n"
                md += f"**Difficulty:** {exercise['difficulty'].title()} | **Duration:** {exercise['duration']}\n\n"
                md += "**Steps:**\n"
                for step_num, step in enumerate(exercise['steps'], 1):
                    md += f"{step_num}. {step}\n"
                md += "\n"

            md += "---\n\n"

        md += """## 📝 Progress Tracking

After each exercise:
1. Log to `rodbt-progress.json`
2. Note: What did you observe?
3. Avoid judging outcomes as "success" or "failure"
4. Track patterns over time

## 💡 Remember

- Start with easy exercises
- Discomfort is information, not danger
- Consistency > intensity
- Celebrate small brave steps
- Progress isn't linear

---

*Generated by exercise-generator.py*
*Track progress in .claude/skills/data/rodbt-progress.json*
"""

        return md


def load_patterns_from_analysis(filepath: Path) -> List[str]:
    """Extract patterns from journal analysis markdown file"""
    patterns = []

    with open(filepath, 'r') as f:
        content = f.read()

    # Look for pattern section (simplified extraction)
    # In real implementation, could use more sophisticated parsing
    if 'withdrawal' in content.lower():
        patterns.append('withdrawal')
    if 'perfectionism' in content.lower():
        patterns.append('perfectionism')
    if 'avoidance' in content.lower():
        patterns.append('strategic_avoidance')
    if 'self-disclosure' in content.lower() or 'disclosure' in content.lower():
        patterns.append('low_self_disclosure')
    if 'detail' in content.lower():
        patterns.append('detail_focused')
    if 'envy' in content.lower():
        patterns.append('compulsive_envy')
    if 'inhibition' in content.lower() or 'suppressed' in content.lower():
        patterns.append('emotional_inhibition')
    if 'rigid' in content.lower():
        patterns.append('rigid_thinking')

    return patterns


def interactive_mode() -> List[str]:
    """Interactive pattern selection"""
    print("\n🎯 RO-DBT Exercise Generator - Interactive Mode\n")
    print("Select patterns to address (enter numbers, comma-separated):\n")

    pattern_list = list(PATTERN_EXERCISES.keys())
    for i, pattern_key in enumerate(pattern_list, 1):
        print(f"{i}. {PATTERN_EXERCISES[pattern_key]['name']}")

    selection = input("\nEnter pattern numbers (e.g., 1,3,5): ").strip()

    selected_indices = [int(x.strip()) - 1 for x in selection.split(',')]
    selected_patterns = [pattern_list[i] for i in selected_indices if 0 <= i < len(pattern_list)]

    return selected_patterns


def main():
    parser = argparse.ArgumentParser(description='Generate personalized RO-DBT exercises')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--patterns', help='Comma-separated pattern keys')
    group.add_argument('--from-analysis', help='Path to journal analysis markdown file')
    group.add_argument('--interactive', action='store_true', help='Interactive pattern selection')

    parser.add_argument('--output', help='Output file path (default: auto-generated)')

    args = parser.parse_args()

    # Determine patterns to address
    if args.interactive:
        patterns = interactive_mode()
    elif args.patterns:
        patterns = [p.strip() for p in args.patterns.split(',')]
    else:
        # Load from analysis file
        analysis_path = Path(args.from_analysis)
        if not analysis_path.exists():
            print(f"❌ Analysis file not found: {analysis_path}")
            return 1
        patterns = load_patterns_from_analysis(analysis_path)
        print(f"\n📖 Extracted patterns from analysis: {', '.join(patterns)}\n")

    if not patterns:
        print("❌ No patterns identified. Please specify patterns to address.")
        return 1

    # Generate exercises
    generator = ExerciseGenerator(patterns)
    exercise_data = generator.generate_exercises()

    # Format output
    markdown = generator.format_as_markdown(exercise_data)

    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_path = Path(__file__).parent / f"exercise-plan_{timestamp}.md"

    # Write output
    with open(output_path, 'w') as f:
        f.write(markdown)

    print(f"\n✅ Exercise plan generated: {output_path}")
    print(f"\n📊 Summary:")
    print(f"   Patterns addressed: {len(patterns)}")
    print(f"   Total exercises: {sum(len(PATTERN_EXERCISES[p]['exercises']) for p in patterns if p in PATTERN_EXERCISES)}")
    print(f"\n💡 Next steps:")
    print(f"   1. Review the exercise plan")
    print(f"   2. Choose ONE easy exercise to start")
    print(f"   3. Practice consistently")
    print(f"   4. Track progress in rodbt-progress.json\n")

    return 0


if __name__ == '__main__':
    exit(main())
