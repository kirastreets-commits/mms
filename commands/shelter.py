import discord

from systems.save_system import get_or_create_player
from systems.shelter_system import (
    update_shelter,
    SHELTER_LEVELS,
    generate_shelter_description,
)
from data.resources import RESOURCES


def setup(bot):

    @bot.command()
    async def shelter(ctx, creature_name: str):
        player = get_or_create_player(ctx.author)

        creature = player.get_creature(creature_name)

        if not creature:
            return await ctx.send("You don't have a creature with that name.")

        # -----------------------------
        # Update Shelter
        # -----------------------------
        shelter_name = creature.shelter.get("type", "Shelter")

        shelter_result = update_shelter(creature)

        comfort = shelter_result["comfort"]
        level = shelter_result["new_level"]

        # -----------------------------
        # Progress
        # -----------------------------
        next_level = level + 1

        if next_level in SHELTER_LEVELS:
            progress = f"{comfort} / {SHELTER_LEVELS[next_level]} Comfort"
        else:
            progress = "✨ Maximum Shelter Level"

        # -----------------------------
        # Embed
        # -----------------------------
        embed = discord.Embed(
            title=f"🏡 {creature.name}'s {shelter_name}",
            description=(
                f"⭐ **Comfort:** {comfort}\n"
                f"🏠 **Shelter Level:** {level}\n\n"
            ),
            color=0x6BBF59
        )

        # -----------------------------
        # Shelter Description
        # -----------------------------
        embed.add_field(
            name="📖 Description",
            value=generate_shelter_description(creature),
            inline=False
        )

        # -----------------------------
        # Shelter Items
        # -----------------------------
        items = creature.shelter.get("items", [])

        if items:

            favorite_items = []
            regular_items = []

            for entry in items:
                resource = RESOURCES.get(entry["item"], {})

                emoji = resource.get("emoji", "📦")
                name = resource.get(
                    "name",
                    entry["item"].replace("_", " ").title()
                )

                line = f"{emoji} **{name}**"

                if entry.get("state") == "favorite":
                    favorite_items.append(f"🌟 {line}")
                else:
                    regular_items.append(f"🏡 {line}")

            if favorite_items:
                embed.add_field(
                    name="🌟 Favorite Decorations",
                    value="\n".join(favorite_items),
                    inline=False
                )

            if regular_items:
                embed.add_field(
                    name="🪴 Shelter Decorations",
                    value="\n".join(regular_items),
                    inline=False
                )

        else:
            embed.add_field(
                name="🪴 Shelter Decorations",
                value="*This shelter hasn't been decorated yet.*",
                inline=False
            )

        tag_counts = {}

        for entry in items:
            resource = RESOURCES.get(entry["item"])
            if not resource:
                continue

            for tag in resource.get("tags", []):
                tag_counts[tag] = tag_counts.get(tag, 0) + 1

        if tag_counts.get("flowers", 0) >= 2:
            description += " Fragrant flowers bloom throughout the shelter."

        if tag_counts.get("glowing", 0):
            description += " A gentle glow lights every corner."

        if tag_counts.get("cozy", 0):
            description += " Thick blankets and soft bedding make it difficult to leave."

        # -----------------------------
        # Progress
        # -----------------------------
        embed.add_field(
            name="📈 Next Upgrade",
            value=progress,
            inline=False
        )

        await ctx.send(embed=embed)
