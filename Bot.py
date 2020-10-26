import os
import discord
import nltk
from BinarySearchTree import *
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

# command for testing purposes. 
# prints a bst with a users messages tagged by pos
# call using -words 
@bot.command(name='words', help='testing method')
async def words(ctx):
    await ctx.send('grabbing message history...')
    messages = await bot.getChatLogs(ctx)
    
    bst = bot.createBST(messages, ctx)
    bst.printBST()
    await ctx.send('done!')

bot.run(TOKEN)

# TODO
# caching a users bst?
# create a user class to save there messages
    # maybe unnecessary if we can create bst / parse message history fast enough
# filter by pos
# exception handling
# multiple channels
# images may break ?
# links/audio/other files may break ?
# currently parses commands given to bot. should not do this
# BST only adds to right and prints right