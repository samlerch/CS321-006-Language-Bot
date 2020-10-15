import os
import discord

from dotenv import load_dotenv

load_dotenv("language_bot.env") # name of env file goes here
TOKEN=os.getenv('DISCORD_TOKEN') # bot token is in env file
GUILD=os.getenv('DISCORD_GUILD') # guild token is in env file
client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{client.user} is connected to the following guild: \n'
        f'{guild.name}(id: {guild.id})')
            
    print(f'{client.user} has connected to discord!')
    
client.run(TOKEN)