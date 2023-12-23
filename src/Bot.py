import discord
import discord.ext.commands as commands
import os
from dotenv import load_dotenv
import asyncio


intents = discord.Intents.default()
intents.message_content = True
pim = commands.Bot(command_prefix='.', intents=intents, help_command=None)
load_dotenv()


@pim.event
async def on_ready():
    print(f'We have logged in as {pim.user}')


async def load():
    for directory in os.listdir('./cogs'):
        for file in os.listdir('./cogs/' + directory):
            if file.endswith('.py'):
                await pim.load_extension(f'cogs.{directory}.{file[:-3]}')


async def main():
    await load()
    await pim.start(os.getenv('TOKEN'))

asyncio.run(main())
