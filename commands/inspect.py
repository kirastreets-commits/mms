import discord

from systems.save_system import get_or_create_player
from systems.preserve_system import get_preserve
from data.personality import PERSONALITIES
from data.species import SPECIES_REGISTRY


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
        # PERSONALITY INFO
        # ----------------------------

        personality_data = PERSONALITIES.get(creature.personality, {})
        personality_description = personality_data.get(
            "description",
            "This creature has a unique personality."
        )

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

        species = SPECIES_REGISTRY.get(creature.species, {})
        emoji = species.get("emoji", "🐾")

        embed = discord.Embed(
            title=f"{emoji} {creature.name}",
            description=f"Species: **{creature.species}**",
            color=color
        )

        # ----------------------------
        # SHELTER INFO
        # ----------------------------

        shelter = creature.shelter

        location_id = shelter.get("location")

        if location_id:
            preserve = get_preserve(location_id)
            preserve_name = preserve["name"] if preserve else location_id
        else:
            preserve_name = "Not Settled"

        site_name = shelter.get("site", "None")
        shelter_name = shelter.get("type", "Basic Shelter").replace("_", " ").title()
        shelter_level = shelter.get("level", 1)

        embed.add_field(
            name=f"🏡 {creature.name}'s Shelter",
            value=(
                f"**Preserve:** {preserve_name}\n"
                f"**Site:** {site_name}\n"
                f"**Shelter:** {shelter_name} (Lv.{shelter_level})"
            ),
            inline=False
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
        # MOOD
        # ----------------------------

        embed.add_field(
            name="🌦 Mood",
            value=creature.mood.title(),
            inline=True
        )

        # ----------------------------
        # PERSONALITY
        # ----------------------------

        embed.add_field(
            name="🎭 Personality",
            value=(
                f"**{creature.personality.title()}**\n"
                f"*{personality_description}*"
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
