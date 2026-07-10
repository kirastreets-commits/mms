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

        # ---------------------------------
        # Progression
        # ---------------------------------
        "starting_capacity": 3,
        "capacity_per_level": 2,
        "max_level": 5,
        "unlock_level": 1,

        # ---------------------------------
        # Upgrade Projects
        # ---------------------------------
        "upgrade_names": {
            2: "Restore Woodland Paths",
            3: "Plant Ancient Saplings",
            4: "Create Wildlife Glades",
            5: "Awaken the Elder Grove"
        },

        "level_descriptions": {
            1: (
                "Only a handful of shelters have been restored. "
                "Much of the preserve remains overgrown and forgotten."
            ),

            2: (
                "Safe woodland trails wind beneath the trees, making it easier "
                "for creatures to travel between their homes."
            ),

            3: (
                "Ancient saplings and native plants have been replanted. "
                "Birdsong fills the forest once more."
            ),

            4: (
                "Open glades provide peaceful gathering places while wildlife "
                "returns to every corner of the preserve."
            ),

            5: (
                "The legendary Elder Grove has awakened. Ancient trees radiate "
                "gentle magic that comforts every creature living here."
            )
        },

        # ---------------------------------
        # Upgrade Costs
        # ---------------------------------
        "upgrade_costs": {

            2: {
                "wood": 40,
                "sticks": 30,
                "moss": 20,
                "soft_bedding": 15
            },

            3: {
                "wood": 70,
                "berries": 40,
                "wildflowers": 35,
                "moss": 30
            },

            4: {
                "wood": 100,
                "wildflowers": 60,
                "berries": 50,
                "soft_bedding": 40
            },

            5: {
                "wood": 150,
                "wildflowers": 80,
                "berries": 80,
                "moss": 60,
                "crystal_shard": 15
            }
        },

        # ---------------------------------
        # Bonuses
        # ---------------------------------
        "upgrade_bonuses": {

            2: {
                "capacity": 2,
                "comfort": 2,
                "description": (
                    "Additional woodland shelters become available."
                )
            },

            3: {
                "capacity": 2,
                "comfort": 4,
                "resource_bonus": 10,
                "description": (
                    "Forest plants begin naturally replenishing."
                )
            },

            4: {
                "capacity": 2,
                "comfort": 6,
                "resource_bonus": 20,
                "rare_event_bonus": 5,
                "description": (
                    "Wild creatures are drawn to the flourishing forest."
                )
            },

            5: {
                "capacity": 2,
                "comfort": 10,
                "resource_bonus": 30,
                "rare_event_bonus": 10,
                "bond_bonus": 1,
                "description": (
                    "The Elder Grove grants peace to every resident."
                )
            }
        },

        # ---------------------------------
        # Passive Effects
        # ---------------------------------
        "passive_effects": [

            "Forest creatures recover +5 Energy while resting.",

            "Gathering has a higher chance of finding berries.",

            "Rare woodland visitors occasionally appear.",

            "Creatures living here slowly gain Trust over time."
        ],

        # ---------------------------------
        # Random Events
        # ---------------------------------
        "events": [

            "A family of birds builds a nest nearby.",

            "A curious fox leaves behind a polished stone.",

            "Ancient trees softly hum beneath the moonlight.",

            "A hidden spring begins flowing once again.",

            "Butterflies gather around a newly blooming clearing.",

            "A shy woodland spirit briefly watches from afar.",

            "Fresh berries ripen earlier than expected.",

            "Fireflies illuminate the forest after sunset."
        ],

        # ---------------------------------
        # Shelter Types
        # ---------------------------------
        "allowed_shelters": [
            "Burrow",
            "Den",
            "Nest",
            "Tree Hollow",
            "Hollow Log"
        ],

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

        # ---------------------------------
        # Resources
        # ---------------------------------
        "resources": [
            "moss",
            "wildflowers",
            "berries",
            "sticks",
            "soft_bedding"
        ],

        # ---------------------------------
        # Atmosphere
        # ---------------------------------
        "atmosphere": [

            "A gentle breeze rustles through the towering trees.",

            "Birdsong echoes throughout the preserve.",

            "Golden sunlight filters through the forest canopy.",

            "The scent of moss and damp earth fills the air.",

            "Fireflies drift between ancient branches.",

            "Leaves dance gently across the woodland floor."
        ],

        # ---------------------------------
        # Weather
        # ---------------------------------
        "possible_weather": [
            "Sunny",
            "Light Rain",
            "Morning Mist"
        ],

        # ---------------------------------
        # Discoveries
        # ---------------------------------
        "discoveries": [

            "Ancient Stone Circle",

            "Hidden Wildflower Patch",

            "Forgotten Woodland Shrine",

            "Crystal Spring",

            "Sleeping Guardian Tree",

            "Lost Ranger Camp",

            "Whispering Oak",

            "Moonlit Pond"
        ]
},

    "emberlands": {
        "name": "Emberlands Preserve",
        "emoji": "🔥",
        "theme": "volcanic",

        "description": (
            "Fed by the warmth beneath Moonlit Meadows, Emberlands Preserve is a "
            "rugged landscape of volcanic stone, glowing vents, obsidian cliffs "
            "and rivers of slow-moving lava. Despite its harsh appearance, many "
            "fire-loving creatures call these lands home."
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
                "description": "Collapsed lava tunnels are reopened."
            },
            3: {
                "capacity": 2,
                "comfort": 4,
                "resource_bonus": 10,
                "description": "Fresh geothermal vents encourage new growth."
            },
            4: {
                "capacity": 2,
                "comfort": 6,
                "resource_bonus": 20,
                "rare_event_bonus": 5,
                "description": "Ancient fire spirits once again roam the preserve."
            },
            5: {
                "capacity": 2,
                "comfort": 10,
                "resource_bonus": 30,
                "rare_event_bonus": 10,
                "bond_bonus": 1,
                "description": "The legendary Ember Heart radiates life throughout the preserve."
            }
        },

        # -----------------------------
        # Upgrade Projects
        # -----------------------------
        "upgrade_names": {
            2: "Clear Ashfall Trails",
            3: "Stabilise Lava Vents",
            4: "Restore Firestone Caverns",
            5: "Awaken the Ember Heart"
        },

        # -----------------------------
        # Level Descriptions
        # -----------------------------
        "level_descriptions": {
            1: "Only a handful of cooled caverns offer shelter among the volcanic stone.",
            2: "Ancient lava paths have been cleared, making travel much safer.",
            3: "Stable geothermal vents provide warmth throughout the preserve.",
            4: "The volcanic landscape flourishes as crystal fires and rare flora return.",
            5: "The Ember Heart glows peacefully, creating one of Moonlit Meadows' greatest sanctuaries."
        },

        # -----------------------------
        # Upgrade Projects
        # -----------------------------
        "projects": {
            2: {
                "title": "Clear Ashfall Trails",
                "description": (
                    "Old lava flows and ash have buried the preserve's ancient paths. "
                    "Clearing them allows creatures to safely reach new shelter sites."
                ),
                "cost": {
                    "charcoal": 20,
                    "stone": 30,
                    "warm_pebbles": 15
                },
                "reward": (
                    "+2 Capacity\n"
                    "New shelter sites become available."
                )
            },

            3: {
                "title": "Stabilise Lava Vents",
                "description": (
                    "The geothermal vents have become unstable over time. Restoring "
                    "them creates warm resting places and encourages rare resources."
                ),
                "cost": {
                    "fire_crystal": 20,
                    "ember_moss": 25,
                    "charcoal": 25
                },
                "reward": (
                    "+Comfort\n"
                    "+10% Resource Yield"
                )
            },

            4: {
                "title": "Restore Firestone Caverns",
                "description": (
                    "Collapsed crystal caverns once sheltered generations of fire creatures. "
                    "Rebuilding them transforms the preserve into a thriving habitat."
                ),
                "cost": {
                    "obsidian": 25,
                    "fire_crystal": 30,
                    "stone": 40
                },
                "reward": (
                    "+Comfort\n"
                    "+20% Resource Yield\n"
                    "Rare Events become more common."
                )
            },

            5: {
                "title": "Awaken the Ember Heart",
                "description": (
                    "Deep beneath the preserve lies an ancient crystal heart that once "
                    "kept these lands alive. Rekindling it restores Emberlands to its "
                    "former glory."
                ),
                "cost": {
                    "fire_crystal": 50,
                    "ember_moss": 40,
                    "obsidian": 40
                },
                "reward": (
                    "+Maximum Comfort\n"
                    "+30% Resource Yield\n"
                    "+Rare Events\n"
                    "Creatures gain Bond slightly faster while living here."
                )
            }
        },

        # -----------------------------
        # Passive Bonuses
        # -----------------------------
        "passive_effects": [
            "Fire creatures recover extra Health while resting.",
            "Warm resources appear more frequently.",
            "Occasionally produces bonus Fire Crystals.",
            "Volcanic shelters naturally provide additional Comfort."
        ],

        # -----------------------------
        # Rare Events
        # -----------------------------
        "events": [
            "Warm embers drift peacefully through the preserve.",
            "A dormant lava vent releases a gentle glow.",
            "A rare Fire Crystal emerges from the volcanic rock.",
            "The mountain rumbles softly before falling silent.",
            "Tiny flame spirits dance around the shelters.",
            "Fresh obsidian forms after a distant eruption."
        ],

        # -----------------------------
        # Shelter Types
        # -----------------------------
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
            "Smouldering Cavern",
            "Firestone Hollow",
            "Molten Pass",
            "Obsidian Shelter",
            "Cinder Grove",
            "Blazing Crag"
        ],

        # -----------------------------
        # Resources
        # -----------------------------
        "resources": [
            "warm_pebbles",
            "charcoal",
            "ember_moss",
            "fire_crystal",
            "obsidian"
        ],

        # -----------------------------
        # Atmosphere
        # -----------------------------
        "atmosphere": [
            "Warm air rises gently from the earth.",
            "Tiny embers drift lazily across the preserve.",
            "The distant volcano rumbles peacefully.",
            "Heat radiates from the black volcanic stone.",
            "Orange light flickers across the cliffs.",
            "The scent of ash and minerals lingers in the air."
        ],

        # -----------------------------
        # Weather
        # -----------------------------
        "possible_weather": [
            "Clear",
            "Ashfall",
            "Heat Haze",
            "Warm Winds"
        ],

        # -----------------------------
        # Discoveries
        # -----------------------------
        "discoveries": [
            "Ancient Lava Shrine",
            "Fire Crystal Vein",
            "Hidden Lava Tube",
            "The Ember Heart",
            "Forgotten Forge",
            "Sleeping Fire Spirit"
        ]
    },

    "frostwild": {
        "name": "Frostwild Preserve",
        "emoji": "❄️",
        "theme": "arctic",

        "description": (
            "Blanketed in snow throughout the year, Frostwild Preserve is a peaceful "
            "expanse of frozen forests, crystal lakes and towering glaciers. Though "
            "cold, it offers remarkable tranquility to the creatures that call it home."
        ),

        # ---------------------------------
        # Progression
        # ---------------------------------
        "starting_capacity": 3,
        "capacity_per_level": 2,
        "max_level": 5,
        "unlock_level": 1,

        # ---------------------------------
        # Upgrade Projects
        # ---------------------------------
        "upgrade_names": {
            2: "Strengthen Snow Paths",
            3: "Restore Frozen Springs",
            4: "Raise Crystal Ice Shelters",
            5: "Blessing of the Aurora"
        },

        "restoration_milestones": {
            2: "Snow Paths",
            3: "Frozen Springs",
            4: "Crystal Shelters",
            5: "Aurora Shrine"
        },

        # ---------------------------------
        # Level Descriptions
        # ---------------------------------
        "level_descriptions": {
            1: (
                "Only a few snow burrows protect creatures from the bitter cold. "
                "The preserve remains quiet and isolated."
            ),

            2: (
                "Safe snow paths connect the shelters, making travel through the "
                "blizzards much easier."
            ),

            3: (
                "Ancient frozen springs once buried beneath the ice now flow again, "
                "bringing life back to Frostwild."
            ),

            4: (
                "Beautiful crystal ice shelters shimmer beneath the sunlight while "
                "majestic glaciers provide safety and comfort."
            ),

            5: (
                "The Aurora Shrine awakens. Every night brilliant lights dance across "
                "the sky, filling the preserve with peaceful magic."
            )
        },

        # ---------------------------------
        # Upgrade Costs
        # ---------------------------------
        "upgrade_costs": {

            2: {
                "wood": 30,
                "sticks": 25,
                "ice_crystal": 20,
                "snowberries": 15
            },

            3: {
                "ice_crystal": 40,
                "frost_flower": 25,
                "snowberries": 30,
                "fresh_water": 15
            },

            4: {
                "ice_crystal": 70,
                "crystal_shard": 20,
                "wood": 50,
                "frost_flower": 40
            },

            5: {
                "ice_crystal": 120,
                "crystal_shard": 40,
                "glow_mushroom": 20,
                "frost_flower": 60,
                "snowberries": 70
            }
        },

        # ---------------------------------
        # Upgrade Bonuses
        # ---------------------------------
        "upgrade_bonuses": {

            2: {
                "capacity": 2,
                "comfort": 2,
                "description": (
                    "Snow paths make travel easier for every resident."
                )
            },

            3: {
                "capacity": 2,
                "comfort": 4,
                "energy_bonus": 5,
                "resource_bonus": 10,
                "description": (
                    "Frozen springs provide fresh water and renewed energy."
                )
            },

            4: {
                "capacity": 2,
                "comfort": 7,
                "energy_bonus": 10,
                "resource_bonus": 20,
                "rare_event_bonus": 5,
                "description": (
                    "Crystal shelters greatly improve creature comfort."
                )
            },

            5: {
                "capacity": 2,
                "comfort": 12,
                "energy_bonus": 15,
                "resource_bonus": 30,
                "rare_event_bonus": 10,
                "well_rested_bonus": 1,
                "description": (
                    "The Aurora blesses every creature with peaceful rest."
                )
            }
        },

        # ---------------------------------
        # Passive Effects
        # ---------------------------------
        "passive_effects": [

            "Creatures recover additional Energy while resting.",

            "The Rest command restores slightly more Energy.",

            "Ice resources are gathered more frequently.",

            "Sleeping creatures occasionally awaken Well Rested.",

            "Cold-loving creatures slowly gain Happiness."
        ],

        # ---------------------------------
        # Preserve Events
        # ---------------------------------
        "events": [

            "An aurora paints the night sky with brilliant colours.",

            "Fresh snow quietly blankets every shelter.",

            "A frozen spring bubbles beneath crystal-clear ice.",

            "Ice crystals bloom across the nearby lake.",

            "A family of snow foxes races through the preserve.",

            "Snowbirds build a tiny nest atop an icy cliff.",

            "Gentle winds carry sparkling snowflakes through the forest.",

            "A distant glacier echoes softly across the valley."
        ],

        # ---------------------------------
        # Shelter Types
        # ---------------------------------
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

        # ---------------------------------
        # Resources
        # ---------------------------------
        "resources": [
            "ice_crystal",
            "snowberries",
            "frost_flower"
        ],

        # ---------------------------------
        # Atmosphere
        # ---------------------------------
        "atmosphere": [

            "Snowflakes drift silently through the crisp air.",

            "Everything is peaceful beneath a blanket of white.",

            "The frozen lake sparkles like glass.",

            "Icicles shimmer beneath the pale sunlight.",

            "A cool breeze carries sparkling snow across the preserve.",

            "The silence is broken only by distant birds."
        ],

        # ---------------------------------
        # Weather
        # ---------------------------------
        "possible_weather": [
            "Snow",
            "Gentle Snowfall",
            "Blizzard",
            "Clear Skies",
            "Aurora Night"
        ],

        # ---------------------------------
        # Discoveries
        # ---------------------------------
        "discoveries": [

            "Frozen Waterfall",

            "Crystal Ice Cavern",

            "Ancient Frost Totem",

            "Aurora Shrine",

            "Glacial Mirror Lake",

            "Sleeping Ice Guardian",

            "Snow Owl Nest",

            "Hidden Ice Garden"
        ]
    },

    "sunpetal_prairie": {
        "name": "Sunpetal Prairie",
        "emoji": "🌼",
        "theme": "grassland",

        "description": (
            "Rolling meadows carpeted in colourful wildflowers stretch beneath open skies. "
            "Gentle breezes, buzzing bees and wandering butterflies make Sunpetal Prairie "
            "one of the most peaceful preserves within Moonlit Meadows."
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
                "description": "Flower fields spread across the preserve."
            },
            3: {
                "capacity": 2,
                "comfort": 4,
                "resource_bonus": 10,
                "description": "Pollinators return, enriching the prairie."
            },
            4: {
                "capacity": 2,
                "comfort": 6,
                "resource_bonus": 20,
                "rare_event_bonus": 5,
                "description": "The meadows bloom with incredible life."
            },
            5: {
                "capacity": 2,
                "comfort": 10,
                "resource_bonus": 30,
                "rare_event_bonus": 10,
                "bond_bonus": 1,
                "description": "Sunpetal Prairie blossoms into an endless sea of flowers."
            }
        },

        # -----------------------------
        # Upgrade Projects
        # -----------------------------
        "upgrade_names": {
            2: "Expand Flower Fields",
            3: "Restore Bee Gardens",
            4: "Create Butterfly Sanctuaries",
            5: "Bloom of the Endless Prairie"
        },

        # -----------------------------
        # Level Descriptions
        # -----------------------------
        "level_descriptions": {
            1: "Only a few colourful meadows have begun to recover.",
            2: "Wildflower fields now spread across much of the preserve.",
            3: "Bees and butterflies return, bringing life to every corner.",
            4: "Rolling hills burst into bloom throughout every season.",
            5: "A breathtaking sea of flowers stretches to the horizon, attracting creatures from across Moonlit Meadows."
        },

        # -----------------------------
        # Upgrade Projects
        # -----------------------------
        "projects": {
            2: {
                "title": "Expand Flower Fields",
                "description": (
                    "Years of neglect have left much of the prairie overgrown. "
                    "Planting native flowers restores shelter and feeding grounds "
                    "for many peaceful creatures."
                ),
                "cost": {
                    "wildflowers": 30,
                    "soft_grass": 25,
                    "seeds": 20
                },
                "reward": (
                    "+2 Capacity\n"
                    "New shelter sites become available."
                )
            },

            3: {
                "title": "Restore Bee Gardens",
                "description": (
                    "Special gardens filled with nectar-rich blossoms encourage "
                    "bees and other pollinators to return, strengthening the "
                    "entire ecosystem."
                ),
                "cost": {
                    "wildflowers": 40,
                    "herbs": 25,
                    "seeds": 30
                },
                "reward": (
                    "+Comfort\n"
                    "+10% Resource Yield"
                )
            },

            4: {
                "title": "Create Butterfly Sanctuaries",
                "description": (
                    "Protected flower groves provide safe breeding grounds for "
                    "butterflies, bringing colour and life back to the prairie."
                ),
                "cost": {
                    "wildflowers": 50,
                    "soft_grass": 35,
                    "herbs": 30
                },
                "reward": (
                    "+Comfort\n"
                    "+20% Resource Yield\n"
                    "Rare Events become more common."
                )
            },

            5: {
                "title": "Bloom of the Endless Prairie",
                "description": (
                    "With one final restoration effort, the prairie awakens into a "
                    "legendary landscape where flowers bloom throughout every season."
                ),
                "cost": {
                    "wildflowers": 75,
                    "seeds": 50,
                    "herbs": 40
                },
                "reward": (
                    "+Maximum Comfort\n"
                    "+30% Resource Yield\n"
                    "+Rare Events\n"
                    "Creatures gain Bond slightly faster while living here."
                )
            }
        },

        # -----------------------------
        # Passive Bonuses
        # -----------------------------
        "passive_effects": [
            "Grassland creatures recover extra Happiness while resting.",
            "Flowers and herbs are gathered more frequently.",
            "Butterflies occasionally reveal hidden resources.",
            "Open meadows naturally improve shelter Comfort."
        ],

        # -----------------------------
        # Rare Events
        # -----------------------------
        "events": [
            "Thousands of butterflies gather across the meadow.",
            "Rare wildflowers bloom overnight.",
            "A rainbow stretches across the prairie after gentle rain.",
            "Honeybees establish a thriving new hive.",
            "A herd of peaceful creatures grazes nearby.",
            "The wind carries glowing flower seeds across the hills."
        ],

        # -----------------------------
        # Shelter Types
        # -----------------------------
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

        # -----------------------------
        # Resources
        # -----------------------------
        "resources": [
            "wildflowers",
            "soft_grass",
            "seeds",
            "herbs",
            "nectar"
        ],

        # -----------------------------
        # Atmosphere
        # -----------------------------
        "atmosphere": [
            "Wildflowers sway gently in the breeze.",
            "Butterflies drift from blossom to blossom.",
            "Warm sunlight bathes the rolling meadows.",
            "Bees buzz peacefully among colourful flowers.",
            "Tall grass ripples like gentle waves.",
            "The air carries the sweet scent of blooming petals."
        ],

        # -----------------------------
        # Weather
        # -----------------------------
        "possible_weather": [
            "Sunny",
            "Cloudy",
            "Spring Shower",
            "Rainbow"
        ],

        # -----------------------------
        # Discoveries
        # -----------------------------
        "discoveries": [
            "Rare Flower Patch",
            "Butterfly Grove",
            "Hidden Meadow",
            "Ancient Bee Shrine",
            "Golden Sunflower Field",
            "The Endless Bloom"
        ]
    },

    "mistfen": {
        "name": "Mistfen Preserve",
        "emoji": "🌿",
        "theme": "wetland",

        "description": (
            "A peaceful network of winding streams, quiet ponds and ancient marshes. "
            "Mistfen Preserve is rich with reeds, lilies and crystal-clear waters, "
            "providing a tranquil refuge for creatures who thrive beside the water."
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
                "description": "Boardwalks reconnect the wetlands."
            },
            3: {
                "capacity": 2,
                "comfort": 4,
                "resource_bonus": 10,
                "description": "Protected ponds flourish with life."
            },
            4: {
                "capacity": 2,
                "comfort": 6,
                "resource_bonus": 20,
                "rare_event_bonus": 5,
                "description": "The marsh becomes a sanctuary for rare wildlife."
            },
            5: {
                "capacity": 2,
                "comfort": 10,
                "resource_bonus": 30,
                "rare_event_bonus": 10,
                "bond_bonus": 1,
                "description": "Mistfen becomes one of the most peaceful wetlands in Moonlit Meadows."
            }
        },

        # -----------------------------
        # Upgrade Projects
        # -----------------------------
        "upgrade_names": {
            2: "Restore Boardwalks",
            3: "Protect Lily Ponds",
            4: "Expand Wetlands",
            5: "Heart of the Marsh"
        },

        # -----------------------------
        # Level Descriptions
        # -----------------------------
        "level_descriptions": {
            1: "Only a handful of ponds remain safe for creatures to rest.",
            2: "Wooden walkways reconnect the scattered marshlands.",
            3: "The restored ponds teem with fish, lilies and aquatic life.",
            4: "Rare birds and peaceful wildlife have returned to the wetlands.",
            5: "Mistfen has become a thriving sanctuary where crystal waters nourish every living thing."
        },

        # -----------------------------
        # Upgrade Projects
        # -----------------------------
        "projects": {
            2: {
                "title": "Restore Boardwalks",
                "description": (
                    "Old wooden paths have collapsed into the marsh. Rebuilding them "
                    "allows caretakers and creatures to safely explore the preserve."
                ),
                "cost": {
                    "reeds": 30,
                    "sticks": 30,
                    "smooth_stones": 20
                },
                "reward": (
                    "+2 Capacity\n"
                    "New shelter sites become available."
                )
            },

            3: {
                "title": "Protect Lily Ponds",
                "description": (
                    "Healthy lily ponds support countless forms of life. Restoring "
                    "them provides food, shelter and clean water throughout the preserve."
                ),
                "cost": {
                    "water_lily": 25,
                    "fresh_water": 40,
                    "reeds": 20
                },
                "reward": (
                    "+Comfort\n"
                    "+10% Resource Yield"
                )
            },

            4: {
                "title": "Expand Wetlands",
                "description": (
                    "Allowing the marshlands to spread naturally creates new habitats "
                    "for rare aquatic creatures and strengthens the ecosystem."
                ),
                "cost": {
                    "water_lily": 35,
                    "smooth_stones": 35,
                    "fresh_water": 40
                },
                "reward": (
                    "+Comfort\n"
                    "+20% Resource Yield\n"
                    "Rare Events become more common."
                )
            },

            5: {
                "title": "Heart of the Marsh",
                "description": (
                    "At the centre of Mistfen lies an ancient spring said to have "
                    "given life to the wetlands. Restoring it allows the preserve to "
                    "flourish once more."
                ),
                "cost": {
                    "fresh_water": 60,
                    "water_lily": 40,
                    "smooth_stones": 40
                },
                "reward": (
                    "+Maximum Comfort\n"
                    "+30% Resource Yield\n"
                    "+Rare Events\n"
                    "Creatures gain Bond slightly faster while living here."
                )
            }
        },

        # -----------------------------
        # Passive Bonuses
        # -----------------------------
        "passive_effects": [
            "Wetland creatures recover extra Energy while resting.",
            "Water resources appear more frequently.",
            "Healing plants grow more abundantly.",
            "Shelters near the water naturally provide additional Comfort."
        ],

        # -----------------------------
        # Rare Events
        # -----------------------------
        "events": [
            "Morning mist blankets the preserve.",
            "Dragonflies dance across the still water.",
            "A family of frogs returns to the marsh.",
            "A hidden spring bubbles up from beneath the reeds.",
            "A graceful heron lands beside the pond.",
            "Lotus flowers bloom overnight."
        ],

        # -----------------------------
        # Shelter Types
        # -----------------------------
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

        # -----------------------------
        # Resources
        # -----------------------------
        "resources": [
            "reeds",
            "water_lily",
            "smooth_stones",
            "fresh_water",
            "healing_reeds"
        ],

        # -----------------------------
        # Atmosphere
        # -----------------------------
        "atmosphere": [
            "A blanket of mist hangs over the water.",
            "Dragonflies skim silently across the ponds.",
            "The gentle croaking of frogs echoes through the reeds.",
            "Soft ripples spread across the still marsh.",
            "The scent of fresh rain fills the cool air.",
            "Birdsong drifts through the willow trees."
        ],

        # -----------------------------
        # Weather
        # -----------------------------
        "possible_weather": [
            "Fog",
            "Light Rain",
            "Sunny",
            "Morning Mist"
        ],

        # -----------------------------
        # Discoveries
        # -----------------------------
        "discoveries": [
            "Ancient Boardwalk",
            "Hidden Pond",
            "Rare Water Lily",
            "Crystal Spring",
            "Forgotten Fisher's Hut",
            "Heart of the Marsh"
        ]
    },
}
