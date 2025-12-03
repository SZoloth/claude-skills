---
name: documentation-manager
description: Maintain project continuity by organizing research insights and generating structured documentation. Use proactively when organizing research findings, updating handoff documents, or creating comprehensive project documentation with consistent structure.
---

# Documentation Manager

## Overview

Maintain project continuity and knowledge management through structured documentation. Transform scattered research, meeting notes, and insights into organized, actionable documentation that supports team handoffs and decision-making.

## Core Capabilities

### 1. Handoff documentation

Maintain current project state documentation that enables seamless handoffs:
- Synthesize recent work into "what's done" and "what's next"
- Capture critical context (stakeholder decisions, blockers, open questions)
- Structure for quick consumption (2-minute skim target)
- Link to supporting materials (research docs, meeting notes, JIRA tickets)

Use the handoff template in `assets/handoff-template.md` as starting structure.

### 2. Research organization

Transform raw research into structured insights:
- Extract key findings from interview transcripts and meeting notes
- Group related insights across multiple sources
- Tag by department, stakeholder, or theme
- Create synthesis documents that connect patterns

Reference `references/synthesis-framework.md` for systematic synthesis approaches.

### 3. Progress tracking

Document ongoing work and decisions:
- Update project logs with new milestones and learnings
- Track decision rationale (what was decided, why, by whom)
- Capture blockers and risk factors
- Link outcomes to original assumptions

Use templates in `assets/` for consistent formatting.

### 4. Documentation structure

Maintain consistent organization:
- Apply function-based directory hierarchies
- Use clear naming conventions (ISO dates, descriptive titles)
- Cross-reference related documents
- Archive deprecated materials appropriately

See `references/structure-guidelines.md` for organizing principles.

## When to Use This Skill

Trigger documentation-manager when:
- Finishing a phase of work that requires handoff documentation
- Multiple research documents need synthesis into cohesive insights
- Project status is unclear and stakeholders need current state
- Research is scattered and difficult to navigate
- Creating new documentation that should follow team patterns

## Workflow

### Creating handoff documentation

1. **Gather context**: Read recent work (last 1-2 weeks of commits, meeting notes, completed tasks)
2. **Synthesize accomplishments**: What was delivered? What changed?
3. **Identify next steps**: What's blocked? What needs decisions?
4. **Capture context**: What would a new person need to know?
5. **Draft using template**: Use `assets/handoff-template.md` structure
6. **Link supporting docs**: Reference research, tickets, meeting notes

### Organizing research insights

1. **Scan existing research**: Use Grep to find related themes across docs
2. **Extract key quotes/findings**: Pull specific evidence with file citations
3. **Group by pattern**: Cluster related insights (by department, pain point, opportunity)
4. **Create synthesis**: Write structured document connecting patterns
5. **Update index**: Ensure new doc is discoverable via INDEX.md

### Updating project logs

1. **Review recent activity**: Check commits, closed tickets, completed milestones
2. **Document wins**: What worked well? What was learned?
3. **Capture decisions**: What choices were made? What alternatives were considered?
4. **Note risks/blockers**: What slowed progress? What's uncertain?
5. **Update regularly**: Weekly cadence keeps context fresh

## Resources

### references/
- `synthesis-framework.md` - Systematic approaches for research synthesis
- `structure-guidelines.md` - Function-based organization principles
- `citation-standards.md` - How to cite sources properly

### assets/
- `handoff-template.md` - Standard template for project handoff docs
- `project-log-template.md` - Template for tracking decisions and progress
- `synthesis-template.md` - Template for research synthesis documents

## Output Standards

Documentation produced should:
- **Be scannable**: Headers, bullets, concise language (2-minute skim target)
- **Include citations**: All quotes and data must cite sources (file:line)
- **Link to evidence**: Reference supporting materials (transcripts, tickets, research)
- **Separate fact from interpretation**: Clearly distinguish verified research from analysis
- **Use consistent structure**: Follow templates and organizational patterns
