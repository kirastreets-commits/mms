import discord


class HeadCaretakerView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=180)

    # -------------------------
    # 🏷️ RENAME BUTTON
    # -------------------------
    @discord.ui.button(
        label="Rename Creature",
        style=discord.ButtonStyle.primary,
        emoji="🏷️"
    )
    async def rename_button(self, interaction: discord.Interaction, button: discord.ui.Button):

        await interaction.response.send_message(
            "Which creature would you like to rename?",
            view=RenameSelectView(interaction.user.id),
            ephemeral=True
        )

    # -------------------------
    # 🕊️ RELEASE BUTTON
    # -------------------------
    @discord.ui.button(
        label="Release Creature",
        style=discord.ButtonStyle.danger,
        emoji="🕊️"
    )
    async def release_button(self, interaction: discord.Interaction, button: discord.ui.Button):

        await interaction.response.send_message(
            "Which creature would you like to release?",
            view=ReleaseSelectView(interaction.user.id),
            ephemeral=True
        )
