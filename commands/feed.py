from systems.action_renderer import render_action_embed
from systems.save_system import get_or_create_player, save_player


def setup(bot):

    @bot.command()
    async def feed(ctx, creature_name: str):

        player = get_or_create_player(ctx.author)

        creature = player.get_creature(creature_name)

        if not creature:
            return await ctx.send("You don't have a creature with that name.")

        result = creature.feed()

        save_player(player)
    

        embed = render_action_embed(
            title="🍖 Feeding Time",
            creature=creature,
            result=result,
            action_text=f"You make **{creature.name}'s** food and put it down in front of them."
        )

        await ctx.send(embed=embed)
