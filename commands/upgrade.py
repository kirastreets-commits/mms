import discord

from systems.save_system import (
    get_or_create_player,
    save_player
)

from systems.preserve_system import (
    can_upgrade_preserve,
    upgrade_preserve
)

from ui.upgrade_preserve_view import UpgradePreserveView


def setup(bot):

    @bot.command()
    async def upgrade(ctx):

        player = get_or_create_player(ctx.author)

        view = UpgradePreserveView(
            player=player,
            on_upgrade=lambda interaction, preserve_id:
                handle_upgrade(
                    interaction,
                    player,
                    preserve_id
                )
        )

        await ctx.send(
            "🏗️ **Choose a preserve to restore.**",
            view=view
        )


async def handle_upgrade(
    interaction,
    player,
    preserve_id
):

    if not can_upgrade_preserve(player, preserve_id):

        return await interaction.response.send_message(
            "That preserve can't be upgraded.",
            ephemeral=True
        )

    upgrade_preserve(
        player,
        preserve_id
    )

    save_player(player)

    await interaction.response.send_message(
        "✨ Preserve upgraded!",
        ephemeral=True
    )