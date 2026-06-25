import discord


def setup(bot):

    @bot.command(name="headcaretaker")
    async def headcaretaker(ctx):

        embed = discord.Embed(
            title="🌿 Head Caretaker",
            description=(
                "The Head Caretaker looks up from their work and smiles warmly.\n\n"
                "\"Welcome back, caretaker. Every creature here deserves kindness and patience. "
                "How may I help you today?\""
            ),
            color=discord.Color.green()
        )

        embed.add_field(
            name="Available Services",
            value=(
                "🏷️ **Rename Creature** *(Coming Soon)*\n"
                "🕊️ **Release Creature** *(Coming Soon)*"
            ),
            inline=False
        )

        embed.set_footer(
            text="More services will become available as Moonlit Meadows Sanctuary grows."
        )

        await ctx.send(embed=embed)
