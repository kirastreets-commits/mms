import discord
import random

from systems.save_system import save_player
from data.locations import LOCATIONS
from data.resources import RESOURCES
from data.species import get_species
from models.creature import Creature
from ui.modals.adopt_name_modal import AdoptNameModal

class ExploreMenuView(discord.ui.View):
    def __init__(self, player):
        super().__init__(timeout=60)
        self.player = player

    @discord.ui.button(label="🏠 Inside Sanctuary", style=discord.ButtonStyle.primary)
    async def inside(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.open_location_menu(interaction, "inside")

    @discord.ui.button(label="🌳 Sanctuary Grounds", style=discord.ButtonStyle.success)
    async def grounds(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.open_location_menu(interaction, "grounds")

    @discord.ui.button(label="🌌 Outside Sanctuary", style=discord.ButtonStyle.danger)
    async def outside(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.open_location_menu(interaction, "outside")


    async def open_location_menu(self, interaction, location_type):
        view = LocationSelectView(self.player, location_type)

        embed = discord.Embed(
            title=f"🧭 {location_type.title()} Exploration",
            description="Choose a specific location:",
            color=0x3498db
        )

        await interaction.response.edit_message(embed=embed, view=view)

class LocationSelectView(discord.ui.View):
    def __init__(self, player, location_type):
        super().__init__(timeout=60)
        self.player = player
        self.location_type = location_type

        options = []

        for loc_id, data in LOCATIONS.items():
            if data["type"] == location_type and loc_id in player.unlocked_locations:
                options.append(
                    discord.SelectOption(
                        label=data["name"],
                        value=loc_id
                    )
                )

        if options:
            self.add_item(LocationSelectMenu(player, options))
        else:
            self.add_item(
                discord.ui.Select(
                    placeholder="No locations unlocked",
                    options=[
                        discord.SelectOption(
                            label="No locations available",
                            value="none"
                        )
                    ],
                    disabled=True
                )
            )

class LocationSelectMenu(discord.ui.Select):
    def __init__(self, player, options):
        self.player = player

        super().__init__(
            placeholder="Choose a location...",
            options=options
        )

    async def callback(self, interaction: discord.Interaction):

        if not self.values:
            await interaction.response.send_message(
                "No selection detected.",
                ephemeral=True
            )
            return
    
        location_id = self.values[0]
        location = LOCATIONS[location_id]
    
        message, view = self.explore_location(
            self.player,
            location_id,
            location
        )
    
        save_player(self.player)
    
        embed = discord.Embed(
            title=f"✨ Exploring {location['name']}",
            description=message,
            color=0xf1c40f
        )
    
        await interaction.response.edit_message(
            embed=embed,
            view=view
        )

    from models.creature import Creature


    
    
    def explore_location(self, player, location_id, location):
    
            roll = random.randint(1, 100)
        
            # 🌫 Nothing
            if roll < 20:
                return (
                    "The area is quiet… nothing unusual stirs.",
                    None
                )
        
            # 🌿 Resources
            elif roll < 55:
        
                resources = location.get("resources", [])
        
                if not resources:
                    return (
                        "You search the area but find nothing useful.",
                        None
                    )
        
                resource_id = random.choice(resources)
                resource = RESOURCES[resource_id]
        
                amount = random.randint(1, 3)
                player.add_to_inventory(resource_id, amount)
        
                return (
                    f"You found {resource['emoji']} **{resource['name']}** x{amount}!",
                    None
                )
        
            # 📜 Lore
            elif roll < 75:
        
                lore = f"A forgotten memory stirs in {location['name']}..."
        
                if lore not in player.journal_entries:
                    player.journal_entries.append(lore)
        
                return (
                    f"📜 Lore discovered:\n*{lore}*",
                    None
                )
        
            # 🐾 Creature
            elif roll < 90:
        
                available = location.get("available_creatures", [])
        
                if not available:
                    return (
                        "You thought you saw movement, but nothing appeared.",
                        None
                    )
        
                species_name = random.choice(available)
        
                discovered = False
        
                if species_name not in player.discovered_species:
                    player.discovered_species.append(species_name)
                    discovered = True
        
                # 25% chance the creature needs rescuing
                if random.random() < 0.90:
        
                    message = (
                        f"🐾 You discover an injured **{species_name}** hiding nearby.\n\n"
                        "It looks frightened, but doesn't run away."
                    )
        
                    if discovered:
                        message += "\n\n📖 **New species discovered!**"
        
                    return (
                        message,
                        RescueView(player, species_name)
                    )
        
                message = (
                    f"🐾 You spot a **{species_name}** watching you curiously from the shadows."
                )
        
                if discovered:
                    message += "\n\n📖 **New species discovered!**"
        
                return (
                    message,
                    RescueView(player, species_name)
                )
        
            # 🔓 Unlock new locations
            else:
                return (
                    self.progress_unlock(player, location_id),
                    None
                )
            
    def progress_unlock(self, player, location_id):
        location = LOCATIONS[location_id]

        if "connected" not in location:
            return "You sense no new paths from here."

        for next_loc in location["connected"]:
            if next_loc not in player.unlocked_locations:
                player.unlocked_locations.append(next_loc)
                print(player.unlocked_locations)
                return f"🔓 A new path has opened: **{LOCATIONS[next_loc]['name']}**"

        return "You feel this area is already fully explored."
            
class RescueView(discord.ui.View):

    def __init__(self, player, species_name):
        super().__init__(timeout=60)

        self.player = player
        self.species_name = species_name

    @discord.ui.button(
        label="🤝 Approach",
        style=discord.ButtonStyle.success
    )
    async def approach(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        await interaction.response.edit_message(
            embed=discord.Embed(
                title="🐾 Careful Approach...",
                description=(
                    f"You slowly step toward the **{self.species_name}**.\n\n"
                    "It watches you closely, unsure whether to trust you..."
                ),
                color=0xf1c40f
            ),
            view=TrustView(self.player, self.species_name)
        )

    @discord.ui.button(
        label="👀 Observe",
        style=discord.ButtonStyle.primary
    )
    async def observe(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        embed = discord.Embed(
            title=self.species_name,
            description=(
                "You remain still and quietly observe the creature.\n\n"
                "It seems wary, but not hostile."
            ),
            color=0x3498db
        )

        await interaction.response.edit_message(
            embed=embed,
            view=self
        )

    @discord.ui.button(
        label="🚶 Leave",
        style=discord.ButtonStyle.secondary
    )
    async def leave(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        embed = discord.Embed(
            title="The creature slips away...",
            description="Perhaps your paths will cross again someday.",
            color=0x95a5a6
        )

        await interaction.response.edit_message(
            embed=embed,
            view=None
        )

class TrustView(discord.ui.View):

    def __init__(self, player, species_name):
        super().__init__(timeout=60)

        self.player = player
        self.species_name = species_name

    @discord.ui.button(
        label="✨ Offer Calm Reassurance",
        style=discord.ButtonStyle.success
    )
    async def reassure(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        embed = discord.Embed(
            title="💞 Trust Forms",
            description=(
                f"The **{self.species_name}** slowly relaxes.\n\n"
                "It no longer seems afraid of you...\n"
                "It might be ready to come with you."
            ),
            color=0x57F287
        )

        await interaction.response.edit_message(
            embed=embed,
            view=NameCreatureView(self.player, self.species_name)
        )

    @discord.ui.button(
        label="🚶 Back Away",
        style=discord.ButtonStyle.secondary
    )
    async def leave(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        embed = discord.Embed(
            title="The moment fades...",
            description="You step away and the creature retreats into the wild.",
            color=0x95a5a6
        )

        await interaction.response.edit_message(
            embed=embed,
            view=None
        )

class NameCreatureView(discord.ui.View):

    def __init__(self, player, species_name):
        super().__init__(timeout=60)

        self.player = player
        self.species_name = species_name

    @discord.ui.button(
        label="✏️ Name Creature",
        style=discord.ButtonStyle.primary
    )
    async def name(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        await interaction.response.send_modal(
            AdoptNameModal(self.player, self.species_name)
        )

    @discord.ui.button(
        label="✨ Keep It Wild (No Name)",
        style=discord.ButtonStyle.secondary
    )
    async def keep_wild(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        creature = Creature(
            self.species_name,
            self.species_name
        )

        self.player.creatures.append(creature)
        save_player(self.player)

        embed = discord.Embed(
            title="🌿 Creature Freed",
            description=f"The **{self.species_name}** joins your sanctuary… but remains wild.",
            color=0x95a5a6
        )

        await interaction.response.edit_message(
            embed=embed,
            view=None
        )

    
