# Hybrid Skills + Agents Architecture

**Version:** 1.0.0
**Last Updated:** 2025-11-27
**Status:** Production

## Overview

This is a hybrid architecture that combines **Claude Code Skills** (conversational frameworks) with **autonomous agents** (TypeScript/Python workflows) and **code execution** (data processing) to provide comprehensive life coaching across multiple domains.

### Design Philosophy

1. **Skills provide framework and context** - They know WHEN to act, WHAT framework to apply, and HOW to delegate
2. **Agents execute complex workflows** - Multi-step autonomous processes (company research, journal analysis)
3. **Code handles data operations** - Python scripts for templating, analysis, and data manipulation (95% token savings)
4. **Orchestrator integrates domains** - Meta-skill that routes, synthesizes, and maintains coherence

### Token Efficiency

- **Conversational approach:** ~50,000 tokens to process job search data via MCP
- **Code execution approach:** ~2,500 tokens (95% savings)
- **Hybrid approach:** Strategic conversation + efficient data processing

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    holistic-life-coach                       │
│                   (Meta-Orchestrator)                        │
│                                                              │
│  • Detects domains via domain-map.json                      │
│  • Routes to specialist skills                              │
│  • Runs integration-engine.py for cross-domain analysis     │
│  • Synthesizes insights back to Sam                         │
└──────────────────┬──────────────────────────────────────────┘
                   │
         ┌─────────┴─────────┐
         │                   │
         ▼                   ▼
┌─────────────────┐   ┌──────────────────┐
│ job-search-      │   │ rodbt-coach      │
│ specialist       │   │                  │
│                  │   │                  │
│ • Career strategy│   │ • RO-DBT guidance│
│ • Interview prep │   │ • Pattern work   │
│ • Applications   │   │ • Self-enquiry   │
└────────┬─────────┘   └────────┬─────────┘
         │                      │
    ┌────┴────┐           ┌────┴─────┐
    ▼         ▼           ▼          ▼
┌────────┐ ┌──────┐   ┌──────┐  ┌──────┐
│company-│ │inter-│   │jour- │  │exer- │
│research│ │view- │   │nal-  │  │cise- │
│agent.ts│ │prep  │   │anal- │  │gen   │
│        │ │.py   │   │yzer  │  │.py   │
│TypeSc- │ │Python│   │agent │  │Python│
│ript    │ │      │   │.ts   │  │      │
│Agent   │ │Script│   │Agent │  │Script│
│SDK     │ │      │   │SDK   │  │      │
└────────┘ └──────┘   └──────┘  └──────┘

         DATA LAYER
┌─────────────────────────────────────────┐
│ .claude/skills/data/                    │
│                                         │
│ • rodbt-progress.json                   │
│ • needle-mover-data.json                │
│ • outreach-streak.json                  │
│ • [other tracking files]                │
└─────────────────────────────────────────┘
```

## Domain Structure

### 1. Job Search Specialist
**Location:** `.claude/skills/job-search-specialist/`

**Components:**
- `SKILL.md` - Framework and delegation patterns
- `agents/company-research/agent.ts` - Autonomous company research (TypeScript + Agent SDK)
- `scripts/interview-prep.py` - Interview preparation templating (Python)

**When to Use:**
- Job search strategy, applications, networking
- Interview prep, offer negotiation
- Company research
- Never Search Alone methodology

**Delegation Patterns:**
- **Conversational:** Strategic guidance, framework application
- **Agent (company-research):** Multi-step company intel workflow
- **Script (interview-prep.py):** Template STAR stories and practice questions

**Example:**
```
User: "Research Anthropic thoroughly for my interview"
→ job-search-specialist delegates to company-research agent
→ Agent runs 5-step autonomous workflow
→ Returns comprehensive markdown report with talking points
```

### 2. RODBT Coach
**Location:** `.claude/skills/rodbt-coach/`

**Components:**
- `SKILL.md` - RO-DBT framework and therapeutic guidance
- `agents/journal-analyzer/agent.ts` - Journal analysis for patterns (TypeScript + Agent SDK)
- `scripts/exercise-generator.py` - Exercise plan generation (Python)
- `references/` - Core RO-DBT concepts, patterns, methods
- `data/rodbt-progress.json` - Progress tracking

**When to Use:**
- Overcontrol patterns (withdrawal, perfectionism, avoidance, etc.)
- Emotional processing, relationship dynamics
- RO-DBT practice, edge questions, self-enquiry
- Therapeutic progress tracking

**Delegation Patterns:**
- **Conversational:** Self-enquiry facilitation, edge question generation
- **Agent (journal-analyzer):** Analyze journal entries for patterns
- **Script (exercise-generator.py):** Generate personalized exercise plans

**Example:**
```
User: "Analyze my recent journal entries for patterns"
→ rodbt-coach delegates to journal-analyzer agent
→ Agent analyzes entries from Obsidian vault OR pasted text
→ Returns pattern analysis, emotional arc, edge questions
→ rodbt-coach facilitates discussion of insights
```

### 3. Holistic Life Coach
**Location:** `.claude/skills/holistic-life-coach/`

**Components:**
- `SKILL.md` - Orchestrator logic and integration framework
- `scripts/integration-engine.py` - Cross-domain analysis (Python)
- `config/domain-map.json` - Routing rules and keyword mappings

**When to Use:**
- Cross-domain queries spanning multiple areas
- Life momentum synthesis ("How am I doing overall?")
- Conflicting priorities ("Should I focus on X or Y?")
- Pattern recognition across domains
- Opportunity identification for compounding efforts

**Delegation Patterns:**
- **Conversational:** Values alignment, meta-questions, emotional support
- **Domain routing:** Delegates to job-search-specialist or rodbt-coach based on keywords
- **Code execution:** Runs integration-engine.py for cross-domain analysis

**Integration Engine Modes:**
1. **Synthesis:** Overall momentum across all domains
2. **Priority:** Resolve conflicting priorities
3. **Patterns:** Identify recurring patterns across domains
4. **Opportunities:** Find cross-domain synergies

**Example:**
```
User: "I'm avoiding job applications because I'm afraid of rejection"
→ holistic-life-coach detects: career + emotional_health domains
→ Runs integration-engine.py to analyze pattern intersection
→ Delegates to rodbt-coach for strategic avoidance pattern work
→ Delegates to job-search-specialist for low-friction application tasks
→ Synthesizes: "Treat job outreach as edge question practice"
```

## Usage Examples

### Example 1: Single Domain Query

**User:** "Help me prepare for an interview at Anthropic"

**Flow:**
1. holistic-life-coach detects keywords: "interview", "prepare"
2. domain-map.json routes to: job-search-specialist
3. job-search-specialist recognizes pattern: "Research [Company] thoroughly"
4. Delegates to company-research agent (agent.ts)
5. Agent runs autonomous workflow:
   - Step 1: Company background research
   - Step 2: Role analysis
   - Step 3: Culture assessment
   - Step 4: Competitive landscape
   - Step 5: Synthesize report
6. Returns comprehensive report
7. job-search-specialist then offers interview-prep.py to generate practice questions

**Result:** Company research report + tailored interview prep materials

---

### Example 2: Cross-Domain Query

**User:** "I'm avoiding job applications because I'm afraid of rejection"

**Flow:**
1. holistic-life-coach detects multiple domains:
   - Keywords: "avoiding" (emotional_health), "job applications" (career)
2. Runs integration-engine.py --mode=patterns
3. Identifies pattern: Strategic Avoidance (manifests in career + emotional_health)
4. Synthesizes integrated approach:
   - First: Address avoidance pattern via rodbt-coach
   - Then: Create small brave steps via job-search-specialist
5. Provides edge question: "What if the discomfort is information, not danger?"
6. Suggests: Treat job outreach as edge question practice

**Result:** RO-DBT framework applied to career challenge + actionable job search steps

---

### Example 3: Life Momentum Synthesis

**User:** "How am I doing across all areas of my life?"

**Flow:**
1. holistic-life-coach recognizes synthesis request
2. Runs integration-engine.py --mode=synthesis --domains=all
3. Engine analyzes:
   - Career: Pulls from outreach-streak, job pipeline data
   - Emotional Health: Reads rodbt-progress.json
   - Relationships: Checks carter-rituals tracking
   - Fitness: Could integrate with Strava data
   - Personal Dev: Reviews learning/project progress
4. Calculates momentum scores, balance metrics
5. Identifies cross-domain patterns and opportunities
6. Generates synthesis report

**Result:** Holistic momentum snapshot with actionable insights

---

### Example 4: Conflicting Priorities

**User:** "Should I focus on marathon training or job applications this week?"

**Flow:**
1. holistic-life-coach detects conflicting priorities
2. Runs integration-engine.py --mode=priority --domains=fitness,career
3. Engine scores each domain on:
   - Urgency (job search: high, marathon: medium)
   - Current momentum
   - Integration potential
4. Recommends integrated approach:
   - Morning: Marathon training (energy-giving)
   - Afternoon: 2 job applications (leverage post-run clarity)
5. Identifies opportunity: Post-run mental state for difficult tasks

**Result:** Integrated schedule that maintains momentum in both domains

## Implementation Patterns

### When to Use Conversational Coaching

**Use direct conversational approach when:**
- Strategic guidance and framework application
- Values clarification and identity work
- Quick emotional support
- Celebrating wins
- Meta-questions about life direction

**Example:**
```
User: "I feel stuck in my job search"
Assistant: "Let's explore what 'stuck' means - is this strategic avoidance,
perfectionism blocking action, or something else? [Facilitates self-enquiry]"
```

### When to Use Task Subagents

**Use Agent SDK agents when:**
- Multi-step autonomous workflows
- Research-intensive tasks
- Complex analysis requiring multiple passes
- Self-contained processes with clear output

**Example:**
```
User: "Research Stripe thoroughly"
Assistant: [Launches company-research agent]
Agent autonomously:
1. Researches company background
2. Analyzes role requirements
3. Assesses culture fit
4. Reviews competitive landscape
5. Synthesizes insights
Returns: Comprehensive markdown report
```

### When to Use Code Execution

**Use Python scripts when:**
- Data-intensive operations (95% token savings)
- Templating and data transformation
- Simple workflows without complex decision trees
- Batch processing

**Example:**
```
User: "Generate a practice interview plan"
Assistant: [Runs interview-prep.py]
Script:
1. Loads company research if available
2. Templates STAR story recommendations
3. Generates practice questions
4. Creates talking points
Returns: Formatted interview prep doc
```

### When to Use Integration Engine

**Use integration-engine.py when:**
- Cross-domain analysis needed
- Momentum synthesis across life areas
- Conflicting priority resolution
- Pattern detection across domains
- Opportunity identification

**Example:**
```
User: "I keep avoiding important tasks"
Assistant: [Runs integration-engine.py --mode=patterns]
Engine detects: Strategic avoidance in career + emotional_health + personal_dev
Returns: Pattern manifestations, underlying causes, interventions
```

## File Structure

```
.claude/skills/
├── README.md (this file)
│
├── data/
│   ├── rodbt-progress.json
│   ├── needle-mover-data.json
│   └── [other tracking files]
│
├── job-search-specialist/
│   ├── SKILL.md
│   ├── agents/
│   │   └── company-research/
│   │       ├── agent.ts
│   │       ├── package.json
│   │       └── tsconfig.json
│   └── scripts/
│       └── interview-prep.py
│
├── rodbt-coach/
│   ├── SKILL.md
│   ├── agents/
│   │   └── journal-analyzer/
│   │       ├── agent.ts
│   │       ├── package.json
│   │       └── tsconfig.json
│   ├── scripts/
│   │   └── exercise-generator.py
│   └── references/
│       ├── rodbt-principles.md
│       ├── self-enquiry-method.md
│       └── overcontrol-patterns.md
│
└── holistic-life-coach/
    ├── SKILL.md
    ├── config/
    │   └── domain-map.json
    └── scripts/
        └── integration-engine.py
```

## Running Agents and Scripts

### TypeScript Agents (Agent SDK)

**Setup:**
```bash
cd .claude/skills/[skill-name]/agents/[agent-name]/
npm install  # or pnpm install
```

**Run:**
```bash
# Company Research Agent
tsx .claude/skills/job-search-specialist/agents/company-research/agent.ts \
  --company "Anthropic" \
  --role "Senior Software Engineer"

# Journal Analyzer Agent
tsx .claude/skills/rodbt-coach/agents/journal-analyzer/agent.ts \
  --vault recent

# Or with pasted text:
tsx .claude/skills/rodbt-coach/agents/journal-analyzer/agent.ts \
  --text "Journal entry text here..."
```

### Python Scripts

**Run:**
```bash
# Interview Prep Generator
python .claude/skills/job-search-specialist/scripts/interview-prep.py \
  --company "Anthropic" \
  --role "Senior Software Engineer"

# Exercise Generator
python .claude/skills/rodbt-coach/scripts/exercise-generator.py \
  --patterns "withdrawal,perfectionism" \
  --output exercise-plan.md

# Or interactive mode:
python .claude/skills/rodbt-coach/scripts/exercise-generator.py \
  --interactive

# Integration Engine
python .claude/skills/holistic-life-coach/scripts/integration-engine.py \
  --mode=synthesis \
  --domains=all

python .claude/skills/holistic-life-coach/scripts/integration-engine.py \
  --mode=priority \
  --domains=career,fitness

python .claude/skills/holistic-life-coach/scripts/integration-engine.py \
  --mode=patterns \
  --lookback=30days

python .claude/skills/holistic-life-coach/scripts/integration-engine.py \
  --mode=opportunities
```

## Data Persistence

### rodbt-progress.json
**Location:** `.claude/skills/data/rodbt-progress.json`

**Schema:**
```json
{
  "sessions": [
    {
      "date": "2025-11-27",
      "patterns_identified": ["withdrawal", "perfectionism"],
      "edge_questions_practiced": ["What would happen if I shared hurt?"],
      "insights": "...",
      "progress_notes": "..."
    }
  ],
  "active_edge_questions": [
    {
      "question": "What would happen if I shared hurt instead of retreating?",
      "pattern": "withdrawal",
      "started_date": "2025-11-20",
      "observations": []
    }
  ],
  "core_patterns_tracking": {
    "withdrawal": {
      "first_identified": "2025-11-15",
      "frequency": "recurring",
      "contexts": ["relationship with Carter", "post-rejection in job search"],
      "progress_trend": "improving"
    }
  }
}
```

### Other Tracking Files
- `needle-mover-data.json` - Daily high-impact actions
- `outreach-streak.json` - Job search outreach tracking
- `carter-rituals.json` - Relationship ritual tracking
- (Future) `fitness-data.json` - Marathon training tracking

## Troubleshooting

### Agent Won't Run

**Problem:** TypeScript agent fails to execute

**Solutions:**
1. Ensure dependencies installed: `cd [agent-dir] && npm install`
2. Check ANTHROPIC_API_KEY is set: `echo $ANTHROPIC_API_KEY`
3. Verify tsx is available: `npm install -g tsx` or use `npx tsx`

### Integration Engine Errors

**Problem:** Python script fails

**Solutions:**
1. Check Python version: `python --version` (should be 3.8+)
2. Verify file paths in script match your system
3. Ensure data files exist in `.claude/skills/data/`

### Skills Not Triggering

**Problem:** Specialist skills not being invoked

**Solutions:**
1. Check domain-map.json for keyword matches
2. Verify skill files are in correct locations
3. Review holistic-life-coach SKILL.md delegation logic

## Future Enhancements

### Phase 5: Additional Domains
- **fitness-coach** - Dedicated marathon training guidance
- **financial-coach** - Budget and runway management
- **denver-social-coach** - Local friendship building

### Integration Improvements
- **Real data connections:** Actually read from Strava, Things 3, Google Calendar APIs
- **Automated pattern detection:** ML-based pattern recognition across journal entries
- **Predictive insights:** "Based on patterns, you might struggle with X this week"

### Agent Enhancements
- **job-search-specialist:**
  - salary-negotiation agent
  - resume-optimizer agent

- **rodbt-coach:**
  - progress-visualizer agent
  - pattern-tracker agent

### Code Execution Optimizations
- **Batch operations:** Process multiple tasks in single execution
- **Caching:** Cache frequently accessed data
- **Parallel processing:** Run multiple analyses simultaneously

## Maintenance

### Regular Updates
- **Weekly:** Review and update domain-map.json keywords
- **Monthly:** Update reference files with new RO-DBT insights
- **Quarterly:** Review architecture for optimization opportunities

### Data Hygiene
- **Archive old data:** Move completed sessions to archive files
- **Validate schemas:** Ensure JSON files match expected structure
- **Backup tracking data:** Regular backups of progress files

## Success Metrics

### Token Efficiency
- Target: 90%+ savings on data operations via code execution
- Current: ~95% savings (50k tokens → 2.5k tokens)

### Domain Coverage
- Phase 1: Career ✓
- Phase 2: Emotional Health ✓
- Phase 3: Orchestration ✓
- Future: Fitness, Financial, Social

### User Experience
- Fast response times via efficient routing
- Coherent cross-domain synthesis
- Actionable insights, not just analysis

## Architecture Principles

### 1. Separation of Concerns
- Skills = Framework and context
- Agents = Autonomous workflows
- Scripts = Data processing
- Orchestrator = Integration and routing

### 2. Token Efficiency First
- Use code execution for data-intensive operations
- Reserve conversation for strategic guidance
- Cache and reuse processed results

### 3. Proactive, Not Reactive
- Orchestrator detects patterns before Sam asks
- Skills suggest interventions based on context
- Integration engine surfaces opportunities

### 4. Human-Centric Design
- Celebrate wins across domains
- Hold complexity without oversimplifying
- Ground decisions in Sam's values
- Maintain authentic coaching relationship

---

**Questions or issues?** Update this README or consult individual SKILL.md files for domain-specific guidance.

**Version History:**
- 1.0.0 (2025-11-27): Initial hybrid architecture implementation
