from data.gift_responses import (
    LOVE_MESSAGES,
    LIKE_MESSAGES,
    NEUTRAL_MESSAGES,
    DISLIKE_MESSAGES
)
from data.gift_responses import get_gift_message


def build_gift_embed(creature, result):
    embed = discord.Embed()

    embed.description = get_gift_message(creature, result)

    embed.add_field(
        name="Bond",
        value=f"+{result['bond_gain']}",
        inline=True
    )

    embed.add_field(
        name="Comfort",
        value=f"+{result['comfort_gain']}",
        inline=True
    )

    return embed

