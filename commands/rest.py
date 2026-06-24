from systems.action_renderer import render_action_embed
from systems.save_system import get_or_create_player, save_player


def setup(bot):

    @bot.command()
    async def rest(ctx, creature_name: str):

        player = get_or_create_player(ctx.author)

        creature = player.get_creature(creature_name)

        if not creature:
            return await ctx.send("You don't have a creature with that name.")

        result = creature.rest()

        save_player(player)

        embed = render_action_embed(
            title="💤 Resting Time",
            creature=creature,
            result=result,
            action_text=f"You bring **{creature.name}** to its {creature.shelter_name()}."
        )

        await ctx.send(embed=embed)
