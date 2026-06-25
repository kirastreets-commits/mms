from systems.save_system import get_or_create_player, save_player
from systems.gift_system import gift_creature

def setup(bot):

    @bot.command()
    async def gift(ctx, creature_name: str, item_id: str):
        player = get_or_create_player(ctx.author)
        creature = player.get_creature(creature_name)
    
        if not creature:
            return await ctx.send("You don't have that creature.")
    
        result = gift_creature(player, creature, item_id)
    
        if not result["success"]:
            return await ctx.send(result["message"])
    
        embed = build_gift_embed(creature, item_id, result)
    
        await ctx.send(embed=embed)
