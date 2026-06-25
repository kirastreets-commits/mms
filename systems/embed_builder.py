import discord
from systems.narrative_system import get_gift_message

def build_gift_embed(creature, result):
    embed = discord.Embed(
        title=f"{creature.name} received a gift!",
        description=get_gift_message(creature, result),
        color=discord.Color.green()
    )

    embed.add_field(
        name="Bond Change",
        value=f"+{result['bond_gain']}",
        inline=True
    )

    embed.add_field(
        name="Comfort",
        value=f"+{result['comfort_gain']}",
        inline=True
    )

    return embed
