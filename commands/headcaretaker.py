import discord


def setup(bot):

    @bot.command()
    async def headcaretaker(ctx):
    
        embed = discord.Embed(
            title="🌿 Head Caretaker",
            description=(
                "The Head Caretaker looks up and offers a gentle smile.\n\n"
                "\"Welcome back, caretaker. How may I help you today?\""
            ),
            color=discord.Color.green()
        )
    
        await ctx.send(embed=embed, view=HeadCaretakerView())
