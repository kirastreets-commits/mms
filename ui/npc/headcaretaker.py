import discord
from ui.npc.base_npc import BaseNPC
from ui.npc.base_view import BaseNPCView
from ui.components.creature_select import CreatureSelectView
from systems.save_system import get_or_create_player, save_player


class HeadCaretaker(BaseNPC):
    def __init__(self):
        super().__init__(
            name="headcaretaker",
            title="🌿 Head Caretaker",
            description=(
                "The Head Caretaker looks up and smiles warmly.\n\n"
                "\"Welcome back, caretaker. How may I help you today?\""
            ),
            color=discord.Color.green()
        )

    # -------------------------
    # VIEW BUILDER
    # -------------------------
    def get_view(self, user_id):
        return HeadCaretakerView(self, user_id)


# -------------------------
# VIEW (buttons live here)
# -------------------------
class HeadCaretakerView(BaseNPCView):

    @discord.ui.button(label="Rename Creature", style=discord.ButtonStyle.primary, emoji="🏷️")
    async def rename(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "Select a creature to rename...",
            ephemeral=True
        )

    @discord.ui.button(label="Release Creature", style=discord.ButtonStyle.danger, emoji="🕊️")
    async def release(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "Select a creature to release...",
            ephemeral=True
        )
