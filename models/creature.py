# CREATURE
import random
from data.species import SPECIES_REGISTRY, get_species_data, get_species, get_species_stat
from data.personality import PERSONALITIES
from systems.personality_system import apply_personality
from systems.mood_system import update_mood
from systems.memory_system import default_memory
from systems.memory_system import update_memory 
from systems.memory_system import ensure_memory





class Creature:
    def __init__(
        self,
        name: str,
        species: str,
        personality=None,
        mood="neutral",
        trust: int = 20,
        health: int = 20,
        energy: int = 20,
        hunger: int = 20,
        happiness: int = 10
    ):
        self.name = name
        self.species = species

        self.species_data = get_species_data(species) or {}

        self.shelter = {
            "type": self.species_data.get("shelter", "basic"),
            "level": 1,
            "items": []
        }

        self.personality = personality or random.choice(list(PERSONALITIES.keys()))
        self.mood = mood

        self.preferences_learned = {}
        self.recent_gifts = []
        self.memory = default_memory()

        # ----------------------------
        # MAX STAT LIMITS
        # ----------------------------
        self.max_health = get_species_stat(species, "max_health", 100)
        self.max_energy = get_species_stat(species, "max_energy", 100)
        self.max_hunger = get_species_stat(species, "max_hunger", 100)
        self.max_happiness = get_species_stat(species, "max_happiness", 100)
        self.max_trust = get_species_stat(species, "max_trust", 100)

        self.trust = trust
        self.health = health
        self.energy = energy
        self.hunger = hunger
        self.happiness = happiness

        # ----------------------------
        # 🔥 CLAMP HERE (IMPORTANT)
        # ----------------------------
        self.health = max(0, min(self.max_health, self.health))
        self.energy = max(0, min(self.max_energy, self.energy))
        self.hunger = max(0, min(self.max_hunger, self.hunger))
        self.happiness = max(0, min(self.max_happiness, self.happiness))
        self.trust = max(0, min(self.max_trust, self.trust))


   
# ----------------------------
    def shelter_name(self):
        return self.shelter["type"]


    
# 🧠 STATE UPDATES
# ----------------------------
    def play(self):
        
        from data.play_responses import PLAY_MESSAGES, PLAY_PERSONALITY_LINES, RARE_PLAY_MESSAGES

        result = {
            "success": True,
            "message": "",
            "stat_changes": [],
            "mood_change": None,
            "bond_change": None,
            "rare_event": None
        }

        # ----------------------------
        # BASE RECOVERY
        # ----------------------------
        old_bond = self.bond_level()
        
        happiness_gain = 3
        trust_gain = 3
        hunger_loss = -10

        self.happiness = min(100, self.happiness + happiness_gain)
        self.trust = min(100, self.trust + trust_gain)   # ✔ FIXED
        self.hunger = max(0, self.hunger + hunger_loss)

        result["stat_changes"].extend([
            ("Happiness", happiness_gain),
            ("Trust", trust_gain),
            ("Hunger", hunger_loss)
        ])

        # ----------------------------
        # BOND BONUS
        # ----------------------------

        bond = self.bond_level()

        if bond == "friendly":
            self.happiness = min(100, self.happiness + 2)
            result["stat_changes"].append(("Happiness", 2))

        elif bond == "trusted":
            self.happiness = min(100, self.happiness + 3)
            self.trust = min(100, self.trust + 2)

            result["stat_changes"].extend([
                ("Happiness", 3),
                ("Trust", 2)
            ])

        elif bond == "devoted":
            self.happiness = min(100, self.happiness + 5)
            self.trust = min(100, self.trust + 3)

            result["stat_changes"].extend([
                ("Happiness", 5),
                ("Trust", 3)
            ])

        # ----------------------------
        # PERSONALITY EFFECTS
        # ----------------------------

        personality_changes = apply_personality(self, "play")
        result["stat_changes"].extend(personality_changes)

        # ----------------------------
        # MOOD UPDATE
        # ----------------------------

        old_mood = self.mood
        update_mood(self)

        if old_mood != self.mood:
            result["mood_change"] = self.mood

        # ----------------------------
        # BASE MESSAGE
        # ----------------------------

        message = random.choice(
            PLAY_MESSAGES.get(self.mood, PLAY_MESSAGES["neutral"])
        ).format(name=self.name)

        # ----------------------------
        # PERSONALITY FLAVOUR
        # ----------------------------

        if self.personality in PLAY_PERSONALITY_LINES:
            message += "\n\n" + random.choice(
                PLAY_PERSONALITY_LINES[self.personality]
            ).format(name=self.name)

        # ----------------------------
        # BOND FLAVOUR
        # ----------------------------

        BOND_LINES = {
            "friendly": "It seems comfortable around you.",
            "trusted": "It clearly trusts your presence.",
            "devoted": "It relaxes completely when you're nearby."
        }

        if bond in BOND_LINES:
            message += "\n\n" + BOND_LINES[bond]

        # ----------------------------
        # RARE EVENT
        # ----------------------------

        if random.random() < 0.08:
            result["rare_event"] = random.choice(RARE_PLAY_MESSAGES).format(name=self.name)

        # ----------------------------
        # FINALISE RESULT
        # ----------------------------

        result["message"] = message

        # 🧠 MEMORY PIPELINE CALL (IMPORTANT)
        update_memory(self, "play", result)

        return result
    
    def feed(self):

        import random

        from systems.mood_system import update_mood
        from systems.personality_system import apply_personality
        from data.feed_responses import FEED_MESSAGES, FEED_PERSONALITY_LINES, RARE_FEED_MESSAGES

        result = {
            "success": True,
            "message": "",
            "stat_changes": [],
            "mood_change": None,
            "bond_change": None,
            "rare_event": None
        }

        # ----------------------------
        # BASE RECOVERY
        # ----------------------------

        old_bond = self.bond_level()

        hunger_gain = 20
        happiness_gain = 5
        trust_gain =5

        self.hunger = min(100, self.hunger + hunger_gain)
        self.happiness = min(100, self.happiness + happiness_gain)
        self.trust = min(100, self.trust + trust_gain)

        result["stat_changes"].extend([
            ("Hunger", hunger_gain),
            ("Happiness", happiness_gain),
            ("Trust", trust_gain)
        ])

        # ----------------------------
        # BOND BONUS
        # ----------------------------
        bond = self.bond_level()

        if bond == "friendly":


            self.happiness = min(100, self.happiness + 2)


            result["stat_changes"].append(
                ("Happiness", 2)
            )


        elif bond == "trusted":


            self.happiness = min(100, self.happiness + 3)
            self.trust = min(100, self.trust + 2)


            result["stat_changes"].extend([
                ("Happiness", 3),
                ("Trust", 2)
            ])


        elif bond == "devoted":


            self.happiness = min(100, self.happiness + 5)
            self.trust = min(100, self.trust + 3)


            result["stat_changes"].extend([
                ("Happiness", 5),
                ("Trust", 3)
            ])


        # ----------------------------
        # PERSONALITY EFFECTS
        # ----------------------------
        personality_changes = apply_personality(
            self,
            "feed"
        )


        result["stat_changes"].extend(
            personality_changes
        )

        # ----------------------------
        # MOOD UPDATE
        # ----------------------------


        old_mood = self.mood


        update_mood(self)


        if old_mood != self.mood:
            result["mood_change"] = self.mood

        #MEMORY
        self.memory["interactions"]["feed"].append(self.mood)
        
        if self.mood == "happy":
            self.memory["emotional"]["comfort_level"] += 2

        # ----------------------------
        # BASE MOOD RESPONSE
        # ----------------------------
        message = random.choice(
            FEED_MESSAGES.get(
                self.mood,
                FEED_MESSAGES["neutral"]
            )
        ).format(name=self.name)

        # ----------------------------
        # PERSONALITY FLAVOUR
        # ----------------------------


        if self.personality in FEED_PERSONALITY_LINES:
            message += "\n\n" + random.choice(FEED_PERSONALITY_LINES[self.personality]).format(name=self.name)


        # BOND FLAVOUR
        # ----------------------------

        BOND_LINES = {


            "friendly":
                "It seems comfortable around you.",


            "trusted":
                "It clearly trusts your presence.",


            "devoted":
                "It relaxes completely when you're nearby."
        }


        if bond in BOND_LINES:
            message += "\n\n" + BOND_LINES[bond]

        # RARE MESSAGES

        if random.random() < 0.08:
            result["rare_event"] = random.choice(RARE_FEED_MESSAGES).format(name=self.name)


        new_bond = self.bond_level()

        if old_bond != new_bond:
            result["bond_change"] = new_bond

        # ----------------------------
        # FINAL MESSAGE
        # ----------------------------


        result["message"] = message
       
        # 🧠 MEMORY PIPELINE CALL (IMPORTANT)
        update_memory(self, "feed", result)

        return result

    def heal(self):
        import random
        from systems.mood_system import update_mood
        from data.heal_responses import (
            HEAL_FAILURE_MESSAGES,
            HEAL_PARTIAL_MESSAGES,
            HEAL_SUCCESS_MESSAGES,
            HEAL_CRIT_SUCCESS_MESSAGES,
            HEAL_CRIT_FAIL_MESSAGES
        )

        result = {
            "success": True,
            "message": "",
            "stat_changes": [],
            "mood_change": None,
            "bond_change": None,
            "rare_event": None
        }

        old_bond = self.bond_level()

        # ----------------------------
        # SUCCESS CHANCE SYSTEM
        # ----------------------------

        success_chance = 60

        if self.trust >= 70:
            success_chance += 20
        elif self.trust >= 40:
            success_chance += 10
        elif self.trust < 20:
            success_chance -= 20

        if self.personality == "calm":
            success_chance += 10
        elif self.personality == "stubborn":
            success_chance -= 5

        if self.mood == "scared":
            success_chance -= 25
        elif self.mood == "happy":
            success_chance += 10
        elif self.mood == "tired":
            success_chance += 5

        roll = random.randint(1, 100)

        # ----------------------------
        # CRITICAL FAILURE
        # ----------------------------

        if roll <= 5:
            result["message"] = random.choice(HEAL_CRIT_FAIL_MESSAGES).format(name=self.name)

            trust_loss = -5
            self.trust = max(0, self.trust + trust_loss)

            self.memory["experience"]["healing_bad"] += 1
            self.memory["emotional"]["stress_level"] += 10
            self.memory["flags"]["afraid_of_healing"] = True


            result["stat_changes"].append(("Trust", trust_loss))
            update_mood(self)
            result["mood_change"] = self.mood

            return result

        # ----------------------------
        # FAILURE
        # ----------------------------

        if roll > success_chance:
            result["message"] = random.choice(HEAL_FAILURE_MESSAGES).format(name=self.name)

            trust_loss = -2
            self.trust = max(0, self.trust + trust_loss)

            self.memory["experience"]["healing_bad"] += 1
            self.memory["emotional"]["stress_level"] += 10
            self.memory["flags"]["afraid_of_healing"] = True

            result["stat_changes"].append(("Trust", trust_loss))
            update_mood(self)
            result["mood_change"] = self.mood

            return result

        # ----------------------------
        # CRITICAL SUCCESS
        # ----------------------------

        if roll >= 95:
            heal_amount = 30
            trust_gain = 3

            self.health = min(100, self.health + heal_amount)
            self.trust = min(100, self.trust + trust_gain)

            self.health = min(100, self.health + heal_amount)
            self.trust = min(100, self.trust + trust_gain)

            self.memory["experience"]["healing_good"] += 1
            self.memory["emotional"]["stress_level"] = max(
                0,
                self.memory["emotional"]["stress_level"] - 5
            )

            result["message"] = random.choice(HEAL_CRIT_SUCCESS_MESSAGES).format(name=self.name)
            result["stat_changes"].append(("Health", heal_amount))
            result["stat_changes"].append(("Trust", trust_gain))

        # ----------------------------
        # FULL SUCCESS
        # ----------------------------

        elif roll > success_chance - 20:
            heal_amount = 20
            trust_gain = 2

            self.health = min(100, self.health + heal_amount)
            self.trust = min(100, self.trust + trust_gain)

            self.memory["experience"]["healing_good"] += 1
            self.memory["emotional"]["stress_level"] = max(
                0,
                self.memory["emotional"]["stress_level"] - 5
            )

            result["message"] = random.choice(HEAL_SUCCESS_MESSAGES).format(name=self.name)
            result["stat_changes"].append(("Health", heal_amount))
            result["stat_changes"].append(("Trust", trust_gain))

        # ----------------------------
        # PARTIAL SUCCESS
        # ----------------------------

        else:
            heal_amount = 10

            self.health = min(100, self.health + heal_amount)

            result["message"] = random.choice(HEAL_PARTIAL_MESSAGES).format(name=self.name)
            result["stat_changes"].append(("Health", heal_amount))

        # ----------------------------
        # MOOD UPDATE
        # ----------------------------

        update_mood(self)
        result["mood_change"] = self.mood

        # ----------------------------
        # RARE EVENT
        # ----------------------------

        if random.random() < 0.05:
            result["rare_event"] = random.choice([
                "{name} relaxes noticeably after treatment.",
                "{name} leans into your presence slightly more than before.",
                "{name} rests quietly beside you.",
                "{name} seems comforted by your care."
            ]).format(name=self.name)

        # 🧠 MEMORY PIPELINE CALL (IMPORTANT)
        update_memory(self, "heal", result)

        new_bond = self.bond_level()

        if old_bond != new_bond:
            result["bond_change"] = new_bond

        return result
    
    def rest(self):
    
        import random
    
        from systems.mood_system import update_mood
        from systems.personality_system import apply_personality
        from data.rest_responses import REST_MESSAGES, REST_PERSONALITY_LINES
    
        result = {
            "success": True,
            "message": "",
            "stat_changes": [],
            "mood_change": None,
            "bond_change": None,
            "rare_event": None
        }
    
        old_bond = self.bond_level()

        # ----------------------------
        # SHELTER VALUES
        # ----------------------------
    
        level = self.shelter.get("level", 1)
        comfort = self.shelter.get("comfort", 0)
    
        # ----------------------------
        # BASE RECOVERY (unchanged baseline feel)
        # ----------------------------
    
        energy_gain = 25
        happiness_gain = 10
    
        # ----------------------------
        # SHELTER BONUSES
        # ----------------------------
    
        energy_gain += (level - 1) * 2
        energy_gain += comfort // 10   # stronger comfort scaling
    
        happiness_gain += (level - 1)
        happiness_gain += comfort // 25
    
        trust_gain = (level - 1) // 2
    
        self.energy = min(100, self.energy + energy_gain)
        self.happiness = min(100, self.happiness + happiness_gain)
        self.trust = min(100, self.trust + trust_gain)
    
        result["stat_changes"].extend([
            ("Energy", energy_gain),
            ("Happiness", happiness_gain),
            ("Trust", trust_gain)
        ])
    
        # ----------------------------
        # BOND BONUS
        # ----------------------------
    
        bond = self.bond_level()
    
        if bond == "friendly":
            self.happiness = min(100, self.happiness + 2)
            result["stat_changes"].append(("Happiness", 2))
    
        elif bond == "trusted":
            self.happiness = min(100, self.happiness + 3)
            self.trust = min(100, self.trust + 2)
            result["stat_changes"].extend([("Happiness", 3), ("Trust", 2)])
    
        elif bond == "devoted":
            self.happiness = min(100, self.happiness + 5)
            self.trust = min(100, self.trust + 3)
            result["stat_changes"].extend([("Happiness", 5), ("Trust", 3)])
    
        # ----------------------------
        # PERSONALITY EFFECTS
        # ----------------------------
    
        personality_changes = apply_personality(self, "rest")
        result["stat_changes"].extend(personality_changes)
    
        # ----------------------------
        # MOOD UPDATE
        # ----------------------------
    
        old_mood = self.mood
        update_mood(self)
    
        if old_mood != self.mood:
            result["mood_change"] = self.mood
    
        # ----------------------------
        # BASE MESSAGE
        # ----------------------------
    
        message = random.choice(
            REST_MESSAGES.get(self.mood, REST_MESSAGES["neutral"])
        ).format(name=self.name)
    
        # ----------------------------
        # PERSONALITY FLAVOUR
        # ----------------------------
    
        if self.personality in REST_PERSONALITY_LINES:
            message += "\n\n" + REST_PERSONALITY_LINES[self.personality]
    
        # ----------------------------
        # BOND FLAVOUR
        # ----------------------------
    
        BOND_LINES = {
            "friendly": "It seems comfortable around you.",
            "trusted": "It clearly trusts your presence.",
            "devoted": "It relaxes completely when you're nearby."
        }
    
        if bond in BOND_LINES:
            message += "\n\n" + BOND_LINES[bond]
    
        # ----------------------------
        # SHELTER FLAVOUR (NEW)
        # ----------------------------
    
        if level >= 5:
            message += f"\n\nIts beautifully decorated home leaves {self.name} completely refreshed."
    
        elif level >= 3:
            message += f"\n\n{self.name} wakes feeling comfortable in its well-kept home."
    
        elif comfort >= 20:
            message += f"\n\n{self.name} seems to appreciate the comfort of its home."
    
        # ----------------------------
        # FAVOURITE ITEM BONUS (NEW)
        # ----------------------------
    
        favorites = self.memory.get("favorites", {}).get("items", [])
    
        if favorites and random.random() < 0.25:
            self.happiness = min(100, self.happiness + 2)
    
            result["stat_changes"].append(("Happiness", 2))
    
            message += f"\n\nBefore settling down, {self.name} curls up beside one of its favourite possessions."
    
        # ----------------------------
        # RARE EVENT
        # ----------------------------
    
        if random.random() < 0.08:
    
            result["rare_event"] = random.choice([
    
                f"{self.name} shifts closer to you in its sleep.",
                f"You notice {self.name}'s breathing slow into a deep calm rhythm.",
                f"{self.name} lets out a quiet sound before fully resting.",
                f"{self.name} seems to be dreaming peacefully."
            ])
    
        new_bond = self.bond_level()

        if old_bond != new_bond:
            result["bond_change"] = new_bond

        update_memory(self, "rest", result)

        # ----------------------------
        # FINAL MESSAGE
        # ----------------------------
    
        result["message"] = message
    
        return result
     
    # ----------------------------
    # 📊 STATUS CHECKS
    # ----------------------------

    def is_starving(self):
        return self.hunger <= 20

    def is_exhausted(self):
        return self.energy <= 20
    
    def is_injured(self):
        return self.health <= 50

    def is_critically_injured(self):
        return self.health <= 20
    

    # ----------------------------
    # 🕒 BOND LEVELS
    # ---------------------------- 
    def bond_level(self):

        if self.trust >= 90:
            return "devoted"

        elif self.trust >= 70:
            return "trusted"

        elif self.trust >= 50:
            return "friendly"

        elif self.trust >= 20:
            return "wary"

        return "hostile"
        
    

    #MERGER HEALPER

    from collections import defaultdict

    @staticmethod
    def merge_stat_changes(changes):
        merged = defaultdict(int)

        for stat, value in changes:
            merged[stat] += value

        return merged

# ----------------------------
    @staticmethod
    def get_random_species():
        return random.choice(list(SPECIES_REGISTRY))
    
# ----------------------------
    # 💾 SERIALISATION (for JSON saving)
    # ----------------------------

    def to_dict(self):
        return {
            "name": self.name,
            "species": self.species,
            "trust": self.trust,
            "personality": self.personality,
            "mood": self.mood,
            "preferences_learned": self.preferences_learned,
            "recent_gifts": self.recent_gifts,
            "memory": self.memory,
            "health": self.health,
            "energy": self.energy,
            "hunger": self.hunger,
            "happiness": self.happiness,
            "shelter": {
            "level": self.shelter.get("level", 1),
            "items": self.shelter.get("items", [])
            }
        }
    def compare_stats(self, before):
        changes = []

        stats = {
            "hunger": "🍖 Hunger",
            "happiness": "😊 Happiness",
            "energy": "⚡ Energy",
            "health": "❤️ Health",
            "trust": "🤝 Trust",
            "personality": "Personality",
            "mood": "Mood"
        }

        current = self.to_dict()

        for stat, label in stats.items():

            old = before[stat]
            new = current[stat]

            if old == new:
                continue

            diff = new - old

            if diff > 0:
                changes.append(f"{label} +{diff}")
            else:
                changes.append(f"{label} {diff}")

        return changes


    @classmethod
    def from_dict(cls, data: dict):
        creature = cls(
        name=data["name"],
        species=data["species"],
        personality=data.get("personality") or random.choice(list(PERSONALITIES.keys())),
        mood=data.get("mood", "neutral"),
        trust=data.get("trust", 20),
        health=data.get("health", 20),
        energy=data.get("energy", 20),
        hunger=data.get("hunger", 20),
        happiness=data.get("happiness", 10),
    )

        creature.preferences_learned = data.get("preferences_learned", {})
        creature.recent_gifts = data.get("recent_gifts", [])

        creature.shelter = {
        "type": get_species_data(creature.species).get("shelter", "basic"),
        "level": data.get("shelter", {}).get("level", 1),
        "items": data.get("shelter", {}).get("items", [])
    }

    # ----------------------------
    # MEMORY PATCH (IMPORTANT)
    # ----------------------------
        creature.memory = data.get("memory", default_memory())

        from systems.memory_system import ensure_memory
        ensure_memory(creature.memory)

        return creature

    # ----------------------------
    # 🎲 RANDOM EVENTS
    # ----------------------------

    def random_event(self):
        events = [
            "found something shiny in the nest",
            "took a nap in the sun",
            "stole something from a nearby stash",
            "got into a small fight",
            "watched the sky for a while",
        ]
        return random.choice(events)
