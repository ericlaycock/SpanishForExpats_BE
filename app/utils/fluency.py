import math


def compute_fluency_level(hf_rehearsed_or_higher: int) -> int:
    """Convert raw HF word count (mastery >= 2) to fluency level.

    Uses the same formula as the frontend:
    Math.floor(20 * Math.log(hfCount / 20 + 1))
    """
    if hf_rehearsed_or_higher <= 0:
        return 0
    return int(20 * math.log(hf_rehearsed_or_higher / 20 + 1))
