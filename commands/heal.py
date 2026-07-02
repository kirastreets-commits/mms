from systems.action_renderer import render_action_embed
from systems.save_system import get_or_create_player, save_player


def setup(bot):

    @bot.command()
    async def heal(ctx, creature_name: str):

        player = get_or_create_player(ctx.author)

        creature = player.get_creature(creature_name)

        if not creature:
            return await ctx.send("You don't have a creature with that name.")

        result = creature.heal()


        save_player(player)

        embed = render_action_embed(
            title="🩹 Healing Session",
            creature=creature,
            result=result,
            action_text=f"You carefully tend to **{creature.name}**."
        )

        if result["healing_item"]:
            item = result["healing_item"]
            embed.add_field(
                name="Healing Resource",
                value=f'{item["emoji"]} {item["name"]}',
                inline=False
            )

        await ctx.send(embed=embed)
