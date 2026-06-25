import discord
from data.gift_responses import get_gift_message


def get_shelter_text(result):
    return {
        "favorite": "It places the item somewhere special in its shelter.",
        "kept": "It adds the item to its shelter.",
        "ignored": "It leaves the item in its shelter without much interest.",
        "rejected": "It refuses to keep the gift."
    }.get(result["shelter_action"], "")

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
    embed.add_field(
        name="Shelter",
        value=get_shelter_text(result),
        inline=False
    )
    

    return embed
