PRESERVES = {

    "elderwood": {
        "name": "Elderwood Preserve",
        "emoji": "🌲",
        "theme": "forest",

        "description": (
            "One of the oldest forests within Moonlit Meadows, Elderwood Preserve "
            "is a peaceful wilderness of towering trees, moss-covered stones, "
            "gentle streams, and hidden clearings."
        ),

        # Gameplay
        "starting_capacity": 3,
        "capacity_per_level": 2,
        "unlock_level": 1,

        # Allowed shelter types
        "allowed_shelters": [
            "Burrow",
            "Den",
            "Nest",
            "Tree Hollow",
            "Hollow Log"
        ],

        # Resources
        "resources": [
            "moss",
            "wildflowers",
            "berries",
            "sticks",
            "soft_bedding"
        ]
    },

    "emberlands": {
        "name": "Emberlands Preserve",
        "theme": "volcanic",
        "emoji": "🔥",

        "description": (
            "Fed by the warmth beneath Moonlit Meadows, Emberlands Preserve is a "
            "rugged landscape of volcanic stone, warm earth, glowing vents and "
            "gentle streams of lava. Though fierce in appearance, it provides a "
            "safe haven for creatures that thrive in heat."
        ),

        # Gameplay
        "starting_capacity": 3,
        "capacity_per_level": 2,
        "unlock_level": 1,

        # Allowed shelter types
        "allowed_shelters": [
            "Stone Den",
            "Den",
            "Cave",
            "Burrow"
        ],

        # Resources
        "resources": [
            "warm_pebbles",
            "charcoal",
            "ember_moss",
            "fire_crystal"
        ]
    },

    "frostwild": {
        "name": "Frostwild Preserve",
        "theme": "arctic",
        "emoji": "❄️",

        "description": (
            "Blanketed in snow throughout the year, Frostwild Preserve is a quiet "
            "expanse of frozen forests, glittering ice and peaceful silence. Hidden "
            "beneath the snow are warm dens where arctic creatures feel truly at home."
        ),

        # Gameplay
        "starting_capacity": 3,
        "capacity_per_level": 2,
        "unlock_level": 1,


        # Allowed shelter types
        "allowed_shelters": [
            "Snow Burrow",
            "Den",
            "Ice Cave",
            "Cave"
        ],

        # Resources
        "resources": [
            "ice_crystal",
            "snowberries",
            "frost_flower"
        ]
    },

    "crystal_reach": {
        "name": "Crystal Reach",
        "theme": "crystal",
        "emoji": "💎",

        "description": (
            "Towering crystal formations rise from the earth, filling the preserve "
            "with shimmering light. Every surface sparkles softly, creating a calm "
            "and enchanting home for creatures drawn to minerals and glowing caves."
        ),

        # Gameplay
        "starting_capacity": 3,
        "capacity_per_level": 2,
        "unlock_level": 1,


        # Allowed shelter types
        "allowed_shelters": [
            "Crystal Hollow",
            "Crystal Den",
            "Cave",
            "Stone Den"
        ],

        # Resources
        "resources": [
            "crystal_shard",
            "glow_mushroom",
            "crystal_dust"
        ]
    },

    "sunpetal_prairie": {
        "name": "Sunpetal Prairie",
        "theme": "grassland",
        "emoji": "🌼",

        "description": (
            "Rolling meadows stretch as far as the eye can see, dotted with wildflowers "
            "that sway gently in the breeze. It is a peaceful preserve where grazing "
            "and burrowing creatures flourish beneath open skies."
        ),

        # Gameplay
        "starting_capacity": 3,
        "capacity_per_level": 2,
        "unlock_level": 1,


        # Allowed shelter types
        "allowed_shelters": [
            "Burrow",
            "Nest",
            "Den"
        ],

        # Resources
        "resources": [
            "wildflowers",
            "soft_grass",
            "seeds",
            "herbs"
        ]
    },

    "mistfen": {
        "name": "Mistfen Preserve",
        "theme": "wetland",
        "emoji": "🌿",

        "description": (
            "A tranquil wetland of reeds, ponds and winding streams, Mistfen Preserve "
            "is often cloaked in a gentle morning mist. The rich wetlands support "
            "countless aquatic plants and creatures."
        ),

        # Gameplay
        "starting_capacity": 3,
        "capacity_per_level": 2,
        "unlock_level": 1,

        # Allowed shelter types
        "allowed_shelters": [
            "Reed Nest",
            "Burrow",
            "Driftwood Shelter"
        ],

        "resources": [
            "reeds",
            "water_lily",
            "smooth_stones",
            "fresh_water"
        ]
    }
}

# HELPER FUNCTIONS

def get_preserve(preserve_id):
    return PRESERVES.get(preserve_id)
