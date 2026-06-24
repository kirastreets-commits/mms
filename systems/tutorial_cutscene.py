import discord
from systems.save_system import get_or_create_player, save_player


class IntroView(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=120)


    @discord.ui.button(label="Yes, I will", style=discord.ButtonStyle.green)
    async def accept(self, interaction, button):

        await interaction.response.defer()

        player = get_or_create_player(interaction.user)

        player.tutorial_stage = 1
        save_player(player)

        await self.show_scene_2(interaction)


    @discord.ui.button(label="Tell me more", style=discord.ButtonStyle.gray)
    async def info(self, interaction, button):

        await interaction.response.send_message(
            "The Sanctuary once protected magical creatures.\n"
            "But it was abandoned and left to decay.\n"
            "No one knows what happened to the previous keepers...\n\n",
            ephemeral=True
        )


    async def show_scene_2(self, interaction):

        await interaction.edit_original_response(
            content=
            "🌿 The gates open slowly...\n\n"
            "\"Caretaker... welcome to your new home.\"",
            view=None
        )

        from commands.starter import StarterView

        await interaction.followup.send(
            "The head caretaker offers you a choice of three creatures to care for and nurture.\n",
            view=StarterView()
        )

async def start_intro(ctx, player):

    if player.tutorial_complete:
        return

    view = IntroView()

    await ctx.send(
        "🌿 **Welcome to Moonlit Meadow's Sanctuary**🌿\n"
        "It was once a thriving refuge for magical creatures, but it was abandoned and left to decay.\n"
        "You have been given the opportunity to be one of the new caretakers...\n"
        "Will you accept this responsibility?\n\n",
        view=view
    )
