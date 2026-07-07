import discord

from systems.save_system import get_or_create_player
from data.species import SPECIES_REGISTRY


def bar(value, max_value=100, length=6):
    value = max(0, min(value, max_value))
    filled = int((value / max_value) * length)
    return "█" * filled + "░" * (length - filled)


def get_status(creature):

    if creature.health <= 20:
        return "❤️ Needs Healing"

    if creature.hunger <= 20:
        return "🍖 Hungry"

    if creature.energy <= 20:
        return "💤 Needs Rest"

    if creature.happiness <= 20:
        return "💔 Unhappy"

    if creature.happiness >= 90:
        return "🌿 Thriving"

    return "🌱 Doing Well"


def setup(bot):

    @bot.command()
    async def overview(ctx):

        player = get_or_create_player(ctx.author)

        if not player.creatures:
            await ctx.send(
                "🏡 Your sanctuary is quiet...\n"
                "No creatures are currently in your care.\n\n"
                "Try `!starter` or `!adopt` to begin your journey."
            )
            return

        embed = discord.Embed(
            title="🏡 Sanctuary Overview",
            description=(
                f"🐾 **Creatures:** {len(player.creatures)}\n"
                "A quick look at everyone currently living in your sanctuary."
            ),
            color=discord.Color.blurple()
        )

        for creature in player.creatures:

            species = SPECIES_REGISTRY.get(creature.species, {})
            emoji = species.get("emoji", "🐾")

            embed.add_field(
                name=f"{emoji} {creature.name}",
                value=(
                    f"**{creature.species}** • {creature.bond_level()}\n"
                    f"{get_status(creature)}\n\n"
                    f"❤️ {bar(creature.health)}\n"
                    f"🍖 {bar(creature.hunger)}"
                ),
                inline=True
            )

        embed.set_footer(
            text="Use !inspect <name> to view a creature's full profile."
        )

        await ctx.send(embed=embed)
