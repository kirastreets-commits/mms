from systems.save_system import get_or_create_player, save_player
from systems.gift_system import gift_creature

import discord

def build_gift_embed(creature, item_id, result):
    reaction = result["reaction"]
    action = result["shelter_action"]

    color_map = {
        "loves": discord.Color.green(),
        "likes": discord.Color.blurple(),
        "neutral": discord.Color.greyple(),
        "dislikes": discord.Color.red()
    }

    embed = discord.Embed(
        title=f"{creature.name} received a gift!",
        description=f"The creature looks **{reaction}** about it.",
        color=color_map.get(reaction, discord.Color.default())
    )

    embed.add_field(
        name="Bond Change",
        value=f"+{result['bond_gain']} trust",
        inline=True
    )

    embed.add_field(
        name="Comfort",
        value=f"+{result['comfort_gain']}",
        inline=True
    )

    # 🏡 Shelter result message
    shelter_text = {
        "favorite": "It placed the item in a special corner of its shelter.",
        "kept": "It added the item to its shelter.",
        "ignored": "It left the item in its shelter without interest.",
        "rejected": "It rejected the gift and refuses to keep it."
    }

    embed.add_field(
        name="Shelter",
        value=shelter_text.get(action, "No change."),
        inline=False
    )

    if item_id:
        embed.set_footer(text=f"Item: {item_id}")

    return embed


def setup(bot):

    @bot.command()
    async def gift(ctx, creature_name: str, item_id: str):
        player = get_or_create_player(ctx.author)
        creature = player.get_creature(creature_name)
    
        if not creature:
            return await ctx.send("You don't have that creature.")
    
        result = gift_creature(player, creature, item_id)
    
        if not result["success"]:
            return await ctx.send(result["message"])
    
        embed = build_gift_embed(creature, item_id, result)
    
        await ctx.send(embed=embed)
