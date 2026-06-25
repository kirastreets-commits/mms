from systems.tutorial_cutscene import start_intro
from commands.starter import show_starter_selection

async def continue_tutorial(ctx, player):

    stage = player.tutorial_stage

    if stage == 0:
        await start_intro(ctx, player)

    elif stage == 1:
        await show_starter_selection(ctx)

    else:
        await ctx.send("Tutorial stage not implemented yet.")
