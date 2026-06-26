import discord


class CreatureSelectView(discord.ui.View):
    def __init__(self, creatures, on_select_callback, user_id):
        super().__init__(timeout=120)

        self.creatures = creatures
        self.on_select_callback = on_select_callback
        self.user_id = user_id

        options = [
            discord.SelectOption(
                label=c.name,
                value=c.name,
                description=f"Lvl {getattr(c, 'level', '?')}"
            )
            for c in creatures
        ]

        self.add_item(CreatureSelect(options))

class CreatureSelect(discord.ui.Select):
    def __init__(self, options):
        super().__init__(
            placeholder="Choose a creature...",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        view: CreatureSelectView = self.view

        creature_name = self.values[0]

        # call the NPC-provided callback
        await view.on_select_callback(interaction, creature_name)
