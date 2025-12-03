# Documentation Structure Guidelines

## Function-Based Organization

Organize by what the content does (function), not when it was created (chronology).

### Directory Hierarchy

**Good examples:**
```
02-departments/story/research/      # Function: research about Story dept
03-strategy/product-strategy/       # Function: strategic planning
04-product-development/jira-tickets/  # Function: development tickets
```

**Avoid:**
```
july-2024/                          # Time-based (hard to find)
misc/                               # Generic (no clear function)
notes/                              # Too vague (notes about what?)
```

### Naming Conventions

**Files:**
- Use ISO dates for temporal docs: `2025-10-21-stakeholder-interview-heidi.md`
- Use descriptive names for evergreen docs: `lasso-architecture-overview.md`
- Separate words with hyphens, not underscores or spaces

**Directories:**
- Lowercase with hyphens: `final-layout/` not `Final_Layout/` or `FinalLayout/`
- Plural for collections: `meeting-notes/` not `meeting-note/`
- Function-focused: `discovery/` not `stuff/`

## Cross-Referencing

Link related documents explicitly:
```markdown
Related research: See [Heidi Gilbert interview](../transcripts/2025-07-15-heidi-interview.md:42)
Follow-up: [Story workflow analysis](story-workflow-synthesis.md)
```

Benefits:
- Enables navigation between related materials
- Provides context breadcrumbs
- Makes citations traceable

## Index Maintenance

Keep `INDEX.md` files current in major directories:
- List key documents with one-line descriptions
- Group by sub-function or topic
- Update when adding significant new content
- Reference from parent directory's index

Example:
```markdown
# 02-departments/story/INDEX.md

## Research
- `discovery/collections-pain-points.md` - Analysis of current collections workflow challenges
- `discovery/heidi-gilbert-interview.md` - July 2025 interview with Story TD

## Product Development
- `requirements/collections-manager-v1.md` - Requirements for collections management feature
```

## Archiving

Move superseded content to `99-archive/`:
- Include original date in archived filename
- Add note explaining why archived and what replaced it
- Keep directory structure in archive: `99-archive/02-departments/story/old-research.md`

Example archive note:
```markdown
> **Archived:** 2025-10-21
> **Reason:** Superseded by [updated synthesis](../../02-departments/story/discovery/collections-synthesis-v2.md)
> **Historical value:** Initial assumptions before validation pilot
```

## Document Headers

Start documents with clear metadata:
```markdown
# Document Title

**Date:** 2025-10-21
**Author:** Sam
**Status:** Draft | Active | Archived
**Related:** [Link to related doc]

Brief (1-2 sentence) summary of what this document contains.
```

Benefits:
- Provides context without reading full doc
- Establishes provenance and currency
- Enables quick assessment of relevance
