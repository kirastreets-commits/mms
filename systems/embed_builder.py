import discord
from data.gift_responses import get_gift_message


def get_shelter_text(creature, result):
    shelter_name = creature.shelter.get("type", "shelter")
    shelter_name = shelter_name.replace("_", " ").title()

    return {
        "favorite": f"{creature.name} proudly places it in a special spot inside its {shelter_name}.",
        "kept": f"{creature.name} carries it back to its {shelter_name} and finds the perfect place for it.",
        "ignored": f"{creature.name} sets it inside its {shelter_name}, though it doesn't seem particularly interested.",
        "rejected": f"{creature.name} refuses the gift and leaves it outside its {shelter_name}."
    }.get(result["shelter_action"], "")


def build_gift_embed(creature, result):
    embed = discord.Embed(
        title=f"🎁 {creature.name} received a gift!",
        description=get_gift_message(creature, result),
        color=discord.Color.green()
    )

    embed.add_field(
        name="Trust",
        value=f"{result['bond_gain']:+}",
        inline=True
    )

    embed.add_field(
        name="Comfort",
        value=f"{result['comfort_gain']:+}",
        inline=True
    )

    shelter_name = creature.shelter.get("type", "Shelter")
    shelter_name = shelter_name.replace("_", " ").title()

    embed.add_field(
        name=shelter_name,
        value=get_shelter_text(creature, result),
        inline=False
    )

    return embed
