
import discord
from discord import reaction

from models import creature


def setup(bot):

    @bot.command()
    async def shelter(ctx, creature_name: str):

        player = get_or_create_player(ctx.author)

        creature = player.get_creature(creature_name)

        if not creature:
            return await ctx.send("You don't have a creature with that name.")

        shelter_name = creature.shelter.get("type", "shelter")

        embed = discord.Embed(
        title=f"{creature.name}'s {shelter_name}",
        description=f"Comfort: {creature.shelter.get('comfort', 0)} ⭐\nLevel: {creature.shelter.get('level', 1)}",
        color=colors.get(reaction, discord.Color.green())
        )

        await ctx.send(embed=embed)