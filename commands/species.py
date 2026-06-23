from systems.save_system import get_or_create_player, save_player
from data.species import SPECIES_REGISTRY, get_species_description, get_species_shelter, get_species_data
import discord

def setup(bot):

    @bot.command()
    async def species(ctx, *, species_name: str):

        player = get_or_create_player(ctx.author)


        species_lookup = None

        for species in player.discovered_species:

            if species.lower() == species_name.lower():

                species_lookup = species
                break

        if species_lookup is None:

            if species_lookup is None:

                discovered = ", ".join(player.discovered_species)

                await ctx.send(
                    f"You haven't discovered '{species_name}'.\n\n"
                    f"Known species:\n{discovered}"
                )

                return

        species_data = get_species_data(species_lookup)

        embed = discord.Embed(
            title=f"📖 {species_lookup}",
            description= species_data["description"],
            color=0x6bbf59
            )

        embed.add_field(
            name="🏡 Preferred Shelter",
            value=species_data["shelter"],
            inline=False
            )

        embed.add_field(
            name="⭐ Rarity",
            value=species_data.get("rarity", "Common"),
            inline=True
        )

        embed.add_field(
            name="🌿 Habitat",
            value=species_data.get("habitat", "Unknown"),
            inline=True
        )
        
        owned = any(
            creature.species == species_lookup
            for creature in player.creatures
        )

        embed.set_footer(
            text="Currently in Sanctuary" if owned
            else "Previously Discovered"
        )

        await ctx.send(embed=embed)