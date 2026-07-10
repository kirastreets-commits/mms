import discord

from data.preserves import PRESERVES
from systems.preserve_system import (
    get_preserve_capacity,
    get_preserve_residents,
    preserve_has_space,
)


class PreserveView(discord.ui.View):

    def __init__(
        self,
        player,
        available_preserves,
        on_select_callback,
        creature=None,
        check_capacity=False,
        placeholder="Choose a preserve..."
    ):
        super().__init__(timeout=120)

        self.player = player
        self.creature = creature
        self.user_id = str(player.user_id)
        self.on_select_callback = on_select_callback
        self.check_capacity = check_capacity

        options = []

        for preserve_id in available_preserves:

            preserve = PRESERVES.get(preserve_id)

            if not preserve:
                continue

            level = player.preserves[preserve_id]["level"]

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
                    description=f"Lv {level} • {occupied}/{capacity} creatures"
                )
            )

        if options:
            self.add_item(
                PreserveSelect(
                    options,
                    placeholder
                )
            )


class PreserveSelect(discord.ui.Select):

    def __init__(
        self,
        options,
        placeholder
    ):
        super().__init__(
            placeholder=placeholder,
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(
        self,
        interaction: discord.Interaction
    ):

        view: PreserveView = self.view

        if str(interaction.user.id) != view.user_id:
            return await interaction.response.send_message(
                "This menu isn't for you.",
                ephemeral=True
            )

        preserve_id = self.values[0]

        if (
            view.check_capacity
            and not preserve_has_space(
                view.player,
                preserve_id
            )
        ):
            return await interaction.response.send_message(
                "That preserve is currently full.",
                ephemeral=True
            )

        await view.on_select_callback(
            interaction,
            preserve_id
        )