import discord
from discord.ext import commands
from config import settings

bot = commands.Bot(command_prefix=settings['prefix'])


@bot.command()
async def phil(ctx):
    await ctx.send('Всех приветсвую на этом сервере!')


bot.run(settings['token'])
