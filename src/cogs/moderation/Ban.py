import discord.ext.commands as commands
from discord import Member


class Ban(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: Member, reason=""):
        await member.ban(reason=reason)
        await ctx.send(f'{member.name} banned.')


async def setup(bot):
    await bot.add_cog(Ban(bot=bot))
