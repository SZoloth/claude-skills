# System Archetypes - Common Patterns

System archetypes are recurring structures that produce characteristic behaviors. Recognizing these patterns helps diagnose problems and design interventions.

## 1. Fixes That Fail

**Structure:** Quick fix solves symptom but has delayed unintended consequence that makes problem worse.

**Behavior:** Problem improves temporarily, then gets worse than before.

**Diagram:**
```
Problem → Quick Fix → Problem Reduced (initially)
               ↓
         Unintended Consequence (delayed)
               ↓
         Problem Worse
```

**Example:**
- **Problem:** Bugs in production
- **Quick fix:** Skip code review to ship faster
- **Unintended consequence:** More bugs, technical debt
- **Result:** Even more bugs, even less time for quality

**Intervention:**
- Focus on root cause, not symptom
- Make delayed consequences visible sooner
- Build in time for addressing fundamentals

---

## 2. Shifting the Burden

**Structure:** Symptomatic solution provides quick relief but prevents addressing fundamental solution. Over time, capability to use fundamental solution atrophies.

**Behavior:** System becomes dependent on symptomatic solution.

**Diagram:**
```
Problem Symptom
    ↓
Symptomatic Solution (quick) ← Addictive
    ↓
Symptom Relieved

Fundamental Solution (slow, harder) ← Atrophies over time
```

**Example:**
- **Problem:** Artists can't find assets
- **Symptomatic solution:** Hire dedicated "finder" to search for others
- **Fundamental solution:** Fix search system
- **Result:** Teams become dependent on finder, search never improves, doesn't scale

**Intervention:**
- Invest in fundamental solution even while using symptomatic one
- Set deadline for moving away from workaround
- Make cost of symptomatic solution visible

---

## 3. Tragedy of the Commons

**Structure:** Multiple individuals deplete shared resource for individual gain, destroying resource for all.

**Behavior:** Resource degrades over time despite everyone's short-term rationality.

**Diagram:**
```
Shared Resource (codebase quality, shared tool, network bandwidth)
    ↑↓
Individual withdrawals for personal benefit
    ↓
Resource degrades
    ↓
Everyone suffers
```

**Example:**
- **Shared resource:** Codebase quality
- **Individual action:** Each team adds hacky code to meet their deadline
- **Result:** Codebase becomes unmaintainable, slows everyone down

**Intervention:**
- Make resource health visible to all
- Create rules that limit individual impact
- Assign stewardship/ownership
- Align individual incentives with collective good

---

## 4. Drift to Low Performance (Eroding Goals)

**Structure:** When performance falls below goal, instead of improving performance, goal is lowered to match performance.

**Behavior:** Gradual decline in standards and performance.

**Diagram:**
```
Goal → Gap → Action to Close Gap
 ↓
Performance falls
 ↓
Lower goal (instead of improving performance)
 ↓
New, lower baseline
```

**Example:**
- **Start:** Ship features with <5% bug rate
- **Reality:** Features shipping with 15% bug rate
- **Response:** "15% is the new normal"
- **Result:** Quality standards erode, bar keeps lowering

**Intervention:**
- Hold the standard firm
- Make gap visible and painful
- Celebrate improvements, not lowered expectations
- Provide resources to actually close gap

---

## 5. Success to the Successful

**Structure:** Winner of competition gains advantage, ensuring continued winning. Loser's disadvantage compounds.

**Behavior:** Rich get richer, poor get poorer. Dominance increases over time.

**Diagram:**
```
Resource Pool
    ↓
Winner gets more resources → More success → More resources
Loser gets fewer resources → Less success → Fewer resources
```

**Example:**
- **Product A:** Gets users, gets features, gets more users
- **Product B:** Loses users, loses funding, loses more users
- **Result:** Winner-take-all dynamics

**Intervention:**
- Level playing field periodically
- Provide safety net for losers
- Rotate resources
- Recognize when to cut losses vs double down

---

## 6. Limits to Growth

**Structure:** Growth process creates success, which eventually hits a limiting constraint.

**Behavior:** Initial exponential growth, then plateau or decline.

**Diagram:**
```
Reinforcing Growth Loop → Success
    ↓
Hits Limiting Factor
    ↓
Balancing Loop Slows Growth
    ↓
Plateau or Decline
```

**Example:**
- **Growth:** Feature adoption increasing
- **Limit:** Only works for small datasets
- **Result:** Growth stops when users hit scale limit

**Intervention:**
- Identify the constraint early
- Address constraint before it hits
- Look for next constraint after removing current one
- Sometimes: Accept limit and shift focus

---

## 7. Escalation

**Structure:** Two parties compete, each responding to other's actions by intensifying own actions.

**Behavior:** Mutually reinforcing competition spirals out of control.

**Diagram:**
```
Party A's Action → Threat to Party B → Party B's Counter-action
    ↓                                           ↓
Escalation                               Escalation
```

**Example:**
- **Team A:** Builds workaround for shared tool
- **Team B:** Sees workaround, builds their own different workaround
- **Result:** Fragmentation, incompatibility, wasted effort

**Intervention:**
- Unilateral de-escalation
- Negotiate shared standards
- Create shared goals that require cooperation
- Make escalation costs visible

---

## 8. Accidental Adversaries

**Structure:** Partners become competitors due to misalignment or poor communication.

**Behavior:** Actions meant to help oneself inadvertently harm partner, triggering retaliation.

**Diagram:**
```
Party A's Action (intended to help self)
    ↓
Harms Party B
    ↓
Party B's Retaliation
    ↓
Harms Party A
```

**Example:**
- **Product team:** Builds feature quickly
- **Infrastructure team:** Gets paged at night due to poor scaling
- **Infrastructure:** Blocks future deploys
- **Product:** Works around infrastructure
- **Result:** Teams at odds despite shared company goals

**Intervention:**
- Make each party's constraints visible to other
- Create shared success metrics
- Involve each in other's planning
- Build trust through joint problem-solving

---

## Using Archetypes for Diagnosis

### When you notice:
- **Same problem recurring** → Fixes That Fail
- **Growing dependence on workarounds** → Shifting the Burden
- **Shared resource degrading** → Tragedy of the Commons
- **Standards slipping** → Drift to Low Performance
- **Dominant player crushing others** → Success to the Successful
- **Growth suddenly stopping** → Limits to Growth
- **Arms race between teams** → Escalation
- **Allies becoming enemies** → Accidental Adversaries

### Questions to ask:
1. What's the recurring pattern?
2. What reinforcing loops are amplifying problems?
3. What balancing loops are resisting solutions?
4. Where are the delays hiding consequences?
5. What information is invisible that should be visible?
6. What rules or incentives drive unwanted behavior?

### Design better systems:
- Make feedback loops explicit
- Reduce delays between action and consequence
- Align individual and collective incentives
- Build in periodic reflection and adjustment
- Create transparency around shared resources
- Establish clear ownership and accountability
