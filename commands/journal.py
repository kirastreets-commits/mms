from ui.journal.journal_view import JournalHomeView

def setup(bot):

    @bot.command()
    async def journal(ctx):

        player = get_or_create_player(ctx.author)

        embed = discord.Embed(
            title="📖 Caretaker's Journal",
            description=(
                "The memories of Moonlit Meadows "
                "are recorded here.\n\n"
                "Choose a section to browse."
            ),
            color=0x6b8e23
        )

        await ctx.send(
            embed=embed,
            view=JournalHomeView(player)
        )
