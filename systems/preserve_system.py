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

from data.preserves import PRESERVES


def get_upgrade_cost(preserve_id, next_level):
    """Return the resource cost for upgrading to the given level."""

    preserve = PRESERVES[preserve_id]

    return preserve.get("upgrade_costs", {}).get(next_level)


def can_upgrade(player, preserve_id):
    """Check whether a preserve can currently be upgraded."""

    preserve = PRESERVES[preserve_id]

    current_level = player.preserves[preserve_id]["level"]

    if current_level >= preserve["max_level"]:
        return False, "This preserve is already fully restored."

    cost = get_upgrade_cost(
        preserve_id,
        current_level + 1
    )

    if cost is None:
        return False, "No upgrade data found."

    for item, amount in cost.items():

        if player.inventory.get(item, 0) < amount:
            return False, f"You need {amount}x {item.replace('_', ' ').title()}."

    return True, None


def upgrade_preserve(player, preserve_id):
    """Spend resources and upgrade the preserve."""

    success, reason = can_upgrade(
        player,
        preserve_id
    )

    if not success:
        return False, reason

    current_level = player.preserves[preserve_id]["level"]

    next_level = current_level + 1

    cost = get_upgrade_cost(
        preserve_id,
        next_level
    )

    for item, amount in cost.items():
        player.remove_from_inventory(item, amount)

    player.preserves[preserve_id]["level"] = next_level

    return True, next_level


def can_upgrade_preserve(player, preserve_id):

    preserve = player.preserves[preserve_id]

    level = preserve["level"]

    max_level = PRESERVES[preserve_id]["max_level"]

    if level >= max_level:
        return False

    return preserve["restoration"] >= restoration_required(level + 1)

def restoration_required(level):

    costs = {
        2: 100,
        3: 250,
        4: 500,
        5: 1000
    }

    return costs[level]

def upgrade_preserve(player, preserve_id):

    preserve = player.preserves[preserve_id]

    preserve["level"] += 1

    preserve["restoration"] = 0
