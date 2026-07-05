        embed.add_field(
            name="📈 Progress",
            value=progress,
            inline=False
        )

        # Shelter description
        description = generate_shelter_description(creature)

        embed.add_field(
            name="📖 Description",
            value=description,
            inline=False
        )

        # Shelter items
        items = creature.shelter.get("items", [])

        if items:
            item_lines = []

            for entry in items:
                resource = RESOURCES.get(entry["item"], {})

                emoji = resource.get("emoji", "📦")
                name = resource.get(
                    "name",
                    entry["item"].replace("_", " ").title()
                )

                state = entry.get("state", "kept")

                state_icon = {
                    "favorite": "🌟",
                    "kept": "🏡",
                    "ignored": "📦"
                }.get(state, "•")

                item_lines.append(f"{state_icon} {emoji} **{name}**")

            embed.add_field(
                name="🪴 Shelter Items",
                value="\n".join(item_lines),
                inline=False
            )
        else:
            embed.add_field(
                name="🪴 Shelter Items",
                value="*This shelter is empty for now.*",
                inline=False
            )

        await ctx.send(embed=embed)
