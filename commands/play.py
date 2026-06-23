from systems.action_renderer import render_action_embed
from systems.save_system import get_or_create_player, save_player


def setup(bot):

    @bot.command()
    async def play(ctx, creature_name: str):

        player = get_or_create_player(ctx.author)

        creature = player.get_creature(creature_name)

        if not creature:
            return await ctx.send("You don't have a creature with that name.")

        result = creature.play()

        save_player(player)

        embed = render_action_embed(
            title="Play Session",
            creature=creature,
            result=result,
            action_text=f"You bring **{creature.name}** to the Play Area."
        )

        await ctx.send(embed=embed)

