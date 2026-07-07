# ----------------------------------------
# Helper Functions
# ----------------------------------------
from data.preserves import PRESERVES

def get_preserve(preserve_id):
    return PRESERVES.get(preserve_id)


def get_preserve_capacity(player, preserve_id):
    """Calculate the current shelter capacity of a preserve."""

    preserve = PRESERVES[preserve_id]

    player_data = player.preserves.get(
        preserve_id,
        {"level": 1}
    )

    level = player_data.get("level", 1)

    return min(
        preserve["starting_capacity"]
        + (level - 1) * preserve["capacity_per_level"],
        len(preserve["shelter_sites"])
    )


def get_preserve_residents(player, preserve_id):
    """Return every creature currently living in this preserve."""

    return [
        creature
        for creature in player.creatures
        if creature.shelter.get("location") == preserve_id
    ]


def preserve_has_space(player, preserve_id):
    """Return True if the preserve has room for another shelter."""

    return (
        len(get_preserve_residents(player, preserve_id))
        < get_preserve_capacity(player, preserve_id)
    )


def get_available_shelter_sites(player, preserve_id):
    """Return every shelter site that hasn't been claimed."""

    preserve = PRESERVES[preserve_id]

    capacity = get_preserve_capacity(player, preserve_id)

    available_sites = preserve["shelter_sites"][:capacity]

    occupied_sites = {
        creature.shelter.get("site")
        for creature in get_preserve_residents(player, preserve_id)
        if creature.shelter.get("site")
    }

    return [
        site
        for site in available_sites
        if site not in occupied_sites
    ]

def get_available_preserves(player, creature):
    """
    Return preserves that:
    - are unlocked by the player
    - have available space
    - can house the creature species
    """

    available = []

    for preserve_id, preserve in PRESERVES.items():

        # Check player has unlocked this preserve
        player_data = player.preserves.get(preserve_id)

        if not player_data:
            continue

        if not player_data.get("unlocked", False):
            continue

        # Check capacity
        if not preserve_has_space(player, preserve_id):
            continue

        # Check species compatibility
        allowed_species = preserve.get(
            "available_creatures",
            []
        )

        # If no restrictions, allow all creatures
        if allowed_species:
            if creature.species not in allowed_species:
                continue

        available.append(preserve_id)

    return available
