def setup(bot):

    @bot.command()
    async def reset_tutorial(ctx):

        player = get_or_create_player(ctx.author)

        player.tutorial_stage = 0
        player.tutorial_complete = False

        save_player(player)

        await ctx.send("Tutorial reset.")
