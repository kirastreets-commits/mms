class ReleaseSelectView(discord.ui.View):
    def __init__(self, user_id: int):
        super().__init__(timeout=120)
        self.user_id = user_id

        player = get_or_create_player_by_id(user_id)

        options = [
            discord.SelectOption(
                label=creature.nickname or creature.name,
                value=creature.name
            )
            for creature in player.creatures
        ]

        self.add_item(ReleaseSelect(options))

    def interaction_check(self, interaction: discord.Interaction):
        return interaction.user.id == self.user_id
