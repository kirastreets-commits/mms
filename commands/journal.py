from ui.journal.journal_view import JournalHomeView


@bot.command()
async def journal(ctx):

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
