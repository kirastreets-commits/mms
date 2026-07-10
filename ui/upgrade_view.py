import discord

from data.preserves import PRESERVES

from systems.save_system import save_player
from systems.preserve_system import (
    restoration_required,
    can_upgrade_preserve,
    upgrade_preserve
)


class UpgradeView(discord.ui.View):

    def __init__(self, player, preserve_id):
        super().__init__(timeout=120)

        self.player = player
        self.preserve_id = preserve_id

        preserve = player.preserves[preserve_id]
        data = PRESERVES[preserve_id]

        # Disable the button if max level or not enough restoration
        if (
            preserve["level"] >= data["max_level"]
            or not can_upgrade_preserve(player, preserve_id)
        ):
            self.upgrade_button.disabled = True

    def build_embed(self):

        preserve = self.player.preserves[self.preserve_id]
        data = PRESERVES[self.preserve_id]

        level = preserve["level"]
        max_level = data["max_level"]

        embed = discord.Embed(
            title=f"{data['emoji']} {data['name']}",
            description=data["description"],
            colour=discord.Colour.green()
        )

        embed.add_field(
            name="Current Level",
            value=f"Level {level}/{max_level}",
            inline=True
        )

        embed.add_field(
            name="Capacity",
            value=f"{3 + ((level - 1) * 2)} creatures",
            inline=True
        )

        embed.add_field(
            name="Restoration",
            value=f"{preserve['restoration']} points",
            inline=True
        )

        # --------------------------
        # MAX LEVEL
        # --------------------------

        if level >= max_level:

            embed.add_field(
                name="Status",
                value="🏆 This preserve has been fully restored.",
                inline=False
            )

            return embed

        next_level = level + 1

        required = restoration_required(next_level)

        project = data["upgrade_projects"][next_level]
        bonus = data["upgrade_bonuses"][next_level]

        embed.add_field(
            name="Current Project",
            value=(
                f"**{project['title']}**\n"
                f"{project['description']}"
            ),
            inline=False
        )

        embed.add_field(
            name="Progress",
            value=f"{preserve['restoration']} / {required} Restoration",
            inline=True
        )

        rewards = [
            f"+{bonus['capacity']} Capacity",
            f"+{bonus['comfort']} Comfort"
        ]

        if "resource_bonus" in bonus:
            rewards.append(
                f"+{bonus['resource_bonus']}% Resources"
            )

        if "rare_event_bonus" in bonus:
            rewards.append(
                f"+{bonus['rare_event_bonus']}% Rare Events"
            )

        if "bond_bonus" in bonus:
            rewards.append(
                f"+{bonus['bond_bonus']} Daily Bond"
            )

        embed.add_field(
            name="Rewards",
            value="\n".join(rewards),
            inline=False
        )

        return embed

    @discord.ui.button(
        label="Upgrade Preserve",
        emoji="⬆️",
        style=discord.ButtonStyle.green
    )
    async def upgrade_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        if str(interaction.user.id) != str(self.player.user_id):
            return await interaction.response.send_message(
                "This isn't your menu.",
                ephemeral=True
            )

        if not can_upgrade_preserve(
            self.player,
            self.preserve_id
        ):
            return await interaction.response.send_message(
                "This preserve isn't ready to upgrade yet.",
                ephemeral=True
            )

        upgrade_preserve(
            self.player,
            self.preserve_id
        )

        save_player(self.player)

        # Disable button if we've reached max level or no longer have enough restoration
        preserve = self.player.preserves[self.preserve_id]
        data = PRESERVES[self.preserve_id]

        if (
            preserve["level"] >= data["max_level"]
            or not can_upgrade_preserve(
                self.player,
                self.preserve_id
            )
        ):
            button.disabled = True

        await interaction.response.edit_message(
            content="✨ The restoration project has been completed!",
            embed=self.build_embed(),
            view=self
        )