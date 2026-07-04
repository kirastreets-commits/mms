import discord
from systems.save_system import get_or_create_player
from systems.shelter_system import update_shelter, SHELTER_LEVELS
from data.resources import RESOURCES


def setup(bot):

    @bot.command()
    async def shelter(ctx, creature_name: str):

        player = get_or_create_player(ctx.author)

        creature = player.get_creature(creature_name)

        if not creature:
            return await ctx.send("You don't have a creature with that name.")

        shelter_name = creature.shelter.get("type", "Shelter")

        # Update shelter stats
        shelter_result = update_shelter(creature)

        comfort = shelter_result["comfort"]
        level = shelter_result["new_level"]

        # Comfort description
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

        # Progress to next level
        next_level = level + 1
        if next_level in SHELTER_LEVELS:
            progress = f"{comfort} / {SHELTER_LEVELS[next_level]} Comfort"
        else:
            progress = "Maximum Level"

        embed = discord.Embed(
            title=f"🏡 {creature.name}'s {shelter_name}",
            description=(
                f"⭐ **Comfort:** {comfort}\n"
                f"🏠 **Level:** {level}\n\n"
                f"*{comfort_text}*"
            ),
            color=0x6BBF59
        )

        embed.add_field(
            name="📈 Progress",
            value=progress,
            inline=False
        )

        # Shelter items
        items = creature.shelter.get("items", [])

        if items:
            item_lines = []

            for entry in items:
                resource = RESOURCES.get(entry["item"], {})

                emoji = resource.get("emoji", "📦")
                name = resource.get(
                    "name",
                    entry["item"].replace("_", " ").title()
                )

                state = entry.get("state", "kept")

                state_icon = {
                    "favorite": "🌟",
                    "kept": "🏡",
                    "ignored": "📦"
                }.get(state, "•")

                item_lines.append(f"{state_icon} {emoji} **{name}**")

            embed.add_field(
                name="🪴 Shelter Items",
                value="\n".join(item_lines),
                inline=False
            )
        else:
            embed.add_field(
                name="🪴 Shelter Items",
                value="*This shelter is empty for now.*",
                inline=False
            )

        await ctx.send(embed=embed)
