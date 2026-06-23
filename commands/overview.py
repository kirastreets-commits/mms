import discord
from systems.save_system import get_or_create_player


def bar(value, max_value=100, length=8):
    filled = int((value / max_value) * length)
    return "█" * filled + "░" * (length - filled)


def setup(bot):

    @bot.command()
    async def overview(ctx):

        player = get_or_create_player(ctx.author)

        if not player.creatures:
            await ctx.send("🏡 Your sanctuary is empty. Use !starter or !adopt to begin your journey.")
            return

        embed = discord.Embed(
            title="🏡 Sanctuary Overview",
            description="A quick look at all your creatures",
            color=discord.Color.blurple()
        )

        # ----------------------------
        # CREATURE LIST
        # ----------------------------

        for creature in player.creatures:

            warnings = []

            if creature.hunger <= 20:
                warnings.append("🍖 Starving")

            if creature.health <= 20:
                warnings.append("❤️ Critical")

            if creature.energy <= 20:
                warnings.append("⚡ Exhausted")

            if creature.happiness <= 20:
                warnings.append("😊 Unhappy")

            warning_text = " | ".join(warnings) if warnings else "OK"

            embed.add_field(
                name=f"{creature.name} ({creature.species})",
                value=(
                    f"💞 {creature.bond_level()} | 🌦 {creature.mood}\n"
                    f"❤️ {bar(creature.health)} {creature.health}/100\n"
                    f"⚡ {bar(creature.energy)} {creature.energy}/100\n"
                    f"🍖 {bar(creature.hunger)} {creature.hunger}/100\n"
                    f"😊 {bar(creature.happiness)} {creature.happiness}/100\n"
                    f"⚠️ {warning_text}"
                ),
                inline=False
            )

        embed.set_footer(
            text="Use !inspect <name> to interact with a creature."
        )

        await ctx.send(embed=embed)