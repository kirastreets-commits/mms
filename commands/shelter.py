import discord

from systems.save_system import (
    get_or_create_player,
    save_player,
)
from systems.shelter_system import (
    update_shelter,
    SHELTER_LEVELS,
    generate_shelter_description,
)
from systems.preserve_system import (
    get_preserve,
    get_available_shelter_sites,
    get_preserve_capacity,
    get_preserve_residents,
)
from data.resources import RESOURCES


def setup(bot):

    @bot.command()
    async def shelter(ctx, creature_name: str):

        player = get_or_create_player(ctx.author)
        creature = player.get_creature(creature_name)

        if not creature:
            return await ctx.send("You don't have a creature with that name.")

        # --------------------------------------------------
        # Upgrade older save files by assigning a shelter site
        # --------------------------------------------------
        if (
            creature.shelter.get("location")
            and creature.shelter.get("site") is None
        ):
            available_sites = get_available_shelter_sites(
                player,
                creature.shelter["location"]
            )

            if available_sites:
                creature.shelter["site"] = available_sites[0]
                save_player(player)

        # --------------------------------------------------
        # Update shelter
        # --------------------------------------------------
        shelter_name = creature.shelter.get("type", "Shelter")

        shelter_result = update_shelter(creature)

        comfort = shelter_result["comfort"]
        level = shelter_result["new_level"]

        # Save updated comfort/level
        save_player(player)

        items = creature.shelter.get("items", [])

        # --------------------------------------------------
        # Preserve information
        # --------------------------------------------------
        species_data = creature.species_data
        is_native = species_data.get("sanctuary_native", False)

        shelter_name = creature.shelter.get("type", "Shelter")

        if is_native:
            preserve_name = "Moonlit Meadows Sanctuary"
            shelter_site = creature.shelter.get("site", "Sanctuary Home")
        else:
            preserve_name = "Unsettled"

            location = creature.shelter.get("location")
            if location:
                preserve = get_preserve(location)
                if preserve:
                    preserve_name = preserve["name"]

            shelter_site = creature.shelter.get("site", "—")

        # --------------------------------------------------
        # Progress
        # --------------------------------------------------
        next_level = level + 1

        if next_level in SHELTER_LEVELS:
            progress = (
                f"{comfort} / "
                f"{SHELTER_LEVELS[next_level]} Comfort"
            )
        else:
            progress = "✨ Maximum Shelter Level"

        # --------------------------------------------------
        # Embed
        # --------------------------------------------------
        embed = discord.Embed(
            title=f"🏡 {creature.name}'s {shelter_name}",
            description=(
                f"📍 **{preserve_name}**\n"
                f"🌿 **{shelter_site}**\n\n"
                f"⭐ **Comfort:** {comfort}\n"
                f"🏠 **Shelter Level:** {level}"
            ),
            color=0x6BBF59
        )

        # --------------------------------------------------
        # Description
        # --------------------------------------------------
        embed.add_field(
            name="📖 Description",
            value=generate_shelter_description(creature),
            inline=False
        )

        # --------------------------------------------------
        # Decorations
        # --------------------------------------------------
        if items:

            favorite_items = []
            regular_items = []

            for entry in items:

                resource = RESOURCES.get(entry["item"], {})

                emoji = resource.get("emoji", "📦")
                name = resource.get(
                    "name",
                    entry["item"].replace("_", " ").title()
                )

                line = f"{emoji} **{name}**"

                if entry.get("state") == "favorite":
                    favorite_items.append(f"🌟 {line}")
                else:
                    regular_items.append(f"🏡 {line}")

            if favorite_items:
                embed.add_field(
                    name="🌟 Favorite Decorations",
                    value="\n".join(favorite_items),
                    inline=False
                )

            if regular_items:
                embed.add_field(
                    name="🪴 Shelter Decorations",
                    value="\n".join(regular_items),
                    inline=False
                )

        else:
            embed.add_field(
                name="🪴 Shelter Decorations",
                value="*This shelter hasn't been decorated yet.*",
                inline=False
            )

        # --------------------------------------------------
        # Upgrade Progress
        # --------------------------------------------------
        embed.add_field(
            name="📈 Next Upgrade",
            value=progress,
            inline=False
        )

        await ctx.send(embed=embed)
