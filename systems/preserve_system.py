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

        # -----------------------------
        # Progression
        # -----------------------------
        "starting_capacity": 3,
        "capacity_per_level": 2,
        "max_level": 5,
        "unlock_level": 1,

        # -----------------------------
        # Upgrade Bonuses
        # -----------------------------
        "upgrade_bonuses": {
            2: {
                "capacity": 2,
                "comfort": 2,
                "description": "Additional shelter sites are restored."
            },
            3: {
                "capacity": 2,
                "comfort": 4,
                "resource_bonus": 10,
                "description": "Wild resources flourish throughout the preserve."
            },
            4: {
                "capacity": 2,
                "comfort": 6,
                "resource_bonus": 20,
                "rare_event_bonus": 5,
                "description": "The preserve attracts many wandering creatures."
            },
            5: {
                "capacity": 2,
                "comfort": 10,
                "resource_bonus": 30,
                "rare_event_bonus": 10,
                "bond_bonus": 1,
                "description": "The preserve has become a sanctuary of exceptional beauty."
            }
        },

        # -----------------------------
        # Upgrade Projects
        # -----------------------------
        "upgrade_names": {
            2: "Restore Woodland Paths",
            3: "Plant Ancient Saplings",
            4: "Create Wildlife Glades",
            5: "Awaken the Elder Grove"
        },

        "level_descriptions": {
            1: "A newly restored preserve with only a few safe shelters.",
            2: "Well-maintained paths now connect several comfortable homes.",
            3: "Wildlife has begun returning and the preserve feels alive.",
            4: "The preserve flourishes with abundant life and thriving shelters.",
            5: "One of the greatest sanctuaries in Moonlit Meadows, overflowing with life."
        },


        # -----------------------------
        # Passive Bonuses
        # -----------------------------
        "passive_effects": [
            "Forest creatures recover extra Energy while resting.",
            "Gathering berries is slightly more rewarding.",
            "Occasionally attracts woodland visitors."
        ],

        # -----------------------------
        # Rare Events
        # -----------------------------
        "events": [
            "A family of birds builds a nest nearby.",
            "A curious fox leaves behind a shiny trinket.",
            "Ancient trees seem to hum quietly at dusk.",
            "A hidden spring begins flowing once again."
        ],

        # -----------------------------
        # Shelter Types
        # -----------------------------
        "allowed_shelters": [
            "Burrow",
            "Den",
            "Nest",
            "Tree Hollow",
            "Hollow Log"
        ],

        # Named shelter sites
        "shelter_sites": [
            "Mossy Hollow",
            "Old Oak Burrow",
            "Fern Clearing",
            "Whispering Roots",
            "Foxglove Grove",
            "Ancient Oak Hollow",
            "Sunlit Knoll",
            "Hidden Spring",
            "Willow Thicket",
            "Stone Moss Den",
            "Twilight Hollow"
        ],

        # -----------------------------
        # Resources
        # -----------------------------
        "resources": [
            "moss",
            "wildflowers",
            "berries",
            "sticks",
            "soft_bedding"
        ],

        # -----------------------------
        # Atmosphere
        # -----------------------------
        "atmosphere": [
            "A gentle breeze rustles through the towering trees.",
            "Birdsong echoes throughout the preserve.",
            "Golden rays of sunlight filter through the forest canopy.",
            "The scent of moss and damp earth fills the air."
        ],

        # -----------------------------
        # Weather
        # -----------------------------
        "possible_weather": [
            "Sunny",
            "Light Rain",
            "Morning Mist"
        ],

        # -----------------------------
        # Discoveries
        # -----------------------------
        "discoveries": [
            "Ancient Stone Circle",
            "Hidden Wildflower Patch",
            "Forgotten Woodland Shrine",
            "Crystal Spring"
        ],

        "upgrade_costs": {
            2: {
                "wood": 30,
                "stone": 20
            },
            3: {
                "wood": 60,
                "stone": 40,
                "healing_moss": 15
            },
            4: {
                "wood": 90,
                "stone": 70,
                "crystal_shard": 20
            },
            5: {
                "wood": 120,
                "stone": 100,
                "moon_crystal": 30
            }
        },
    },

    "emberlands": {
        "name": "Emberlands Preserve",
        "emoji": "🔥",
        "theme": "volcanic",

        "description": (
            "Fed by the warmth beneath Moonlit Meadows, Emberlands Preserve is a "
            "rugged landscape of volcanic stone, glowing vents and rivers of lava."
        ),

        "starting_capacity": 3,
        "capacity_per_level": 2,
        "max_level": 5,
        "unlock_level": 1,

        "level_descriptions": {
            1: "A handful of cooled caverns provide safe shelter among the volcanic stone.",
            2: "Old lava paths have been cleared, making travel much safer.",
            3: "Warm crystal vents return, filling the preserve with gentle heat.",
            4: "The volcanic landscape is thriving with life adapted to the fire.",
            5: "The legendary Ember Heart burns peacefully, making this a haven for fire creatures."
        },

        # -----------------------------
        # Upgrade Bonuses
        # -----------------------------
        "upgrade_bonuses": {
            2: {
                "capacity": 2,
                "comfort": 2,
                "description": "Additional shelter sites are restored."
            },
            3: {
                "capacity": 2,
                "comfort": 4,
                "resource_bonus": 10,
                "description": "Wild resources flourish throughout the preserve."
            },
            4: {
                "capacity": 2,
                "comfort": 6,
                "resource_bonus": 20,
                "rare_event_bonus": 5,
                "description": "The preserve attracts many wandering creatures."
            },
            5: {
                "capacity": 2,
                "comfort": 10,
                "resource_bonus": 30,
                "rare_event_bonus": 10,
                "bond_bonus": 1,
                "description": "The preserve has become a sanctuary of exceptional beauty."
            }
        },

        "upgrade_names": {
        2: "Clear Ashfall Trails",
        3: "Stabilise Lava Vents",
        4: "Restore Firestone Caverns",
        5: "Awaken the Ember Heart"
    },

    "passive_effects": [
        "Fire creatures recover more Health while resting.",
        "Warm resources appear more often.",
        "Rare fire crystals occasionally emerge."
    ],

    "events": [
        "Warm embers drift gently through the preserve.",
        "A dormant lava vent briefly glows.",
        "Fire crystals erupt from the stone.",
        "The mountain lets out a peaceful rumble."
    ],

        "allowed_shelters": [
            "Stone Den",
            "Den",
            "Cave",
            "Burrow"
        ],

        "shelter_sites": [
            "Ashfall Cave",
            "Ember Hollow",
            "Basalt Burrow",
            "Lava Tube",
            "Scorched Ridge",
            "Smoldering Cavern",
            "Firestone Hollow",
            "Molten Pass",
            "Obsidian Shelter",
            "Cinder Grove",
            "Blazing Crag"
        ],

        "resources": [
            "warm_pebbles",
            "charcoal",
            "ember_moss",
            "fire_crystal"
        ],

        "atmosphere": [
            "Warm air rises from the earth.",
            "Tiny embers drift lazily through the preserve.",
            "The distant rumble of the volcano echoes softly.",
            "Heat radiates from the black stone beneath your feet."
        ],

        "possible_weather": [
            "Clear",
            "Ashfall",
            "Heat Haze"
        ],

        "discoveries": [
            "Ancient Lava Shrine",
            "Fire Crystal Vein",
            "Hidden Lava Tube"
        ],

        "upgrade_costs": {
            2: {
                "wood": 30,
                "stone": 20
            },
            3: {
                "wood": 60,
                "stone": 40,
                "healing_moss": 15
            },
            4: {
                "wood": 90,
                "stone": 70,
                "crystal_shard": 20
            },
            5: {
                "wood": 120,
                "stone": 100,
                "moon_crystal": 30
            }
        },
    },

    "frostwild": {
        "name": "Frostwild Preserve",
        "emoji": "❄️",
        "theme": "arctic",

        "description": (
            "Blanketed in snow throughout the year, Frostwild Preserve is a peaceful "
            "land of frozen forests, icy lakes and sparkling glaciers."
        ),

        "starting_capacity": 3,
        "capacity_per_level": 2,
        "max_level": 5,
        "unlock_level": 1,

        "level_descriptions": {
            1: "Only a few sheltered snow dens have been restored.",
            2: "Safe trails now connect the frozen shelters.",
            3: "Ancient glaciers sparkle with renewed life.",
            4: "Auroras regularly dance across the night sky.",
            5: "Frostwild has become a peaceful kingdom of snow and ice."
        },

        # -----------------------------
        # Upgrade Bonuses
        # -----------------------------
        "upgrade_bonuses": {
            2: {
                "capacity": 2,
                "comfort": 2,
                "description": "Additional shelter sites are restored."
            },
            3: {
                "capacity": 2,
                "comfort": 4,
                "resource_bonus": 10,
                "description": "Wild resources flourish throughout the preserve."
            },
            4: {
                "capacity": 2,
                "comfort": 6,
                "resource_bonus": 20,
                "rare_event_bonus": 5,
                "description": "The preserve attracts many wandering creatures."
            },
            5: {
                "capacity": 2,
                "comfort": 10,
                "resource_bonus": 30,
                "rare_event_bonus": 10,
                "bond_bonus": 1,
                "description": "The preserve has become a sanctuary of exceptional beauty."
            }
        },

        "upgrade_names": {
        2: "Strengthen Snow Paths",
        3: "Restore Frozen Springs",
        4: "Raise Ice Shelters",
        5: "Blessing of the Aurora"
    },

        "passive_effects": [
            "Cold creatures lose less Energy.",
            "Ice resources become more common.",
            "Snowstorms reveal hidden treasures."
        ],

        "events": [
            "An aurora illuminates the night sky.",
            "Fresh snow blankets every shelter.",
            "Ice crystals form beautiful patterns.",
            "A glacier softly cracks in the distance."
    ],

        "allowed_shelters": [
            "Snow Burrow",
            "Den",
            "Ice Cave",
            "Cave"
        ],

        "shelter_sites": [
            "Snowdrift Burrow",
            "Frozen Hollow",
            "Crystal Ice Cave",
            "Aurora Ridge",
            "Glacier Den",
            "Winter Hollow",
            "Ice Blossom Grove",
            "Frostpine Shelter",
            "Silent Cavern",
            "Snowy Clearing",
            "Shimmering Glacier"
        ],

        "resources": [
            "ice_crystal",
            "snowberries",
            "frost_flower"
        ],

        "atmosphere": [
            "Snowflakes drift silently through the air.",
            "The crisp air sparkles beneath the sunlight.",
            "Everything is wonderfully quiet.",
            "A shimmering aurora dances overhead."
        ],

        "possible_weather": [
            "Snow",
            "Blizzard",
            "Clear Skies"
        ],

        "discoveries": [
            "Frozen Waterfall",
            "Ice Crystal Cavern",
            "Ancient Frost Totem"
        ],

        "upgrade_costs": {
            2: {
                "wood": 30,
                "stone": 20
            },
            3: {
                "wood": 60,
                "stone": 40,
                "healing_moss": 15
            },
            4: {
                "wood": 90,
                "stone": 70,
                "crystal_shard": 20
            },
            5: {
                "wood": 120,
                "stone": 100,
                "moon_crystal": 30
            }
        },
    },

    "crystal_reach": {
        "name": "Crystal Reach",
        "emoji": "💎",
        "theme": "crystal",

        "description": (
            "Towering crystal formations fill the landscape with shimmering light."
        ),

        "starting_capacity": 3,
        "capacity_per_level": 2,
        "max_level": 5,
        "unlock_level": 1,

        # Crystal Reach
        "level_descriptions": {
            1: "Only a handful of crystal caverns have been made safe for creatures.",
            2: "Ancient crystal bridges shimmer once more between the towering formations.",
            3: "The great crystal spires resonate with gentle magical energy.",
            4: "Radiant caverns illuminate the preserve day and night.",
            5: "Crystal Reach has become a legendary sanctuary of light and living crystal."
        },

        # -----------------------------
        # Upgrade Bonuses
        # -----------------------------
        "upgrade_bonuses": {
            2: {
                "capacity": 2,
                "comfort": 2,
                "description": "Additional shelter sites are restored."
            },
            3: {
                "capacity": 2,
                "comfort": 4,
                "resource_bonus": 10,
                "description": "Wild resources flourish throughout the preserve."
            },
            4: {
                "capacity": 2,
                "comfort": 6,
                "resource_bonus": 20,
                "rare_event_bonus": 5,
                "description": "The preserve attracts many wandering creatures."
            },
            5: {
                "capacity": 2,
                "comfort": 10,
                "resource_bonus": 30,
                "rare_event_bonus": 10,
                "bond_bonus": 1,
                "description": "The preserve has become a sanctuary of exceptional beauty."
            }
        },

        "upgrade_names": {
            2: "Restore Crystal Bridges",
            3: "Polish Ancient Formations",
            4: "Illuminate the Crystal Caves",
            5: "Heart of the Reach"
        },

        "passive_effects": [
            "Crystal creatures gain additional Happiness.",
            "Crystal resources are more abundant.",
            "Rare gems occasionally appear."
        ],

        "events": [
            "Sunlight scatters through thousands of crystals.",
            "A hidden chamber begins glowing.",
            "Crystal chimes echo softly.",
            "Tiny gemstones emerge overnight."
        ],

        "allowed_shelters": [
            "Crystal Hollow",
            "Crystal Den",
            "Cave",
            "Stone Den"
        ],

        "shelter_sites": [
            "Amethyst Hollow",
            "Crystal Cavern",
            "Shimmering Grotto",
            "Quartz Ridge",
            "Prism Hollow",
            "Glittering Cavern",
            "Moonstone Den",
            "Crystal Garden",
            "Gemstone Pass",
            "Radiant Hollow",
            "Echo Crystal Cave"
        ],

        "resources": [
            "crystal_shard",
            "glow_mushroom",
            "crystal_dust"
        ],

        "atmosphere": [
            "Crystals sparkle in every direction.",
            "Soft light dances across the cavern walls.",
            "Tiny fragments shimmer beneath your feet."
        ],

        "possible_weather": [
            "Clear",
            "Crystal Rain"
        ],

        "discoveries": [
            "Heart Crystal",
            "Glowing Cavern",
            "Ancient Crystal Altar"
        ]
    },

    "sunpetal_prairie": {
        "name": "Sunpetal Prairie",
        "emoji": "🌼",
        "theme": "grassland",

        "description": (
            "Rolling meadows filled with colourful wildflowers stretch beneath open skies."
        ),

        "starting_capacity": 3,
        "capacity_per_level": 2,
        "max_level": 5,
        "unlock_level": 1,

        # Sunpetal Prairie
        "level_descriptions": {
            1: "A few peaceful meadows provide safe shelter among the wildflowers.",
            2: "Blooming flower fields stretch further across the prairie.",
            3: "Bees and butterflies return in great numbers, bringing life to every corner.",
            4: "Golden meadows sway beneath endless skies, alive with colour.",
            5: "Sunpetal Prairie has become a breathtaking sea of flowers and thriving wildlife."
        },

        # -----------------------------
        # Upgrade Bonuses
        # -----------------------------
        "upgrade_bonuses": {
            2: {
                "capacity": 2,
                "comfort": 2,
                "description": "Additional shelter sites are restored."
            },
            3: {
                "capacity": 2,
                "comfort": 4,
                "resource_bonus": 10,
                "description": "Wild resources flourish throughout the preserve."
            },
            4: {
                "capacity": 2,
                "comfort": 6,
                "resource_bonus": 20,
                "rare_event_bonus": 5,
                "description": "The preserve attracts many wandering creatures."
            },
            5: {
                "capacity": 2,
                "comfort": 10,
                "resource_bonus": 30,
                "rare_event_bonus": 10,
                "bond_bonus": 1,
                "description": "The preserve has become a sanctuary of exceptional beauty."
            }
        },

        "upgrade_names": {
            2: "Expand Flower Fields",
            3: "Restore Bee Gardens",
            4: "Create Butterfly Sanctuaries",
            5: "Bloom of the Endless Prairie"
        },

        "passive_effects": [
            "Grassland creatures become happier while resting.",
            "Flowers grow more frequently.",
            "Butterflies occasionally guide you to resources."
        ],

        "events": [
            "Butterflies gather across the meadow.",
            "Rare flowers bloom overnight.",
            "A rainbow appears after gentle rain.",
            "Honeybees create a thriving hive."
        ],

        "allowed_shelters": [
            "Burrow",
            "Nest",
            "Den"
        ],

        "shelter_sites": [
            "Buttercup Hollow",
            "Sunflower Knoll",
            "Wildflower Burrow",
            "Golden Meadow",
            "Bluebell Rise",
            "Daisy Hollow",
            "Poppy Field",
            "Sunny Clearing",
            "Breezy Hill",
            "Honey Meadow",
            "Lavender Hollow"
        ],

        "resources": [
            "wildflowers",
            "soft_grass",
            "seeds",
            "herbs"
        ],

        "atmosphere": [
            "Wildflowers sway gently in the breeze.",
            "Butterflies drift between colourful blossoms.",
            "The warm sun bathes the prairie in golden light."
        ],

        "possible_weather": [
            "Sunny",
            "Cloudy",
            "Spring Shower"
        ],

        "discoveries": [
            "Rare Flower Patch",
            "Butterfly Grove",
            "Hidden Meadow"
        ],

        "upgrade_costs": {
            2: {
                "wood": 30,
                "stone": 20
            },
            3: {
                "wood": 60,
                "stone": 40,
                "healing_moss": 15
            },
            4: {
                "wood": 90,
                "stone": 70,
                "crystal_shard": 20
            },
            5: {
                "wood": 120,
                "stone": 100,
                "moon_crystal": 30
            }
        },
    },

    "mistfen": {
        "name": "Mistfen Preserve",
        "emoji": "🌿",
        "theme": "wetland",

        "description": (
            "A peaceful wetland of winding streams, reeds and quiet ponds."
        ),

        "starting_capacity": 3,
        "capacity_per_level": 2,
        "max_level": 5,
        "unlock_level": 1,

       # Mistfen
        "level_descriptions": {
            1: "A quiet marsh with only a few restored nesting grounds.",
            2: "Safe boardwalks now weave through the mist-covered wetlands.",
            3: "The ponds and reeds teem with returning wildlife.",
            4: "Crystal-clear springs nourish every corner of the preserve.",
            5: "Mistfen has become a tranquil sanctuary where water and wildlife flourish together."
        },

        # -----------------------------
        # Upgrade Bonuses
        # -----------------------------
        "upgrade_bonuses": {
            2: {
                "capacity": 2,
                "comfort": 2,
                "description": "Additional shelter sites are restored."
            },
            3: {
                "capacity": 2,
                "comfort": 4,
                "resource_bonus": 10,
                "description": "Wild resources flourish throughout the preserve."
            },
            4: {
                "capacity": 2,
                "comfort": 6,
                "resource_bonus": 20,
                "rare_event_bonus": 5,
                "description": "The preserve attracts many wandering creatures."
            },
            5: {
                "capacity": 2,
                "comfort": 10,
                "resource_bonus": 30,
                "rare_event_bonus": 10,
                "bond_bonus": 1,
                "description": "The preserve has become a sanctuary of exceptional beauty."
            }
        },

        "upgrade_names": {
            2: "Restore Boardwalks",
            3: "Protect Lily Ponds",
            4: "Expand Wetlands",
            5: "Heart of the Marsh"
        },

        "passive_effects": [
            "Wetland creatures recover additional Energy.",
            "Water resources become more common.",
            "Peaceful wildlife visits more often."
        ],

        "events": [
            "Morning mist blankets the preserve.",
            "Dragonflies dance over the water.",
            "A family of frogs returns.",
            "A hidden spring is discovered."
        ],

        "allowed_shelters": [
            "Reed Nest",
            "Burrow",
            "Driftwood Shelter"
        ],

        "shelter_sites": [
            "Reed Haven",
            "Willow Bank",
            "Misty Hollow",
            "Driftwood Point",
            "Lily Pond",
            "Foggy Nest",
            "Heron Marsh",
            "Quiet Creek",
            "Silver Reeds",
            "Water's Edge",
            "Hidden Lagoon"
        ],

        "resources": [
            "reeds",
            "water_lily",
            "smooth_stones",
            "fresh_water"
        ],

        "atmosphere": [
            "A blanket of mist hangs over the water.",
            "The gentle croaking of frogs echoes through the marsh.",
            "Dragonflies skim across the still ponds."
        ],

        "possible_weather": [
            "Fog",
            "Rain",
            "Sunny"
        ],

        "discoveries": [
            "Ancient Boardwalk",
            "Hidden Pond",
            "Rare Water Lily"
        ],

        "upgrade_costs": {
            2: {
                "wood": 30,
                "stone": 20
            },
            3: {
                "wood": 60,
                "stone": 40,
                "healing_moss": 15
            },
            4: {
                "wood": 90,
                "stone": 70,
                "crystal_shard": 20
            },
            5: {
                "wood": 120,
                "stone": 100,
                "moon_crystal": 30
            }
        },
    }
}
