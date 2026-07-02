from systems.save_system import get_or_create_player, save_player
from systems.gift_system import gift_creature
from ui.gift_views import GiftView

def setup(bot):

    @bot.command()
    async def gift(ctx, creature_name: str):
        player = get_or_create_player(ctx.author)
        creature = player.get_creature(creature_name)
    
        if not creature:
            return await ctx.send("You don't have that creature.")

        save_player(player)
    
        view = GiftView(player, creature)
        
        await ctx.send(
                f"Choose a gift for **{creature.name}**.",
                view=view
            )

