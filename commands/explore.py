from models.creature import Creature
from systems.save_system import get_or_create_player, save_player
from data.species import SPECIES_REGISTRY
from data.resources import RESOURCES
import random
import discord



# ----------------------------
# 🌍 EXPLORE + NAME SYSTEM
# ----------------------------
# =========================================================
# 🌱 NAME MODAL
# =========================================================
class NameCreatureModal(discord.ui.Modal):

    def __init__(self, player, species_name, species_data):
        super().__init__(title="Name your new companion")

        self.player = player
        self.species_name = species_name
        self.species_data = species_data

        self.name_input = discord.ui.TextInput(
            label="Creature Name",
            placeholder="e.g. Ember, Moss, Luna...",
            max_length=20
        )

        self.add_item(self.name_input)

    async def on_submit(self, interaction: discord.Interaction):

        creature = Creature(
            name=self.name_input.value,
            species=self.species_name,
        )

        self.player.creatures.append(creature)
        self.player.journal_entries.append(f"{creature.name} joined the sanctuary.")
        print(self.player.journal_entries)
        save_player(self.player)
        

        await interaction.response.send_message(
            f"💚 **{creature.name}** the {self.species_name} has joined your sanctuary!",
            ephemeral=False
        )


# =========================================================
# 🌿 ENCOUNTER VIEW (ADOPT / LEAVE)
# =========================================================
class EncounterView(discord.ui.View):

    def __init__(self, player, species_name, species_data):
        super().__init__(timeout=60)

        self.player = player
        self.species_name = species_name
        self.species_data = species_data

    @discord.ui.button(label="🟢 Adopt", style=discord.ButtonStyle.green)
    async def adopt(self, interaction: discord.Interaction, button: discord.ui.Button):

        if interaction.user.id != int(self.player.user_id):
            return await interaction.response.send_message(
                "This isn't your encounter.",
                ephemeral=True
            )

        await interaction.response.send_modal(
            NameCreatureModal(self.player, self.species_name, self.species_data)
        )

    @discord.ui.button(label="🔴 Leave", style=discord.ButtonStyle.red)
    async def leave(self, interaction: discord.Interaction, button: discord.ui.Button):

        if interaction.user.id != int(self.player.user_id):
            return await interaction.response.edit_message(
                content="🌿 You quietly leave the creature behind...",
                view=None
            )


# =========================================================
# 🌍 EXPLORE COMMAND
# =========================================================
def setup(bot):

    @bot.command()
    async def explore(ctx):

        player = get_or_create_player(ctx.author)

        def add_to_inventory(player, item_id, amount=1):

            if item_id not in player.inventory:
                player.inventory[item_id] = 0
        
            player.inventory[item_id] += amount

        # --------------------------------
        # NO CREATURE FOUND
        # --------------------------------
        if random.randint(1, 100) < 50:

            resource_id = random.choice(list(RESOURCES.keys()))
            resource = RESOURCES[resource_id]
        
            amount = random.randint(1, 3)
        
            add_to_inventory(player, resource_id, amount)
        
            embed = discord.Embed(
                title="🌿 Exploration Complete",
                description=(
                    f"You didn't find any creatures today.\n\n"
                    f"You gathered {resource['emoji']} "
                    f"**{resource['name']} x{amount}**."
                ),
                color=0x6bbf59
            )
    
            await ctx.send(embed=embed)
            return

        # --------------------------------
        # CREATURE FOUND
        # --------------------------------
        species_name = random.choice(list(SPECIES_REGISTRY.keys()))
        species_data = SPECIES_REGISTRY[species_name]

        is_new = species_name not in player.discovered_species

        if is_new:
            player.discovered_species.append(species_name)
            player.journal_entries.append(f"Discovered a new species: {species_name}")
            save_player(player)


        embed = discord.Embed(
            title="✨ Creature Encountered!",
            description=f"You found a **{species_name}**!",
            color=0x6bbf59
        )

        if is_new:
            embed.add_field(
                name="📖 New Discovery",
                value=species_data["description"],
                inline=False
            )

        embed.add_field(
            name="🤍 What will you do?",
            value="You can choose to adopt this creature or leave it in the wild.",
            inline=False
        )

        view = EncounterView(player, species_name, species_data)

        

        await ctx.send(embed=embed, view=view)
