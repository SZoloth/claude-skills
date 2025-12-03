# BLUF Examples - Before/After Transformations

## Research Report

### Before (Narrative)
Over the past month, we conducted in-depth interviews with 12 story artists across three active productions at DreamWorks. The interviews focused on understanding their daily workflows, pain points, and tool usage patterns. We asked about their reference management processes, collaboration practices, and time allocation. Several common themes emerged across all interviews. Many artists mentioned spending significant time searching for assets. Version control was cited as a source of confusion. Collaboration between teams was described as challenging. Based on this research, our team believes that implementing a collections management system would address many of these challenges and improve workflow efficiency.

### After (BLUF)
**Recommendation:** Implement collections management system for Story department

**Key findings:**
- Artists lose 30-40% of work time to asset search (12 of 12 cited as top pain)
- Version confusion causes estimated 15-20% rework across productions
- Teams duplicate work due to inability to discover existing references

**Next step:** 2-week validation pilot with 5 artists to test semantic search + collections prototype

[Full research synthesis](story-research.md) | [Interview transcripts](transcripts/)

---

## Stakeholder Update

### Before (Chronological)
Last week, our team met with the Previz department to discuss their asset installer workflow. They walked us through their current process, which involves manually copying files from a central repository to local machines. This process takes about 45 minutes per production setup. They also showed us how they currently organize assets using a shelf button system. During our conversation, we learned that the shelf button approach has some limitations - it doesn't handle dependencies well and requires manual updates. After the meeting, we discussed potential improvements with our development team. We think we could automate parts of the installer process and improve the shelf organization. We're planning to prototype something next sprint.

### After (BLUF)
**Status:** Previz installer automation - ready to prototype

**What's changing:**
- Automate asset installation (reduce 45min setup to <5min)
- Add dependency management to shelf organization
- Enable one-click updates for asset changes

**Validated with:** Theo Wilson, Jon Garcia (Previz TDs)

**Next:** 2-week development sprint → pilot with 3 artists → rollout decision

[Technical spec](previz-installer-spec.md) | [User research](previz-discovery.md)

---

## Decision Memo

### Before (Exploratory)
We've been thinking about how to prioritize our roadmap for the next quarter. There are several important initiatives we could work on. The Story department has been asking for collections management for a while now. That seems pretty important. The Previz team also needs installer improvements - that affects a lot of people daily. Then there's the FLO migration project that Charles mentioned. We should probably consider that too. Each of these has different impacts and effort levels. Collections would help 40+ artists but might take 12 weeks. Previz affects 15 artists and could be done in 4 weeks. FLO is a longer-term play with uncertain scope. We need to decide which one to tackle first.

### After (BLUF)
**Decision needed:** Q4 roadmap prioritization
**Deadline:** Oct 25 (to align with sprint planning)

**Recommendation:** Prioritize Previz installer → Collections management → FLO migration

**Rationale:**
- **Previz installer:** 15 artists impacted daily, 4-week effort, high confidence
- **Collections:** 40+ artists impacted, 12-week effort, validated pain
- **FLO migration:** 3 artists, undefined scope, requires more discovery

**Options considered:**
1. **Collections first** (rejected: longer payback, higher risk)
2. **FLO first** (rejected: scope unclear, low artist count)
3. **Previz first** (recommended: quick win builds momentum)

**If approved:** Start Previz sprint Oct 28, Collections discovery in parallel

[Detailed scoring](roadmap-prioritization.md) | [Stakeholder input](charles-1on1.md)

---

## Pattern Summary

**Key BLUF techniques:**
1. **Lead with decision/recommendation/status** - Bury nothing important
2. **Support with 3-5 key points** - Ranked by importance
3. **Link to details** - Full analysis available but not required
4. **Make it scannable** - Headers, bullets, white space
5. **Target 50% reduction** - Half the words, same information
