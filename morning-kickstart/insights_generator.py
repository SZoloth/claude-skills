"""
Cross-domain insights generator for morning-kickstart.

Generates bi-directional insights by having data sources inform each other:
- Things tasks → Needle-mover suggestions
- Strava training → Energy-appropriate tasks
- Workout plan → Denver challenge timing
- Task tags → Outreach tracking alignment
"""

from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime


def suggest_needle_mover(
    things_tasks: List[Dict[str, Any]],
    energy_level: str,
    current_streak: int,
    category_history: Optional[Dict[str, int]] = None
) -> Tuple[str, str, List[str]]:
    """
    Suggest today's needle-mover based on Things tasks and energy level.

    Args:
        things_tasks: Tasks from Things (today + upcoming)
        energy_level: 'HIGH', 'MEDIUM', or 'LOW' from Strava
        current_streak: Current needle-mover streak
        category_history: Dict of category -> days since last (e.g., {'job_search': 2})

    Returns:
        Tuple of (category, action, context_lines)
        - category: 'job_search', 'creation', 'social', 'relationship', 'vision'
        - action: The suggested action text
        - context_lines: List of context strings explaining why this was chosen

    Logic:
        1. Filter to P1 tasks or high-priority tasks (#job-search tags)
        2. On HIGH energy → suggest uncomfortable/hard tasks
        3. On LOW energy → suggest easier but important tasks
        4. Weight toward job_search (90-day focus)
        5. Avoid categories done recently (unless critical)

    Example:
        tasks = things.get_today()
        energy = strava.calculate_energy_level(activities, plan)
        category, action, context = suggest_needle_mover(tasks, energy, 4)

        print(f"[{category.upper()}] {action}")
        for line in context:
            print(f"  {line}")
    """
    context_lines = []

    # Filter to high-priority tasks
    p1_tasks = [t for t in things_tasks if t.get('priority') == 'P1']
    job_search_tasks = [t for t in things_tasks if '#job-search' in t.get('tags', [])]

    # Combine and deduplicate
    priority_tasks = {t['id']: t for t in (p1_tasks + job_search_tasks)}.values()
    priority_tasks = list(priority_tasks)

    context_lines.append(f"{len(priority_tasks)} priority tasks available")

    if not priority_tasks:
        # Fallback: use any task from today
        priority_tasks = things_tasks[:3]  # Top 3 tasks
        context_lines.append("No P1/job-search tasks, using top tasks")

    # Score tasks based on criteria
    scored_tasks = []

    for task in priority_tasks:
        score = 0
        title = task.get('title', '')
        tags = task.get('tags', [])
        notes = task.get('notes', '')

        # Job search tasks get priority (90-day focus)
        if '#job-search' in tags or 'job' in title.lower() or 'apply' in title.lower():
            score += 10
            category = 'job_search'
        elif any(tag in tags for tag in ['#carter', '#relationship']):
            score += 5
            category = 'relationship'
        elif any(tag in tags for tag in ['#denver', '#social', '#friends']):
            score += 3
            category = 'social'
        elif 'write' in title.lower() or 'create' in title.lower():
            score += 4
            category = 'creation'
        else:
            score += 1
            category = 'vision'

        # Uncomfortable tasks = important
        uncomfortable_keywords = ['outreach', 'apply', 'call', 'reach out', 'contact', 'network']
        if any(keyword in title.lower() for keyword in uncomfortable_keywords):
            score += 5

        # Energy-appropriate scoring
        if energy_level == 'HIGH':
            # On high energy, prefer uncomfortable tasks
            if any(keyword in title.lower() for keyword in uncomfortable_keywords):
                score += 3
        elif energy_level == 'LOW':
            # On low energy, prefer easier tasks (but still important)
            if not any(keyword in title.lower() for keyword in uncomfortable_keywords):
                score += 2

        # Deadline urgency
        if task.get('deadline'):
            score += 3

        scored_tasks.append((score, category, task))

    # Sort by score (highest first)
    scored_tasks.sort(key=lambda x: x[0], reverse=True)

    if scored_tasks:
        score, category, best_task = scored_tasks[0]
        action = best_task['title']

        # Add context
        if '#job-search' in best_task.get('tags', []):
            context_lines.append("Job search tagged → aligns with 90-day focus")

        if energy_level == 'HIGH':
            context_lines.append("High energy day → good for uncomfortable work")
        elif energy_level == 'LOW':
            context_lines.append("Training day → save energy, but stay productive")

    else:
        # Ultimate fallback
        category = 'job_search'
        action = "Personalized outreach to target company"
        context_lines.append("Default suggestion: job search is priority")

    return category, action, context_lines


def contextualize_outreach(
    outreach_data: Dict[str, Any],
    things_tasks: List[Dict[str, Any]],
    energy_level: str
) -> Dict[str, Any]:
    """
    Add Things and Strava context to outreach streak data.

    Args:
        outreach_data: Data from outreach-streak tracker
        things_tasks: Tasks from Things
        energy_level: Energy level from Strava

    Returns:
        Enhanced outreach dict with:
        - things_context: List of job-search tasks from Things
        - energy_suggestion: Suggestion based on energy level
        - alignment_message: If tasks align with tracker

    Example:
        outreach = json.load(open('outreach-streak-data.json'))
        tasks = things.get_today()
        enhanced = contextualize_outreach(outreach, tasks, 'HIGH')

        print(enhanced['energy_suggestion'])
        for task in enhanced['things_context']:
            print(f"  - {task}")
    """
    # Find job-search related tasks in Things
    job_tasks = [
        t for t in things_tasks
        if any(tag in ['#job-search', '#application', '#outreach', '#networking']
               for tag in t.get('tags', []))
        or any(keyword in t.get('title', '').lower()
               for keyword in ['apply', 'outreach', 'network', 'recruiter', 'interview'])
    ]

    # Count current week's outreaches
    current_count = len(outreach_data.get('outreaches', []))
    target = 10
    remaining = target - current_count

    # Energy-based suggestion
    if energy_level == 'HIGH':
        energy_suggestion = f"High energy → aim for 2-3 quality outreaches today"
    elif energy_level == 'MEDIUM':
        energy_suggestion = f"Moderate energy → 1-2 outreaches manageable"
    else:  # LOW
        energy_suggestion = f"Low energy → keep it simple, focus on quality over quantity"

    # Alignment check
    if job_tasks and remaining > 0:
        alignment_message = f"{len(job_tasks)} tasks tagged #job-search → log completions to tracker"
    elif job_tasks:
        alignment_message = f"{len(job_tasks)} job-search tasks (already hit {target}/week!)"
    else:
        alignment_message = f"No job-search tasks in Things → add {remaining} to reach {target}/week"

    return {
        'things_context': [t['title'] for t in job_tasks[:5]],  # Top 5
        'energy_suggestion': energy_suggestion,
        'alignment_message': alignment_message,
        'things_count': len(job_tasks),
        'tracker_remaining': remaining
    }


def contextualize_denver(
    denver_data: Dict[str, Any],
    workout_metadata: Dict[str, Any],
    strava_activities: List[Dict[str, Any]]
) -> Dict[str, str]:
    """
    Add training tie-ins to Denver connection challenges.

    Args:
        denver_data: Data from denver-connect tracker
        workout_metadata: Workout plan metadata
        strava_activities: Recent Strava activities

    Returns:
        Dict with:
        - training_tie_in: Suggestion to combine training with social
        - energy_context: Whether energy supports social activity

    Example:
        denver = json.load(open('denver-connect-data.json'))
        metadata = load_workout_metadata()
        activities = strava.get_recent_activities()

        context = contextualize_denver(denver, metadata, activities)
        print(context['training_tie_in'])
    """
    from datetime import datetime, timedelta

    # Get today's day of week
    day_of_week = datetime.now().strftime('%a')

    # Get today's workout
    weekly_template = workout_metadata.get('weekly_template', {})
    todays_workout = weekly_template.get(day_of_week, '')

    # Get upcoming weekend workout
    saturday_workout = weekly_template.get('Sat', '')
    sunday_workout = weekly_template.get('Sun', '')

    training_tie_in = ""
    energy_context = ""

    # Suggest social + training combinations
    if 'Long Run' in saturday_workout or 'Long Run' in sunday_workout:
        training_tie_in = "Weekend long run → try joining a run club!"
    elif 'Strength' in todays_workout or 'SKI STRENGTH' in todays_workout:
        training_tie_in = "Strength day → climbing gym or group fitness class?"
    elif 'REST' in todays_workout:
        training_tie_in = "Rest day → coffee shop or casual meetup (low physical demand)"
        energy_context = "High energy available for social interaction"
    elif 'Easy' in todays_workout:
        training_tie_in = "Easy run day → social run or walking coffee chat"
        energy_context = "Moderate energy, low-key social works well"
    else:
        # Hard workout day
        training_tie_in = "Hard workout today → save social energy for weekend"
        energy_context = "Training day, keep social interactions light"

    return {
        'training_tie_in': training_tie_in,
        'energy_context': energy_context or "Energy level supports social activity"
    }


def contextualize_carter(
    carter_data: Dict[str, Any],
    things_tasks: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """
    Check if Carter rituals are planned in Things but not logged in tracker.

    Args:
        carter_data: Data from carter-rituals tracker
        things_tasks: Tasks from Things

    Returns:
        Dict with:
        - planned_but_not_logged: List of rituals planned in Things
        - suggestions: List of suggestions

    Example:
        carter = json.load(open('carter-rituals-data.json'))
        tasks = things.get_today()

        context = contextualize_carter(carter, tasks)
        if context['planned_but_not_logged']:
            print("Planned but not logged:", context['planned_but_not_logged'])
    """
    # Find Carter-related tasks
    carter_tasks = [
        t for t in things_tasks
        if any(tag in ['#carter', '#date', '#date-night', '#flowers', '#relationship']
               for tag in t.get('tags', []))
        or 'carter' in t.get('title', '').lower()
        or 'date' in t.get('title', '').lower()
    ]

    planned_but_not_logged = []
    suggestions = []

    # Check for date nights
    date_tasks = [t for t in carter_tasks if 'date' in t.get('title', '').lower()]
    if date_tasks:
        # Check if logged in tracker
        recent_dates = [
            r for r in carter_data.get('rituals', [])
            if r.get('type') == 'weekly_date'
        ]
        if not recent_dates:  # None logged this week
            planned_but_not_logged.append("Date night planned in Things")
            suggestions.append("Log date night to tracker after completion")

    # Check for note writing
    note_tasks = [t for t in carter_tasks if 'note' in t.get('title', '').lower() or 'validation' in t.get('title', '').lower()]
    if note_tasks:
        planned_but_not_logged.append("Validating note planned")

    # Check for flowers
    flower_tasks = [t for t in carter_tasks if 'flower' in t.get('title', '').lower()]
    if flower_tasks:
        planned_but_not_logged.append("Flowers task in Things")

    return {
        'planned_but_not_logged': planned_but_not_logged,
        'suggestions': suggestions,
        'carter_tasks_count': len(carter_tasks)
    }


def generate_avoidance_check(
    suggested_action: str,
    energy_level: str
) -> Optional[str]:
    """
    Generate avoidance pattern check message.

    Args:
        suggested_action: The suggested needle-mover action
        energy_level: Energy level for the day

    Returns:
        Avoidance check message or None

    Logic:
        - If uncomfortable task + high energy → "Uncomfortable = important"
        - If easy task + high energy → "Is this avoidance?"
        - If planning/system task → "Architect pattern?"

    Example:
        check = generate_avoidance_check(
            "Personalized outreach to Stripe",
            "HIGH"
        )
        if check:
            print(f"⚠️  {check}")
    """
    uncomfortable_keywords = ['outreach', 'apply', 'call', 'reach out', 'contact', 'network', 'phone']
    avoidance_keywords = ['plan', 'organize', 'setup', 'configure', 'research', 'learn', 'read']

    action_lower = suggested_action.lower()

    # Check for uncomfortable tasks (good!)
    if any(keyword in action_lower for keyword in uncomfortable_keywords):
        if energy_level == 'HIGH':
            return "AVOIDANCE CHECK: Uncomfortable = important. Do it first."
        return None

    # Check for potential avoidance (bad)
    if any(keyword in action_lower for keyword in avoidance_keywords):
        if energy_level in ['HIGH', 'MEDIUM']:
            return "⚠️  ARCHITECT PATTERN: Are you building systems to avoid doing hard work?"
        return None

    return None


if __name__ == '__main__':
    # Test the insights generator
    print("Testing insights generator...")

    # Mock data
    mock_tasks = [
        {'id': '1', 'title': 'Personalized outreach to Stripe PM', 'priority': 'P1', 'tags': ['#job-search']},
        {'id': '2', 'title': 'Apply to Figma Senior PM role', 'priority': 'P1', 'tags': ['#job-search', '#application']},
        {'id': '3', 'title': 'Write validating note for Carter', 'tags': ['#carter', '#relationship']},
        {'id': '4', 'title': 'Research Denver run clubs', 'tags': ['#denver', '#social']},
    ]

    category, action, context = suggest_needle_mover(mock_tasks, 'HIGH', 4)
    print(f"\nNeedle-mover suggestion:")
    print(f"  [{category.upper()}] {action}")
    for line in context:
        print(f"  - {line}")

    check = generate_avoidance_check(action, 'HIGH')
    if check:
        print(f"\n  {check}")

    print("\n✓ Insights generator working!")
