def give_item(creature, item_id, player_id=None):
    from data.resources import RESOURCES
    from data.species import get_species_preferences

    resource = RESOURCES.get(item_id)
    if not resource:
        return {
            "success": False,
            "message": "That item doesn't exist."
        }

    # ----------------------------
    # PREFERENCES (clean split)
    # ----------------------------
    preferences_raw = get_species_preferences(creature.species)

    preferences = {
        "tags": set(preferences_raw),   # treat species prefs as tags for now
        "types": set()                  # optional future expansion
    }

    # ----------------------------
    # RESULT BASE
    # ----------------------------
    result = {
        "success": True,
        "reaction": "neutral",
        "message": "",
        "comfort_gain": 0,
        "bond_gain": 0
    }

    # ----------------------------
    # MATCH SCORING
    # ----------------------------
    item_tags = set(resource.get("tags", []))
    item_type = resource.get("type")

    match_score = 0

    if item_type in preferences["types"]:
        match_score += 2

    match_score += len(item_tags.intersection(preferences["tags"]))

    # ----------------------------
    # REACTION LOGIC (balanced)
    # ----------------------------
    if match_score >= 3:
        result["reaction"] = "loves"
        result["bond_gain"] = 5
        result["comfort_gain"] = 3

    elif match_score == 2:
        result["reaction"] = "likes"
        result["bond_gain"] = 2
        result["comfort_gain"] = 2

    elif match_score == 1:
        result["reaction"] = "neutral"
        result["bond_gain"] = 0
        result["comfort_gain"] = 1

    else:
        result["reaction"] = "dislikes"
        result["bond_gain"] = -2
        result["comfort_gain"] = -1

    # ----------------------------
    # APPLY STAT CHANGES
    # ----------------------------
    creature.trust = max(
        0,
        min(creature.max_trust, creature.trust + result["bond_gain"])
    )

    # ----------------------------
    # ADD ITEM TO SHELTER (AFTER REACTION)
    # ----------------------------
    creature.shelter.setdefault("items", []).append({
        "item": item_id,
        "reaction": result["reaction"]
    })

    # ----------------------------
    # MEMORY UPDATE (MANDATORY)
    # ----------------------------
    add_gift_memory(creature, item_id, result["reaction"], player_id)

    return result

def add_gift_memory(creature, item_id, reaction, player_id=None):
    mem = creature.memory

    # ----------------------------
    # LOG INTERACTION
    # ----------------------------
    mem["interactions"]["gift"].append({
        "item": item_id,
        "reaction": reaction
    })

    # ----------------------------
    # LEARN PREFERENCE
    # ----------------------------
    if reaction in ["loves", "likes"]:
        mem["preferences"]["liked_items"][item_id] = \
            mem["preferences"]["liked_items"].get(item_id, 0) + 1

    elif reaction == "dislikes":
        mem["preferences"]["disliked_items"][item_id] = \
            mem["preferences"]["disliked_items"].get(item_id, 0) + 1

    # ----------------------------
    # EMOTIONAL IMPACT
    # ----------------------------
    if reaction == "loves":
        mem["emotional"]["comfort_level"] += 3
    elif reaction == "dislikes":
        mem["emotional"]["stress_level"] += 2

    # ----------------------------
    # PLAYER BOND TRACKING (optional)
    # ----------------------------
    if player_id:
        mem["flags"]["favorite_player"] = player_id

    
def gift_creature(player, creature, item_id):
    from data.resources import RESOURCES
    from systems.memory_system import update_memory

    if player.inventory.get(item_id, 0) <= 0:
        return {"success": False, "message": "You don't have that item."}

    # remove item from player
    player.inventory[item_id] -= 1
    if player.inventory[item_id] <= 0:
        del player.inventory[item_id]

    # calculate reaction
    result = give_item(creature, item_id, player_id=player.user_id)

    # apply shelter outcome
    apply_gift_outcome(creature, item_id, result)

    # memory update (if not already inside give_item)
    update_memory(creature, "gift", result)

    return {
        "success": True,
        "reaction": result["reaction"],
        "message": result["message"]
    }

def apply_gift_outcome(creature, item_id, result):
    reaction = result["reaction"]

    # ----------------------------
    # ❤️ FAVORITE ITEMS
    # ----------------------------
    if reaction == "loves":
        creature.memory.setdefault("favorites", {}).setdefault("items", [])

        if item_id not in creature.memory["favorites"]["items"]:
            creature.memory["favorites"]["items"].append(item_id)

        creature.shelter["items"].append({
            "item": item_id,
            "state": "favorite"
        })

    # ----------------------------
    # 😊 LIKES → KEEP IN SHELTER
    # ----------------------------
    elif reaction == "likes":
        creature.shelter["items"].append({
            "item": item_id,
            "state": "kept"
        })

    # ----------------------------
    # 😐 NEUTRAL → OPTIONAL KEEP
    # ----------------------------
    elif reaction == "neutral":
        creature.shelter["items"].append({
            "item": item_id,
            "state": "ignored"
        })

    # ----------------------------
    # ❌ DISLIKES → RETURN ITEM
    # ----------------------------
    elif reaction == "dislikes":
        return_item_to_player(creature, item_id)

#HELPER  

def return_item_to_player(creature, item_id):
    # This assumes you pass player context in real system
    creature.memory.setdefault("rejected_items", [])
    creature.memory["rejected_items"].append(item_id)

    return {
        "returned": True,
        "message": f"{creature.name} rejected the item."
    }