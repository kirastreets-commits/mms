import discord

from systems.save_system import get_or_create_player


def setup(bot):

    @bot.command(aliases=["inv", "bag"])
    async def inventory(ctx):

        player = get_or_create_player(ctx.author)

        embed = discord.Embed(
            title=f"🎒 {ctx.author.display_name}'s Inventory",
            color=discord.Color.green()
        )

        if not player.inventory:
            embed.description = "Your inventory is empty."
            return await ctx.send(embed=embed)

        # Group items by type
        grouped = {}

        for item_id, amount in player.inventory.items():
            if amount <= 0:
                continue

            # If your item data is stored in RESOURCES
            from data.resources import RESOURCES

            item = RESOURCES.get(item_id)

            if not item:
                continue

            item_type = item.get("type", "Other").title()

            grouped.setdefault(item_type, []).append(
                f"{item['emoji']} **{item['name']}** × {amount}"
            )

        if not grouped:
            embed.description = "Your inventory is empty."
            return await ctx.send(embed=embed)

        for category, items in grouped.items():
            embed.add_field(
                name=category,
                value="\n".join(items),
                inline=False
            )

        await ctx.send(embed=embed)
