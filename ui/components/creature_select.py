import discord


class CreatureSelectView(discord.ui.View):
    def __init__(self, creatures, on_select_callback, user_id):
        super().__init__(timeout=120)

        self.creatures = creatures
        self.on_select_callback = on_select_callback
        self.user_id = user_id

        options = [
            discord.SelectOption(
                label=c.name,
                value=c.name,
                description=f"Lvl {getattr(c, 'level', '?')}"
            )
            for c in creatures
        ]

        self.add_item(CreatureSelect(options))
