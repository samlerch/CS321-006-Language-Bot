# sub class of discord bot
import nltk
from discord.ext import commands
class LanguageBot(commands.Bot):
    # test command
    def printTest(self):
        print(f'Working...\n')
    
    # accepts a string and returns a tokenized list of words with parts of speech (pos)
    def parseMessage(self, message):
        pos = nltk.word_tokenize(message)
        pos = nltk.pos_tag(pos)
        return pos