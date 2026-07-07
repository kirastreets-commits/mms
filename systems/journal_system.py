from datetime import datetime

CATEGORY_ICONS = {
    "adoption": "🏡",
    "discovery": "🐾",
    "bond": "❤️",
    "shelter": "🛖",
    "memory": "✨",
    "lore": "📜",
    "milestone": "⭐"
}

def add_entry(player, category, text, day=None):
    """Add a journal entry to the player's journal."""

    if not hasattr(player, "journal_entries"):
        player.journal_entries = []

    player.journal_entries.append({
        "category": category,
        "text": text,
        "day": day,
        "timestamp": datetime.now().isoformat()
    })

    # Keep only the most recent 200 entries
    player.journal_entries = player.journal_entries[-200:]


def record_adoption(player, creature, named=True):
    """Record a creature joining the sanctuary."""

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
    """Record discovering a new species."""

    add_entry(
        player,
        "discovery",
        f"You discovered a {species} while exploring."
    )


def record_bond(player, creature, level):
    """Record reaching a new bond level."""

    add_entry(
        player,
        "bond",
        f"{creature.name} has become {level.title()} with you."
    )


def record_shelter_upgrade(player, creature):
    """Record a shelter upgrade."""

    add_entry(
        player,
        "shelter",
        f"{creature.name}'s shelter was upgraded to Level {creature.shelter['level']}."
    )


def record_memory(player, creature, text):
    """Record a memorable event."""

    add_entry(
        player,
        "memory",
        text
    )

def record_settlement(player, creature, preserve):
    """Record a creature settling in a preserve."""
    add_entry(
        player,
        "shelter",
        f"{creature.name} settled in {preserve['name']}."
    )
