import os
import discord
import nltk
from RedBlackTree import RedBlackTree
from discord.ext import commands
from dotenv import load_dotenv
from LanguageBot import LanguageBot

load_dotenv("bot.env") # name of env file goes here
TOKEN=os.getenv('DISCORD_TOKEN') # bot token is in env file
GUILD=os.getenv('DISCORD_GUILD') # guild token is in env file

# prefix used before all commands
bot = LanguageBot(command_prefix='-')

print(f'Connecting...')
  
# Checks if bot connected to discord
@bot.listen()
async def on_ready():
    print(f'{bot} has connected to {bot.guilds}')

# sends an embed to discord with the users nouns sorted by count
@bot.command(name='nouns', help='prints users nouns')
async def nouns(ctx):
    userLogs = await bot.getLogs(ctx)
    nouns = bot.getNouns(userLogs, ctx)
    await ctx.send(embed=bot.createEmbed('Nouns', nouns))

# sends an embed to discord with the users pronouns sorted by count
@bot.command(name='pronouns', help='prints users pronouns')
async def pronouns(ctx):
    userLogs = await bot.getLogs(ctx)
    pronouns = bot.getPronouns(userLogs, ctx)
    await ctx.send(embed=bot.createEmbed('Pronouns', pronouns))

bot.run(TOKEN)
