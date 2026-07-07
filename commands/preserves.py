import discord

from systems.save_system import get_or_create_player
from data.preserves import PRESERVES
from systems.preserve_system import (
    get_preserve_capacity,
    get_preserve_residents
)


def setup(bot):

    @bot.command()
    async def preserves(ctx):

        player = get_or_create_player(ctx.author)

        embed = discord.Embed(
            title="🌿 Sanctuary Preserves",
            description=(
                "Your restored lands slowly begin to awaken...\n"
                "Each preserve provides a home for your rescued creatures."
            ),
            color=discord.Color.green()
        )

        for preserve_id, preserve_data in PRESERVES.items():

            # Player preserve data
            player_data = player.preserves.get(
                preserve_id,
                {}
            )

            level = player_data.get(
                "level",
                1
            )

            unlocked = player_data.get(
                "unlocked",
                False
            )

            # Locked preserves
            if not unlocked:
                embed.add_field(
                    name=f"🔒 {preserve_data['name']}",
                    value=(
                        f"Requires Sanctuary Progress\n"
                        f"Unlock Level: {preserve_data.get('unlock_level', '?')}"
                    ),
                    inline=False
                )
                continue


            capacity = get_preserve_capacity(
                player,
                preserve_id
            )

            residents = get_preserve_residents(
                player,
                preserve_id
            )


            resident_text = ""

            if residents:
                for creature in residents:
                    site = creature.shelter.get(
                        "site",
                        "Unknown Site"
                    )

                    resident_text += (
                        f"🏡 {creature.name} "
                        f"({site})\n"
                    )
            else:
                resident_text = "No creatures settled here yet."


            embed.add_field(
                name=(
                    f"{preserve_data['emoji']} "
                    f"{preserve_data['name']} "
                    f"(Lv {level})"
                ),
                value=(
                    f"👥 Residents: {len(residents)}/{capacity}\n\n"
                    f"{resident_text}"
                ),
                inline=False
            )


        embed.set_footer(
            text="Use !settle <creature name> to choose a new home."
        )

        await ctx.send(embed=embed)