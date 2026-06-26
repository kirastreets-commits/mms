import discord
from systems.save_system import get_or_create_player


def bar(value, max_value=100, length=8):
    filled = int((value / max_value) * length)
    return "█" * filled + "░" * (length - filled)


def get_status(creature):

    if creature.health <= 20:
        return "🆘 Critical"
    if creature.hunger <= 20:
        return "🍖 Starving"
    if creature.energy <= 20:
        return "⚡ Exhausted"
    if creature.happiness <= 20:
        return "💔 Distressed"

    if creature.happiness >= 80:
        return "🌿 Thriving"
    if creature.energy >= 80:
        return "✨ Energetic"

    return "🌱 Stable"


def setup(bot):

    @bot.command()
    async def overview(ctx):

        player = get_or_create_player(ctx.author)

        if not player.creatures:
            await ctx.send(
                "🏡 Your sanctuary is quiet…\n"
                "No creatures are currently in your care.\n\n"
                "Try `!starter` or `!adopt` to begin your journey."
            )
            return

        embed = discord.Embed(
            title="🏡 Sanctuary Overview",
            description=(
                "The Head Caretaker observes your sanctuary from afar...\n"
                "\"All creatures are accounted for.\""
            ),
            color=discord.Color.blurple()
        )

        for creature in player.creatures:

            status = get_status(creature)

            embed.add_field(
                name=f"{creature.name} • {creature.species}",
                value=(
                    f"{status} • 💞 Bond {creature.bond_level()}\n\n"

                    f"❤️ Health   {bar(creature.health)} {creature.health}/100\n"
                    f"⚡ Energy   {bar(creature.energy)} {creature.energy}/100\n"
                    f"🍖 Hunger   {bar(creature.hunger)} {creature.hunger}/100\n"
                    f"😊 Mood     {creature.mood}\n"
                    f"🌿 Status   {status}"
                ),
                inline=False
            )

        embed.set_footer(
            text="Tip: Use the Head Caretaker to rename, release, or manage creatures."
        )

        await ctx.send(embed=embed)
