import discord

from systems.save_system import save_player


class AdoptNameModal(discord.ui.Modal, title="Name Your New Companion"):

    creature_name = discord.ui.TextInput(
        label="Choose a name",
        placeholder="What will you call them?",
        max_length=20
    )

    def __init__(self, player, creature):
        super().__init__()

        self.player = player
        self.creature = creature

    async def on_submit(self, interaction: discord.Interaction):

        new_name = self.creature_name.value.strip()
    
        if not new_name:
            return await interaction.response.send_message(
                "Please choose a name.",
                ephemeral=True
            )
    
        # Give the creature its name
        self.creature.name = new_name
    
        self.player.add_creature(self.creature, named=True)
        save_player(self.player)
        from ui.explore_views import get_home_message
    
        embed = discord.Embed(
            title="✨ A New Beginning",
            description=(
                f"The little **{self.creature.species}** looks up at you.\n\n"
                f'You softly whisper, **"{new_name}."**\n\n'
                f"They tilt their head before happily accepting the name.\n\n"
                f"💚 **{new_name} has joined your sanctuary!**\n\n"
                f"{get_home_message(self.creature)}"
            ),
            colour=discord.Color.green()
        )
    
        await interaction.response.send_message(
            embed=embed,
            ephemeral=True
        )
