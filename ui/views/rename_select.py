class RenameSelect(discord.ui.Select):
    def __init__(self, options):
        super().__init__(
            placeholder="Choose a creature...",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):

        creature_name = self.values[0]

        await interaction.response.send_modal(
            RenameModal(creature_name)
        )
