# ----------------------------------------
# Helper Functions
# ----------------------------------------

def get_preserve(preserve_id):
    return PRESERVES.get(preserve_id)


def get_preserve_capacity(player, preserve_id):
    """Calculate the current shelter capacity of a preserve."""

    preserve = PRESERVES[preserve_id]
    level = player.preserves[preserve_id]["level"]

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