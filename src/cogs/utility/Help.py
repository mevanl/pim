import discord.ext.commands as commands
from Bot import category


class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        msg: str = ''
        for key in category:
            msg += f'**{key}**:\n'
            for command in category[key]:
                msg += f'{command}, '
            msg += '\n'

        await ctx.send(msg)


async def setup(bot):
    await bot.add_cog(Help(bot=bot))
