from systems.save_system import save_player

async def show_intro(ctx, player):

    if player.tutorial_seen:
        return

    intro = (
        "🌿 **Welcome to the Moonlit Meadows Sanctuary!** 🌿\n\n"
        "You are the one of the caretakers in a growing sanctuary for magical creatures.\n\n"
        "🐉 Adopt creatures with `!adopt <name>`\n"
        "📋 View your sanctuary with `!status`\n"
        "🍖 Feed creatures with `!feed <name>`\n"
        "🎮 More systems will unlock as you grow.\n\n"
        "Take good care of your creatures..."
    )

    await ctx.send(intro)

    player.tutorial_seen = True

    save_player(player)