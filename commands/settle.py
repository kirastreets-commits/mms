import discord

from data.preserves import PRESERVES

from systems.preserve_system import (
    get_preserve,
    get_available_preserves,
    get_available_shelter_sites,
    preserve_has_space,
)

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

        # -------------------------
        # Already settled
        # -------------------------

        if creature.shelter.get("location"):

            preserve = get_preserve(
                creature.shelter["location"]
            )

            preserve_name = (
                preserve["name"]
                if preserve
                else creature.shelter["location"]
            )

            return await ctx.send(
                f"🏡 **{creature.name}** already lives in **{preserve_name}**."
            )

        # -------------------------
        # Find suitable preserves
        # -------------------------

        available = get_available_preserves(
            player,
            creature
        )

        if not available:
            return await ctx.send(
                "There aren't any suitable preserves available right now."
            )

        # -------------------------
        # Called when preserve selected
        # -------------------------

        async def choose_preserve(interaction, preserve_id):

            # Check capacity again
            if not preserve_has_space(
                player,
                preserve_id
            ):
                return await interaction.response.send_message(
                    "That preserve is currently full.",
                    ephemeral=True
                )

            available_sites = get_available_shelter_sites(
                player,
                preserve_id
            )

            if not available_sites:
                return await interaction.response.send_message(
                    "There are no available shelter sites there.",
                    ephemeral=True
                )

            # Pick first available shelter site
            site = available_sites[0]

            # Assign creature home
            creature.shelter["location"] = preserve_id
            creature.shelter["site"] = site

            # Journal entry
            record_settlement(
                player,
                creature,
                PRESERVES[preserve_id]
            )

            save_player(player)

            preserve = PRESERVES[preserve_id]

            await interaction.response.edit_message(
                content=(
                    f"{preserve['emoji']} **{creature.name}** has settled into "
                    f"**{preserve['name']}**!\n\n"
                    f"They chose **{site}** as the perfect place to build "
                    f"their **{creature.shelter['type']}**."
                ),
                view=None
            )

        # -------------------------
        # Show preserve selection
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