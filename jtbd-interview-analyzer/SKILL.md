---
name: jtbd-interview-analyzer
description: Analyze JTBD interview transcripts to extract four forces, identify patterns, and synthesize insights. Use when processing interview recordings, transcripts, or notes to understand adoption causality and prepare actionable findings.
---

# JTBD Interview Analyzer

## Overview

Transform raw JTBD interview transcripts into structured insights by extracting the four forces timeline, identifying adoption patterns, and synthesizing findings across multiple interviews.

## When to Use

- Analyzing interview transcripts or recordings
- Extracting four forces from interview notes
- Identifying patterns across 6-10+ interviews
- Synthesizing cross-department adoption insights
- Converting qualitative insights to ODI outcomes

## Individual Interview Analysis

**Extract timeline with four forces:**
1. Identify six stages: First Thought → Passive Looking → Active Looking → Decision → First Use → Ongoing Use
2. For each stage, extract quotes showing Push (pain), Pull (attraction), Anxiety (fear), Habit (inertia)
3. Note dates, people, artifacts, milestones
4. Flag gaps for follow-up

**Classify adoption path:**
- Drip→Trigger: Series of exposures + time wall
- Deep Dive→Unlock: Comprehensive learning + gated step

**Tag trigger type:** Milestone, Outage, Policy, Pilot, Peer proof

**Measure enablement:** Request date → First use date = Enablement lag

## Cross-Interview Pattern Recognition

After 6-10 interviews, identify:

**Common triggers:** What time walls appear repeatedly?
**Shared forces:** Which pains/attractions/fears appear across interviews?
**Role dynamics:** How do doer/decider/TD experiences differ?
**Friction points:** Integration, Discovery, Learning, or Social Proof friction?

## Extraction Techniques

**Find four forces in transcripts:**
- Push: "couldn't," "broken," "too slow," "frustrating," "forced"
- Pull: "hoped," "wanted," "saw," "could finally," "would let me"
- Anxiety: "worried," "risk," "unsure," "what if," "might break"
- Habit: "always done," "comfortable," "would have to learn," "everyone knows"

**Reconstruct timeline:** Look for temporal markers like "first heard in [month]," "decided during [milestone]"

**Verify causality:** Check for "because," "when," "after" - not just coincidence

## Quality Checks

**Interview completeness:**
- All six stages addressed
- Four forces per stage
- Specific dates/people/artifacts
- Time wall identified
- Adoption path classifiable

**Evidence quality:**
- Quotes with specific language
- Citations with source/timestamp
- Numbers from data, not estimates
- No role conflation (doer vs decider)

## Converting to ODI Outcomes

- Push pains → "Minimize/Reduce" statements
- Pull desires → "Increase" statements
- Anxiety concerns → "Reduce risk" statements
- Habit barriers → "Increase compatibility" statements

See `odi-outcome-generator` skill for detailed methodology.

## Resources

### assets/
- `interview-synthesis-template.md` - Individual interview analysis template
- `cross-interview-synthesis-template.md` - Pattern synthesis across interviews
