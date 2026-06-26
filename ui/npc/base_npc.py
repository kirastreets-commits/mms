import discord


class BaseNPC:
    def __init__(self, name, title, description, color=discord.Color.green()):
        self.name = name
        self.title = title
        self.description = description
        self.color = color

    # -------------------------
    # Embed builder (shared)
    # -------------------------
    def build_embed(self, dialogue: str):
        embed = discord.Embed(
            title=self.title,
            description=dialogue,
            color=self.color
        )
        return embed

    # -------------------------
    # Open NPC UI
    # -------------------------
    async def open(self, ctx, view):
        embed = self.build_embed(self.description)
        await ctx.send(embed=embed, view=view)
