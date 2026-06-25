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

        if not result.get("success"):
            return await ctx.send(result.get("message", "Something went wrong."))

        save_player(player)

        await ctx.send(
            f"🎁 {creature.name} {result.get('reaction', 'accepted')} the gift!\n"
            f"🤝 Bond: {result.get('bond_gain', 0):+}\n"
            f"🏡 Comfort: {result.get('comfort_gain', 0):+}"
        )
