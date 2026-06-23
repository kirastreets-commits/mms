# RESPONSE GENERATION

def get_creature_response(creature, action: str):

    base = f"{creature.name} looks at you."

    # mood influence
    if creature.mood == "hungry":
        base += " It's stomach growls loudly."

    elif creature.mood == "happy":
        base += " It seems content and relaxed."

    elif creature.mood == "tired":
        base += " It yawns and seems ready for a nap."

    elif creature.mood == "lonely":
        base += " It looks at you with longing eyes, seeking attention."

    return base