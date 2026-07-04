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

def generate_shelter_description(creature):
    shelter = creature.shelter
    items = shelter.get("items", [])
    comfort = shelter.get("comfort", 0)

    # Overall atmosphere
    if comfort < 10:
        opening = "The shelter is simple, with just a few comforts."
    elif comfort < 25:
        opening = "The shelter feels warm and welcoming."
    elif comfort < 45:
        opening = "The shelter is wonderfully cozy and well cared for."
    elif comfort < 70:
        opening = "Every corner of the shelter feels thoughtfully decorated and inviting."
    else:
        opening = "The shelter has become a breathtaking sanctuary, overflowing with comfort and personality."

    # Mention favourite items
    favorites = []
    decorations = []

    from data.resources import RESOURCES

    for entry in items:
        resource = RESOURCES.get(entry["item"])
        if not resource:
            continue

        name = resource["name"]

        if entry.get("state") == "favorite":
            favorites.append(name)
        else:
            decorations.append(name)

    text = opening

    if favorites:
        if len(favorites) == 1:
            text += f" Its favourite possession is **{favorites[0]}**, carefully displayed where everyone can see it."
        elif len(favorites) == 2:
            text += f" Its favourite possessions are **{favorites[0]}** and **{favorites[1]}**."
        else:
            text += " Several treasured belongings have pride of place throughout the shelter."

    if len(decorations) >= 3:
        text += " Decorations fill the space, making it feel truly lived in."
    elif len(decorations) > 0:
        text += " A few carefully chosen decorations add charm to the home."

    return text
