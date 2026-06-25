import discord

def setup(bot):
    @bot.command()
    async def help(ctx):

        embed = discord.Embed(
            title="🌿 Moonlit Meadows Help",
            description="Available commands",
            color=0x6bbf59
        )

        embed.add_field(
            name="🐾 Creature Care",
            value=(
                "`!feed <creature>`\n"
                "`!play <creature>`\n"
                "`!rest <creature>`\n"
                "`!heal <creature>`\n"
                "`!gift <creature> <item_name>`"
            ),
            inline=False
        )

        embed.add_field(
            name="👤Player",
            value=(
                "!inventory"
            ),
            inline=False
        )

        embed.add_field(
            name="🌍 Exploration",
            value=(
                "`!explore`\n"
                "`!explore_sanctuary <creature>`"
            ),
            inline=False
        )

        embed.add_field(
            name="📖 Journal",
            value=(
                "`!journal`\n"
                "`!species <species>`"
            ),
            inline=False
        )

        embed.add_field(
            name="🏡 Sanctuary",
            value=(
                "`!overview`\n"
                "`!inspect <creature>`"
            ),
            inline=False
        )

        await ctx.send(embed=embed)
