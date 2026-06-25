VALID_ACTIONS = {"play", "feed", "heal", "rest", "gift"}


def ensure_valid_action(action_type):
    return action_type in VALID_ACTIONS


def default_memory():
    return {
        "interactions": {
            "play": [],
            "feed": [],
            "heal": [],
            "rest": [],
            "gift": []
        },
        "emotional": {
            "comfort_level": 0,
            "stress_level": 0
        },
        "experience": {
            "healing_good": 0,
            "healing_bad": 0
        },
        "preferences": {
            "liked_items": {},
            "disliked_items": {}
        },
        "favorites": {
            "items": []
        },
        "flags": {
            "afraid_of_healing": False,
            "favorite_player": None
        },
        "events": []
    }


def update_memory(creature, action_type, result):
    memory = creature.memory

    # ----------------------------
    # VALID ACTION CHECK (SAFE)
    # ----------------------------
    if action_type not in VALID_ACTIONS:
        return

    # ----------------------------
    # SAFE INITIALISATION
    # ----------------------------
    memory.setdefault("interactions", {
        "play": [],
        "feed": [],
        "heal": [],
        "rest": [],
        "gift": []
    })

    for key in VALID_ACTIONS:
        memory["interactions"].setdefault(key, [])

    memory.setdefault("emotional", {})
    memory.setdefault("experience", {})
    memory.setdefault("flags", {})
    memory.setdefault("events", [])

    memory["emotional"].setdefault("comfort_level", 0)
    memory["emotional"].setdefault("stress_level", 0)

    memory["experience"].setdefault("healing_good", 0)
    memory["experience"].setdefault("healing_bad", 0)

    # ----------------------------
    # INTERACTION LOG
    # ----------------------------
    memory["interactions"][action_type].append({
        "success": result.get("success", True),
        "mood": creature.mood,
        "reaction": result.get("reaction")
    })

    # ----------------------------
    # EMOTION SCALING
    # ----------------------------
    emotion_scale = {
        "feed": (2, 1),
        "play": (3, 0),
        "heal": (1, 4),
        "rest": (2, -1),
        "gift": (3, 2)
    }

    comfort_gain, stress_gain = emotion_scale.get(action_type, (2, 2))

    if result.get("success", True):
        memory["emotional"]["comfort_level"] += comfort_gain
        memory["emotional"]["stress_level"] = max(
            0,
            memory["emotional"]["stress_level"] - stress_gain
        )
    else:
        memory["emotional"]["stress_level"] += stress_gain * 2

    # ----------------------------
    # EXPERIENCE TRACKING
    # ----------------------------
    if action_type == "heal":
        if result.get("success", True):
            memory["experience"]["healing_good"] += 1
        else:
            memory["experience"]["healing_bad"] += 1

    # ----------------------------
    # FEAR FLAG
    # ----------------------------
    if memory["experience"]["healing_bad"] >= 3:
        memory["flags"]["afraid_of_healing"] = True

    # ----------------------------
    # RARE EVENTS (LIMITED)
    # ----------------------------
    if result.get("rare_event"):
        memory["events"].append(result["rare_event"])

        if len(memory["events"]) > 20:
            memory["events"].pop(0)
