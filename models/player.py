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
        tutorial_stage=0,
        tutorial_complete=False,
        has_starter=False
    ):

        self.user_id = user_id
        self.name = name

        self.inventory = inventory or {}
        self.creatures = creatures or []
        self.discovered_species = discovered_species or []
        self.journal_entries = journal_entries or []

        self.has_starter = has_starter

        self.tutorial_stage = tutorial_stage
        self.tutorial_complete = tutorial_complete

    # ----------------------------
    # 🐉 CREATURE MANAGEMENT
    # ----------------------------


    def add_discovered_species(self, discovered_species):
        self.discovered_species.append(species)
        species = species_name

    def add_creature(self, creature):
        self.creatures.append(creature)

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
    
    # JOURNAL

    def add_journal_entry(self, text):

        self.journal_entries.append(text)

        # Keep only latest 100 entries
        self.journal_entries = self.journal_entries[-100:]
    
    # ----------------------------
    # 🎒 INVENTORY SYSTEM
    # ----------------------------

    def add_item(self, item):
        self.inventory.append(item)

    def add_to_inventory(player, item_id, amount=1):
        player.inventory[item_id] = player.inventory.get(item_id, 0) + amount

    def remove_item(self, item):

        if item in self.inventory:
            self.inventory.remove(item)

    # ----------------------------
    # 💾 SAVE SYSTEM
    # ----------------------------

    def to_dict(self):

        return {
            "user_id": self.user_id,
            "name": self.name,
            "inventory": self.inventory,
            "discovered_species": self.discovered_species,
            "journal_entries": self.journal_entries,
            "tutorial_stage": self.tutorial_stage,
            "tutorial_complete": self.tutorial_complete,
            "has_starter": self.has_starter,

            "creatures": [
                creature.to_dict()
                for creature in self.creatures
            ]
        }

    @classmethod
    def from_dict(cls, data, Creature):

        creatures = [
            Creature.from_dict(c_data)
            for c_data in data.get("creatures", [])
        ]

        return cls(
            user_id=data["user_id"],
            name=data["name"],
            inventory=data.get("inventory", []),
            creatures=creatures,
            discovered_species=data.get("discovered_species", []),
            journal_entries=data.get("journal_entries") or [], 
            tutorial_stage=data.get("tutorial_stage", 0),
            tutorial_complete=data.get("tutorial_complete", False),
            has_starter=data.get("has_starter", False)
        )
