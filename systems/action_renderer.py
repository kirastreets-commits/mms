import discord
from collections import defaultdict


# ----------------------------
# MOOD COLOUR MAP
# ----------------------------
COLOR_MAP = {
    "happy": 0x7CFC90,
    "tired": 0x6B7CFF,
    "scared": 0x9B59B6,
    "neutral": 0x95A5A6
}


# ----------------------------
# MERGE STAT CHANGES
# ----------------------------
def merge_stat_changes(changes):
    merged = defaultdict(int)

    for stat, value in changes:
        merged[stat] += value

    return merged


# ----------------------------
# MAIN RENDER FUNCTION
# ----------------------------
def render_action_embed(
    *,
    title: str,
    creature,
    result: dict,
    action_text: str
):
    """
    Standard embed renderer for ALL creature actions.
    """

    embed = discord.Embed(
        title=title,
        description=f"{action_text}\n\n{result['message']}",
        color=COLOR_MAP.get(creature.mood, 0x6bbf59)
    )

    # ----------------------------
    # STATS
    # ----------------------------
    changes = merge_stat_changes(result.get("stat_changes", []))

    if changes:
        stat_text = ""

        for stat, value in changes.items():
            sign = "+" if value > 0 else ""
            stat_text += f"**{stat}**: {sign}{value}\n"

        embed.add_field(
            name="📊 Stat Changes",
            value=stat_text.strip(),
            inline=False
        )

    # ----------------------------
    # RARE EVENT
    # ----------------------------
    if result.get("rare_event"):
        embed.add_field(
            name="✨ Rare Event",
            value=result["rare_event"],
            inline=False
        )

    # ----------------------------
    # MOOD
    # ----------------------------
    embed.add_field(
        name="🌦 Mood",
        value=creature.mood.capitalize(),
        inline=True
    )

    return embed