# inside your data file
LOCATION_TYPES = ["inside", "grounds", "outside"]

LOCATIONS = {
    "sanctuary_core": {
        "name": "The Grand Hearth Hall",
        "type": "inside",
        "resources": [
            "soft_bedding",
            "large_cushions",
            "warm_pebbles",
            "fireplace_stone",
            "hearth_blanket",
            "everwarm_coal",
            "knitted_pillow"
        ],
        "available_creatures": ["Emberbun"],
        "lore_chance": 0.15,
        "lore": ["**Caretaker's Note**: 'If you wake to find an Emberbun "
        "sleeping beside you, consider yourself fortunate. "
        "They have a habit of finding those who need comfort "
        "before they realize it themselves.'"],
        "connected": ["healing_conservatory", "arcanum_archive", "feeding_hall", "sanctuary_gardens"]
    },

    "healing_conservatory": {
        "name": "The Healing Conservatory",
        "type": "inside",
        "resources": [
            "healing_moss",
            "glowing_mushrooms",
            "wild_lavender",
            "healing_herbs"
        ],
        "available_creatures": ["Glowfern"],
        "lore_chance": 0.15,
        "lore": ["**Caretaker's Note**:'Leave a bowl of fresh dew near "
        "the herb beds before dawn. If it's empty by sunrise, a "
        "Glowfern has accepted your kindness. If it leaves a sprig of "
        "lavender behind, you've earned its trust."],
        "connected": ["sanctuary_gardens"]
    },

    "arcanum_archive": {
        "name": "The Arcanum Archive",
        "type": "inside",
        "resources": [
            "velvet_reading_cushion",
            "handwritten_research_note"
        ],
        "available_creatures": ["Whispermoth"],
        "lore_chance": 0.15,
        "lore": ["**Caretaker's Note**: 'If a Whispermoth settles upon your book, "
        "don't turn the page just yet. The elders say it has found a passage worth remembering.'"],
        "connected": ["sanctuary_gardens"]
    },

    "feeding_hall": {
        "name": "The Feeding Hall",
        "type": "inside",
        "resources": [
            "sweetberries",
            "woven_basket",
            "grain_sack",
            "picnic_blanket"
        ],
        "available_creatures": ["Crumblepuff"],
        "lore_chance": 0.15,
        "lore": ["**Caretaker's Note**:'Never shoo away a Crumblepuff after supper. It isn't begging—it "
        "simply wants to make sure no creature goes to bed hungry.'"
        ],
        "connected": ["sanctuary_gardens", "sanctuary_core"]
    },
        
    "sanctuary_gardens": {
        "name": "Moonlit Gardens",
        "type": "grounds",
        "resources": [
            "wildflowers",
            "picnic_blanket",
            "firebloom_petals",
            "wild_lavender",
            "sweet_grass",
            "golden_nectar",
            "moonflower_petals"
            ],
        "available_creatures": ["Lunabloom"],
        "lore_chance": 0.25,
        "lore": ["**Caretaker's Note**: Don't chase a Lunabloom. "
        "Sit quietly instead. "
        "If it believes your heart is gentle, it will be the one to approach you."
        ],
        "connected": ["sanctuary_core", "moonlit_forest"]
    },

    "moonlit_forest": {
        "name": "Moonlit Forest",
        "type": "outside",
        "resources": [
            "soft_moss",
            "vines",
            "tree_roots",
            "thorn_branches",
            "healing_moss",
            "sweetberries",
            "glowing_mushrooms",
            "wild_lavender"
        ],
        "available_creatures": ["Cinderware", "Emberfox", "Fernpaw", "Thornhare", "Mossling"],
        "lore_chance": 0.4,
        "lore": [
            "**Caretaker's Note**: 'The Moonlit Forest does not sleep. It listens. Walk too loudly, and you will only find silence where paths once were.'",
            "**Caretaker's Note**: 'If the fireflies gather above your head here, do not fear. They are not watching you — they are guiding you back out.'"
        ],
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
        "lore": [
            "**Caretaker's Note**: 'Stonehorns are not born in Emberlight Hollow. They are carved into being by heat, pressure, and time. Treat them gently—they remember the fire that made them.'",
            "**Caretaker's Note**: 'The ground here breathes. If you feel it shift beneath your feet, it is not anger. It is waking.'"
        ],
        "connected": ["moonlit_forest", "ashenpeak_highlands"]
    },

    "ashenpeak_highlands": {
        "name": "Ashenpeak Highlands",
        "type": "outside",
        "resources": [
            "obsidian_shards",
            "lava_rock",
            "heat_crystal",
            "mineral_salt_block",
            "warm_pebbles",
            "firebloom_petals",
            "everwarm_coal",
            "glowing_mushrooms"
        ],
        "available_creatures": ["Stonehorn", "Fire Dragon"],
        "lore_chance": 0.4,
        "lore": [
            "The Ashenpeak Highlands remind all who visit that even the fiercest fire can become a source of warmth, life, and home.",
            "Many fire-affinity creatures make their homes among these warm cliffs, where lava, stone, and steam offer both shelter and safety.",
            "Towering above Emberlight Hollow, the Ashenpeak Highlands are a chain of ancient volcanoes whose gentle warmth has shaped the land for centuries."
        ],
        "connected": ["moonlit_forest", "emberlight_hollow"]
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
        "lore": [
            "**Caretaker's Note**: 'Frostfoxes do not leave tracks for long. If you see one, remember the direction it came from — it may be the only way back.'",
            "**Caretaker's Note**: 'The frostpines sing when the wind is right. It is said they are mourning something that has not yet happened.'"
        ],
        "connected": ["moonlit_forest"]
    }
}
