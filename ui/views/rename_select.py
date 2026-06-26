class RenameSelectView(discord.ui.View):
    def __init__(self, user_id):
        super().__init__(timeout=120)
        self.user_id = user_id

    @discord.ui.select(placeholder="Choose a creature to rename")
    async def select_creature(self, interaction: discord.Interaction, select: discord.ui.Select):

        creature_name = select.values[0]

        await interaction.response.send_modal(
            RenameModal(creature_name)
        )
