
import discord
from systems.save_system import get_or_create_player, save_player
from systems.shelter_system import get_shelter_comfort
from systems.shelter_system import update_shelter
from models import creature


def setup(bot):

    @bot.command()
    async def shelter(ctx, creature_name: str):

        player = get_or_create_player(ctx.author)

        creature = player.get_creature(creature_name)

        if not creature:
            return await ctx.send("You don't have a creature with that name.")

        shelter_name = creature.shelter.get("type", "shelter")
        comfort = get_shelter_comfort(creature.shelter)

        from data.resources import RESOURCES

        item_lines = []

        for entry in items:
            resource = RESOURCES.get(entry["item"], {})

            emoji = resource.get("emoji", "📦")
            name = resource.get("name", entry["item"].replace("_", " ").title())

            state = entry.get("state", "kept")

            state_icon = {
                "favorite": "🌟",
                "kept": "🏡",
                "ignored": "📦"
            }.get(state, "•")

            item_lines.append(f"{state_icon} {emoji} **{name}**")
        
        shelter_result = update_shelter(creature)
        
        embed = discord.Embed(
        title=f"{creature.name}'s {shelter_name}",
        description=f"Comfort: {shelter_result['comfort']} \nLevel: {shelter_result['new_level']}",
        color=0x6bbf59
        )

        items = creature.shelter.get("items", [])
        


        if items:
            item_list = "\n".join(
                f"- {entry['item']} (State: {entry.get('state', 'normal')})"
                for entry in items
            )
            embed.add_field(name=f"Items in {shelter_name}", value=item_list, inline=False)

        comfort = shelter_result["comfort"]

        if comfort < 10:
            comfort_text = "A simple shelter."
        elif comfort < 25:
            comfort_text = "Warm and comfortable."
        elif comfort < 45:
            comfort_text = "Very cozy."
        elif comfort < 70:
            comfort_text = "A beautiful home."
        else:
            comfort_text = "A luxurious sanctuary."

        embed.description = (
            f"⭐ **Comfort:** {comfort}\n"
            f"🏠 **Level:** {shelter_result['new_level']}\n\n"
            f"*{comfort_text}*"
        )

        await ctx.send(embed=embed)
