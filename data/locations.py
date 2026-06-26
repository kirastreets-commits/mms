# inside your data file
LOCATION_TYPES = ["inside", "grounds", "outside"]

LOCATIONS = {
    "sanctuary_core": {
        "name": "Sanctuary Core",
        "type": "inside",
        "resources": ["healing_moss"],
        "lore_chance": 0.15,
        "connected": ["healing_room", "sanctuary_gardens"]
    },

    "healing_room": {
        "name": "Healing Room",
        "type": "inside",
        "resources": ["healing_moss, glowing_mushrooms"],
        "lore_chance": 0.15,
        "connected": ["sanctuary_gardens"]
    },

    "sanctuary_gardens": {
        "name": "Moonlit Gardens",
        "type": "grounds",
        "resources": ["sweetberries", "moonflowers"],
        "lore_chance": 0.25,
        "connected": ["sanctuary_core", "moonlit_forest"]
    },

    "moonlit_forest": {
        "name": "Moonlit Forest",
        "type": "outside",
        "resources": ["rare_herbs"],
        "lore_chance": 0.4,
        "connected": ["sanctuary_gardens"]
    }
}

