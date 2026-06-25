import discord
from discord.ext import commands

from commands import feed, heal, rest, play, start, starter, inspect, overview, explore_sanctuary, explore, journal, species, reset_tutorial, help

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)
from systems.database import get_connection


try:
    conn = get_connection()
    print("✅ Database connected")
    conn.close()

except Exception as e:
    print(f"❌ Database error: {e}")



@bot.event
async def on_ready():
    print(f"🐉 Sanctuary is online as {bot.user}")

feed.setup(bot)
heal.setup(bot)
rest.setup(bot)
play.setup(bot)
starter.setup(bot)
start.setup(bot)
inspect.setup(bot)
overview.setup(bot)
explore_sanctuary.setup(bot)
explore.setup(bot)
journal.setup(bot)
species.setup(bot)
help.setup(bot)
reset_tutorial.setup(bot)

from systems.tutorial_cutscene import start_intro

import os

bot.run(os.getenv("DISCORD_TOKEN"))
