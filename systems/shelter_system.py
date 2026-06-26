from data.resources import RESOURCES
from data.species import get_species_preferences

SHELTER_LEVELS = {
    1: 0,
    2: 15,
    3: 35,
    4: 60,
    5: 100
}


from data.resources import RESOURCES
from data.species import get_species_preferences

SHELTER_LEVELS = {
    1: 0,
    2: 15,
    3: 35,
    4: 60,
    5: 100
}


def update_shelter(creature):

    creature.shelter.setdefault("items", [])
    creature.shelter.setdefault("comfort", 0)
    creature.shelter.setdefault("level", 1)

    preferences = set(
        tag.lower().strip()
        for tag in get_species_preferences(creature.species)
    )

    comfort = 0

    for entry in creature.shelter["items"]:

        item_id = entry["item"]

        resource = RESOURCES.get(item_id)

        if not resource:
            continue

        # Base comfort from the item
        comfort += resource.get("comfort", 0)

        # Bonus comfort for preferred tags
        for tag in resource.get("tags", []):

            if tag.lower().strip() in preferences:
                comfort += 2

        # Favourite items are worth extra
        if entry.get("state") == "favorite":
            comfort += 5

    creature.shelter["comfort"] = comfort

    previous_level = creature.shelter["level"]

    new_level = 1

    for level, required in sorted(SHELTER_LEVELS.items()):

        if comfort >= required:
            new_level = level

    creature.shelter["level"] = new_level

    return {
        "comfort": comfort,
        "old_level": previous_level,
        "new_level": new_level,
        "leveled_up": new_level > previous_level
    }
