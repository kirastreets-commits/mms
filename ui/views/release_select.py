class ReleaseSelect(discord.ui.Select):
    def __init__(self, options):
        super().__init__(
            placeholder="Choose a creature to release...",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):

        creature_name = self.values[0]

        player = get_or_create_player(interaction.user)
        creature = player.get_creature(creature_name)

        if not creature:
            return await interaction.response.send_message(
                "That creature could not be found.",
                ephemeral=True
            )

        player.creatures.remove(creature)
        save_player(player)

        await interaction.response.send_message(
            f"🕊️ {creature.nickname or creature.name} has been gently released back into the wild.",
            ephemeral=True
        )
