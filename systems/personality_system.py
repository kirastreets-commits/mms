from data.personality import PERSONALITIES


'''def apply_personality(creature, action):

    personality = PERSONALITIES.get(creature.personality)

    stat_changes = []

    if not personality:
        return stat_changes

    if action in personality.get("likes", []):
        creature.happiness = min(100, creature.happiness + 3)
        creature.trust = min(100, creature.trust + 2)

        stat_changes.append(("Happiness", 3))
        stat_changes.append(("Trust", 2))

    if action in personality.get("dislikes", []):
        creature.happiness = max(0, creature.happiness - 2)

        stat_changes.append(("Happiness", -2))

    return stat_changes'''

PERSONALITY_ACTIONS = {

    "playful": {
        "play": {
            "Happiness": 5
        }
    },

    "lazy": {
        "rest": {
            "Energy": 10
        },

        "play": {
            "Energy": -5
        }
    },

    "protective": {
        "heal": {
            "Trust": 3
        }
    },

    "mischievous": {
        "play": {
            "Happiness": 3
        }
    }
}

def apply_personality(creature, action):

    changes = []

    personality = creature.personality

    modifiers = (
        PERSONALITY_ACTIONS
        .get(personality, {})
        .get(action, {})
    )

    for stat, amount in modifiers.items():

        attr = stat.lower()

        current = getattr(creature, attr)

        setattr(
            creature,
            attr,
            max(0, min(100, current + amount))
        )

        changes.append((stat, amount))

    return changes