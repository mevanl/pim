import discord.ext.commands as commands


class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Current ping: {round(self.bot.latency * 1000, 2)} ms')


async def setup(bot):
    await bot.add_cog(Ping(bot=bot))
