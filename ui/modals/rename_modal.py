class RenameModal(discord.ui.Modal, title="Rename Creature"):
    new_name = discord.ui.TextInput(
        label="New Name",
        placeholder="Enter a new name...",
        max_length=20
    )

    def __init__(self, creature_name):
        super().__init__()
        self.creature_name = creature_name

    async def on_submit(self, interaction: discord.Interaction):

        player = get_or_create_player(interaction.user)
        creature = player.get_creature(self.creature_name)

        if not creature:
            return await interaction.response.send_message(
                "That creature could not be found.",
                ephemeral=True
            )

        old_name = creature.name
        creature.nickname = self.new_name.value

        save_player(player)

        await interaction.response.send_message(
            f"🌿 The Head Caretaker smiles softly...\n\n"
            f"\"{self.new_name.value}... yes, that suits them.\"\n\n"
            f"✨ **{old_name} is now known as {self.new_name.value}.**",
            ephemeral=True
        )
