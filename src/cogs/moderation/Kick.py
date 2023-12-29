import discord.ext.commands as commands
from discord import Member


class Kick(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: Member, reason=""):
        await member.kick(reason=reason)
        await ctx.send(f'{member.name} kicked.')


async def setup(bot):
    await bot.add_cog(Kick(bot=bot))
