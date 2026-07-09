PAGE_SIZE = 6


def get_entries_by_category(player, category):

    if not hasattr(player, "journal_entries"):
        return []

    return [
        entry
        for entry in player.journal_entries
        if entry.get("category") == category
    ]


def format_entry(entry):

    icons = {
        "adoption": "🐾",
        "discovery": "🌿",
        "bond": "❤️",
        "shelter": "🏡",
        "memory": "✨",
        "lore": "📜"
    }

    icon = icons.get(
        entry.get("category"),
        "📖"
    )

    return (
        f"{icon} {entry.get('text')}"
    )


def paginate(entries, page):

    start = page * PAGE_SIZE
    end = start + PAGE_SIZE

    return entries[start:end]