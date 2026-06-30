# BALANCING AND DATA
import discord
# ----------------------------
# SPECIES REGISTRY
# ----------------------------

SPECIES_REGISTRY = {
    "Fire Dragon": {
        "description": "Aggressive dragons with burning breath.",
        "shelter": "nest",
            "shelter_preferences": [
                "warm",
                "stone",
                "crystal"
            ],
        "rarity": "rare",
        "habitat": "volcanic",
        "diet": "carnivore",
        "is_starter": False,

        "growth_stages": ["hatchling", "juvenile", "adult", "elder"],

        "stats": {
            "max_health": 100,
            "max_energy": 100,
            "max_hunger": 100,
            "max_happiness": 100,
            "max_trust": 100,

            "base_health": 40,
            "base_energy": 30,
            "base_happiness": 20,
        }
    },

    "Ice Dragon": {
        "description": "Calm dragons from frozen lands.",
        "shelter": "nest",
        "shelter_preferences": [
            "cold",
            "crystal",
            "soft"
        ],
        "rarity": "rare",
        "habitat": "arctic",
        "diet": "carnivore",
        "is_starter": False,

        "growth_stages": ["hatchling", "juvenile", "adult", "elder"],

        "stats": {
            "max_health": 100,
            "max_energy": 100,
            "max_hunger": 100,
            "max_happiness": 100,
            "max_trust": 100,

            "base_health": 35,
            "base_energy": 40,
            "base_happiness": 25,
        }
    },

    "Emberfox": {
        "description": "A fox-like creature with glowing warm fur.",
        "shelter": "den",
        "shelter_preferences": [
            "warm",
            "soft",
            "cozy"
        ],
        "rarity": "common",
        "habitat": "forest",
        "diet": "omnivore",
        "is_starter": True,
        "emoji": "🔥",
        "button_style": discord.ButtonStyle.red,

        "growth_stages": ["kit", "juvenile", "adult"],

        "stats": {
            "max_health": 100,
            "max_energy": 100,
            "max_hunger": 100,
            "max_happiness": 100,
            "max_trust": 100,

            "base_health": 20,
            "base_energy": 30,
            "base_happiness": 35,
        }
    },

    "Cinderware": {
            "description": "Bear-like creatures that leave glowing pawprints wherever they walk.",
            "shelter": "den",
            "shelter_preferences": [
                "warm",
                "soft",
                "large"
            ],
            "rarity": "common",
            "habitat": "forest",
            "diet": "carnivore",
            "is_starter": False,
            "emoji": "🔥",
            "button_style": discord.ButtonStyle.red,

            "growth_stages": ["cub", "juvenile", "adult"],

            "stats": {
                "max_health": 100,
                "max_energy": 100,
                "max_hunger": 100,
                "max_happiness": 100,
                "max_trust": 100,

                "base_health": 20,
                "base_energy": 30,
                "base_happiness": 35,
            }
        },

    "Stonehorn": {
        "description": "Goat-like creatures with volcanic stone horns.",
        "shelter": "den",
        "shelter_preferences": [
            "stone",
            "mineral",
            "sturdy"
        ],
        "rarity": "common",
        "habitat": "volcanic",
        "diet": "carnivore",
        "is_starter": False,
        "emoji": "🔥",
        "button_style": discord.ButtonStyle.red,

        "growth_stages": ["kid", "juvenile", "adult"],

        "stats": {
            "max_health": 100,
            "max_energy": 100,
            "max_hunger": 100,
            "max_happiness": 100,
            "max_trust": 100,

            "base_health": 20,
            "base_energy": 30,
            "base_happiness": 35,
            }
        },

    "Frosthopper": {
        "description": "A small, agile creature that can leap great distances. It has a coat of fine, frost-covered fur..",
        "shelter": "den",
        "rarity": "common",
        "shelter_preferences": [
            "cold",
            "soft",
            "flower"
        ],
        "habitat": "arctic",
        "diet": "omnivore",
        "is_starter": True,
        "emoji": "❄️",
        "button_style": discord.ButtonStyle.blurple,

        "growth_stages": ["kit", "juvenile", "adult"],

        "stats": {
            "max_health": 100,
            "max_energy": 100,
            "max_hunger": 100,
            "max_happiness": 100,
            "max_trust": 100,

            "base_health": 20,
            "base_energy": 30,
            "base_happiness": 35,
        }
    },

    "Frostfox": {
            "description": "Fox-like creatures with tails resembling drifting snowfall.",
            "shelter": "den",
            "shelter_preferences": [
                "cold",
                "soft",
                "shiny"
            ],
            "rarity": "common",
            "habitat": "arctic",
            "diet": "omnivore",
            "is_starter": False,
            "emoji": "❄️",
            "button_style": discord.ButtonStyle.blurple,

            "growth_stages": ["kit", "juvenile", "adult"],

            "stats": {
                "max_health": 100,
                "max_energy": 100,
                "max_hunger": 100,
                "max_happiness": 100,
                "max_trust": 100,

                "base_health": 20,
                "base_energy": 30,
                "base_happiness": 35,
            }
    },

    "Mossling": {
        "description": "A small woodland creature covered in soft moss and tiny sprouts.",
        "shelter": "burrow",
        "shelter_preferences": [
            "plant",
            "soft",
            "natural"
        ],
        "rarity": "common",
        "habitat": "forest",
        "diet": "herbivore",
        "is_starter": True,
        "emoji": "🌿",
        "button_style": discord.ButtonStyle.green,

        "growth_stages": ["sporeling", "sprout", "mossling", "eldergrove"],

        "stats": {
            "max_health": 100,
            "max_energy": 100,
            "max_hunger": 100,
            "max_happiness": 100,
            "max_trust": 100,

            "base_health": 20,
            "base_energy": 30,
            "base_happiness": 35,
            }
    },
        "Thornhare": {
        "description": "Rabbit-like creatures with thorny vines growing through their fur.",
        "shelter": "den",
        "shelter_preferences": [
            "plant",
            "thorny",
            "natural"
        ],
        "rarity": "common",
        "habitat": "forest",
        "diet": "herbivore",
        "is_starter": False,
        "emoji": "🌿",
        "button_style": discord.ButtonStyle.green,

        "growth_stages": ["kit", "juvenile", "adult"],

        "stats": {
            "max_health": 100,
            "max_energy": 100,
            "max_hunger": 100,
            "max_happiness": 100,
            "max_trust": 100,

            "base_health": 20,
            "base_energy": 30,
            "base_happiness": 35,
        },
    },
        "Fernpaw": {
        "description": "Feline creatures with leafy tails and glowing green eyes.",
        "shelter": "den",
        "shelter_preferences": [
            "plant",
            "soft",
            "glowing"
        ],
        "rarity": "common",
        "habitat": "forest",
        "diet": "omnivore",
        "is_starter": False,
        "emoji": "🌿",
        "button_style": discord.ButtonStyle.green,

        "growth_stages": ["kit", "juvenile", "adult"],

        "stats": {
            "max_health": 100,
            "max_energy": 100,
            "max_hunger": 100,
            "max_happiness": 100,
            "max_trust": 100,

            "base_health": 20,
            "base_energy": 30,
            "base_happiness": 35,
        }
    },
        "Lunabloom": {
        "description": "A gentle spirit creature said to bloom wherever moonlight lingers the longest.",
        "shelter": "nest",
        "shelter_preferences": [
            "plant",
            "soft",
            "glowing",
            "flower"
        ],
        "rarity": "uncommon",
        "habitat": "gardens",
        "diet": "omnivore",
        "is_starter": False,
        "emoji": "🌿",
        "button_style": discord.ButtonStyle.green,

        "growth_stages": ["kit", "juvenile", "adult"],

        "stats": {
            "max_health": 100,
            "max_energy": 100,
            "max_hunger": 100,
            "max_happiness": 100,
            "max_trust": 100,

            "base_health": 20,
            "base_energy": 30,
            "base_happiness": 35,
        }
    },
        "Whispermoth": {
        "description": "Whispermoths are delicate spirit moths drawn to stories,"
        " songs, and written knowledge. Their shimmering wings are said to capture echoes of conversations "
        "and preserve memories that might otherwise fade with time.",
        "shelter": "nest",
        "shelter_preferences": [
            "crystal",
            "soft",
            "glowing"
        ],
        "rarity": "uncommon",
        "habitat": "libaries",
        "diet": "omnivore",
        "is_starter": False,
        "emoji": "🌿",
        "button_style": discord.ButtonStyle.green,

        "growth_stages": ["kit", "juvenile", "adult"],

        "stats": {
            "max_health": 100,
            "max_energy": 100,
            "max_hunger": 100,
            "max_happiness": 100,
            "max_trust": 100,

            "base_health": 20,
            "base_energy": 30,
            "base_happiness": 35,
        }
    },
        "Glowfern": {
            "description": "Glowferns are timid woodland spirits covered in soft moss and glowing fern "
            "fronds. They quietly tend to injured plants and resting creatures, believing "
            "every wound deserves patience and every life deserves another chance.",
            "shelter": "nest",
            "shelter_preferences": [
                "plant",
                "soft",
                "glowing",
                "flower"
            ],
            "rarity": "uncommon",
            "habitat": "forest",
            "diet": "omnivore",
            "is_starter": False,
            "emoji": "🌿",
            "button_style": discord.ButtonStyle.green,

            "growth_stages": ["kit", "juvenile", "adult"],

            "stats": {
                "max_health": 100,
                "max_energy": 100,
                "max_hunger": 100,
                "max_happiness": 100,
                "max_trust": 100,

                "base_health": 20,
                "base_energy": 30,
                "base_happiness": 35,
            }
        },

        "Emberbun": {
            "description": "Small hearth spirits that resemble fluffy rabbits with glowing ember-like fur. Emberbuns are drawn to warm fireplaces and the comforting presence of others, often curling beside tired caretakers after long days.",
            "shelter": "nest",
            "shelter_preferences": [
                "plant",
                "soft",
                "glowing",
                "flower"
            ],
            "rarity": "common",
            "habitat": "fireplaces",
            "diet": "herbivore",
            "is_starter": False,
            "emoji": "🔥",
            "button_style": discord.ButtonStyle.red,

            "growth_stages": ["kit", "juvenile", "adult"],

            "stats": {
                "max_health": 100,
                "max_energy": 100,
                "max_hunger": 100,
                "max_happiness": 100,
                "max_trust": 100,

                "base_health": 20,
                "base_energy": 30,
                "base_happiness": 35,
            }
    }
}


def get_species_data(species_name):
    if species_name in SPECIES_REGISTRY:
        return SPECIES_REGISTRY[species_name]
    
    return {}

def get_species(species_name):
    return SPECIES_REGISTRY.get(species_name)

def get_species_description(species_name):
    species = SPECIES_REGISTRY.get(species_name)
    return species.get("description") if species else None

def get_species_stat(species_name, key, default=100):
    species = get_species(species_name)
    if not species:
        return default
    return species.get("stats", {}).get(key, default)


def get_starters():
    return {
        name: data
        for name, data in SPECIES_REGISTRY.items()
        if data.get("is_starter")
    }

def get_species_preferences(species_name):
    species = get_species(species_name)

    if not species:
        return []

    return species.get("shelter_preferences", [])

def get_species_shelter(species_name):
    species = get_species(species_name)

    if not species:
        return "shelter"

    return species.get("shelter", "shelter")
