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

class RenameModal(discord.ui.Modal, title="Rename Creature"):

    new_name = discord.ui.TextInput(
        label="New Name",
        max_length=20
    )

    def __init__(self, creature_name):
        super().__init__()
        self.creature_name = creature_name

    async def on_submit(self, interaction: discord.Interaction):

        player = get_or_create_player(interaction.user)
        creature = player.get_creature(self.creature_name)

        creature.name = self.new_name.value

        save_player(player)

        await interaction.response.send_message(
            f"🌿 The creature is now known as **{self.new_name.value}**.",
            ephemeral=True
        )
# -------------------------
# VIEW (buttons live here)
# -------------------------
class HeadCaretakerView(BaseNPCView):

    @discord.ui.button(label="Rename Creature", style=discord.ButtonStyle.primary, emoji="🏷️")
    async def rename(self, interaction: discord.Interaction, button: discord.ui.Button):
    
        player = get_or_create_player(interaction.user)
    
        async def after_select(inter, creature_name):
    
            creature = player.get_creature(creature_name)
    
            if not creature:
                return await inter.response.send_message("Creature not found.", ephemeral=True)
    
            await inter.response.send_modal(
                RenameModal(creature_name)
            )
    
        view = CreatureSelectView(
            creatures=player.creatures,
            on_select_callback=after_select,
            user_id=interaction.user.id
        )
    
        await interaction.response.send_message(
            "Select a creature to rename:",
            view=view,
            ephemeral=True
        )

    @discord.ui.button(label="Release Creature", style=discord.ButtonStyle.danger, emoji="🕊️")
    async def release(self, interaction, button):
    
        player = get_or_create_player(interaction.user)
    
        async def after_select(inter, creature_name):
    
            creature = player.get_creature(creature_name)
    
            player.creatures.remove(creature)
            save_player(player)
    
            await inter.response.send_message(
                f"🕊️ {creature_name} has been released into the wild.",
                ephemeral=True
            )
    
        view = CreatureSelectView(
            creatures=player.creatures,
            on_select_callback=after_select,
            user_id=interaction.user.id
        )
    
        await interaction.response.send_message(
            "Select a creature to release:",
            view=view,
            ephemeral=True
        )
