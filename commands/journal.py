from systems.save_system import get_or_create_player, save_player
import discord

def setup(bot):

    @bot.command()
    async def journal(ctx):

        player = get_or_create_player(ctx.author)

        embed = discord.Embed(
            title="📖 Caretaker Journal",
            description="A record of your journey as a creature caretaker.",
            color=0x6bbf59
        )

        # ----------------------------
        # SANCTUARY OVERVIEW
        # ----------------------------

        embed.add_field(
            name="🌿 Sanctuary Overview",
            value=(
                f"Creatures: **{len(player.creatures)}**\n"
                f"Species Discovered: **{len(player.discovered_species)}**"
            ),
            inline=False
        )

        # ----------------------------
        # DISCOVERED SPECIES
        # ----------------------------

        if player.discovered_species:

            species_text = "\n".join(
                f"✔ {species}"
                for species in sorted(player.discovered_species)
            )

        else:

            species_text = "No species discovered yet."

        embed.add_field(
            name="📚 Known Species",
            value=species_text,
            inline=False
        )

        # ----------------------------
        # RECENT JOURNAL ENTRIES
        # ----------------------------

        if player.journal_entries:

            entries = player.journal_entries[-10:]

            entry_text = "\n".join(
                f"• {entry}"
                for entry in reversed(entries)
            )

        else:

            entry_text = "No journal entries yet."

        embed.add_field(
            name="📝 Recent Notes",
            value=entry_text,
            inline=False

        )
        embed.set_footer(
            text="Use !species <species name> to see your known information about the species."
        )

        print("Loaded journal:", player.journal_entries)
        
        await ctx.send(embed=embed)