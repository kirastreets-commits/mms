import discord
from discord.ext import commands

from systems.save_system import get_or_create_player, save_player
from data.locations import LOCATIONS
from ui.explore_views import ExploreMenuView


def setup(bot):

    @bot.command()
    async def explore(ctx):
        player = get_or_create_player(ctx.author)

        view = ExploreMenuView(player)
        embed = discord.Embed(
            title="🌿 Explore the Sanctuary",
            description="Where would you like to go?",
            color=0x2ecc71
        )

        await ctx.send(embed=embed, view=view)
