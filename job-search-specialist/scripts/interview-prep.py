#!/usr/bin/env python3
"""
Interview Prep Script

Generates comprehensive interview preparation package for a specific company and role.
Simpler workflow than company-research agent - primarily templates existing data.

Features:
- Loads company research if available
- Matches STAR stories to role requirements
- Generates practice questions
- Creates talking points and questions to ask
- Outputs prep package as markdown

Usage:
    python interview-prep.py "Stripe" "Senior Product Manager" "2025-12-15"
    python interview-prep.py "Figma" "Director of Product"
"""

import sys
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict

# Standard STAR story categories for PM roles
STORY_CATEGORIES = {
    "product_strategy": [
        "Led product vision and strategy",
        "Defined product roadmap",
        "Prioritized features based on impact"
    ],
    "growth_metrics": [
        "Drove user growth or engagement",
        "Improved conversion rates",
        "Analyzed metrics to inform decisions"
    ],
    "cross_functional": [
        "Led cross-functional teams",
        "Managed stakeholder expectations",
        "Navigated organizational complexity"
    ],
    "technical": [
        "Worked with engineering on architecture",
        "Made technical trade-off decisions",
        "Shipped complex technical features"
    ],
    "user_research": [
        "Conducted user research",
        "Validated assumptions with data",
        "Synthesized user insights into product decisions"
    ]
}

# Common PM interview question templates
INTERVIEW_QUESTIONS = {
    "behavioral": [
        "Tell me about a time you disagreed with a stakeholder. How did you handle it?",
        "Describe a product you're proud of building. What made it successful?",
        "Tell me about a time a product you launched failed. What did you learn?",
        "How do you prioritize features when everything seems important?",
        "Describe a time you had to make a decision with incomplete information."
    ],
    "product_sense": [
        "How would you improve [company's product]?",
        "Design a product for [specific user need].",
        "How would you measure success for [feature/product]?",
        "Walk me through how you would approach [product problem].",
        "If you could add one feature to [product], what would it be and why?"
    ],
    "analytical": [
        "You notice a 20% drop in user engagement. How do you investigate?",
        "How would you estimate [market size/metric]?",
        "What metrics would you track for [product/feature]?",
        "A/B test results are inconclusive. What do you do?",
        "How do you know if a feature is successful?"
    ],
    "strategy": [
        "Where do you see [company/product] in 5 years?",
        "How should [company] approach [competitive threat]?",
        "What's [company]'s biggest opportunity right now?",
        "If you were CEO, what would you prioritize?",
        "How would you enter [new market/segment]?"
    ]
}

class InterviewPrepGenerator:
    def __init__(self, company: str, role: str, interview_date: Optional[str] = None):
        self.company = company
        self.role = role
        self.interview_date = interview_date or "TBD"
        self.research_data = self.load_company_research()

    def load_company_research(self) -> Optional[Dict]:
        """Load company research from agent output if available"""
        # Look for recent company research files
        agents_dir = Path(__file__).parent.parent / "agents" / "company-research"

        if not agents_dir.exists():
            return None

        # Find most recent research file for this company
        research_files = list(agents_dir.glob(f"{self.company.lower().replace(' ', '-')}*.md"))

        if not research_files:
            return None

        # Return the most recent file path
        latest_file = max(research_files, key=lambda p: p.stat().st_mtime)
        return {"file_path": str(latest_file)}

    def generate_star_story_matches(self) -> Dict[str, List[str]]:
        """Generate recommended STAR stories for this role"""
        # For now, return category recommendations
        # In future, could integrate with actual Case_Stories_Repository

        matches = {}

        if "senior" in self.role.lower() or "director" in self.role.lower():
            matches["must_have"] = [
                "Product strategy story (vision, roadmap, market positioning)",
                "Cross-functional leadership (managing up, influencing without authority)",
                "Data-driven decision making (metrics, experimentation, analysis)"
            ]
            matches["nice_to_have"] = [
                "Scaling story (0-1 or scaling product/team)",
                "Technical depth (API design, architecture decisions)",
                "Stakeholder management (executive alignment, difficult conversations)"
            ]
        else:
            matches["must_have"] = [
                "Product execution story (shipped feature, measurable impact)",
                "User research story (validated assumptions, learned from users)",
                "Cross-functional collaboration (worked with eng/design)"
            ]
            matches["nice_to_have"] = [
                "Growth experiment (A/B test, optimization)",
                "Technical contribution (worked closely with engineering)",
                "Problem-solving (ambiguous problem, creative solution)"
            ]

        return matches

    def generate_practice_questions(self) -> Dict[str, List[str]]:
        """Generate likely interview questions based on company and role"""
        questions = {}

        for category, question_templates in INTERVIEW_QUESTIONS.items():
            questions[category] = []

            for template in question_templates[:3]:  # Top 3 per category
                # Customize template with company name where applicable
                question = template.replace("[company's product]", f"{self.company}'s product")
                question = question.replace("[company/product]", self.company)
                question = question.replace("[company]", self.company)
                questions[category].append(question)

        return questions

    def generate_talking_points(self) -> List[str]:
        """Generate talking points based on company research"""
        points = [
            f"Why {self.company}? (Authentic connection to mission/product)",
            f"What excites you about this {self.role} role?",
            f"How does this fit your 5-year vision?",
            "Relevant experience that maps to role requirements",
            f"Questions that demonstrate research about {self.company}"
        ]

        if self.research_data:
            points.append(f"Reference insights from research report: {self.research_data['file_path']}")

        return points

    def generate_questions_to_ask(self) -> Dict[str, List[str]]:
        """Generate thoughtful questions to ask interviewers"""
        return {
            "about_role": [
                "What does success look like in this role in the first 90 days? First year?",
                f"What are the biggest challenges facing the {self.role} right now?",
                "How does this role fit into the broader product organization?",
                "What would you want this person to prioritize first?"
            ],
            "about_team": [
                "Tell me about the product team structure and how we collaborate.",
                "What's the decision-making process for product prioritization?",
                "How do product, engineering, and design work together here?",
                f"What's your favorite thing about working at {self.company}?"
            ],
            "about_company": [
                f"Where do you see {self.company} in 2-3 years?",
                f"What's {self.company}'s biggest opportunity right now?",
                f"How does {self.company} think about product strategy and vision?",
                "What makes a great product manager succeed here?"
            ],
            "about_growth": [
                f"How does {self.company} support PM career development?",
                "What opportunities exist for growth and advancement?",
                "How do you give and receive feedback here?",
                "What's the culture around work-life balance?"
            ]
        }

    def generate_prep_package(self) -> str:
        """Generate complete interview prep package as markdown"""
        star_matches = self.generate_star_story_matches()
        practice_questions = self.generate_practice_questions()
        talking_points = self.generate_talking_points()
        questions_to_ask = self.generate_questions_to_ask()

        # Build markdown document
        md = f"""# Interview Prep: {self.company}
## {self.role}

**Interview Date:** {self.interview_date}
**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M")}

---

## Company Research

"""

        if self.research_data:
            md += f"📊 **Research Report Available:** {self.research_data['file_path']}\n\n"
            md += "Review the research report for:\n"
            md += "- Company background and market position\n"
            md += "- Culture and values assessment\n"
            md += "- Competitive landscape\n"
            md += "- Pre-prepared talking points\n\n"
        else:
            md += f"⚠️ **No research report found.** Consider running:\n"
            md += f"```bash\n"
            md += f'tsx company-research/agent.ts "{self.company}" "{self.role}"\n'
            md += f"```\n\n"

        md += "---\n\n## STAR Story Selection\n\n"
        md += "### Must-Have Stories\n\n"
        for story in star_matches["must_have"]:
            md += f"- [ ] {story}\n"

        md += "\n### Nice-to-Have Stories\n\n"
        for story in star_matches["nice_to_have"]:
            md += f"- [ ] {story}\n"

        md += "\n> **Action:** Map your case stories to these categories and practice 2-minute STAR responses for each.\n\n"

        md += "---\n\n## Practice Questions\n\n"
        for category, questions in practice_questions.items():
            md += f"### {category.replace('_', ' ').title()}\n\n"
            for q in questions:
                md += f"- {q}\n"
            md += "\n"

        md += "---\n\n## Your Talking Points\n\n"
        for i, point in enumerate(talking_points, 1):
            md += f"{i}. **{point}**\n"
        md += "\n"

        md += "---\n\n## Questions to Ask Interviewers\n\n"
        for category, questions in questions_to_ask.items():
            md += f"### {category.replace('_', ' ').title()}\n\n"
            for q in questions:
                md += f"- {q}\n"
            md += "\n"

        md += "---\n\n## Interview Day Checklist\n\n"
        md += "- [ ] Review company research report\n"
        md += "- [ ] Practice STAR stories (2-minute versions)\n"
        md += "- [ ] Review recent company news/announcements\n"
        md += "- [ ] Prepare 5-7 questions to ask\n"
        md += f"- [ ] Research interviewer backgrounds (LinkedIn)\n"
        md += "- [ ] Set up tech (headphones, camera, quiet space)\n"
        md += "- [ ] Have resume and notes ready\n"
        md += "- [ ] Arrive 5 minutes early\n\n"

        md += "---\n\n*Generated by interview-prep.py*\n"

        return md

    def save_prep_package(self, output_dir: Optional[Path] = None) -> Path:
        """Save prep package to markdown file"""
        if output_dir is None:
            output_dir = Path(__file__).parent

        output_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d")
        filename = f"{self.company.lower().replace(' ', '-')}_interview_prep_{timestamp}.md"
        filepath = output_dir / filename

        content = self.generate_prep_package()
        filepath.write_text(content, encoding='utf-8')

        return filepath

def main():
    if len(sys.argv) < 3:
        print("Usage: python interview-prep.py \"Company\" \"Role\" [\"Interview Date\"]")
        print('Example: python interview-prep.py "Stripe" "Senior Product Manager" "2025-12-15"')
        sys.exit(1)

    company = sys.argv[1]
    role = sys.argv[2]
    interview_date = sys.argv[3] if len(sys.argv) > 3 else None

    print(f"\n📝 Generating interview prep for {company} - {role}...\n")

    generator = InterviewPrepGenerator(company, role, interview_date)
    filepath = generator.save_prep_package()

    print(f"✅ Interview prep package saved to: {filepath}\n")
    print("Next steps:")
    print("1. Review the prep package")
    print("2. Map your STAR stories to required categories")
    print("3. Practice responses out loud")
    print("4. Research your interviewers on LinkedIn")
    print("5. Prepare thoughtful questions to ask\n")

if __name__ == "__main__":
    main()
