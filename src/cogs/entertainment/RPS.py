import discord.ext.commands as commands
import random

rps = ['Rock!', 'Paper!', 'Scissors']


class RPS(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def rps(self, ctx, userChoice: str):
        pimChoice: str = random.choice(rps)
        await ctx.send(f'{pimChoice}')

        # same choice
        if pimChoice[0].lower() == userChoice[0].lower():
            await ctx.send('***We tied!***')
            return

        # pim chose rock
        if pimChoice[0].lower() == 'r' and userChoice[0].lower() == 'p':
            await ctx.send('***You won!***')
            return

        if pimChoice[0].lower() == 'r' and userChoice[0].lower() == 's':
            await ctx.send('***You lost!***')
            return

        # pim chose scissors
        if pimChoice[0].lower() == 's' and userChoice[0].lower() == 'r':
            await ctx.send('***You won!***')
            return

        if pimChoice[0].lower() == 's' and userChoice[0].lower() == 'p':
            await ctx.send('***You lost!***')
            return

        # pim chose paper
        if pimChoice[0].lower() == 'p' and userChoice[0].lower() == 's':
            await ctx.send('***You won!***')
            return

        if pimChoice[0].lower() == 'p' and userChoice[0].lower() == 'r':
            await ctx.send('***You lost!***')
            return


async def setup(bot):
    await bot.add_cog(RPS(bot=bot))
