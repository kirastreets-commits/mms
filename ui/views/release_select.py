class ReleaseSelectView(discord.ui.View):
    def __init__(self, user_id):
        super().__init__(timeout=120)
        self.user_id = user_id

    @discord.ui.select(placeholder="Choose a creature to release")
    async def select_creature(self, interaction: discord.Interaction, select: discord.ui.Select):

        creature_name = select.values[0]

        await interaction.response.send_message(
            f"Are you sure you want to release **{creature_name}**?",
            ephemeral=True
        )
