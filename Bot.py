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

bot.printTest()    
# connection from bot to client
@bot.listen()
async def on_ready():
    print(f'{bot} has connected to {bot.guilds}')

# bot command prints users 100 most recent messages
# call using -words 
@bot.command(name='words', help='provides a users top 10 words')
async def words(ctx):
    await ctx.send('grabbing message history...')
    messages = await ctx.channel.history().flatten()
    
    bst = BinarySearchTree()
    counter = 0
    
    # breaks apart a message into words with part of speech tags.
    for message in messages:
        if(ctx.author == message.author):
            words = bot.parseMessage(message.content)
            for word in words:
                bst.insert(Node(word))
    bst.printBST()
    await ctx.send('done!')
    
bot.run(TOKEN)

# TODO
# exception handling
# multiple channels
# images may break ?
# links/audio/other files may break ?
# currently parses commands given to bot. should not do this
# BST only adds to right and prints right