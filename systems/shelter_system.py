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

    # -----------------------------
    # Overall atmosphere
    # -----------------------------
    if comfort < 10:
        text = "The shelter is simple, with just a few comforts."
    elif comfort < 25:
        text = "The shelter feels warm and welcoming."
    elif comfort < 45:
        text = "The shelter is wonderfully cozy and well cared for."
    elif comfort < 70:
        text = "Every corner of the shelter feels thoughtfully decorated and inviting."
    else:
        text = "The shelter has become a breathtaking sanctuary, overflowing with comfort and personality."

    favorites = []
    decorations = []
    tag_counts = {}

    # -----------------------------
    # Scan every decoration
    # -----------------------------
    for entry in items:

        resource = RESOURCES.get(entry["item"])

        if not resource:
            continue

        name = resource.get("name", entry["item"])

        if entry.get("state") == "favorite":
            favorites.append(name)
        else:
            decorations.append(name)

        for tag in resource.get("tags", []):
            tag = tag.lower().strip()
            tag_counts[tag] = tag_counts.get(tag, 0) + 1

    # -----------------------------
    # Favourite decorations
    # -----------------------------
    if favorites:

        if len(favorites) == 1:
            text += f" Its favourite possession is **{favorites[0]}**, carefully displayed where everyone can admire it."

        elif len(favorites) == 2:
            text += f" Its favourite possessions are **{favorites[0]}** and **{favorites[1]}**."

        else:
            text += " Several treasured belongings have pride of place throughout the shelter."

    # -----------------------------
    # General decorations
    # -----------------------------
    if len(decorations) >= 3:
        text += " Decorations fill the space, making it feel truly lived in."

    elif decorations:
        text += " A few carefully chosen decorations add charm to the home."

    # -----------------------------
    # Tag flavour
    # -----------------------------
    if tag_counts.get("flowers", 0) >= 2:
        text += " Fragrant flowers bloom throughout the shelter, filling the air with a gentle scent."

    if tag_counts.get("plant", 0):
        text += " Lush greenery breathes life into every corner."

    if tag_counts.get("natural", 0):
        text += " Natural materials blend seamlessly into the surroundings."

    if tag_counts.get("glowing", 0):
        text += " A soft glow illuminates the shelter."

    if tag_counts.get("cozy", 0):
        text += " Thick blankets and soft bedding make the shelter feel wonderfully comfortable."

    if tag_counts.get("knowledge", 0):
        text += " Books and curious trinkets give the shelter a scholarly atmosphere."

    if tag_counts.get("crystal", 0):
        text += " Glittering crystals catch the light with every movement."

    if tag_counts.get("water", 0):
        text += " The gentle sound of flowing water brings a peaceful calm."

    if tag_counts.get("fire", 0):
        text += " A comforting warmth lingers throughout the shelter."

    if tag_counts.get("mushroom", 0):
        text += " Tiny mushrooms add an enchanting woodland feel."

    return text
