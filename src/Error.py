import discord
import discord.ext.commands as commands


async def command_error_handle(ctx, error: discord.DiscordException):
    
    # If need more control over errors, can edit here
    #if isinstance(error, commands.ConversionError):
        #pass
    #elif isinstance(error, commands.UserInputError):
        #pass
    #elif isinstance(error, commands.CommandNotFound):
        #pass
    #elif isinstance(error, commands.CheckFailure):
        #pass
    #elif isinstance(error, commands.DisabledCommand):
        #pass
    #elif isinstance(error, commands.CommandInvokeError):
        #pass

    await ctx.send(error)
