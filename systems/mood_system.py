import random

MOODS = [
    "happy",
    "neutral",
    "hungry",
    "tired",
    "excited",
    "lonely"
]


def update_mood(creature):

    # simple rule-based mood logic
    if creature.hunger < 30:
        creature.mood = "hungry"

    elif creature.energy < 30:
        creature.mood = "tired"

    elif creature.happiness > 80:
        creature.mood = "happy"

    elif creature.trust < 30:
        creature.mood = "lonely"

    else:
        creature.mood = "neutral"

