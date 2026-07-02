from systems.action_renderer import render_action_embed
from systems.save_system import get_or_create_player, save_player
from ui.heal_views import HealView


def setup(bot):

    @bot.command()
    async def heal(ctx, creature_name: str):

        player = get_or_create_player(ctx.author)

        creature = player.get_creature(creature_name)

        if not creature:
            return await ctx.send("You don't have a creature with that name.")

        result = creature.heal()


        save_player(player)

        view = HealView(player, creature)

        await ctx.send(
            f"Choose a healing resource for **{creature.name}**.",
            view=view
        )
