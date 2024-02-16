import discord
import discord.ext.commands as commands
import os
from dotenv import load_dotenv
import asyncio
from Error import command_error_handle


intents = discord.Intents.default()
intents.message_content = True
pim = commands.Bot(command_prefix='.', intents=intents, help_command=None)
load_dotenv()


@pim.event
async def on_ready():
    print(f'We have logged in as {pim.user}')


@pim.event
async def on_command_error(ctx, error):
    await command_error_handle(ctx, error)

# list of categories containing list of commands
category = {}


# Load all the commands, and get command category types
async def load_cogs():
    for directory in os.listdir('./cogs'):
        category[directory] = []
        for file in os.listdir('./cogs/' + directory):
            if file.endswith('.py'):
                category[directory].append(file)
                await pim.load_extension(f'cogs.{directory}.{file[:-3]}')


async def main():
    await load_cogs()
    await pim.start(os.getenv('TOKEN'))

asyncio.run(main())
