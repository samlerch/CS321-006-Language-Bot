# sub class of discord bot
import nltk
from discord.ext import commands
from BinarySearchTree import BinarySearchTree
from Node import Node
class LanguageBot(commands.Bot):

    # accepts a string and returns a tokenized list of words with parts of speech (pos)
    def parseMessage(self, message):
        pos = nltk.word_tokenize(message)
        pos = nltk.pos_tag(pos)
        return pos
    
    # accepts the context of the the bot and returns a list of strings
    # each string is a message from the user that called it in that channel
    # limit is the maximum number of messages to grab 
    # note that limit=100 may not grab 100 messages if the user has < 100 messages 
    # or other users have messages in between    
    def getChatLogs(self, ctx):
        userMessages = ctx.channel.history(limit=100).flatten()
        return userMessages
    
    # accepts the context of the bot and a list of user messages (strings)
    # returns a bst with each word in the string as a node
    def createBST(self, userMessages, ctx):
        bst = BinarySearchTree()
        for message in userMessages:
            if(ctx.author == message.author):
                parsedMessage = self.parseMessage(message.content)
                for word in parsedMessage:
                    bst.insert(Node(word))
        return bst
    
    # accepts a string and the context of the bot
    # returns synonyms for the string
    def synonyms(self, word, ctx):
        pass
        
    def getWordCount():
        pass
        
    def getWordsCount():
        pass
        
    def getNouns():
        pass
    
    def getVerbs():
        pass
        
    def getAdverbs():
        pass
        
    def getConjunctions():
        pass
        
    def getOther():
        pass