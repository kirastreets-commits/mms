import discord

from data.resources import RESOURCES
from systems.action_renderer import render_action_embed
from systems.save_system import save_player

class HealResourceSelect(discord.ui.Select):

    def __init__(self, player, creature):

        self.player = player
        self.creature = creature

        options = [
            discord.SelectOption(
                label="No Healing Resource",
                value="none",
                emoji="🩹",
                description="Heal normally."
            )
        ]

        for item_id, amount in player.inventory.items():

            if amount <= 0:
                continue

            item = RESOURCES[item_id]

            if item["type"] != "healing":
                continue

            options.append(
                discord.SelectOption(
                    label=f'{item["name"]} x{amount}',
                    value=item_id,
                    emoji=item.get("emoji"),
                    description=f"+{item.get('healing_bonus', 0)}% healing success"
                )
            )

        super().__init__(
            placeholder="Choose a healing resource...",
            options=options
        )

    async def callback(self, interaction: discord.Interaction):

        healing_item = None

        if self.values[0] != "none":
            item_id = self.values[0]
            healing_item = RESOURCES[item_id]
            self.player.remove_from_inventory(item_id, 1)

        result = self.creature.heal(healing_item)

        save_player(self.player)

        embed = render_action_embed(
            title="🩹 Healing Session",
            creature=self.creature,
            result=result,
            action_text=f"You attempt to tend to **{self.creature.name}**."
        )

        if result.get("healing_item"):
            item = result["healing_item"]
            embed.add_field(
                name="Healing Resource",
                value=f'{item["emoji"]} {item["name"]}',
                inline=False
            )

        await interaction.response.edit_message(
            embed=embed,
            view=None
        )


class HealView(discord.ui.View):

    def __init__(self, player, creature):

        super().__init__(timeout=60)

        self.add_item(
            HealResourceSelect(player, creature)
        )
