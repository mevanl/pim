import discord.ext.commands as commands


class Avatar(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx):
        await ctx.send(f'{ctx.author.avatar}')


async def setup(bot):
    await bot.add_cog(Avatar(bot=bot))
