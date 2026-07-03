
import discord
from systems.save_system import get_or_create_player, save_player

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
        description=f"Comfort: {creature.shelter.get('comfort')} \nLevel: {creature.shelter.get('level', 1)}",
        color=0x6bbf59
        )

        items = creature.shelter.get("items", [])


        if items:
            item_list = "\n".join(
                f"- {entry['item']} (State: {entry.get('state', 'normal')})"
                for entry in items
            )
            embed.add_field(name=f"Items in {shelter_name}", value=item_list, inline=False)

        await ctx.send(embed=embed)
