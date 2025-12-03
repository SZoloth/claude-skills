# Citation Standards

## Why Citations Matter

**Research integrity:** Citations enable verification of claims and prevent fabrication.
**Traceability:** Readers can check original context and assess interpretation quality.
**Accountability:** Clear sources distinguish verified research from analysis.

## Citation Format

### Stakeholder quotes

**Format:** `filename:line` after quote

**Example:**
> "Artists spend 30-40% of their time just searching for the right asset version."
> — Heidi Gilbert, Story TD (heidi-gilbert-interview-2025-07-15.md:127)

**Required elements:**
- Exact quote in quotation marks
- Speaker name and role
- Source file with line number

### Data and metrics

**Format:** Inline citation immediately after claim

**Example:**
The Story department manages over 500TB of reference imagery across 12 active productions (charles-adams-architecture-review.md:89).

**Required elements:**
- Specific numbers (not "lots" or "many")
- Source file with line number
- Context (what was being measured, when)

### Meeting decisions

**Format:** Decision + context + citation

**Example:**
**Decision:** Prioritize Previz installer workflow over FLO migration
**Rationale:** Installer impacts 15 artists daily vs 3 for FLO
**Decided by:** Charles Adams, Product Owner
**Source:** product-prioritization-meeting-2025-10-01.md:156

**Required elements:**
- What was decided
- Why (rationale)
- Who made the decision
- When/where documented

## Verification Checklist

Before publishing document with citations:
- [ ] Every quote has filename:line citation
- [ ] All data/metrics cite source documents
- [ ] Stakeholder names and roles are accurate
- [ ] File citations point to real files (not fabricated)
- [ ] Line numbers are approximately correct (±5 lines acceptable)
- [ ] Decisions attributed to correct decision-maker

## Common Mistakes

### ❌ Fabricated quotes
**Bad:**
> "We need better search capabilities." — Generic Artist

**Good:**
> "I waste hours every week searching through folders. We need semantic search, not just filename matching."
> — Heidi Gilbert (heidi-interview.md:142)

### ❌ Unsourced metrics
**Bad:**
Artists spend a lot of time searching for assets.

**Good:**
Artists spend 30-40% of their time searching for assets (heidi-interview.md:127).

### ❌ Vague attribution
**Bad:**
Stakeholders want collections management.

**Good:**
Story department leads (Heidi Gilbert, Doug Johnson) prioritized collections management as their #1 workflow pain point (story-synthesis.md:23).

## When Context is Missing

If you don't have a source:
- **Option 1:** Mark as assumption/hypothesis: "Hypothesis: Artists may prefer visual search over text search (not validated)"
- **Option 2:** Note the gap: "Need to validate: Do artists actually use collections this way?"
- **Option 3:** Ask for source: "Can you point me to where this was mentioned?"

**Never fabricate citations to fill gaps.**
