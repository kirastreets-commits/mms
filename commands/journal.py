import discord

from systems.save_system import get_or_create_player
from data.journal import JOURNAL_ICONS


def setup(bot):

    @bot.command()
    async def journal(ctx):

        player = get_or_create_player(ctx.author)

        embed = discord.Embed(
            title="📖 Head Caretaker's Journal",
            description=(
                "A record of your sanctuary, your discoveries, "
                "and the creatures who now call Moonlit Meadows home."
            ),
            color=0x6BBF59
        )

        # -----------------------------------
        # 🌿 SANCTUARY OVERVIEW
        # -----------------------------------

        embed.add_field(
            name="🌿 Sanctuary Overview",
            value=(
                f"🐾 Creatures: **{len(player.creatures)}**\n"
                f"📚 Species Known: **{len(player.discovered_species)}**"
            ),
            inline=False
        )

        # -----------------------------------
        # 📚 KNOWN SPECIES
        # -----------------------------------

        if player.discovered_species:

            species_text = "\n".join(
                f"• {species}"
                for species in sorted(player.discovered_species)
            )

        else:

            species_text = (
                "You haven't discovered any species yet.\n"
                "Go exploring!"
            )

        embed.add_field(
            name="📚 Known Species",
            value=species_text,
            inline=False
        )

        # -----------------------------------
        # 📖 RECENT JOURNAL ENTRIES
        # -----------------------------------

        if player.journal_entries:

            entries = player.journal_entries[-10:]

            lines = []

            for entry in reversed(entries):

                # ----------------------------
                # Old save compatibility
                # ----------------------------

                if isinstance(entry, str):
                    lines.append(f"📖 {entry}")
                    continue

                icon = JOURNAL_ICONS.get(
                    entry.get("category", "general"),
                    "📖"
                )

                text = entry.get("text", "")

                day = entry.get("day")

                if day is not None:
                    lines.append(
                        f"{icon} **Day {day}** • {text}"
                    )
                else:
                    lines.append(
                        f"{icon} {text}"
                    )

            entry_text = "\n\n".join(lines)

        else:

            entry_text = (
                "Your journal is empty.\n\n"
                "Every creature you meet will become part of your story."
            )

        embed.add_field(
            name="📖 Recent Journal Entries",
            value=entry_text,
            inline=False
        )

        embed.set_footer(
            text="Every discovery, friendship and milestone will be recorded here."
        )

        await ctx.send(embed=embed)
