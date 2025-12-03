# Evidence-Based Discovery Standards

Principles and practices for coaching rigorous, evidence-based product discovery.

## Core Principle

**Evidence-based discovery** means distinguishing between:
- What we **observe** (validated evidence)
- What we **think** (hypotheses requiring validation)
- What we **assume** (unvalidated beliefs)

## Evidence Quality Standards

### ✅ Good Evidence

**Observable Behaviors**:
- "User clicked through 3 menu locations before finding import option"
- "Took 4 minutes to complete package submission"
- "Cursed under breath while navigating dialog"

**Verbatim Quotes with Citations**:
- "I always forget where the import button is" (melissa-walkthrough-2025-11-14:23)
- "This is so tedious, I wish it was automatic" (coordinator-interview-03:15)

**Quantified Impact**:
- Time cost: "Adds 3-5 minutes per package"
- Frequency: "Happens 100% of the time"
- Error rate: "Mistakes occur in 30% of submissions"

**Pattern Recognition**:
- "Observed in 4 of 5 sessions"
- "All experienced users mentioned this pain point"

**Source Attribution**:
- Session file and timestamp/line number
- User name and role
- Date of observation

### ❌ Bad Evidence

**Interpretations Presented as Facts**:
- "Users are frustrated" (What did you observe? What did they say?)
- "The workflow is inefficient" (How do you measure that?)

**Vague Descriptions**:
- "Navigation is tedious" (How many clicks? How much time?)
- "This happens often" (How often exactly?)

**Framework Language Users Didn't Say**:
- "Context switching creates cognitive load" (Did user say this?)
- "Mental model mismatch" (User's words or your interpretation?)

**Missing Citations**:
- Claims without sources
- No session references
- Can't verify with original data

**Single-User Generalizations**:
- "Users need X" based on one interview
- Treating outliers as patterns

## Citation Standards

Every insight must be traceable to source:

**Format**: `[session-name]:[location]`

**Examples**:
- `melissa-walkthrough-2025-11-14:23` (line 23 of transcript)
- `coordinator-interview-03:15:30` (timestamp 15:30)
- `observation-session-02:page-5` (page 5 of notes)

## Discovery Methods and Evidence Types

### User Interviews

**Good Practice**:
- "Tell me about the last time you submitted a package"
- Observe while they demonstrate
- Capture verbatim quotes
- Note emotional reactions

**Evidence Produced**:
- User quotes (verbatim)
- Described behaviors (their account)
- Pain points (their language)
- Workarounds discovered

**Limitations**:
- Self-reported (may not match actual behavior)
- Memory bias
- Social desirability

### Think-Aloud Observation

**Good Practice**:
- Watch user work on real task
- Ask them to narrate thinking
- Note hesitations and struggles
- Minimal interviewer intervention

**Evidence Produced**:
- Observable behaviors (actual actions)
- Time measurements
- Click/navigation paths
- Verbal reactions (authentic)

**Strengths**:
- Reveals actual behavior
- Shows unexpected workarounds
- Captures real friction points

### Data Analysis

**Good Practice**:
- Query analytics systems
- Look for behavioral patterns
- Identify drop-off points
- Segment by user type

**Evidence Produced**:
- Usage metrics
- Conversion rates
- Time-on-task measurements
- Feature adoption rates

**Limitations**:
- Shows what, not why
- Correlation ≠ causation
- Requires qualitative validation

## Common Coaching Scenarios

### Scenario 1: Assumption-Based Claims

**What You Hear**:
"Users find this confusing and want it simplified."

**Coaching Response**:
"How do you know that? Which users did you observe? Can you show me the evidence?"

**Teaching Moment**:
Evidence requires observable behavior or quotes. "Confusing" is interpretation. What did you actually see users do or hear them say?

### Scenario 2: Vague Pain Points

**What You See**:
Journey map with pink sticky: "Tedious navigation"

**Coaching Response**:
"Can we make this more specific? How many clicks? How much time does it add? What happens when navigation fails?"

**Teaching Moment**:
Vague descriptions don't guide solutions. Quantify and specify: "8 clicks across 3 screens, adds 2-4 minutes per package."

### Scenario 3: Single-User Generalization

**What You Hear**:
"We interviewed Sarah and she needs feature X, so we should build it."

**Coaching Response**:
"Interesting insight from Sarah. Have we seen this pattern in other users? How do we know this represents a broader need?"

**Teaching Moment**:
Look for patterns across multiple users. One user's need might be an outlier. Validate before generalizing.

### Scenario 4: Framework Language

**What You See**:
Research notes: "Users experience context switching fatigue leading to cognitive overhead."

**Coaching Response**:
"That's good analysis, but what were the user's actual words? Let's separate our interpretation from their language."

**Teaching Moment**:
Users don't say "context switching" - they say "I lost my place" or "I have to remember where I was." Use their language.

### Scenario 5: Building Without Validation

**What You Hear**:
"We think users need this feature, so let's add it to the roadmap."

**Coaching Response**:
"That's a hypothesis worth testing. How can we validate this with users before committing to build?"

**Teaching Moment**:
Discovery validates before delivery. Prototype, test, gather evidence. Then decide whether to build.

## Assumption Flagging

When evidence is missing, explicitly flag assumptions:

### Template

```markdown
### [Claim] (ASSUMPTION - NOT VALIDATED)

**Evidence**: None

**Hypothesis**: [Explain what you believe and why]

**Validation needed**: [How to test this]

**Priority**: [High/Medium/Low]
```

### Example

```markdown
### Users prefer visual preview over text list (ASSUMPTION - NOT VALIDATED)

**Evidence**: None. Based on general UX principles, not user research.

**Hypothesis**: Visual information is easier to scan than text lists, especially for production coordinators managing many assets.

**Validation needed**: A/B test or prototype testing with 4-6 production coordinators comparing visual vs. text interfaces.

**Priority**: Medium - impacts UI design but not core workflow
```

## Pain Point Documentation Structure

### Complete Pain Point Template

```markdown
### Pain Point: [Short descriptive title]

**Observable behavior**:
[What you saw users do that indicates pain]

**User quote**:
"[Verbatim quote]" (source:location)

**Frequency**:
- [ ] Every time (100%)
- [ ] Most times (>75%)
- [ ] Sometimes (25-75%)
- [ ] Rarely (<25%)
- [X] [Specific measurement if available]

**Impact**:
- **Time cost**: [How much time this adds/wastes]
- **Error risk**: [Mistakes caused, how often]
- **Workaround needed**: [External tools/manual steps]
- **Emotional reaction**: [User's words about frustration]

**Evidence citation**: `[session-file:location]`

**Confidence level**:
- [ ] Validated (observed multiple times across users)
- [ ] Strong (observed clearly in this session)
- [ ] Hypothesis (inferred, needs validation)
```

## Opportunity Statement Template

From validated pain points to strategic opportunities:

```markdown
### Opportunity: [Clear problem statement]

**For whom**: [Specific user type/role]

**Evidence**: [Observable pain with citation]

**Frequency**: [How often this occurs]

**Impact**: [Time/error/business cost]

**User quote**: "[Verbatim]" (source:location)

**Current workaround**: [What users do today]

**Strategic value**: [Why this matters beyond tactical pain]

**Confidence**: [Validated/Strong hypothesis/Needs validation]
```

## Pre-Delivery Checklist

Before considering research "complete":

- [ ] Observable behaviors described (not interpretations)
- [ ] User quotes included (verbatim, with citations)
- [ ] Frequency estimated or flagged as unknown
- [ ] Impact quantified (time/errors/workarounds)
- [ ] Sources cited (session file and location)
- [ ] Confidence level indicated
- [ ] Assumptions separated from observations
- [ ] No framework language users didn't use
- [ ] No fabricated details added
- [ ] Patterns identified across multiple users

**Standard**: If you can't cite it, you can't claim it.

## Coaching Questions for Evidence Quality

**Challenge vague claims**:
- "How do you know that?"
- "Which users did you observe?"
- "Can you show me the evidence?"

**Push for specificity**:
- "Can you quantify that?"
- "How often does this happen?"
- "What's the actual impact?"

**Distinguish evidence from interpretation**:
- "Is that what the user said, or your interpretation?"
- "What did you actually observe?"
- "Can you separate the observation from your analysis?"

**Test for patterns**:
- "Have you seen this in other users?"
- "Is this representative or an outlier?"
- "What's the pattern across sessions?"

**Validate before building**:
- "How will you validate this hypothesis?"
- "What's the riskiest assumption here?"
- "What's the cheapest way to test this?"

## Red Flags in Research Documents

Watch for these warning signs:

- **Temporal words without data**: "recently", "often", "frequently"
- **Framework jargon**: "context switching", "mental model", "cognitive load" (unless user said it)
- **Definitive claims**: "Users need X" vs. "Users may need X"
- **Missing citations**: Claims without source references
- **Vague quantification**: "takes a long time" vs. "takes 3-5 minutes"
- **Single-source patterns**: "Users do X" based on one interview
- **Mixed sections**: Assumptions in "Evidence" sections

When you spot these, it's a teaching moment.
