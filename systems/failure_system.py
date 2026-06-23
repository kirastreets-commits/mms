import random

def chance(percent: float) -> bool:
    """
    Returns True if action succeeds.
    Example: chance(80) = 80% success rate
    """

    return random.random() < (percent / 100)