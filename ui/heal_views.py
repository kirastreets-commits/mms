import discord

from data.resources import RESOURCES

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
                    emoji=item.get("emoji")
                )
            )

        super().__init__(
            placeholder="Choose a healing resource...",
            options=options
        )

        async def callback(self, interaction):

            healing_item = None

            if self.values[0] != "none":

                item_id = self.values[0]

                healing_item = ITEMS[item_id]

                self.player.remove_item(item_id, 1)

            result = self.creature.heal(healing_item)

            save_player(self.player)

            embed = render_action_embed(
                title="🩹 Healing Session",
                creature=self.creature,
                result=result,
                action_text=f"You carefully tend to **{self.creature.name}**."
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
