def default_memory():
    return {
        "interactions": {
            "feed": [],
            "play": [],
            "heal": []
        },
        "events": [],
        "flags": {},
        "emotional": {
            "stress_level": 0,
            "comfort_level": 50
        },
        "experience": {
            "healing_good": 0,
            "healing_bad": 0
        }
    }

def update_memory(creature, action_type, result):
    memory = creature.memory

    # ----------------------------
    # 1. INTERACTIONS LOG
    # ----------------------------
    memory["interactions"][action_type].append({
        "success": result.get("success", True),
        "mood": creature.mood
    })

    # ----------------------------
    # 2. EMOTIONAL SYSTEM
    # ----------------------------
    if result.get("success", True):
        memory["emotional"]["comfort_level"] += 3
        memory["emotional"]["stress_level"] = max(
            0,
            memory["emotional"]["stress_level"] - 2
        )
    else:
        memory["emotional"]["stress_level"] += 8

    # ----------------------------
    # 3. EXPERIENCE SYSTEM (HEAL EXAMPLE)
    # ----------------------------
    if action_type == "heal":
        if result.get("success", True):
            memory["experience"]["healing_good"] += 1
        else:
            memory["experience"]["healing_bad"] += 1

    # ----------------------------
    # 4. FLAGS (BEHAVIOUR CHANGES)
    # ----------------------------
    if memory["experience"]["healing_bad"] >= 3:
        memory["flags"]["afraid_of_healing"] = True

    # ----------------------------
    # 5. RARE EVENTS STORAGE
    # ----------------------------
    if result.get("rare_event"):
        memory["events"].append(result["rare_event"])