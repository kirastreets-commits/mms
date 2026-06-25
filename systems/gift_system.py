from data.gift_responses import (
    LOVE_MESSAGES,
    LIKE_MESSAGES,
    NEUTRAL_MESSAGES,
    DISLIKE_MESSAGES,
    FAVORITE_MESSAGES
)

def give_item(creature, item_id, player_id=None):
    from data.resources import RESOURCES
    from data.species import get_species_preferences

    resource = RESOURCES.get(item_id)
    if not resource:
        return {
            "success": False,
            "message": "That item doesn't exist."
        }

    preferences = set(get_species_preferences(creature.species))

    item_tags = set(resource.get("tags", []))

    match_score = len(item_tags.intersection(preferences))

    result = {
        "success": True,
        "reaction": "neutral",
        "bond_gain": 0,
        "comfort_gain": 0,
        "shelter_action": "ignored"
    }

    if match_score >= 3:
        result.update({
            "reaction": "loves",
            "bond_gain": 5,
            "comfort_gain": 3,
            "shelter_action": "favorite"
        })

    elif match_score == 2:
        result.update({
            "reaction": "likes",
            "bond_gain": 2,
            "comfort_gain": 2,
            "shelter_action": "kept"
        })

    elif match_score == 1:
        result.update({
            "reaction": "neutral",
            "bond_gain": 0,
            "comfort_gain": 1,
            "shelter_action": "kept"
        })

    else:
        result.update({
            "reaction": "dislikes",
            "bond_gain": -2,
            "comfort_gain": -1,
            "shelter_action": "rejected"
        })

    creature.trust = max(0, min(creature.max_trust, creature.trust + result["bond_gain"]))

    return result
from systems.memory_system import ensure_memory
def add_gift_memory(creature, item_id, reaction, player_id=None):
    ensure_memory(creature.memory)
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
    from systems.memory_system import update_memory

    if player.inventory.get(item_id, 0) <= 0:
        return {
            "success": False,
            "message": "You don't have that item."
        }

    # remove item
    player.inventory[item_id] -= 1
    if player.inventory[item_id] <= 0:
        del player.inventory[item_id]

    # reaction
    result = give_item(creature, item_id, player.user_id)

    # apply world changes
    apply_gift_outcome(creature, item_id, result)

    # memory system
    update_memory(creature, "gift", result)

    return {
        "success": True,
        **result
    }

def apply_gift_outcome(creature, item_id, result):
    reaction = result["reaction"]
    action = result["shelter_action"]

    # Ensure structure
    creature.shelter.setdefault("items", [])
    creature.memory.setdefault("favorites", {"items": []})

    # ----------------------------
    # FAVORITE
    # ----------------------------
    if action == "favorite":
        creature.memory["favorites"]["items"].append(item_id)

        creature.shelter["items"].append({
            "item": item_id,
            "state": "favorite"
        })

    # ----------------------------
    # KEPT
    # ----------------------------
    elif action == "kept":
        creature.shelter["items"].append({
            "item": item_id,
            "state": "kept"
        })

    # ----------------------------
    # IGNORED
    # ----------------------------
    elif action == "ignored":
        creature.shelter["items"].append({
            "item": item_id,
            "state": "ignored"
        })

    # ----------------------------
    # REJECTED
    # ----------------------------
    elif action == "rejected":
        creature.memory.setdefault("rejected_items", []).append(item_id)

#HELPER  

def return_item_to_player(creature, item_id):
    # This assumes you pass player context in real system
    creature.memory.setdefault("rejected_items", [])
    creature.memory["rejected_items"].append(item_id)

    return {
        "returned": True,
        "message": f"{creature.name} rejected the item."
    }

import discord

def build_gift_embed(creature, item_id, result):
    reaction = result["reaction"]
    action = result["shelter_action"]

    color_map = {
        "loves": discord.Color.green(),
        "likes": discord.Color.blurple(),
        "neutral": discord.Color.greyple(),
        "dislikes": discord.Color.red()
    }

    embed = discord.Embed(
        title=f"{creature.name} received a gift!",
        description=f"The creature looks **{reaction}** about it.",
        color=color_map.get(reaction, discord.Color.default())
    )

    embed.add_field(
        name="Bond Change",
        value=f"+{result['bond_gain']} trust",
        inline=True
    )

    embed.add_field(
        name="Comfort",
        value=f"+{result['comfort_gain']}",
        inline=True
    )

    # 🏡 Shelter result message
    shelter_text = {
        "favorite": "It placed the item in a special corner of its shelter.",
        "kept": "It added the item to its shelter.",
        "ignored": "It left the item in its shelter without interest.",
        "rejected": "It rejected the gift and refuses to keep it."
    }

    embed.add_field(
        name="Shelter",
        value=shelter_text.get(action, "No change."),
        inline=False
    )

    if item_id:
        embed.set_footer(text=f"Item: {item_id}")

    return embed
