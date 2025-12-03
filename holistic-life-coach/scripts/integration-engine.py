#!/usr/bin/env python3
"""
Integration Engine - Cross-Domain Life Analysis

Analyzes patterns, momentum, and opportunities across multiple life domains
to provide holistic insights for the holistic-life-coach skill.

Modes:
- synthesis: Overall momentum analysis across all domains
- priority: Resolve conflicting priorities between domains
- patterns: Identify recurring patterns across domains
- opportunities: Find cross-domain synergies

Usage:
    python integration-engine.py --mode=synthesis --domains=all
    python integration-engine.py --mode=priority --domains=career,fitness
    python integration-engine.py --mode=patterns --lookback=30days
    python integration-engine.py --mode=opportunities
"""

import json
import argparse
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime, timedelta
from dataclasses import dataclass, asdict


@dataclass
class DomainMomentum:
    """Momentum metrics for a life domain"""
    domain: str
    score: float  # 0-10 scale
    trend: str  # 'up', 'down', 'stable'
    recent_wins: List[str]
    current_challenges: List[str]
    next_actions: List[str]
    energy_level: str  # 'high', 'medium', 'low'


@dataclass
class CrossDomainPattern:
    """Pattern that manifests across multiple domains"""
    pattern_name: str
    domains: List[str]
    manifestations: Dict[str, str]
    underlying_cause: str
    recommended_intervention: str


@dataclass
class CrossDomainOpportunity:
    """Opportunity to leverage one domain to support another"""
    title: str
    primary_domain: str
    supporting_domains: List[str]
    description: str
    action_steps: List[str]
    potential_impact: str  # 'high', 'medium', 'low'


class IntegrationEngine:
    def __init__(self):
        self.data_dir = Path.home() / "Documents/LLM CONTEXT/.claude/skills/data"
        self.skills_dir = Path.home() / "Documents/LLM CONTEXT/.claude/skills"

    def run_synthesis(self, domains: List[str] = None) -> Dict:
        """Analyze overall momentum across all or specified domains"""

        if domains is None or domains == ['all']:
            domains = ['career', 'emotional_health', 'relationships', 'fitness', 'personal_dev']

        momentum_analysis = {}

        for domain in domains:
            momentum_analysis[domain] = self._analyze_domain_momentum(domain)

        # Calculate overall life momentum
        overall_score = sum(m.score for m in momentum_analysis.values()) / len(momentum_analysis)

        # Identify domain balance
        scores = [m.score for m in momentum_analysis.values()]
        balance_metric = min(scores) / max(scores) if max(scores) > 0 else 0  # 1.0 = perfect balance

        return {
            "generated_at": datetime.now().isoformat(),
            "mode": "synthesis",
            "domains_analyzed": domains,
            "overall_momentum": {
                "score": round(overall_score, 1),
                "balance": round(balance_metric, 2),
                "interpretation": self._interpret_momentum(overall_score, balance_metric)
            },
            "domain_details": {k: asdict(v) for k, v in momentum_analysis.items()},
            "cross_domain_insights": self._generate_synthesis_insights(momentum_analysis),
            "recommended_focus": self._recommend_focus_areas(momentum_analysis)
        }

    def run_priority_analysis(self, domains: List[str]) -> Dict:
        """Help resolve conflicting priorities between domains"""

        if len(domains) < 2:
            return {"error": "Priority analysis requires at least 2 domains"}

        domain_data = {}
        for domain in domains:
            domain_data[domain] = {
                "momentum": self._analyze_domain_momentum(domain),
                "urgency": self._assess_urgency(domain),
                "energy_cost": self._estimate_energy_cost(domain),
                "integration_potential": self._assess_integration_potential(domain, domains)
            }

        # Generate recommendation
        recommendation = self._generate_priority_recommendation(domain_data)

        return {
            "generated_at": datetime.now().isoformat(),
            "mode": "priority",
            "competing_domains": domains,
            "domain_analysis": domain_data,
            "recommendation": recommendation,
            "integration_opportunities": self._find_integration_opportunities(domains)
        }

    def run_pattern_detection(self, lookback_days: int = 30) -> Dict:
        """Identify recurring patterns across domains"""

        patterns = []

        # Check for strategic avoidance pattern
        if self._detect_strategic_avoidance():
            patterns.append(CrossDomainPattern(
                pattern_name="Strategic Avoidance",
                domains=["career", "emotional_health", "relationships"],
                manifestations={
                    "career": "Optimizing resume instead of sending applications",
                    "emotional_health": "Creating elaborate systems instead of practicing edge questions",
                    "relationships": "Planning perfect date instead of having vulnerable conversation"
                },
                underlying_cause="Using high-control activities to avoid uncomfortable uncertainty",
                recommended_intervention="Practice 'small brave steps' across all domains. Set 5-minute timers for avoided tasks."
            ))

        # Check for perfectionism pattern
        if self._detect_perfectionism():
            patterns.append(CrossDomainPattern(
                pattern_name="Perfectionism",
                domains=["career", "fitness", "personal_dev"],
                manifestations={
                    "career": "Over-preparing for interviews, delaying applications until 'perfect'",
                    "fitness": "Rigid training plans, frustration with imperfect workouts",
                    "personal_dev": "Analysis paralysis in learning, won't start until 'ready'"
                },
                underlying_cause="Belief that imperfection leads to rejection or failure",
                recommended_intervention="Practice 'good enough' threshold. Celebrate imperfect action over perfect inaction."
            ))

        # Check for withdrawal pattern
        if self._detect_withdrawal():
            patterns.append(CrossDomainPattern(
                pattern_name="Withdrawal When Hurt",
                domains=["relationships", "career", "emotional_health"],
                manifestations={
                    "relationships": "Going silent with Carter when feeling unappreciated",
                    "career": "Disengaging after rejection, avoiding networking",
                    "emotional_health": "Isolating instead of reaching out for support"
                },
                underlying_cause="Protecting vulnerability by creating distance",
                recommended_intervention="Practice opposite action: reach out when hurt. Use 'I' statements to share impact."
            ))

        return {
            "generated_at": datetime.now().isoformat(),
            "mode": "patterns",
            "lookback_days": lookback_days,
            "patterns_detected": [asdict(p) for p in patterns],
            "pattern_count": len(patterns),
            "actionable_interventions": [p.recommended_intervention for p in patterns]
        }

    def run_opportunity_scan(self) -> Dict:
        """Find opportunities to leverage one domain to support another"""

        opportunities = []

        # Check for Denver marathon + friendship building
        opportunities.append(CrossDomainOpportunity(
            title="Marathon Training as Social Connection",
            primary_domain="fitness",
            supporting_domains=["relationships", "emotional_health"],
            description="Join Denver running groups to simultaneously train for marathon AND build local friendships",
            action_steps=[
                "Research Denver running clubs (Fleet Feet, Denver Running Club)",
                "Attend one group run this week",
                "Practice vulnerability: share you're new to Denver",
                "Track: Does social running improve training consistency?"
            ],
            potential_impact="high"
        ))

        # Check for job search + edge question practice
        opportunities.append(CrossDomainOpportunity(
            title="Job Outreach as Edge Question Practice",
            primary_domain="career",
            supporting_domains=["emotional_health"],
            description="Treat job applications as opportunities to practice overcontrol interventions",
            action_steps=[
                "Frame each application as 'practice being imperfect'",
                "Send applications without excessive polishing (edge question practice)",
                "Notice withdrawal urge after rejections, practice opposite action",
                "Log to rodbt-progress.json: connection between job search and growth"
            ],
            potential_impact="high"
        ))

        # Check for relationship vulnerability + professional authenticity
        opportunities.append(CrossDomainOpportunity(
            title="Relationship Vulnerability → Interview Authenticity",
            primary_domain="relationships",
            supporting_domains=["career", "emotional_health"],
            description="Vulnerability practice with Carter builds capacity for authentic interview presence",
            action_steps=[
                "Notice: When you're authentic with Carter, interviews feel easier",
                "Practice self-disclosure in relationship → transfers to interview storytelling",
                "Track the connection in journal entries",
                "Celebrate: 'My relationship work is making me a better interviewee'"
            ],
            potential_impact="medium"
        ))

        # Post-run clarity for job applications
        opportunities.append(CrossDomainOpportunity(
            title="Post-Run State for Difficult Tasks",
            primary_domain="fitness",
            supporting_domains=["career", "emotional_health"],
            description="Leverage post-run mental clarity and reduced anxiety for challenging work",
            action_steps=[
                "Schedule job applications for post-morning run",
                "Use post-run state for difficult conversations",
                "Notice: Does physical exhaustion reduce overthinking?",
                "Optimize schedule: Hard tasks when energy is right"
            ],
            potential_impact="medium"
        ))

        return {
            "generated_at": datetime.now().isoformat(),
            "mode": "opportunities",
            "opportunities_found": [asdict(o) for o in opportunities],
            "high_impact": [o.title for o in opportunities if o.potential_impact == "high"],
            "recommended_next_step": opportunities[0].action_steps[0] if opportunities else None
        }

    # ============================================================================
    # DOMAIN-SPECIFIC ANALYSIS HELPERS
    # ============================================================================

    def _analyze_domain_momentum(self, domain: str) -> DomainMomentum:
        """Analyze momentum for a specific domain"""

        # In real implementation, would read from actual tracking systems
        # For now, return structured analysis

        domain_configs = {
            "career": {
                "score": 7.0,
                "trend": "up",
                "recent_wins": ["5 applications sent this week", "Company research workflow established"],
                "current_challenges": ["Interview anxiety", "Avoiding networking"],
                "next_actions": ["Research 2 target companies", "Practice STAR stories", "Reach out to 1 Denver connection"],
                "energy_level": "medium"
            },
            "emotional_health": {
                "score": 6.5,
                "trend": "up",
                "recent_wins": ["Consistent edge question practice", "Journal analysis completed"],
                "current_challenges": ["Withdrawal pattern with Carter", "Strategic avoidance of difficult conversations"],
                "next_actions": ["Practice self-disclosure this week", "Share hurt instead of retreating", "Log to rodbt-progress.json"],
                "energy_level": "medium"
            },
            "relationships": {
                "score": 7.5,
                "trend": "stable",
                "recent_wins": ["Weekly date night maintained", "Flowers ritual consistent"],
                "current_challenges": ["Low self-disclosure", "Zero local Denver friends"],
                "next_actions": ["Attend Denver social event", "Practice vulnerability with Carter", "Join running group"],
                "energy_level": "high"
            },
            "fitness": {
                "score": 8.0,
                "trend": "stable",
                "recent_wins": ["Marathon training on track", "Consistent running schedule"],
                "current_challenges": ["Perfectionism about workouts", "Not using fitness for social connection"],
                "next_actions": ["Join group run", "Practice 'good enough' workout", "Track recovery"],
                "energy_level": "high"
            },
            "personal_dev": {
                "score": 6.0,
                "trend": "stable",
                "recent_wins": ["RO-DBT learning progressing", "Skills architecture improving"],
                "current_challenges": ["Strategic avoidance of deep work", "Analysis over action"],
                "next_actions": ["Complete one avoided project", "Practice time-boxed decisions", "Celebrate imperfect progress"],
                "energy_level": "low"
            }
        }

        config = domain_configs.get(domain, {
            "score": 5.0,
            "trend": "stable",
            "recent_wins": [],
            "current_challenges": ["Data not available"],
            "next_actions": ["Set up tracking for this domain"],
            "energy_level": "medium"
        })

        return DomainMomentum(domain=domain, **config)

    def _assess_urgency(self, domain: str) -> Dict:
        """Assess urgency of work in a domain"""

        urgency_map = {
            "career": {
                "level": "high",
                "reason": "Job search active, runway timeline matters",
                "timeline": "Applications should go out weekly"
            },
            "emotional_health": {
                "level": "medium",
                "reason": "Foundational work, compounds over time",
                "timeline": "Consistent practice more important than intensity"
            },
            "relationships": {
                "level": "medium",
                "reason": "Maintenance and growth both matter",
                "timeline": "Weekly rituals + ongoing practice"
            },
            "fitness": {
                "level": "medium",
                "reason": "Marathon date approaching but training on track",
                "timeline": "Follow training plan, don't skip weeks"
            },
            "personal_dev": {
                "level": "low",
                "reason": "Important but not time-sensitive",
                "timeline": "Opportunistic learning, no pressure"
            }
        }

        return urgency_map.get(domain, {"level": "unknown", "reason": "Domain not mapped", "timeline": "TBD"})

    def _estimate_energy_cost(self, domain: str) -> str:
        """Estimate energy cost of work in domain"""

        energy_costs = {
            "career": "high",  # Emotionally draining, anxiety-producing
            "emotional_health": "medium",  # Challenging but energizing when done
            "relationships": "low",  # Generally energizing
            "fitness": "medium",  # Physical cost, but mental energy gain
            "personal_dev": "medium"  # Depends on task
        }

        return energy_costs.get(domain, "medium")

    def _assess_integration_potential(self, domain: str, all_domains: List[str]) -> str:
        """How well can this domain integrate with others?"""

        # High integration potential domains can support multiple others
        integration_scores = {
            "fitness": "high",  # Can support emotional health, relationships, career
            "emotional_health": "high",  # Foundational for all others
            "relationships": "medium",  # Can support emotional health, career
            "career": "low",  # Mostly independent focus
            "personal_dev": "medium"  # Can support multiple areas
        }

        return integration_scores.get(domain, "low")

    # ============================================================================
    # PATTERN DETECTION
    # ============================================================================

    def _detect_strategic_avoidance(self) -> bool:
        """Detect if strategic avoidance pattern is active"""
        # In real implementation, would check:
        # - Recent needle-mover data (systems work vs. scary actions)
        # - Journal entries for avoidance keywords
        # - Task completion patterns (easy tasks done, hard ones postponed)
        return True  # Placeholder

    def _detect_perfectionism(self) -> bool:
        """Detect if perfectionism pattern is active"""
        # In real implementation, would check:
        # - Application send delays
        # - Over-preparation for interviews
        # - Rigid fitness/training adherence
        return True  # Placeholder

    def _detect_withdrawal(self) -> bool:
        """Detect if withdrawal pattern is active"""
        # In real implementation, would check:
        # - Journal entries about hurt feelings
        # - Relationship ritual tracking
        # - Communication gaps
        return True  # Placeholder

    # ============================================================================
    # SYNTHESIS AND RECOMMENDATIONS
    # ============================================================================

    def _interpret_momentum(self, score: float, balance: float) -> str:
        """Interpret overall momentum and balance"""

        if score >= 8 and balance >= 0.8:
            return "Strong momentum across all domains with excellent balance"
        elif score >= 7 and balance >= 0.7:
            return "Good momentum with solid balance - maintain consistency"
        elif score >= 6 and balance < 0.6:
            return "Moderate momentum but uneven - some domains need attention"
        elif score < 6:
            return "Lower momentum - identify quick wins to build energy"
        else:
            return "Mixed momentum - focus on areas with highest leverage"

    def _generate_synthesis_insights(self, momentum: Dict[str, DomainMomentum]) -> List[str]:
        """Generate cross-domain insights from momentum analysis"""

        insights = []

        # Check for high-performing domains
        high_performers = [d for d, m in momentum.items() if m.score >= 7.5]
        if high_performers:
            insights.append(f"High momentum in {', '.join(high_performers)} - leverage these to support other areas")

        # Check for struggling domains
        low_performers = [d for d, m in momentum.items() if m.score < 6.0]
        if low_performers:
            insights.append(f"Lower momentum in {', '.join(low_performers)} - identify quick wins to build energy")

        # Check for energy patterns
        high_energy = [d for d, m in momentum.items() if m.energy_level == "high"]
        if high_energy:
            insights.append(f"{', '.join(high_energy)} providing energy - use this fuel for harder work")

        return insights

    def _recommend_focus_areas(self, momentum: Dict[str, DomainMomentum]) -> List[str]:
        """Recommend priority focus areas based on momentum"""

        recommendations = []

        # Prioritize domains with upward trend
        trending_up = [d for d, m in momentum.items() if m.trend == "up"]
        if trending_up:
            recommendations.append(f"Maintain momentum in {', '.join(trending_up)} - consistency compounds")

        # Flag domains with low scores
        needs_attention = sorted(
            [(d, m.score) for d, m in momentum.items()],
            key=lambda x: x[1]
        )[:2]  # Bottom 2

        if needs_attention:
            recommendations.append(
                f"Boost {needs_attention[0][0]} with small wins - currently lowest momentum"
            )

        return recommendations

    def _generate_priority_recommendation(self, domain_data: Dict) -> Dict:
        """Generate recommendation for resolving competing priorities"""

        # Score each domain
        scores = {}
        for domain, data in domain_data.items():
            urgency_score = {"high": 3, "medium": 2, "low": 1}.get(data["urgency"]["level"], 1)
            momentum_score = data["momentum"].score / 10 * 3
            integration_score = {"high": 3, "medium": 2, "low": 1}.get(data["integration_potential"], 1)

            total_score = urgency_score + momentum_score + integration_score
            scores[domain] = total_score

        # Rank domains
        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        return {
            "primary_focus": ranked[0][0],
            "secondary_focus": ranked[1][0] if len(ranked) > 1 else None,
            "reasoning": f"{ranked[0][0]} scores highest on urgency, momentum, and integration potential",
            "integrated_approach": f"Lead with {ranked[0][0]}, integrate {ranked[1][0]} where possible",
            "time_allocation": {
                ranked[0][0]: "60%",
                ranked[1][0]: "40%" if len(ranked) > 1 else "0%"
            }
        }

    def _find_integration_opportunities(self, domains: List[str]) -> List[str]:
        """Find ways to work on multiple domains simultaneously"""

        opportunities = []

        if "fitness" in domains and "relationships" in domains:
            opportunities.append("Join Denver running group (fitness + social connection)")

        if "career" in domains and "emotional_health" in domains:
            opportunities.append("Treat job applications as edge question practice (career + RO-DBT)")

        if "fitness" in domains and "career" in domains:
            opportunities.append("Schedule applications post-run (leverage clarity state)")

        return opportunities


def main():
    parser = argparse.ArgumentParser(description='Cross-domain life analysis engine')

    parser.add_argument(
        '--mode',
        required=True,
        choices=['synthesis', 'priority', 'patterns', 'opportunities'],
        help='Analysis mode to run'
    )

    parser.add_argument(
        '--domains',
        help='Comma-separated list of domains (for synthesis/priority modes)',
        default='all'
    )

    parser.add_argument(
        '--lookback',
        help='Lookback period for pattern detection (e.g., 30days)',
        default='30days'
    )

    parser.add_argument(
        '--output',
        choices=['json', 'markdown'],
        default='json',
        help='Output format'
    )

    args = parser.parse_args()

    engine = IntegrationEngine()

    # Parse domains
    if args.domains and args.domains != 'all':
        domains = [d.strip() for d in args.domains.split(',')]
    else:
        domains = ['all']

    # Run appropriate mode
    if args.mode == 'synthesis':
        result = engine.run_synthesis(domains if domains != ['all'] else None)
    elif args.mode == 'priority':
        result = engine.run_priority_analysis(domains)
    elif args.mode == 'patterns':
        lookback = int(args.lookback.replace('days', ''))
        result = engine.run_pattern_detection(lookback_days=lookback)
    elif args.mode == 'opportunities':
        result = engine.run_opportunity_scan()

    # Output
    if args.output == 'json':
        print(json.dumps(result, indent=2))
    else:
        # TODO: Add markdown formatting
        print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
