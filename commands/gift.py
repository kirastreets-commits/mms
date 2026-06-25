from systems.save_system import get_or_create_player, save_player

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

        await ctx.send(
            f"{creature.name} {result['reaction']} the gift!\n"
            f"+{result['bond_gain']} bond"
    )
