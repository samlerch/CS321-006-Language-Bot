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

# sends an embed to discord with the users verbs sorted by count
@bot.command(name='verbs', help='prints users verbs')
async def verbs(ctx):
    userLogs = await bot.getLogs(ctx)
    verbs = bot.getVerbs(userLogs, ctx)
    await ctx.send(embed=bot.createEmbed('Verbs', verbs))

@bot.command(name='adverbs', help='prints users adverbs')
async def adverbs(ctx):
    userLogs = await bot.getLogs(ctx)
    adverbs = bot.getAdverbs(userLogs, ctx)
    await ctx.send(embed=bot.createEmbed('Adverbs', adverbs))

@bot.command(name='adjectives', help='prints users adjectives')
async def adjectives(ctx):
    userLogs = await bot.getLogs(ctx)
    adjectives = bot.getAdjectives(userLogs, ctx)
    await ctx.send(embed=bot.createEmbed('Adjectives', adjectives))

@bot.command(name='conjunctions', help='prints users conjunctions')
async def conjunctions(ctx):
    userLogs = await bot.getLogs(ctx)
    conjunctions = bot.getConjunctions(userLogs, ctx)
    await ctx.send(embed=bot.createEmbed('Conjunctions', conjunctions))

@bot.command(name='adpositions', help='prints users adpositions')
async def adpositions(ctx):
    userLogs = await bot.getLogs(ctx)
    adpositions = bot.getAdpositions(userLogs, ctx)
    await ctx.send(embed=bot.createEmbed('Adpositions', adpositions))

@bot.command(name='articles', help='prints users articles')
async def articles(ctx):
    userLogs = await bot.getLogs(ctx)
    articles = bot.getArticles(userLogs, ctx)
    await ctx.send(embed=bot.createEmbed('Articles', articles))

@bot.command(name='numerals', help='prints users numerals')
async def numerals(ctx):
    userLogs = await bot.getLogs(ctx)
    numerals = bot.getNumerals(userLogs, ctx)
    await ctx.send(embed=bot.createEmbed('Numerals', numerals))

@bot.command(name='particles', help='prints users particles')
async def particles(ctx):
    userLogs = await bot.getLogs(ctx)
    particles = bot.getParticles(userLogs, ctx)
    await ctx.send(embed=bot.createEmbed('Particles', particles))

@bot.command(name='others', help='prints users other parts of speech')
async def others(ctx):
    userLogs = await bot.getLogs(ctx)
    others = bot.getOthers(userLogs, ctx)
    await ctx.send(embed=bot.createEmbed('Others', others))


@bot.command(name='synonyms', help='prints synonyms for most used words')
async def synonyms(ctx, arg = 10):
	userLogs = await bot.getLogs(ctx)
	synonyms = bot.synonyms(userLogs, int(arg), ctx)
	await ctx.send(embed=bot.createSynonymEmbed('Synonyms', synonyms, int(arg)))


@bot.command(name='emulate', help='prints users other parts of speech')
async def emulate(ctx):
    userLogs = await bot.getLogs(ctx)
    
    #others = bot.getOthers(userLogs, ctx)
    synonym = bot.createGrammar(ctx)
    await ctx.send(synonym)

# sends an embed to discord with synonyms for the users most used words
# Prints the top 10 most used words by default
# enter a number after the command to print up to that many word
@bot.command(name='mostused', help='prints users other parts of speech')
async def mostUsed(ctx, arg = 10):
    userLogs = await bot.getLogs(ctx)
    mostUsed = bot.getMostUsedWords(userLogs, ctx)
    await ctx.send(embed=bot.createEmbed('Most Used', mostUsed, int(arg)))

@bot.command(name='search', help='searches for a word and prints how many times the word has been used')
async def search(ctx, arg):
    userLogs = await bot.getLogs(ctx)
    searched = bot.getWordCount(userLogs, ctx, arg)
    await ctx.send(embed=bot.createEmbedNode('Search result', searched, arg))

@bot.command()
async def print(ctx):
    userLogs = await bot.printLog(ctx)
    await ctx.send(userLogs)

bot.run(TOKEN)
