# sub class of discord bot
import nltk
import discord
from discord.ext import commands
from RedBlackTree import RedBlackTree
from Node import Node
class LanguageBot(commands.Bot):

    # accepts a string and returns a tokenized list of 2-tuples with parts of speech (pos)
    def parseMessage(self, message):
        pos = nltk.word_tokenize(message)
        pos = nltk.pos_tag(pos)
        return pos
        
    # returns a list of messages. each message consists of one or more 2-tuples consisting of a word and pos
    async def getLogs(self, ctx):
        userLogs = self.tagLogs(await ctx.channel.history(limit=1000).flatten(), ctx)
        return userLogs
    
    # accepts a list of strings and returns a list of 
    def tagLogs(self, userMessages, ctx):
        userLogs = []
        for message in userMessages:
            if(ctx.author == message.author):
                userLogs.append(self.parseMessage(message.content))
        return userLogs
    
    # accepts the context of the bot and a list of user messages (strings) and a pos
    # inserts a node for each word that matches the pos
    # returns a rbt
    def createRBT(self, userLogs, pos, ctx):
        rbt = RedBlackTree()
        for message in userLogs:
            for word in message:
                if(word[1] == pos):
                    rbt.insert(Node(word[0]))                 
        return rbt

    # accepts a title(part of speech) and a rbt to create an embed with a users most used words
    def createEmbed(self, mTitle, rbt):
        embed = discord.Embed(title = mTitle, description = '', colour = discord.Colour.green())
        list = rbt.toList()
        count = ''
        word = ''
        for node in list:
            count += str(node.count) + '\n'
            word += str(node.word) + '\n'
        embed.add_field(name='Word', value = word, inline = True)
        embed.add_field(name='Count', value = count, inline = True)
        return embed
    
    # accepts a string and the context of the bot
    # returns synonyms for the string
    def synonyms(self, word, ctx):
        pass
        
    def getWordCount():
        pass
        
    def getWordsCount():
        pass
        
    def getNouns(self, userMessages, ctx):
        nouns = self.createRBT(userMessages, "NN", ctx)
        return nouns
    
    def getVerbs():
        pass
        
    def getAdverbs():
        pass
        
    def getConjunctions():
        pass
    
    def getAdpositions():
        pass
        
    def getArticles():
        pass
        
    def getNumerals():
        pass
    
    def getParticle():
        pass
        
    def getPronouns(self, userMessages, ctx):
        pronouns = self.createRBT(userMessages, "NNP", ctx)
        return pronouns
            
    def getOthers():
        pass