import discord

from data.resources import RESOURCES
from models import creature
from systems.action_renderer import render_action_embed
from systems.gift_system import build_gift_embed, gift_creature, give_item
from systems.save_system import save_player

class GiftResourceSelect(discord.ui.Select):

    def __init__(self, player, creature):

        self.player = player
        self.creature = creature

        options = [
            discord.SelectOption(
                label="No Gift Resource",
                value="none",
                emoji="🎁",
                description="Give a gift normally."
            )
        ]

        for item_id, amount in player.inventory.items():

            if amount <= 0:
                continue

            item = RESOURCES[item_id]

            if item["type"] != "shelter":
                continue

            options.append(
                discord.SelectOption(
                    label=f'{item["name"]} x{amount}',
                    value=item_id,
                    emoji=item.get("emoji")
                )
            )

        super().__init__(
            placeholder="Choose a gift...",
            options=options
        )

    async def callback(self, interaction: discord.Interaction):

        gift_item = None

        if self.values[0] != "none":
            item_id = self.values[0]
            gift_item = RESOURCES[item_id]
            self.player.remove_from_inventory(item_id, 1)

        result = gift_creature(self.creature, gift_item, self.player.user_id)

        if not result["success"]:
            return await ctx.send(result["message"])


        save_player(self.player)

        embed = build_gift_embed(creature, result)

        await interaction.response.edit_message(
            embed=embed,
            view=None
        )


class GiftView(discord.ui.View):

    def __init__(self, player, creature):

        super().__init__(timeout=60)

        self.add_item(
            GiftResourceSelect(player, creature)
        )
