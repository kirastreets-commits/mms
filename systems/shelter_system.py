class Shelter:
    def __init__(self):
        self.items = []

    def calculate_comfort(self, species_name):
        comfort = 0

        preferences = set(
            tag.lower().strip()
            for tag in get_species_preferences(species_name)
        )

        for item_id in self.items:
            resource = RESOURCES.get(item_id)
            if not resource:
                continue

            # base comfort
            comfort += resource.get("comfort", 0)

            # tag matching
            for tag in resource.get("tags", []):
                if tag.lower().strip() in preferences:
                    comfort += 2

        return comfort
        def update_shelter(creature):
        comfort = creature.shelter.get("comfort", 0)

        if comfort >= 100:
            level = 5
        elif comfort >= 60:
            level = 4
        elif comfort >= 35:
            level = 3
        elif comfort >= 15:
            level = 2
        else:
            level = 1
 
        creature.shelter["level"] = level
