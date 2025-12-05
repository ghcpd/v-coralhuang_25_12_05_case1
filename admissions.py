import re
from typing import List, Dict

def validate_student_id(student_id: str) -> bool:
    """Validate ID format UG2025xxxx"""
    return bool(re.match(r"^UG2025\d{4}$", student_id))

def compute_aggregate(scores: Dict[str, int]) -> float:
    """Compute aggregate as sum of provided subject scores."""
    if not scores:
        raise ValueError("No scores provided")
    return sum(scores.values())

def qualify_choice(aggregate: float, cutoffs: List[float]) -> str:
    """
    Given an aggregate and a list of cutoffs [first, second, third],
    return 'First', 'Second', 'Third', or 'None'. Uses if/elif/else.
    Student qualifies for a choice if aggregate >= cutoff (higher is better).
    """
    if aggregate >= cutoffs[0]:
        return 'First'
    elif aggregate >= cutoffs[1]:
        return 'Second'
    elif aggregate >= cutoffs[2]:
        return 'Third'
    else:
        return 'None' 


def suggest_programs(aggregate: float, programs: List[Dict]) -> List[Dict]:
    """Return programs with cutoff <= aggregate (i.e., student qualifies) sorted by cutoff.
    Handle programs dictionaries that may use 'cutoff' or 'Cutoff' keys.
    """
    def cutoff_value(p):
        return p.get('cutoff') if p.get('cutoff') is not None else p.get('Cutoff')
    matches = []
    for p in programs:
        val = cutoff_value(p)
        if val is None:
            continue
        if val <= aggregate:
            matches.append(p)
    matches.sort(key=lambda x: cutoff_value(x))
    return matches
