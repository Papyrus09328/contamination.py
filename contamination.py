import discord

from discord.ext import commands

intents = discord.Intents.default()
intents.message_contents = True

bot = commands.Bot(commands_prefix= '$', intents=intents)

@bot.event
async def on_ready():
    print(f'En que puedo ayudarte? {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f' dime que necesitas saber sobre la contaminacion {bot.user}')
