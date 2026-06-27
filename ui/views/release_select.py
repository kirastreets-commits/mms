class ReleaseSelectView(discord.ui.View):
    def __init__(self, user_id: int):
        super().__init__(timeout=120)
        self.user_id = user_id

        player = get_or_create_player_by_id(user_id)

        options = []

        # Remove any corrupted creatures
        player.creatures = [
            creature
            for creature in player.creatures
            if hasattr(creature, "name") and isinstance(creature.name, str)
        ]
        
        save_player(player)
        
        for creature in player.creatures:
            options.append(
                discord.SelectOption(
                    label=creature.name,
                    value=creature.name
                )
            )

self.add_item(ReleaseSelect(options))

        self.add_item(ReleaseSelect(options))

    def interaction_check(self, interaction: discord.Interaction):
        return interaction.user.id == self.user_id
