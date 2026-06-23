# DECAY SYSTEM

import time

DECAY_AMOUNT = 5 # Amount of health to decay per interval

def apply_decay(creature):
    """Applies decay to the creature's health."""
    creature.hunger -= DECAY_AMOUNT
    if creature.hunger < 0:
        creature.hunger = 0