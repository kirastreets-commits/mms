import discord

from models.creature import Creature
from systems.save_system import get_or_create_player, save_player
from data.species import SPECIES_REGISTRY, get_species


# ----------------------------
# STARTER OPTIONS
# ----------------------------

def get_starters():
    return {
        name: data
        for name, data in SPECIES_REGISTRY.items()
        if data.get("is_starter")
    }

async def show_starter_selection(ctx):

    await ctx.send(
        "🌿 **Choose your first rescued creature:**",
        view=StarterView()
    )
# ----------------------------
# MODAL (NAME INPUT)
# ----------------------------

class StarterNameModal(discord.ui.Modal):

    def __init__(self, species: str):
        super().__init__(title="Name your new companion")

        self.species = species

        self.name_input = discord.ui.TextInput(
            label="Creature Name",
            placeholder="e.g. Sparky, Moss, Ember...",
            max_length=20
        )

        self.add_item(self.name_input)

    
    async def on_submit(self, interaction: discord.Interaction):

        player = get_or_create_player(interaction.user)

        if player.has_starter:
            await interaction.response.send_message(
                "You have already chosen your starter creature.",
                ephemeral=True
            )
            return

        species_data = get_species(self.species)

        creature = Creature(
            name=self.name_input.value,
            species=self.species,
        )

        player.add_creature(creature)

        # 🟢 JOURNAL ENTRY
        entry = {
            "title": "First Companion Adopted",
            "content": f"You adopted {creature.name} the {self.species}. The sanctuary feels a little more alive now.",
            "type": "starter_adoption"
        }
        
        if not hasattr(player, "journal_entries") or player.journal_entries is None:
            player.journal_entries = []
        
        player.journal_entries.append(entry)

        if self.species not in player.discovered_species:
            player.discovered_species.append(self.species)

        player.tutorial_complete = True
        player.tutorial_stage = 3
        player.has_starter = True

        save_player(player)

        await interaction.response.send_message(
            f"🌿 You adopted **{creature.name}** the {self.species}!",
            ephemeral=True
        )



# ----------------------------
# BUTTON VIEW
# ----------------------------

class StarterView(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=120)

        starters = get_starters()

        for species_name in starters.keys():
            self.add_item(StarterButton(species_name))

class StarterButton(discord.ui.Button):

    def __init__(self, species_name: str):

        data = SPECIES_REGISTRY[species_name]

        super().__init__(
            label=species_name.title(),
            emoji=data.get("emoji"),  # ✅ THIS is what you were missing
            style=data.get("button_style", discord.ButtonStyle.green)
        )

        self.species_name = species_name

    async def callback(self, interaction: discord.Interaction):

        modal = StarterNameModal(self.species_name)
        await interaction.response.send_modal(modal)
   
   


# ----------------------------
# COMMAND
# ----------------------------

def setup(bot):

    @bot.command()
    async def starter(ctx):

        player = get_or_create_player(ctx.author)

        # optional: prevent re-using starter system
        
        if player.has_starter:
            await ctx.send("You have already chosen your starter creature.")
            return
            

        await ctx.send(
            "🌿 **Choose your first rescued creature:**",
            view=StarterView()
        )
