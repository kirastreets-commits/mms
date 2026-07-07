import discord

from data.preserves import PRESERVES


class SettleCreatureView(discord.ui.View):
    def __init__(
        self,
        available_preserves,
        player,
        creature,
        on_select_callback
    ):
        super().__init__(timeout=120)

        self.player = player
        self.creature = creature
        self.user_id = str(player.user_id)
        self.on_select_callback = on_select_callback

        options = []

        for preserve_id in available_preserves:

            preserve = PRESERVES[preserve_id]
            player_data = player.preserves[preserve_id]

            occupied = len(player_data["occupied"])

            capacity = (
                preserve["starting_capacity"]
                + (player_data["level"] - 1)
                * preserve["capacity_per_level"]
            )

            options.append(
                discord.SelectOption(
                    label=preserve["name"],
                    value=preserve_id,
                    emoji=preserve["emoji"],
                    description=f"{occupied}/{capacity} shelters"
                )
            )

        self.add_item(SettleCreatureSelect(options))


class SettleCreatureSelect(discord.ui.Select):
    def __init__(self, options):
        super().__init__(
            placeholder="Choose a preserve...",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):

        view: SettleCreatureView = self.view

        # Only the original player can use this menu
        if str(interaction.user.id) != view.user_id:
            return await interaction.response.send_message(
                "This menu isn't for you.",
                ephemeral=True
            )

        preserve_id = self.values[0]

        await view.on_select_callback(
            interaction,
            preserve_id
        )