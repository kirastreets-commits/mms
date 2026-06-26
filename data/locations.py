# inside your data file
LOCATION_TYPES = ["inside", "grounds", "outside"]

LOCATIONS = {
    "sanctuary_core": {
        "name": "The Grand Hearth Hall",
        "type": "inside",
        "resources": [
            "healing_moss",
            "warm_pebbles"
        ],
        "lore_chance": 0.15,
        "connected": ["healing_conservatory", "arcanum_archive", "sanctuary_gardens"]
    },

    "healing_conservatory": {
        "name": "The Healing Conservatory",
        "type": "inside",
        "resources": [
            "healing_moss",
            "glowing_mushrooms"
        ],
        "lore_chance": 0.15,
        "connected": ["sanctuary_gardens"]
    },

    "arcanum_archive": {
        "name": "The Arcanum Archive",
        "type": "inside",
        "resources": [
            "healing_moss",
            "warm_pebbles"
        ],
        "lore_chance": 0.15,
        "connected": ["sanctuary_gardens"]
    },

    "feeding_hall": {
        "name": "The Feeding Hall",
        "type": "inside",
        "resources": [
            "healing_moss",
            "warm_pebbles"
        ],
        "lore_chance": 0.15,
        "connected": ["sanctuary_gardens", "sanctuary_core"]
    },
        
    "sanctuary_gardens": {
        "name": "Moonlit Gardens",
        "type": "grounds",
        "resources": ["wildflowers"],
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

