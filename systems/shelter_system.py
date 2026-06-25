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