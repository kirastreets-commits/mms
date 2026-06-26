import discord


class BaseNPCView(discord.ui.View):
    def __init__(self, npc, user_id):
        super().__init__(timeout=180)
        self.npc = npc
        self.user_id = user_id
