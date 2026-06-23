from systems.save_system import get_or_create_player
from systems.tutorial_cutscene import start_intro


def setup(bot):

    @bot.command()
    async def start(ctx):

        player = get_or_create_player(ctx.author)

        await start_intro(ctx, player)