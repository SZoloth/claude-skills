# Job Search Specialist - Hybrid Skills + Subagents

This skill combines three execution patterns for maximum flexibility and efficiency.

## Phase 1: Complete ✅

**What was built:**
1. **Delegation Patterns** documented in SKILL.md
2. **company-research agent** (TypeScript/Agent SDK) for autonomous deep research
3. **interview-prep.py** (Python script) for templating prep materials
4. **README documentation** (this file)

## Quick Start

### Run Company Research
```bash
cd agents/company-research
npx tsx agent.ts "Stripe" "Senior Product Manager"
```

### Generate Interview Prep
```bash
cd scripts
python3 interview-prep.py "Stripe" "Senior PM" "2025-12-15"
```

### Use Existing Orchestrator
```bash
cd "/Users/samuelz/ObsidianVaults/LLM CONTEXT/PERSONAL/job_search"
python job_search_orchestrator.py track
```

## Execution Patterns

### 🗣️ Conversational Coaching
Ask strategic questions in conversation - no tools needed

### 🤖 Autonomous Agents (NEW)
Complex multi-step research workflows

### 💻 Python Scripts (NEW)
Simple templating and data formatting

### 🔄 Python Orchestrator (EXISTING)
Proven automation for applications and pipeline

## Testing

Both new tools are installed and working:
- ✅ company-research agent shows usage message
- ✅ interview-prep script shows usage message
- ✅ Existing orchestrator is intact

Try them with real companies when you're ready!

## Next: Phase 2

- RODBT Coach skill (therapy domain)
- Holistic Life Coach orchestrator
- Cross-domain synthesis

See the full plan at: `/Users/samuelz/.claude/plans/vectorized-wibbling-lecun.md`
