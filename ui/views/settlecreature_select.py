import discord

from data.preserves import PRESERVES

from systems.preserve_system import (
    get_preserve_capacity,
    get_preserve_residents,
    preserve_has_space
)


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

            preserve = PRESERVES.get(preserve_id)

            if not preserve:
                continue

            capacity = get_preserve_capacity(
                player,
                preserve_id
            )

            occupied = len(
                get_preserve_residents(
                    player,
                    preserve_id
                )
            )

            options.append(
                discord.SelectOption(
                    label=preserve["name"],
                    value=preserve_id,
                    emoji=preserve.get("emoji", "🌿"),
                    description=f"{occupied}/{capacity} creatures"
                )
            )

        # Safety check
        if options:
            self.add_item(
                SettleCreatureSelect(options)
            )


class SettleCreatureSelect(discord.ui.Select):

    def __init__(self, options):

        super().__init__(
            placeholder="Choose a preserve...",
            min_values=1,
            max_values=1,
            options=options
        )


    async def callback(
        self,
        interaction: discord.Interaction
    ):

        view: SettleCreatureView = self.view


        # ----------------------------
        # PLAYER CHECK
        # ----------------------------

        if str(interaction.user.id) != view.user_id:

            return await interaction.response.send_message(
                "This menu isn't for you.",
                ephemeral=True
            )


        preserve_id = self.values[0]


        # ----------------------------
        # CAPACITY CHECK
        # ----------------------------

        if not preserve_has_space(
            view.player,
            preserve_id
        ):

            return await interaction.response.send_message(
                "That preserve is currently full.",
                ephemeral=True
            )


        # ----------------------------
        # CONTINUE SETTLEMENT
        # ----------------------------

        await view.on_select_callback(
            interaction,
            preserve_id
        )
