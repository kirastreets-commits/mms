from systems.journal_system import (
    record_adoption,
    record_discovery,
)

from data.preserves import PRESERVES

# PLAYER

class Player:

    def __init__(
        self,
        user_id,
        name,
        inventory=None,
        creatures=None,
        discovered_species=None,
        journal_entries= None,
        unlocked_locations=None,
        tutorial_stage=0,
        tutorial_complete=False,
        has_starter=False,
        preserves=None
    ):

        self.user_id = user_id
        self.name = name

        self.inventory = inventory if isinstance(inventory, dict) else {}
        self.creatures = creatures if isinstance(creatures, list) else []
        self.discovered_species = discovered_species if isinstance(discovered_species, list) else []
        self.journal_entries = journal_entries if isinstance(journal_entries, list) else []
        self.unlocked_locations = (unlocked_locations if isinstance(unlocked_locations, list) else ["sanctuary_core"])
        self.seen_lore = []

        self.has_starter = has_starter

        self.tutorial_stage = tutorial_stage
        self.tutorial_complete = tutorial_complete

        # ----------------------------
        # 🌿 PRESERVES
        # ----------------------------

        default_preserves = {
            preserve_id: {
                "level": 1,
                "occupied": [],
                "restoration": 0,
                "unlocked": PRESERVES[preserve_id].get("unlock_level", 1) == 1
            }
            for preserve_id in PRESERVES
        }

        # Load existing preserve data if available
        if preserves is None:
            preserves = default_preserves
        else:
            # Add any new preserves that weren't in older save files
            for preserve_id, default_data in default_preserves.items():

                if preserve_id not in preserves:
                    preserves[preserve_id] = default_data
                else:
                    for key, value in default_data.items():
                        preserves[preserve_id].setdefault(key, value)

                    self.preserves = preserves

    # ----------------------------
    # 🐉 CREATURE MANAGEMENT
    # ----------------------------

    
    def add_creature(self, creature, named=True):

        self.creatures.append(creature)

        self.add_discovered_species(creature.species)


        record_adoption(
            self,
            creature,
            named
        )

    def remove_creature(self, creature_name):

        self.creatures = [
            c for c in self.creatures
            if c.name.lower() != creature_name.lower()
        ]

    def get_creature(self, creature_name):

        for creature in self.creatures:

            if creature.name.lower() == creature_name.lower():
                return creature

        return None
    
    def add_discovered_species(self, species_name):

        if species_name not in self.discovered_species:

            self.discovered_species.append(species_name)

            from systems.journal_system import record_discovery

            record_discovery(
                self,
                species_name
            )

            return True

        return False
    
    # JOURNAL


    def add_journal_entry(self, category, text, day=None):
    
        self.journal_entries.append({
            "category": category,
            "text": text,
            "day": day,
            "timestamp": datetime.now().isoformat()
        })
    
        # Keep the latest 200 entries
        self.journal_entries = self.journal_entries[-200:]
    # ----------------------------
    # 🎒 INVENTORY SYSTEM
    # ----------------------------

    def add_to_inventory(self, item_id, amount=1):
        if not isinstance(self.inventory, dict):
            self.inventory = {}
    
        if item_id not in self.inventory:
            self.inventory[item_id] = 0
    
        self.inventory[item_id] += amount
    
    def remove_from_inventory(self, item_id, amount=1):
    
        if item_id not in self.inventory:
            return False
    
        self.inventory[item_id] -= amount
    
        if self.inventory[item_id] <= 0:
            del self.inventory[item_id]
    
        return True

    # ----------------------------
    # 💾 SAVE SYSTEM
    # ----------------------------

    def to_dict(self):

        return {
            "user_id": self.user_id,
            "name": self.name,
            "inventory": self.inventory,
            "creatures": [c.to_dict() for c in self.creatures],
            "discovered_species": self.discovered_species,
            "journal_entries": self.journal_entries,
            "unlocked_locations": self.unlocked_locations,
            "tutorial_stage": self.tutorial_stage,
            "tutorial_complete": self.tutorial_complete,
            "has_starter": self.has_starter,
            "preserves": self.preserves,
        }

    @classmethod
    def from_dict(cls, data, Creature):

        print("RAW CREATURE DATA:", data.get("creatures"))
    
        creatures = [
            Creature.from_dict(c)
            for c in data.get("creatures", [])
        ]
    
        inventory = data.get("inventory", {})
        if not isinstance(inventory, dict):
            inventory = {}

        journal_entries = []

        for entry in data.get("journal_entries", []):

            # Old save format
            if isinstance(entry, str):
                journal_entries.append({
                    "category": "general",
                    "text": entry,
                    "timestamp": None
                })

            # New save format
            else:
                journal_entries.append(entry)
    
        return cls(
            user_id=str(data["user_id"]),
            name=data["name"],
            inventory=inventory,
            creatures=creatures,
            discovered_species=data.get("discovered_species", []),
            journal_entries=journal_entries,
            unlocked_locations=data.get("unlocked_locations", ["sanctuary_core"]),
            tutorial_stage=data.get("tutorial_stage", 0),
            tutorial_complete=data.get("tutorial_complete", False),
            has_starter=data.get("has_starter", False),
            preserves=data.get("preserves")
        )
