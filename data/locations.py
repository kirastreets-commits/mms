LOCATIONS = {
    "sanctuary_core": {
        "name": "Sanctuary Core",
        "type": "inside",
        "items": ["healing_moss"],
        "lore_chance": 0.15,
        "connected": ["healing_den", "sanctuary_gardens"]
    },

    "sanctuary_gardens": {
        "name": "Moonlit Gardens",
        "type": "grounds",
        "items": ["sweetberries", "moonflowers"],
        "lore_chance": 0.25,
        "connected": ["sanctuary_core", "moonlit_forest"]
    },

    "moonlit_forest": {
        "name": "Moonlit Forest",
        "type": "outside",
        "items": ["rare_herbs"],
        "lore_chance": 0.4,
        "connected": ["sanctuary_gardens"]
    }
}
