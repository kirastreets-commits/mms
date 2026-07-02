import discord

from data.resources import RESOURCES
from models import creature, player
from systems.action_renderer import render_action_embed
from systems.gift_system import apply_gift_outcome, build_gift_embed, gift_creature, give_item
from systems.memory_system import update_memory
from systems.save_system import save_player
from models.player import remove_from_inventory

class GiftResourceSelect(discord.ui.Select):

    def __init__(self, player, creature):

        self.player = player
        self.creature = creature

        options = [
            discord.SelectOption(
                label="No Gift Resource",
                value="none",
                emoji="🎁",
                description="Do not give a gift."
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

        self.player = player
        gift_item = None

        if self.values[0] != "none":
            item_id = self.values[0]
            gift_item = RESOURCES[item_id]
            self.player.remove_from_inventory(item_id, 1)

        # reaction
        result = give_item(creature, item_id, player.user_id)

        # apply world changes
        apply_gift_outcome(creature, item_id, result)

        # memory system
        update_memory(creature, "gift", result)

        return {
            "success": True,
            **result
        }

        save_player(self.player)

        embed = build_gift_embed(creature, result)




class GiftView(discord.ui.View):

    def __init__(self, player, creature):

        super().__init__(timeout=60)

        self.add_item(
            GiftResourceSelect(player, creature)
        )
