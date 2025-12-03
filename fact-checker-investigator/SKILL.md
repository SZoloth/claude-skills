---
name: fact-checker-investigator
description: Rigorously verify claims, cross-reference sources, and investigate discrepancies in documents. Use before publishing research reports, when conflicting information exists, or when stakes are high and accuracy is critical.
---

# Fact Checker Investigator

## Overview

Systematically verify claims, validate sources, cross-reference data, and investigate discrepancies. Ensure research integrity by distinguishing verified facts from assumptions, interpretations, and fabrications.

## Core Mission

**Never publish unverified claims as facts.**

Protect research integrity by:
- Verifying all quotes have real sources
- Confirming data and metrics are traceable
- Identifying assumptions masquerading as facts
- Cross-referencing conflicting information
- Flagging fabricated or questionable content

## Verification Checklist

### Stakeholder quotes

**Required for every quote:**
- [ ] Source file exists and is accessible
- [ ] Line number is approximately correct (±5 lines acceptable)
- [ ] Quote matches source text (exact or accurate paraphrase)
- [ ] Speaker attribution is correct (name, role)
- [ ] Context preserved (not taken out of context)

**Red flags:**
- Generic quotes without specific sources ("Artists say...")
- Convenient quotes that perfectly support argument
- Attribution to roles without names ("A story artist mentioned...")
- Line numbers that don't exist in cited file

### Data and metrics

**Required for every number:**
- [ ] Source document cited
- [ ] Measurement definition clear (what's being counted, timeframe)
- [ ] Calculation method traceable
- [ ] Context provided (sample size, conditions)

**Red flags:**
- Round numbers without source (40%, "most", "many")
- Precise statistics without methodology
- Comparisons without baseline
- Trend claims without time series data

### Meeting decisions

**Required for every decision:**
- [ ] What was decided (specific, actionable)
- [ ] Who made decision (decision owner by name)
- [ ] When decided (meeting date)
- [ ] Source documented (meeting notes with line number)
- [ ] Rationale captured (why this choice)

**Red flags:**
- Passive voice decisions ("It was decided...")
- Vague outcomes ("Team agreed to explore...")
- Decisions without decision-maker names
- No source documentation

## Investigation Workflow

### 1. Document audit

Read target document and flag all claims:
- Direct quotes
- Data/metrics
- Decisions
- Timelines
- Stakeholder preferences
- Technical specifications

### 2. Source verification

For each flagged claim:
```markdown
**Claim:** [The assertion being made]
**Source cited:** [What document/line is referenced]
**Verification:**
  - [ ] Source file exists
  - [ ] Content matches claim
  - [ ] Context appropriate
**Status:** ✅ Verified | ⚠️ Questionable | ❌ Unverified
**Notes:** [Any discrepancies or concerns]
```

### 3. Cross-reference investigation

When conflicting information exists:
- Identify all sources making competing claims
- Check dates (is one source more recent/authoritative?)
- Examine context (are they talking about same thing?)
- Note uncertainty ("Sources conflict: A says X, B says Y")

### 4. Gap identification

Flag unverified claims:
- **Missing source:** Claim has no citation
- **Inaccessible source:** Citation points to non-existent file
- **Misattribution:** Quote attributed to wrong person
- **Out of context:** Quote meaning distorted
- **Fabrication suspected:** Claim seems invented

### 5. Recommendation

For each issue found:
- **Fix:** If correction is clear (wrong line number, typo)
- **Verify:** If source exists but needs checking
- **Remove:** If claim is unverifiable and non-critical
- **Clarify:** If claim needs "assumption" or "hypothesis" qualifier

## Investigation Script

Use `scripts/verify_citations.py` to automate source checking:
```bash
python scripts/verify_citations.py document.md --check-quotes --check-line-numbers
```

Output:
- List of all quotes with verification status
- Broken citations (non-existent files/lines)
- Suspicious patterns (many quotes from same line, generic attributions)

## Common Scenarios

### Scenario 1: Pre-publication review

**Context:** Research report ready to share with stakeholders

**Process:**
1. Run automated citation checker
2. Manually verify high-impact claims (decisions, recommendations, key data)
3. Flag assumptions that read like facts
4. Request clarification for questionable content
5. Sign off only when critical claims verified

### Scenario 2: Conflicting information

**Context:** Two documents make contradictory claims

**Process:**
1. Identify exact nature of conflict
2. Check source recency (newer may supersede)
3. Check source authority (who's closer to truth?)
4. Document both perspectives if unresolvable
5. Note explicitly: "Sources conflict on this point"

### Scenario 3: Suspicious document

**Context:** Document has markers of fabricated content

**Markers:**
- Too many "perfect" quotes
- Convenient data supporting conclusions
- Generic attributions
- No line numbers or vague citations

**Process:**
1. Flag all suspicious claims
2. Request source verification from author
3. Do not approve until verification provided
4. Consider full document review if multiple issues

## Output: Verification Report

```markdown
# Fact-Check Report: [Document Name]

**Date:** YYYY-MM-DD
**Reviewer:** [Your name]
**Status:** ✅ Approved | ⚠️ Approved with notes | ❌ Revision needed

## Summary
[Overall assessment: strong/weak evidence, major issues found]

## Critical Issues (Must Fix)
1. **[Claim]** - [Issue: fabricated/misattributed/unverified]
   - Location: [File:line]
   - Recommendation: [Fix/Remove/Verify]

## Minor Issues (Should Fix)
[List of non-critical but important corrections]

## Verified Claims (High Confidence)
[Key claims that passed rigorous checking - builds trust]

## Assumptions Flagged
[Claims that should be marked as assumptions/hypotheses, not facts]
```

## Resources

### scripts/
- `verify_citations.py` - Automated citation checking tool

### references/
- `verification-standards.md` - Detailed criteria for different claim types
- `investigation-techniques.md` - Advanced cross-referencing methods

### assets/
- `verification-report-template.md` - Standard report format

## Red Line Principles

**Never compromise on:**
1. Stakeholder quotes must have real, traceable sources
2. Data must cite methodology and source
3. Decisions must name decision-makers
4. Assumptions must be labeled as such
5. Conflicting evidence must be acknowledged

**When in doubt:** Mark as "unverified" and request clarification. Better to delay publication than publish fiction.
