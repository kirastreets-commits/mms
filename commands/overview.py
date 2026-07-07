import discord

from systems.save_system import get_or_create_player
from systems.preserve_system import get_preserve
from data.species import SPECIES_REGISTRY


# ----------------------------
# UI HELPER
# ----------------------------

def bar(value, max_value=100, length=6):
    value = max(0, min(value, max_value))
    filled = int((value / max_value) * length)
    return "█" * filled + "░" * (length - filled)


# ----------------------------
# CREATURE STATUS
# ----------------------------

def get_status(creature):

    if creature.health <= 20:
        return "❤️ Needs Healing"

    if creature.hunger <= 20:
        return "🍖 Hungry"

    if creature.energy <= 20:
        return "💤 Needs Rest"

    if creature.happiness <= 20:
        return "💔 Unhappy"

    if creature.happiness >= 90:
        return "🌿 Thriving"

    return "🌱 Doing Well"


# ----------------------------
# HOME STATUS
# ----------------------------

def get_home_status(creature):

    species_data = SPECIES_REGISTRY.get(
        creature.species,
        {}
    )


    # Sanctuary native creatures
    if species_data.get("sanctuary_native"):

        home = species_data.get(
            "sanctuary_home",
            {}
        )

        return (
            f"✨ Native Resident\n"
            f"🏡 {home.get('name', 'Sanctuary Home')}"
        )


    # Settled creatures
    if creature.shelter.get("location"):

        preserve = get_preserve(
            creature.shelter["location"]
        )

        preserve_name = (
            preserve["name"]
            if preserve
            else creature.shelter["location"]
        )

        return (
            f"🏡 {preserve_name}\n"
            f"🌿 {creature.shelter.get('site', 'Unknown Site')}"
        )


    # Needs home
    return (
        f"🏡 Needs Shelter\n"
        f"⚠️ Use `!settle {creature.name}`"
    )


# ----------------------------
# OVERVIEW COMMAND
# ----------------------------

def setup(bot):

    @bot.command()
    async def overview(ctx):

        player = get_or_create_player(ctx.author)

        if not player.creatures:
            await ctx.send(
                "🏡 Your sanctuary is quiet...\n"
                "No creatures are currently in your care.\n\n"
                "Try `!starter` or `!adopt` to begin your journey."
            )
            return


        # ----------------------------
        # GROUP CREATURES BY HOME
        # ----------------------------

        preserves = {}

        for creature in player.creatures:

            species_data = SPECIES_REGISTRY.get(
                creature.species,
                {}
            )


            # Sanctuary natives get their own home grouping
            if species_data.get("sanctuary_native"):

                home = species_data.get(
                    "sanctuary_home",
                    {}
                )

                preserve_name = home.get(
                    "name",
                    "Sanctuary Residents"
                )

                preserve_emoji = "✨"


            else:

                location_id = creature.shelter.get("location")

                if location_id:

                    preserve = get_preserve(location_id)

                    preserve_name = (
                        preserve["name"]
                        if preserve
                        else location_id
                    )

                    preserve_emoji = (
                        preserve.get("emoji", "🏡")
                        if preserve
                        else "🏡"
                    )

                else:

                    preserve_name = "Unsettled Creatures"
                    preserve_emoji = "🌱"


            if preserve_name not in preserves:

                preserves[preserve_name] = {
                    "emoji": preserve_emoji,
                    "creatures": []
                }


            preserves[preserve_name]["creatures"].append(
                creature
            )


        # ----------------------------
        # BUILD EMBED
        # ----------------------------

        embed = discord.Embed(
            title="🏡 Sanctuary Overview",
            description=(
                f"🐾 **Creatures:** {len(player.creatures)}\n"
                "Your caretaker watches over every corner of the sanctuary."
            ),
            color=discord.Color.blurple()
        )


        # ----------------------------
        # DISPLAY HOMES
        # ----------------------------

        for preserve_name, data in preserves.items():

            creature_text = ""


            for creature in data["creatures"]:

                species = SPECIES_REGISTRY.get(
                    creature.species,
                    {}
                )

                emoji = species.get(
                    "emoji",
                    "🐾"
                )


                creature_text += (
                    f"{emoji} **{creature.name}**\n"
                    f"{creature.species} • "
                    f"{creature.bond_level()}\n"
                    f"{get_home_status(creature)}\n"
                    f"{get_status(creature)}\n"
                    f"❤️ {bar(creature.health)}\n"
                    f"🍖 {bar(creature.hunger)}\n\n"
                )


            embed.add_field(
                name=(
                    f"{data['emoji']} {preserve_name} "
                    f"({len(data['creatures'])})"
                ),
                value=creature_text,
                inline=False
            )


        embed.set_footer(
            text="Use !inspect <name> to view a creature's full profile."
        )


        await ctx.send(embed=embed)
