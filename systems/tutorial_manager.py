from systems.tutorial_cutscene import start_intro
from commands.starter import show_starter_selection

async def continue_tutorial(ctx, player):
    
    print(f"Tutorial stage = {player.tutorial_stage}")
    
    stage = player.tutorial_stage

    if stage == 0:
        await start_intro(ctx, player)

    elif stage == 1:
        await show_starter_selection(ctx)

    elif stage == 2:
        await first_care_task(ctx, player)

    elif stage >= 3:
        await ctx.send(
            "🌿 Your caretaker training is complete. Explore the sanctuary and care for your creatures."
        )
