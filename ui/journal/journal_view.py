import discord

from ui.journal.journal_pages import (
    get_entries_by_category
)


class JournalHomeView(discord.ui.View):

    def __init__(self, player):
        super().__init__(timeout=60)

        self.player = player


    @discord.ui.button(
        label="📜 Lore",
        style=discord.ButtonStyle.primary
    )
    async def lore(
        self,
        interaction,
        button
    ):

        await self.open_category(
            interaction,
            "lore"
        )


    @discord.ui.button(
        label="🐾 Creatures",
        style=discord.ButtonStyle.success
    )
    async def creatures(
        self,
        interaction,
        button
    ):

        await self.open_category(
            interaction,
            "adoption"
        )


    @discord.ui.button(
        label="❤️ Bonds",
        style=discord.ButtonStyle.danger
    )
    async def bonds(
        self,
        interaction,
        button
    ):

        await self.open_category(
            interaction,
            "bond"
        )


    @discord.ui.button(
        label="🏡 Sanctuary",
        style=discord.ButtonStyle.secondary
    )
    async def sanctuary(
        self,
        interaction,
        button
    ):

        await self.open_category(
            interaction,
            "shelter"
        )


    async def open_category(
        self,
        interaction,
        category
    ):

        view = JournalCategoryView(
            self.player,
            category
        )

        embed = view.build_embed()

        await interaction.response.edit_message(
            embed=embed,
            view=view
        )
        

class JournalCategoryView(discord.ui.View):

    def __init__(
        self,
        player,
        category,
        page=0
    ):

        super().__init__(timeout=60)

        self.player = player
        self.category = category
        self.page = page


    def build_embed(self):

        from ui.journal.journal_pages import (
            get_entries_by_category,
            paginate,
            format_entry
        )


        entries = get_entries_by_category(
            self.player,
            self.category
        )

        page_entries = paginate(
            entries,
            self.page
        )


        if not page_entries:

            description = (
                "No memories have been recorded yet."
            )

        else:

            description = "\n\n".join(
                format_entry(entry)
                for entry in page_entries
            )


        return discord.Embed(
            title=f"📖 {self.category.title()} Journal",
            description=description,
            color=0x6b8e23
        )


    @discord.ui.button(
        label="⬅ Previous",
        style=discord.ButtonStyle.secondary
    )
    async def previous(
        self,
        interaction,
        button
    ):

        if self.page > 0:
            self.page -= 1

        await interaction.response.edit_message(
            embed=self.build_embed(),
            view=self
        )


    @discord.ui.button(
        label="Next ➡",
        style=discord.ButtonStyle.secondary
    )
    async def next(
        self,
        interaction,
        button
    ):

        self.page += 1

        await interaction.response.edit_message(
            embed=self.build_embed(),
            view=self
        )