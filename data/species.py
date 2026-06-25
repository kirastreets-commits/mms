# BALANCING AND DATA
import discord
# ----------------------------
# SPECIES REGISTRY
# ----------------------------

SPECIES_REGISTRY = {
    "Fire Dragon": {
        "description": "Aggressive dragons with burning breath.",
        "shelter": "nest",
            "liked_shelter_items": [
                "warm pebbles",
                "obsidian shards",
                "lava rock",
                "heat crystal"
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
        "liked_shelter_items": [
            "ice crystal",
            "packed snow",
            "frost flowers",
            "glacial stone"
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
        "liked_shelter_items": [
            "warm pebbles",
            "fluffy tuffs",
            "soft bedding",
            "glowing mushrooms"
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
            "liked_shelter_items": [
                "warm pebbles",
                "large cushions",
                "glowing mushrooms"
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
        "liked_shelter_items": [
            "lava rock",
            "obsidian shards",
            "mineral salt block"
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
        "liked_shelter_items": [
            "frost flowers",
            "snow puff moss",
            "ice crystal"
        ],
        "habitat": "artic",
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
            "liked_shelter_items": [
                "snow puff moss",
                "frost flowers",
                "soft bedding",
                "ice crystal"
            ],
            "rarity": "common",
            "habitat": "artic",
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
        "liked_shelter_items": [
            "soft moss",
            "glowing mushrooms",
            "tree roots"
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
        "liked_shelter_items": [
            "vines",
            "soft moss",
            "thorn branches"
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
        "liked_shelter_items": [
            "soft moss",
            "glowing mushrooms",
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
    }
}


def get_species_data(species_name):
    if species_name in SPECIES_REGISTRY:
        return SPECIES_REGISTRY[species_name]
    
    return {}

def get_species(species_name):
    return SPECIES_REGISTRY.get(species_name)

def get_species_description(species_description):
    if species_description in SPECIES_REGISTRY:
        return SPECIES_REGISTRY[species_description]
    
    return {}

def get_species_shelter(species_shelter):
    if species_shelter in SPECIES_REGISTRY:
        return SPECIES_REGISTRY[species_shelter]
    
    return {}

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
