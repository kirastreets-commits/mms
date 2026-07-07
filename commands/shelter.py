import discord

from systems.preserve_system import (
    get_preserve,
    get_available_shelter_sites,
    get_preserve_capacity,
    get_preserve_residents,
)
from models import creature, player
from systems.save_system import (
    get_or_create_player,
    save_player,
)

from systems.journal_system import record_settlement
from ui.views.settlecreature_select import SettleCreatureView


def setup(bot):

    @bot.command()
    async def settle(ctx, creature_name: str):

        player = get_or_create_player(ctx.author)
        creature = player.get_creature(creature_name)

        if not creature:
            return await ctx.send(
                "You don't have a creature with that name."
            )

        # Already settled
        if creature.shelter.get("location"):

            preserve = get_preserve(creature.shelter["location"])

            preserve_name = (
                preserve["name"]
                if preserve
                else creature.shelter["location"]
            )

            return await ctx.send(
                f"🏡 **{creature.name}** already lives in **{preserve_name}**."
            )

        # Find suitable preserves
        available = get_available_preserves(player, creature)

        if not available:
            return await ctx.send(
                "There aren't any suitable preserves available right now."
            )

        # -------------------------
        # Called when a preserve is selected
        # -------------------------
        async def choose_preserve(interaction, preserve_id):

            if not player.preserve_has_space(preserve_id):
                return await interaction.response.send_message(
                    "That preserve is now full.",
                    ephemeral=True
                )
            
            if creature.name not in player.preserves[preserve_id]["occupied"]:
                player.preserves[preserve_id]["occupied"].append(creature.name)
            
            creature.shelter["location"] = preserve_id

            player.preserves[preserve_id]["occupied"].append(
                creature.name
            )

            record_settlement(player, creature, PRESERVES[preserve_id])

            save_player(player)

            preserve = PRESERVES[preserve_id]

            await interaction.response.edit_message(
                content=(
                    f"{preserve['emoji']} **{creature.name}** has settled into "
                    f"**{preserve['name']}**!\n\n"
                    f"They begin building their **{creature.shelter['type']}** among the "
                    f"surrounding wilderness."
                ),
                view=None
            )

        # -------------------------
        # Show the preserve menu
        # -------------------------
        view = SettleCreatureView(
            available_preserves=available,
            player=player,
            creature=creature,
            on_select_callback=choose_preserve,
        )

        await ctx.send(
            f"🏡 Choose where **{creature.name}** should build their shelter.",
            view=view
        )
