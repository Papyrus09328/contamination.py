import discord

from discord.ext import commands

intents = discord.Intents.default()
intents.message_contents = True

bot = commands.Bot(commands_prefix= '$', intents=intents)

@bot.event
async def on_ready():
    print(f' en que puedo ayudarte?')
