from datetime import datetime


def add_entry(player, category, text):

    if not hasattr(player, "journal_entries"):
        player.journal_entries = []

    player.journal_entries.append({
        "category": category,
        "text": text,
        "timestamp": datetime.now().isoformat()
    })

    # Keep newest 200 entries
    player.journal_entries = player.journal_entries[-200:]

def record_adoption(player, creature, named=True):

    if named:
        add_entry(
            player,
            "adoption",
            f"You welcomed {creature.name}, a {creature.species}, into Moonlit Meadows."
        )
    else:
        add_entry(
            player,
            "adoption",
            f"A wild {creature.species} chose to make Moonlit Meadows its home."
        )
    
    def record_discovery(player, species):

    add_entry(
        player,
        "discovery",
        f"You discovered a {species} while exploring."
    )

def record_bond(player, creature, level):

    add_entry(
        player,
        "bond",
        f"{creature.name} has become {level.title()} with you."
    )

def record_shelter_upgrade(player, creature):

    add_entry(
        player,
        "shelter",
        f"{creature.name}'s shelter was upgraded to Level {creature.shelter['level']}."
    )

def record_favourite_food(player, creature, food):

    add_entry(
        player,
        "memory",
        f"{creature.name} discovered they love {food}."
    )
