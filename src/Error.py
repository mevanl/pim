import discord
import discord.ext.commands as commands


async def command_error_handle(ctx, error: discord.DiscordException):
    if isinstance(error, commands.ConversionError):
        pass
    elif isinstance(error, commands.UserInputError):
        await ctx.send("ERROR!!!!!!!")
    elif isinstance(error, commands.CommandNotFound):
        pass
    elif isinstance(error, commands.CheckFailure):
        pass
    elif isinstance(error, commands.DisabledCommand):
        pass
    elif isinstance(error, commands.CommandInvokeError):
        pass
