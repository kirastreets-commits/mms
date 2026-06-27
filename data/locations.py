# inside your data file
LOCATION_TYPES = ["inside", "grounds", "outside"]

LOCATIONS = {
    "sanctuary_core": {
        "name": "The Grand Hearth Hall",
        "type": "inside",
        "resources": [
            "soft_bedding",
            "large_cushions",
            "warm_pebbles"
        ],
        "available_creatures": [],
        "lore_chance": 0.15,
        "connected": ["healing_conservatory", "arcanum_archive", "feeding_hall", "sanctuary_gardens"]
    },

    "healing_conservatory": {
        "name": "The Healing Conservatory",
        "type": "inside",
        "resources": [
            "healing_moss",
            "glowing_mushrooms"
        ],
        "available_creatures": [],
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
        "available_creatures": [],
        "lore_chance": 0.15,
        "connected": ["sanctuary_gardens"]
    },

    "feeding_hall": {
        "name": "The Feeding Hall",
        "type": "inside",
        "resources": [
            "sweetberries"
        ],
        "available_creatures": [],
        "lore_chance": 0.15,
        "connected": ["sanctuary_gardens", "sanctuary_core"]
    },
        
    "sanctuary_gardens": {
        "name": "Moonlit Gardens",
        "type": "grounds",
        "resources": ["wildflowers"],
        "available_creatures": [],
        "lore_chance": 0.25,
        "connected": ["sanctuary_core", "moonlit_forest"]
    },

    "moonlit_forest": {
        "name": "Moonlit Forest",
        "type": "outside",
        "resources": [
            "soft_moss",
            "vines",
            "tree_roots",
            "thorn_branches"
        ],
        "available_creatures": ["Cinderware", "Emberfox", "Fernpaw", "Thornhare", "Mossling"],
        "lore_chance": 0.4,
        "connected": ["sanctuary_gardens", "emberlight_hollow", "frostpine_forest"]
    },
    
    "emberlight_hollow": {
        "name": "Emberlight Hollow",
        "type": "outside",
        "resources": [
            "obsidian_shards",
            "lava_rock",
            "heat_crystal",
            "mineral_salt_block",
            "glowing_mushrooms"
        ],
        "available_creatures": ["Stonehorn"],
        "lore_chance": 0.4,
        "connected": ["moonlit_forest"]
    },
    
    "frostpine_forest": {
        "name": "Frostpine Forest",
        "type": "outside",
        "resources": [
            "snow_puff_moss",
            "packed_snow",
            "frost_flowers"
        ],
        "available_creatures": ["Frostfox", "Frosthopper"],
        "lore_chance": 0.4,
        "connected": ["moonlit_forest"]
    }
}
