from ui.npc.headcaretaker import HeadCaretaker


def setup(bot):

    @bot.command()
    async def headcaretaker(ctx):

        npc = HeadCaretaker()
        view = npc.get_view(ctx.author.id)

        await npc.open(ctx, view)
