"""
Workout plan parser for extracting structured metadata from markdown training plans.

Parses the workout plan markdown file to extract:
- Current training phase
- Phase dates (start/end)
- Weekly workout template
- Volume targets
"""

import json
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional

# Default paths
PLAN_FILE = Path("/Users/samuelz/Documents/LLM CONTEXT/1 - personal/marathon_training/post-marathon-ski-fitness-plan.md")
METADATA_FILE = Path("/Users/samuelz/Documents/LLM CONTEXT/.claude/skills/data/workout-plan-metadata.json")


def parse_workout_plan(plan_path: Path = PLAN_FILE) -> Dict[str, Any]:
    """
    Parse workout plan markdown file to extract structured metadata.

    Args:
        plan_path: Path to workout plan markdown file

    Returns:
        Dict with:
        - plan_file: Path to source file
        - current_phase: Current training phase name
        - phase_start: Phase start date (YYYY-MM-DD)
        - phase_end: Phase end date (YYYY-MM-DD)
        - weekly_template: Dict mapping day abbreviations to workouts
        - weekly_volume_target: Target weekly mileage
        - parsed_at: Timestamp when metadata was generated

    Example:
        metadata = parse_workout_plan()
        print(f"Current phase: {metadata['current_phase']}")
        print(f"Today's workout: {metadata['weekly_template']['Wed']}")
    """
    if not plan_path.exists():
        raise FileNotFoundError(f"Workout plan not found: {plan_path}")

    with open(plan_path, 'r') as f:
        content = f.read()

    # Find the current phase section based on "Current Status" updates
    current_phase_match = re.search(
        r'\*\*Decision:\*\* Starting (Phase \d+[^)]+) (?:fresh on|begins) (?:Monday, )?(\w+ \d+)',
        content,
        re.IGNORECASE
    )

    if not current_phase_match:
        # Fallback: look for phase headers
        phase_match = re.search(r'## .+ (Phase \d+: [^\\n]+)\n\*\*([^-]+)', content)
        if phase_match:
            phase_name = phase_match.group(1).strip()
            dates_str = phase_match.group(2).strip()
        else:
            raise ValueError("Could not determine current training phase")
    else:
        phase_name = current_phase_match.group(1).strip()
        # Need to find phase dates separately
        phase_section = re.search(
            rf'## [^\\n]* {re.escape(phase_name)}[^\\n]*\n\*\*([^-\*]+)',
            content
        )
        if phase_section:
            dates_str = phase_section.group(1).strip()
        else:
            dates_str = None

    # Extract phase dates - look for the phase header with dates
    phase_header_match = re.search(
        rf'## [^#]+ {re.escape(phase_name)}[^\\n]*\n\*\*([^*]+)\*\*',
        content
    )

    phase_start = None
    phase_end = None

    if phase_header_match:
        dates_line = phase_header_match.group(1).strip()
        # Try to parse date range like "Nov 18 - Dec 15, 2025"
        date_match = re.search(
            r'(\w+ \d+)\s*-\s*(\w+ \d+),?\s*(\d{4})',
            dates_line
        )
        if date_match:
            start_str = f"{date_match.group(1)}, {date_match.group(3)}"
            end_str = f"{date_match.group(2)}, {date_match.group(3)}"
            try:
                phase_start = datetime.strptime(start_str, "%b %d, %Y").strftime("%Y-%m-%d")
                phase_end = datetime.strptime(end_str, "%b %d, %Y").strftime("%Y-%m-%d")
            except ValueError:
                pass

    # Find the weekly template for this phase
    # First try to find "Weekly Template Structure" table
    template_match = re.search(
        rf'{re.escape(phase_name)}.*?### Weekly Template Structure.*?\| Day \| Workout \|[^\n]*\n\|[-\s|]+\n((?:\|[^\n]+\n)+)',
        content,
        re.DOTALL
    )

    weekly_template = {}

    if template_match:
        # Parse the Weekly Template Structure table
        table_rows = template_match.group(1).strip().split('\n')
        for row in table_rows:
            if row.startswith('|---') or not row.strip():  # Skip separator row
                continue

            parts = [p.strip() for p in row.split('|')]
            if len(parts) >= 3:
                day = parts[1]  # Mon, Tue, Wed, etc.
                workout = parts[2]

                # Clean up workout description
                workout = re.sub(r'\*\*([^*]+)\*\*', r'\1', workout)  # Remove bold
                weekly_template[day] = workout
    else:
        # Fallback: try to find a week schedule
        phase_schedule = re.search(
            rf'{re.escape(phase_name)}.*?### Week \d+ Schedule.*?\| Day \| Workout \| Details \|.*?\n((?:\|[^\n]+\n)+)',
            content,
            re.DOTALL
        )

        if phase_schedule:
            # Parse the table
            table_rows = phase_schedule.group(1).strip().split('\n')
            for row in table_rows:
                if row.startswith('|---'):  # Skip separator row
                    continue

                parts = [p.strip() for p in row.split('|')]
                if len(parts) >= 3:
                    day = parts[1]  # Mon, Tue, Wed, etc.
                    workout = parts[2]

                    # Clean up workout description
                    workout = re.sub(r'\*\*([^*]+)\*\*', r'\1', workout)  # Remove bold
                    weekly_template[day] = workout
        else:
            # Last resort: create a basic template
            weekly_template = {
                'Mon': 'REST',
                'Tue': 'Run',
                'Wed': 'Strength',
                'Thu': 'Run',
                'Fri': 'Strength',
                'Sat': 'Long Run',
                'Sun': 'REST or Easy'
            }

    # Extract weekly volume target
    volume_match = re.search(
        r'\*\*Weekly Volume[:\]]*\*\* [~]?(\d+-\d+ miles?|\d+ miles?)',
        content,
        re.IGNORECASE
    )

    weekly_volume_target = volume_match.group(1) if volume_match else "Not specified"

    metadata = {
        'plan_file': str(plan_path),
        'current_phase': phase_name,
        'phase_start': phase_start,
        'phase_end': phase_end,
        'weekly_template': weekly_template,
        'weekly_volume_target': weekly_volume_target,
        'parsed_at': datetime.now().isoformat()
    }

    return metadata


def save_workout_metadata(metadata: Dict[str, Any], output_path: Path = METADATA_FILE):
    """
    Save workout metadata to JSON file.

    Args:
        metadata: Metadata dict from parse_workout_plan()
        output_path: Path to save JSON metadata

    Example:
        metadata = parse_workout_plan()
        save_workout_metadata(metadata)
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w') as f:
        json.dump(metadata, f, indent=2)

    print(f"Workout metadata saved to: {output_path}")


def load_workout_metadata(metadata_path: Path = METADATA_FILE) -> Dict[str, Any]:
    """
    Load workout metadata from JSON file.

    Args:
        metadata_path: Path to metadata JSON file

    Returns:
        Metadata dict

    Raises:
        FileNotFoundError: If metadata file doesn't exist

    Example:
        try:
            metadata = load_workout_metadata()
            print(f"Current phase: {metadata['current_phase']}")
        except FileNotFoundError:
            print("Metadata not found, parsing plan...")
            metadata = parse_workout_plan()
            save_workout_metadata(metadata)
    """
    if not metadata_path.exists():
        raise FileNotFoundError(f"Workout metadata not found: {metadata_path}")

    with open(metadata_path, 'r') as f:
        return json.load(f)


def is_metadata_stale(metadata: Dict[str, Any], max_days: int = 30) -> bool:
    """
    Check if workout metadata is stale and needs updating.

    Metadata is considered stale if:
    - Parsed more than max_days ago
    - Phase end date has passed
    - Phase start date hasn't started yet (plan changed)

    Args:
        metadata: Metadata dict from load_workout_metadata()
        max_days: Maximum age in days before considered stale

    Returns:
        True if metadata is stale and should be regenerated

    Example:
        metadata = load_workout_metadata()
        if is_metadata_stale(metadata):
            print("Metadata is stale, reparsing...")
            fresh_metadata = parse_workout_plan()
            save_workout_metadata(fresh_metadata)
    """
    parsed_at = datetime.fromisoformat(metadata['parsed_at'])
    now = datetime.now()

    # Check age
    age_days = (now - parsed_at).days
    if age_days > max_days:
        return True

    # Check if phase ended
    if metadata.get('phase_end'):
        phase_end = datetime.strptime(metadata['phase_end'], '%Y-%m-%d')
        if now.date() > phase_end.date():
            return True

    # Check if we're before phase start (plan changed)
    if metadata.get('phase_start'):
        phase_start = datetime.strptime(metadata['phase_start'], '%Y-%m-%d')
        if now.date() < phase_start.date():
            return True

    return False


def get_or_refresh_metadata(
    metadata_path: Path = METADATA_FILE,
    plan_path: Path = PLAN_FILE,
    force_refresh: bool = False
) -> Dict[str, Any]:
    """
    Get workout metadata, refreshing if stale or missing.

    Args:
        metadata_path: Path to metadata JSON file
        plan_path: Path to workout plan markdown file
        force_refresh: Force reparsing even if metadata exists and is fresh

    Returns:
        Fresh workout metadata dict

    Example:
        # Get metadata, automatically refreshing if needed
        metadata = get_or_refresh_metadata()

        # Force refresh
        metadata = get_or_refresh_metadata(force_refresh=True)
    """
    needs_refresh = force_refresh

    if not needs_refresh:
        try:
            metadata = load_workout_metadata(metadata_path)
            if is_metadata_stale(metadata):
                print("Workout metadata is stale, reparsing...")
                needs_refresh = True
        except FileNotFoundError:
            print("Workout metadata not found, parsing plan...")
            needs_refresh = True

    if needs_refresh:
        metadata = parse_workout_plan(plan_path)
        save_workout_metadata(metadata, metadata_path)

    return metadata


if __name__ == '__main__':
    # Generate initial metadata when run directly
    print("Parsing workout plan...")
    metadata = parse_workout_plan()

    print("\nExtracted metadata:")
    print(f"  Phase: {metadata['current_phase']}")
    print(f"  Dates: {metadata['phase_start']} to {metadata['phase_end']}")
    print(f"  Volume target: {metadata['weekly_volume_target']}")
    print(f"\nWeekly template:")
    for day, workout in metadata['weekly_template'].items():
        print(f"  {day}: {workout}")

    save_workout_metadata(metadata)
    print(f"\nMetadata saved successfully!")
