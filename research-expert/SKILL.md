---
name: research-expert
description: Apply Teresa Torres' Continuous Discovery framework and user research methodologies. Design interview protocols, conduct discovery research, and synthesize insights to inform product decisions. Use when planning research studies or conducting stakeholder/user interviews.
---

# Research Expert

## Overview

Execute rigorous user research using Teresa Torres' Continuous Discovery framework. Design effective interview protocols, conduct systematic discovery, and synthesize findings into actionable product insights.

## Core Philosophy: Continuous Discovery

**Principle:** Build continuous learning into product development, not one-off research projects.

**Key practices:**
- Interview customers weekly (minimum)
- Focus on stories, not opinions
- Map opportunities, not features
- Test assumptions systematically
- Involve whole product trio (PM, Designer, Engineer)

Reference `references/continuous-discovery-framework.md` for complete methodology.

## Interview Protocol Design

### Structure for discovery interviews

**Goal:** Understand user context, pain points, and desired outcomes—not validate solutions.

**Framework:**
1. **Context setting** (5 min)
   - Build rapport
   - Explain interview purpose
   - Set expectations (their experience, not our ideas)

2. **Story elicitation** (35 min)
   - Ask about specific recent experiences
   - Dig into context, actions, and outcomes
   - Follow "tell me about a time when..." pattern
   - Avoid hypotheticals

3. **Reflection** (10 min)
   - Broader patterns from their perspective
   - What works well (preserve this!)
   - What they wish existed

4. **Wrap-up** (5 min)
   - Anything we didn't cover?
   - Follow-up consent
   - Thank you

### Good vs Bad Questions

**Good (story-based):**
- "Tell me about the last time you searched for an asset"
- "Walk me through what happened when you couldn't find what you needed"
- "What did you do next?"

**Bad (hypothetical/leading):**
- "Would you use a semantic search feature?"
- "How important is search to you?" (leads to generic "very important")
- "What features do you want?" (gets wishlist, not real needs)

### Follow-up probes

When user mentions pain point:
- "Tell me more about that"
- "What made that frustrating?"
- "How did you work around it?"
- "How often does this happen?"
- "What's the impact when this goes wrong?"

Reference `references/interview-question-bank.md` for situational templates.

## Research Methodologies

### Discovery interviews

**When:** Exploring problem space, understanding workflows

**Format:** 1-on-1, 45-60 min, semi-structured

**Output:** Stories, pain points, context, opportunities

**Frequency:** Weekly for continuous discovery

### Usability testing

**When:** Evaluating solution effectiveness

**Format:** Task-based observation, think-aloud protocol

**Output:** Friction points, confusion moments, success metrics

**Frequency:** Every sprint for in-development features

### Generative research

**When:** Need inspiration, exploring unknown territory

**Format:** Observation, contextual inquiry, diary studies

**Output:** Unexpected insights, unmet needs, workarounds

**Frequency:** Quarterly deep-dives into new areas

### Validation experiments

**When:** Testing specific assumptions

**Format:** Prototypes, landing pages, concierge tests

**Output:** Evidence for/against hypothesis

**Frequency:** As needed for risky decisions

See `references/research-method-selection-guide.md` for choosing appropriate methods.

## Opportunity Mapping (Teresa Torres)

Transform interview findings into opportunity solution trees.

### Opportunity identification

**From interview transcript:**
1. Identify user stories (specific past experiences)
2. Extract pain points and desired outcomes
3. Frame as opportunities ("Users need to..." not "Build feature X")
4. Group related opportunities
5. Prioritize by evidence strength and impact

**Example:**
- **Story:** "Last week I spent 2 hours searching for reference art. I knew we had something similar in another production but couldn't find it."
- **Opportunity:** Help artists discover relevant reference material across productions
- **Not:** Build cross-production search (that's a solution)

Use `/research:identify-opportunities` slash command for systematic extraction.

### Solution exploration

**For each high-priority opportunity:**
- Generate multiple solution approaches (diverge)
- Small experiments to test assumptions
- Compare tradeoffs before committing
- Choose based on evidence, not opinions

## Research Synthesis

Transform raw research into actionable insights:

**Process:**
1. **Aggregate findings** across multiple interviews
2. **Identify patterns** (mentioned by X of Y participants)
3. **Map to outcomes** (business goals, user jobs-to-be-done)
4. **Prioritize** by frequency, severity, and strategic fit
5. **Recommend** next validation steps

Use `assets/research-synthesis-template.md` for structured output.

## Research Operations

### Participant recruiting

**Best practices:**
- Recruit from actual users, not proxies
- Diverse representation (roles, experience levels, productions)
- Screen for recent relevant experience
- Maintain research panel for quick access
- Compensate appropriately

### Session logistics

**Preparation:**
- Interview guide with key questions
- Recording consent and setup
- Note-taker or recording tool
- Backup tech plan

**During:**
- Start recording
- Take timestamped notes
- Follow curiosity, not just script
- Watch for non-verbal cues
- Capture verbatim quotes

**After:**
- Debrief immediately (fresh insights)
- Tag key moments in recording
- Synthesize within 24 hours
- Share highlights with team

### Documentation standards

**All research docs must include:**
- Participant details (role, experience, anonymized)
- Date and format
- Key insights with verbatim quotes and timestamps
- Opportunities identified
- Next validation steps

See `references/research-documentation-standards.md`.

## Common Pitfalls

**Avoid:**
- Asking for features ("What do you want?")
- Hypothetical scenarios ("Would you use...?")
- Leading questions ("Don't you think search is important?")
- Presenting solutions too early
- Research theater (interviewing to confirm decisions already made)
- Analysis paralysis (research without action)

**Instead:**
- Ask about specific past experiences
- Observe actual behavior
- Stay curious and neutral
- Map opportunities before solutions
- Run small experiments quickly
- Build continuous learning rhythm

## Resources

### references/
- `continuous-discovery-framework.md` - Complete Teresa Torres methodology
- `interview-question-bank.md` - Situational question templates
- `research-method-selection-guide.md` - Choose right research approach
- `research-documentation-standards.md` - How to document findings

### assets/
- `interview-guide-template.md` - Standard interview protocol structure
- `research-synthesis-template.md` - Format for summarizing findings
- `consent-form-template.md` - Participant consent language

## Quality Checks

Before concluding research phase:
- [ ] Interviewed diverse participant set (not just friendly adopters)
- [ ] Asked about specific past experiences (not hypotheticals)
- [ ] Captured verbatim quotes with timestamps
- [ ] Identified opportunities (not jumped to solutions)
- [ ] Patterns supported by multiple participants
- [ ] Conflicting evidence acknowledged
- [ ] Clear next validation steps defined
