import discord
from systems.save_system import get_or_create_player


# ----------------------------
# UI HELPER
# ----------------------------

def bar(value, max_value=100, length=10):
    filled = int((value / max_value) * length)
    return "█" * filled + "░" * (length - filled)


# ----------------------------
# INSPECT COMMAND
# ----------------------------

def setup(bot):

    @bot.command()
    async def inspect(ctx, *, creature_name: str):

        player = get_or_create_player(ctx.author)

        creature = player.get_creature(creature_name)

        if not creature:
            await ctx.send(f"You don't have a creature named '{creature_name}'.")
            return


        # ----------------------------
        # MOOD COLOR SYSTEM
        # ----------------------------

        if creature.mood == "happy":
            color = discord.Color.green()
        elif creature.mood == "scared":
            color = discord.Color.red()
        elif creature.mood == "tired":
            color = discord.Color.dark_grey()
        elif creature.mood == "excited":
            color = discord.Color.orange()
        else:
            color = discord.Color.blurple()


        # ----------------------------
        # BUILD EMBED
        # ----------------------------

        embed = discord.Embed(
            title=f" {creature.name}",
            description=f"Species: **{creature.species}**",
            color=color
        )


        # ----------------------------
        # VITAL STATS
        # ----------------------------

        embed.add_field(
            name="❤️ Health",
            value=f"{bar(creature.health)} {creature.health}/100",
            inline=False
        )

        embed.add_field(
            name="⚡ Energy",
            value=f"{bar(creature.energy)} {creature.energy}/100",
            inline=False
        )

        embed.add_field(
            name="🍖 Hunger",
            value=f"{bar(creature.hunger)} {creature.hunger}/100",
            inline=False
        )

        embed.add_field(
            name="😊 Happiness",
            value=f"{bar(creature.happiness)} {creature.happiness}/100",
            inline=False
        )

        # ----------------------------
        # RELATIONSHIP
        # ----------------------------

        embed.add_field(
            name="💞 Bond",
            value=creature.bond_level(),
            inline=True
        )

        embed.add_field(
            name="🤝 Trust",
            value=f"{creature.trust}/100",
            inline=True
        )

        # ----------------------------
        # PERSONALITY & MOOD
        # ----------------------------

        embed.add_field(
            name="🌦 Mood",
            value=creature.mood,
            inline=True
        )

        embed.add_field(
            name="🎭 Personality",
            value=creature.personality,
            inline=True
        )

        # ----------------------------
        # SHELTER INFO
        # ----------------------------

        # Get shelter data if it exists
        shelter = getattr(creature, "shelter", {})

        # Shelter type
        shelter_name = shelter.get("type", "Basic Shelter").replace("_", " ").title()

        # Shelter level
        shelter_level = shelter.get("level", 1)

        # Number of decorations/items
        item_count = len(shelter.get("items", []))

        # Try to get preserve/site if they exist.
        # Otherwise show defaults.
        preserve_name = shelter.get("preserve", "Main Sanctuary")
        shelter_site = shelter.get("site", "Central Grounds")

        embed.add_field(
            name=f"🏡 {creature.name}'s Shelter",
            value=(
                f"📍 **Preserve:** {preserve_name}\n"
                f"🌿 **Location:** {shelter_site}\n"
                f"🏠 **Type:** {shelter_name} (Lv.{shelter_level})\n"
                f"🪵 **Decorations:** {item_count}"
            ),
            inline=False
        )


        # ----------------------------
        # FOOTER
        # ----------------------------

        embed.set_footer(
            text="Use !feed, !play, !heal, !rest to care for your creature."
        )

        await ctx.send(embed=embed)

