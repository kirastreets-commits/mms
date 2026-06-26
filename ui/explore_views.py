
class ExploreMenuView(discord.ui.View):
    def __init__(self, player):
        super().__init__(timeout=60)
        self.player = player

    @discord.ui.button(label="🏠 Inside Sanctuary", style=discord.ButtonStyle.primary)
    async def inside(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.open_location_menu(interaction, "inside")

    @discord.ui.button(label="🌳 Sanctuary Grounds", style=discord.ButtonStyle.success)
    async def grounds(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.open_location_menu(interaction, "grounds")

    @discord.ui.button(label="🌌 Outside Sanctuary", style=discord.ButtonStyle.danger)
    async def outside(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.open_location_menu(interaction, "outside")

    async def open_location_menu(self, interaction, location_type):
        view = LocationSelectView(self.player, location_type)

        embed = discord.Embed(
            title=f"🧭 {location_type.title()} Exploration",
            description="Choose a specific location:",
            color=0x3498db
        )

        await interaction.response.edit_message(embed=embed, view=view)

  class LocationSelectView(discord.ui.View):
    def __init__(self, player, location_type):
        super().__init__(timeout=60)
        self.player = player
        self.location_type = location_type

        options = []

        for loc_id, data in LOCATIONS.items():
            if data["type"] == location_type and loc_id in player.unlocked_locations:
                options.append(
                    discord.SelectOption(
                        label=data["name"],
                        value=loc_id
                    )
                )

        self.add_item(LocationSelectMenu(player, options))

    class LocationSelectMenu(discord.ui.Select):
    def __init__(self, player, options):
        self.player = player

        super().__init__(
            placeholder="Choose a location...",
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        location_id = self.values[0]
        location = LOCATIONS[location_id]

        result = self.explore_location(self.player, location_id, location)

        save_player(self.player)

        embed = discord.Embed(
            title=f"✨ Exploring {location['name']}",
            description=result,
            color=0xf1c40f
        )

        await interaction.response.edit_message(embed=embed, view=None)

    def explore_location(self, player, location_id, location):
        import random

        roll = random.randint(1, 100)

        # 🌫 Nothing event
        if roll < 20:
            return "The area is quiet… nothing unusual stirs."

        # 🍓 Item event
        elif roll < 55:
            item = random.choice(location["items"])
            player.inventory[item] = player.inventory.get(item, 0) + 1
            return f"You found **{item}** hidden in the area."

        # 📜 Lore event
        elif roll < 75:
            lore = f"A forgotten memory stirs in {location['name']}..."
            player.journal_entries.append(lore)
            return f"📜 Lore discovered:\n*{lore}*"

        # 🐾 Creature event (placeholder for later system)
        elif roll < 90:
            return "A creature watches you from afar… but disappears before you can react."

        # 🔓 Progress event
        else:
            return self.progress_unlock(player, location_id)

    def progress_unlock(self, player, location_id):
        location = LOCATIONS[location_id]

        if "connected" not in location:
            return "You sense no new paths from here."

        for next_loc in location["connected"]:
            if next_loc not in player.unlocked_locations:
                player.unlocked_locations.append(next_loc)
                return f"🔓 A new path has opened: **{next_loc}**"

        return "You feel this area is already fully explored."
