EXPLORATION_EVENTS = [
    {
        "type": "bond",
        "text": "You and your creature explore a quiet corner of the sanctuary together. It feels safe here.",
        "bond": 5,
        "happiness": 3
    },
    {
        "type": "discovery",
        "text": "You discover a hidden overgrown path behind the main structure.",
        "bond": 2,
        "sanctuary_progress": 5
    },
    {
        "type": "bond",
        "text": "Your creature proudly shows you a new behavior it has learned.",
        "bond": 6,
        "trust": 3
    },
    {
        "type": "risk",
        "text": "A loose structure creaks and startles your creature. It becomes uneasy.",
        "happiness": -5,
        "energy": -10
    },
    {
        "type": "rest",
        "text": "You and your creature find a warm resting spot and take a short break.",
        "energy": 10,
        "happiness": 4
    }
]

LOCATIONS = {
    "courtyard": {
        "name": "🌱 Overgrown Courtyard",
        "events": {
            "common": [...],
            "uncommon": [...],
            "rare": [...]
        }
    },
    "healing_wing": {
        "name": "Healing Wing",
        "events": {...}
    },
    "water_gardens": {
        "name": "Water Gardens",
        "events": {...}
    },
        "training_yard": {
    "name": "Training Yard",
    "events": {
        "common": [
            {
                "text": "You and your creature wander into the training yard, inspecting the equipment curiously.",
                "stat_changes": {
                    "bond": 2,
                    "happiness": 1
                }
            }
        ],
        "uncommon": [
            {
                "text": "Your creature attempts to interact with old training dummies, gaining confidence.",
                "stat_changes": {
                    "trust": 3,
                    "happiness": 4,
                    "energy": -5
                }
            }
        ],
        "rare": [
            {
                "text": "A faint magical imprint in the training yard reacts to your creature’s presence.",
                "stat_changes": {
                    "trust": 8,
                    "energy": -10
                }
            }
        ]
    },
        "ancient_library": {
        "name": "Ancient Library",
        "events": {
            "common": [...],
            "uncommon": [...],
            "rare": [...]
        }
    },
        "flower_meadows": {
        "name": "Flower Meadows",
        "events": {
            "common": [...],
            "uncommon": [...],
            "rare": [...]
        }
    },
        "common_rooms": {
        "name": "Common Rooms",
        "events": {
            "common": [...],
            "uncommon": [...],
            "rare": [...]
        }
    }
}}