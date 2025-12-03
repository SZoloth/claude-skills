---
name: avoidance-check
description: Detect strategic avoidance patterns. Use when Sam is unsure if a task is important, questioning priorities, or needs help determining if current activity is prioritization or avoidance. Surfaces the architect-systems-avoid-needle-movers pattern.
---

# Strategic Avoidance Detector

Interactive check to determine if current activity is genuine prioritization or the "architect systems, avoid needle-movers" pattern.

## Purpose

Based on Sam's patterns:
- Scout/Architect mode = comfortable but often avoidance
- Forge/Rogue mode = uncomfortable but usually important

This Skill surfaces avoidance in real-time.

## Data File

Read and write to: `/home/user/llm-context-personal/tools/data/avoidance-check-data.json`

Create if doesn't exist:
```json
{
  "checks": []
}
```

Check entry:
```json
{
  "timestamp": "ISO-8601",
  "activity": "What they were about to do",
  "answers": {
    "discomfort": true,
    "impact": true,
    "mode": "forge",
    "intrinsic": true
  },
  "verdict": "LIKELY AVOIDANCE|LIKELY AUTHENTIC|AMBIGUOUS"
}
```

## Running the Check

Ask these 4 questions about what Sam is about to do:

1. **"What are you about to do?"** (get brief description)

2. **"Does this feel UNCOMFORTABLE?"**
   - Discomfort often signals importance
   - Comfort often signals avoidance

3. **"Will this MOVE THE NEEDLE on a 90-day goal?"**
   - 90-day focus = Job Search
   - High impact vs low impact

4. **"Are you BUILDING/CREATING or RESEARCHING/PLANNING?"**
   - Forge mode = usually important
   - Scout/Architect mode = Sam's avoidance pattern

5. **"Would you still do this if no one ever saw it?"**
   - Intrinsic motivation check

## Scoring

**Avoidance signals** (count these):
- Comfortable (not uncomfortable)
- Low impact (won't move needle)
- Researching/Planning mode
- External motivation only

**Action signals**:
- Uncomfortable
- High impact
- Building/Creating mode
- Intrinsically motivated

## Verdict

- **3-4 avoidance signals**: LIKELY AVOIDANCE
- **3-4 action signals**: LIKELY AUTHENTIC
- **Otherwise**: AMBIGUOUS

## Output Format

```
STRATEGIC AVOIDANCE DETECTOR

Activity: [description]

DIAGNOSTIC:
[+] Uncomfortable = probably important
[!] LOW IMPACT = possible avoidance
[!] PLANNING/RESEARCHING = your avoidance pattern
[+] Intrinsically motivated = authentic

VERDICT: LIKELY AVOIDANCE

This looks like strategic avoidance.
Ask: What am I avoiding by doing this instead?

Needle movers you might be avoiding:
- Send 1 job outreach email
- Build (not plan) 1 app feature
- Message 1 potential Denver friend
- Work on your 2030 vision (deciding, not organizing)
```

## Showing Patterns

When asked to show log/patterns:
1. Show verdict counts
2. Show last 5 checks
3. Help identify recurring patterns

Be direct. Don't soften the verdict.
