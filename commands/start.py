from systems.save_system import get_or_create_player
from systems.tutorial_manager import continue_tutorial 


def setup(bot):
    print("✅ start.py loaded")

    @bot.command()
    async def start(ctx):

        player = get_or_create_player(ctx.author)

        await continue_tutorial(ctx, player)
