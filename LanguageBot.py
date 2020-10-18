import os
import discord
import nltk
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv("bot.env") # name of env file goes here
TOKEN=os.getenv('DISCORD_TOKEN') # bot token is in env file
GUILD=os.getenv('DISCORD_GUILD') # guild token is in env file

# prefix used before all commands
bot = commands.Bot(command_prefix='-')

# accepts a string and returns a tokenized list of words with parts of speech (pos)
def parseMessage(message):
    pos = nltk.word_tokenize(message)
    pos = nltk.pos_tag(pos)
    return pos
    
    
# connection from bot to client
@bot.listen()
async def on_ready():
    print(f'{bot} has connected to {bot.guilds}')

# bot command prints users 100 most recent messages
# call using -words 
@bot.command(name='words', help='provides a users top 10 words')
async def words(ctx):
    await ctx.send('grabbing message history...')
    messages = await ctx.channel.history(limit=100).flatten()
    counter = 0
    for message in messages:
        if(ctx.author == message.author):
            print(f'{counter}. {parseMessage(message.content)}')
            counter += 1

bot.run(TOKEN)

# TODO
# exception handling
# multiple channels