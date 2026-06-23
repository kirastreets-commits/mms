from systems.save_system import get_or_create_player, save_player
from data.exploration import EXPLORATION_EVENTS
import random
import discord


def setup(bot):
    @bot.command()
    async def explore_sanctuary(ctx, *, creature_name: str):
        player = get_or_create_player(ctx.author)

        if not player.creatures:
            await ctx.send("You don't have a creature to explore with yet.")
            return

        creature = player.get_creature(creature_name)

        # basic energy check
        if creature.energy <= 10:
            await ctx.send(f"{creature.name} is too tired to explore right now.")
            return

        event = random.choice(EXPLORATION_EVENTS)

        # apply energy cost
        creature.energy -= 10

        # apply effects safely
        creature.happiness = max(0, creature.happiness + event.get("happiness", 0))
        creature.trust = min(100, creature.trust + event.get("trust", 0))

        # optional: bond system
        if hasattr(creature, "bond"):
            creature.bond += event.get("bond", 0)

        # sanctuary progression hook
        if hasattr(player, "sanctuary_progress"):
            player.sanctuary_progress += event.get("sanctuary_progress", 0)

        save_player(player)

        embed = discord.Embed(
            title="🌿 Sanctuary Exploration",
            description=event["text"],
            color=0x6bbf59
        )

        embed.add_field(name="Creature", value=creature.name, inline=True)
        embed.add_field(name="Current Energy", value=str(creature.energy), inline=True)

        await ctx.send(embed=embed)