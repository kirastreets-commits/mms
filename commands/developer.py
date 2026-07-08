import discord
from discord.ext import commands

from systems.save_system import (
    get_or_create_player,
    save_player,
)

from models.creature import Creature
from data.species import SPECIES_REGISTRY
from data.resources import RESOURCES
from data.preserves import PRESERVES


def setup(bot):

    # --------------------------------------------------
    # Helper Functions
    # --------------------------------------------------

    def get_player(ctx, member=None):
        member = member or ctx.author
        return get_or_create_player(member)

    def success_embed(title, description):
        embed = discord.Embed(
            title=f"✅ {title}",
            description=description,
            color=discord.Color.green()
        )
        return embed

    def error_embed(message):
        embed = discord.Embed(
            title="❌ Error",
            description=message,
            color=discord.Color.red()
        )
        return embed

    # --------------------------------------------------
    # !dev
    # --------------------------------------------------

    @bot.group(invoke_without_command=True)
    @commands.has_permissions(administrator=True)
    async def dev(ctx):

        embed = discord.Embed(
            title="🛠 Developer Commands",
            colour=discord.Color.blurple()
        )

        embed.add_field(
            name="🐾 Creatures",
            value=(
                "`!dev creatures list`\n"
                "`!dev creatures inspect <index>`\n"
                "`!dev creatures remove <index>`\n"
                "`!dev creatures rename <index> <name>`"
            ),
            inline=False
        )

        embed.add_field(
            name="🎒 Inventory",
            value=(
                "`!dev inventory list`\n"
                "`!dev inventory give`\n"
                "`!dev inventory remove`\n"
                "`!dev inventory clear`"
            ),
            inline=False
        )

        embed.add_field(
            name="👤 Player",
            value=(
                "`!dev player info`\n"
                "`!dev player tutorial`\n"
                "`!dev player reset`"
            ),
            inline=False
        )

        embed.add_field(
            name="🌲 Preserves",
            value=(
                "`!dev preserve list`\n"
                "`!dev preserve unlock`\n"
                "`!dev preserve level`"
            ),
            inline=False
        )

        await ctx.send(embed=embed)

    # --------------------------------------------------
    # !dev creatures
    # --------------------------------------------------

    @dev.group(invoke_without_command=True)
    async def creatures(ctx):

        embed = discord.Embed(
            title="🐾 Creature Commands",
            colour=discord.Color.orange()
        )

        embed.description = (
            "`!dev creatures list`\n"
            "`!dev creatures inspect <index>`\n"
            "`!dev creatures remove <index>`\n"
            "`!dev creatures rename <index> <new name>`"
        )

        await ctx.send(embed=embed)

    # --------------------------------------------------
    # LIST
    # --------------------------------------------------

    @creatures.command(name="list")
    async def creature_list(ctx, member: discord.Member = None):

        player = get_player(ctx, member)

        if not player.creatures:
            return await ctx.send(
                embed=error_embed("This player has no creatures.")
            )

        embed = discord.Embed(
            title=f"🐾 {player.name}'s Creatures",
            colour=discord.Color.green()
        )

        for index, creature in enumerate(player.creatures):

            embed.add_field(
                name=f"{index}. {creature.name}",
                value=(
                    f"Species: **{creature.species}**\n"
                    f"❤️ {creature.health}/{creature.max_health}\n"
                    f"⚡ {creature.energy}/{creature.max_energy}\n"
                    f"🍖 {creature.hunger}/{creature.max_hunger}\n"
                    f"😊 {creature.happiness}/{creature.max_happiness}\n"
                    f"🤝 {creature.trust}/{creature.max_trust}"
                ),
                inline=False
            )

        await ctx.send(embed=embed)

    # --------------------------------------------------
    # INSPECT
    # --------------------------------------------------

    @creatures.command(name="inspect")
    async def inspect_creature(
        ctx,
        index: int,
        member: discord.Member = None
    ):

        player = get_player(ctx, member)

        if index < 0 or index >= len(player.creatures):
            return await ctx.send(
                embed=error_embed("Invalid creature index.")
            )

        creature = player.creatures[index]

        embed = discord.Embed(
            title=f"🔍 {creature.name}",
            colour=discord.Color.gold()
        )

        embed.add_field(name="Species", value=creature.species)
        embed.add_field(name="Personality", value=creature.personality)
        embed.add_field(name="Mood", value=creature.mood)

        embed.add_field(
            name="Stats",
            value=(
                f"❤️ Health: {creature.health}/{creature.max_health}\n"
                f"⚡ Energy: {creature.energy}/{creature.max_energy}\n"
                f"🍖 Hunger: {creature.hunger}/{creature.max_hunger}\n"
                f"😊 Happiness: {creature.happiness}/{creature.max_happiness}\n"
                f"🤝 Trust: {creature.trust}/{creature.max_trust}"
            ),
            inline=False
        )

        await ctx.send(embed=embed)

    # --------------------------------------------------
    # REMOVE
    # --------------------------------------------------

    @creatures.command(name="remove")
    async def remove_creature(
        ctx,
        index: int,
        member: discord.Member = None
    ):

        player = get_player(ctx, member)

        if index < 0 or index >= len(player.creatures):
            return await ctx.send(
                embed=error_embed("Invalid creature index.")
            )

        creature = player.creatures.pop(index)

        save_player(player)

        await ctx.send(
            embed=success_embed(
                "Creature Removed",
                f"Removed **{creature.name}** ({creature.species})"
            )
        )

    # --------------------------------------------------
    # RENAME
    # --------------------------------------------------

    @creatures.command(name="rename")
    async def rename_creature(
        ctx,
        index: int,
        *,
        new_name: str
    ):

        player = get_player(ctx)

        if index < 0 or index >= len(player.creatures):
            return await ctx.send(
                embed=error_embed("Invalid creature index.")
            )

        creature = player.creatures[index]

        old_name = creature.name
        creature.name = new_name

        save_player(player)

        await ctx.send(
            embed=success_embed(
                "Creature Renamed",
                f"**{old_name}** ➜ **{new_name}**"
            )
        )

        # --------------------------------------------------
    # !dev inventory
    # --------------------------------------------------

    @dev.group(invoke_without_command=True)
    async def inventory(ctx):

        embed = discord.Embed(
            title="🎒 Inventory Commands",
            colour=discord.Color.blue()
        )

        embed.description = (
            "`!dev inventory list`\n"
            "`!dev inventory give <item> <amount>`\n"
            "`!dev inventory remove <item> <amount>`\n"
            "`!dev inventory clear`"
        )

        await ctx.send(embed=embed)

    # --------------------------------------------------
    # INVENTORY LIST
    # --------------------------------------------------

    @inventory.command(name="list")
    async def inventory_list(ctx, member: discord.Member = None):

        player = get_player(ctx, member)

        if not player.inventory:
            return await ctx.send(
                embed=error_embed("Inventory is empty.")
            )

        embed = discord.Embed(
            title=f"🎒 {player.name}'s Inventory",
            colour=discord.Color.blue()
        )

        for item, amount in sorted(player.inventory.items()):
            embed.add_field(
                name=item,
                value=f"x{amount}",
                inline=True
            )

        await ctx.send(embed=embed)

    # --------------------------------------------------
    # GIVE ITEM
    # --------------------------------------------------

    @inventory.command(name="give")
    async def inventory_give(
        ctx,
        item: str,
        amount: int = 1,
        member: discord.Member = None
    ):

        player = get_player(ctx, member)

        if item not in RESOURCES:
            return await ctx.send(
                embed=error_embed(f"`{item}` doesn't exist.")
            )

        player.add_to_inventory(item, amount)
        save_player(player)

        await ctx.send(
            embed=success_embed(
                "Inventory Updated",
                f"Gave **{amount}x {item}**."
            )
        )

    # --------------------------------------------------
    # REMOVE ITEM
    # --------------------------------------------------

    @inventory.command(name="remove")
    async def inventory_remove(
        ctx,
        item: str,
        amount: int = 1,
        member: discord.Member = None
    ):

        player = get_player(ctx, member)

        if item not in player.inventory:
            return await ctx.send(
                embed=error_embed("Item not found.")
            )

        player.remove_from_inventory(item, amount)
        save_player(player)

        await ctx.send(
            embed=success_embed(
                "Inventory Updated",
                f"Removed **{amount}x {item}**."
            )
        )

    # --------------------------------------------------
    # CLEAR INVENTORY
    # --------------------------------------------------

    @inventory.command(name="clear")
    async def inventory_clear(
        ctx,
        member: discord.Member = None
    ):

        player = get_player(ctx, member)

        player.inventory.clear()

        save_player(player)

        await ctx.send(
            embed=success_embed(
                "Inventory Cleared",
                "All items removed."
            )
        )

    # --------------------------------------------------
    # !dev player
    # --------------------------------------------------

    @dev.group(invoke_without_command=True)
    async def player(ctx):

        embed = discord.Embed(
            title="👤 Player Commands",
            colour=discord.Color.purple()
        )

        embed.description = (
            "`!dev player info`\n"
            "`!dev player tutorial <stage>`\n"
            "`!dev player discover <species>`\n"
            "`!dev player unlock <location>`\n"
            "`!dev player reset`"
        )

        await ctx.send(embed=embed)

    # --------------------------------------------------
    # PLAYER INFO
    # --------------------------------------------------

    @player.command(name="info")
    async def player_info(
        ctx,
        member: discord.Member = None
    ):

        player = get_player(ctx, member)

        embed = discord.Embed(
            title=f"👤 {player.name}",
            colour=discord.Color.purple()
        )

        embed.add_field(
            name="Creatures",
            value=len(player.creatures)
        )

        embed.add_field(
            name="Species Discovered",
            value=len(player.discovered_species)
        )

        embed.add_field(
            name="Tutorial Stage",
            value=player.tutorial_stage
        )

        embed.add_field(
            name="Tutorial Complete",
            value=player.tutorial_complete
        )

        embed.add_field(
            name="Starter",
            value=player.has_starter
        )

        embed.add_field(
            name="Unlocked Locations",
            value=len(player.unlocked_locations)
        )

        await ctx.send(embed=embed)

    # --------------------------------------------------
    # TUTORIAL
    # --------------------------------------------------

    @player.command(name="tutorial")
    async def tutorial_stage(
        ctx,
        stage: int
    ):

        player = get_player(ctx)

        player.tutorial_stage = stage

        save_player(player)

        await ctx.send(
            embed=success_embed(
                "Tutorial Updated",
                f"Stage set to **{stage}**."
            )
        )

    # --------------------------------------------------
    # DISCOVER SPECIES
    # --------------------------------------------------

    @player.command(name="discover")
    async def discover_species(
        ctx,
        species: str
    ):

        player = get_player(ctx)

        if species not in SPECIES_REGISTRY:
            return await ctx.send(
                embed=error_embed("Unknown species.")
            )

        player.add_discovered_species(species)

        save_player(player)

        await ctx.send(
            embed=success_embed(
                "Species Discovered",
                species
            )
        )

    # --------------------------------------------------
    # UNLOCK LOCATION
    # --------------------------------------------------

    @player.command(name="unlock")
    async def unlock_location(
        ctx,
        location: str
    ):

        player = get_player(ctx)

        if location not in player.unlocked_locations:
            player.unlocked_locations.append(location)

        save_player(player)

        await ctx.send(
            embed=success_embed(
                "Location Unlocked",
                location
            )
        )

    # --------------------------------------------------
    # RESET PLAYER
    # --------------------------------------------------

    @player.command(name="reset")
    async def reset_player(ctx):

        player = get_player(ctx)

        player.inventory.clear()
        player.creatures.clear()
        player.discovered_species.clear()
        player.journal_entries.clear()

        player.unlocked_locations = [
            "sanctuary_core"
        ]

        player.tutorial_stage = 0
        player.tutorial_complete = False
        player.has_starter = False

        save_player(player)

        await ctx.send(
            embed=success_embed(
                "Player Reset",
                "Player save has been reset."
            )
        )

        # --------------------------------------------------
    # !dev preserve
    # --------------------------------------------------

    @dev.group(invoke_without_command=True)
    async def preserve(ctx):

        embed = discord.Embed(
            title="🌲 Preserve Commands",
            colour=discord.Color.dark_green()
        )

        embed.description = (
            "`!dev preserve list`\n"
            "`!dev preserve unlock <id>`\n"
            "`!dev preserve level <id> <level>`\n"
            "`!dev preserve restoration <id> <amount>`"
        )

        await ctx.send(embed=embed)

    # --------------------------------------------------
    # PRESERVE LIST
    # --------------------------------------------------

    @preserve.command(name="list")
    async def preserve_list(ctx):

        player = get_player(ctx)

        embed = discord.Embed(
            title="🌲 Player Preserves",
            colour=discord.Color.green()
        )

        for preserve_id, data in player.preserves.items():

            status = "✅" if data["unlocked"] else "🔒"

            embed.add_field(
                name=f"{status} {preserve_id}",
                value=(
                    f"Level: {data['level']}\n"
                    f"Restoration: {data['restoration']}"
                ),
                inline=False
            )

        await ctx.send(embed=embed)

    # --------------------------------------------------
    # UNLOCK PRESERVE
    # --------------------------------------------------

    @preserve.command(name="unlock")
    async def preserve_unlock(ctx, preserve_id: str):

        player = get_player(ctx)

        if preserve_id not in player.preserves:
            return await ctx.send(embed=error_embed("Unknown preserve."))

        player.preserves[preserve_id]["unlocked"] = True

        save_player(player)

        await ctx.send(
            embed=success_embed(
                "Preserve Updated",
                f"Unlocked **{preserve_id}**."
            )
        )

    # --------------------------------------------------
    # LEVEL
    # --------------------------------------------------

    @preserve.command(name="level")
    async def preserve_level(
        ctx,
        preserve_id: str,
        level: int
    ):

        player = get_player(ctx)

        if preserve_id not in player.preserves:
            return await ctx.send(embed=error_embed("Unknown preserve."))

        player.preserves[preserve_id]["level"] = level

        save_player(player)

        await ctx.send(
            embed=success_embed(
                "Preserve Updated",
                f"{preserve_id} is now level {level}."
            )
        )

    # --------------------------------------------------
    # RESTORATION
    # --------------------------------------------------

    @preserve.command(name="restoration")
    async def preserve_restoration(
        ctx,
        preserve_id: str,
        amount: int
    ):

        player = get_player(ctx)

        if preserve_id not in player.preserves:
            return await ctx.send(embed=error_embed("Unknown preserve."))

        player.preserves[preserve_id]["restoration"] = amount

        save_player(player)

        await ctx.send(
            embed=success_embed(
                "Preserve Updated",
                f"Restoration set to {amount}."
            )
        )

    # --------------------------------------------------
    # !dev cleanup
    # --------------------------------------------------

    @dev.command(name="cleanup")
    async def cleanup(ctx):

        player = get_player(ctx)

        removed = 0
        seen = set()

        unique = []

        for creature in player.creatures:

            key = (
                creature.name.lower(),
                creature.species.lower()
            )

            if key in seen:
                removed += 1
                continue

            seen.add(key)
            unique.append(creature)

        player.creatures = unique

        save_player(player)

        await ctx.send(
            embed=success_embed(
                "Cleanup Complete",
                f"Removed **{removed}** duplicate creatures."
            )
        )

    # --------------------------------------------------
    # !dev save
    # --------------------------------------------------

    @dev.command(name="save")
    async def save(ctx):

        player = get_player(ctx)

        save_player(player)

        await ctx.send(
            embed=success_embed(
                "Player Saved",
                "Save written to the database."
            )
        )

    # --------------------------------------------------
    # !dev help
    # --------------------------------------------------

    @dev.command(name="help")
    async def dev_help(ctx):

        embed = discord.Embed(
            title="🛠 Developer Help",
            colour=discord.Color.blurple()
        )

        embed.description = (
            "**Creatures**\n"
            "`!dev creatures list`\n"
            "`!dev creatures inspect`\n"
            "`!dev creatures remove`\n"
            "`!dev creatures rename`\n\n"

            "**Inventory**\n"
            "`!dev inventory list`\n"
            "`!dev inventory give`\n"
            "`!dev inventory remove`\n"
            "`!dev inventory clear`\n\n"

            "**Player**\n"
            "`!dev player info`\n"
            "`!dev player tutorial`\n"
            "`!dev player discover`\n"
            "`!dev player unlock`\n"
            "`!dev player reset`\n\n"

            "**Preserves**\n"
            "`!dev preserve list`\n"
            "`!dev preserve unlock`\n"
            "`!dev preserve level`\n"
            "`!dev preserve restoration`\n\n"

            "**Utilities**\n"
            "`!dev cleanup`\n"
            "`!dev save`"
        )

        await ctx.send(embed=embed)