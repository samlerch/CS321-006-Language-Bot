# sub class of discord bot
import nltk
import discord
from discord.ext import commands
from RedBlackTree import RedBlackTree
from Node import Node
from nltk.corpus import wordnet
from nltk.parse.generate import generate, demo_grammar
from nltk import CFG
class LanguageBot(commands.Bot):

    # accepts a string and returns a tokenized list of 2-tuples with parts of speech (pos)
    def parseMessage(self, message):
        pos = nltk.word_tokenize(message)
        pos = nltk.pos_tag(pos, tagset = 'universal')
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
    def createRBT(self, userLogs, ctx, *pos):
        rbt = RedBlackTree()
        for message in userLogs:
            for word in message:
                if(word[1] in pos):
                    rbt.insert(Node(word[0]))                 
        return rbt

    # accepts a pos and a rbt to create an embed with a users most used words
    #prints number of words up to numPrint. Default -1 prints all words
    def createEmbed(self, pos, rbt, numPrint = -1):
        if rbt.isEmpty():
            embed = discord.Embed(title = pos, description = 'No ' + pos, colour = discord.Colour.green())
            return embed
        list = rbt.toList()
        embed = discord.Embed(title = pos, description = '', colour = discord.Colour.green())
        count = ''
        word = ''
        i = 0
        for node in list:
            if (i == numPrint):
                break
            count += str(node.count) + '\n'
            word += str(node.word) + '\n'
            i+=1
        embed.add_field(name='Word', value = word, inline = True)
        embed.add_field(name='Count', value = count, inline = True)
        return embed

    def createSynonymEmbed(self, pos, lists, numPrint = -1):
        
        
        embed = discord.Embed(title = pos, description = '', colour = discord.Colour.green())
        synonym = ''
        word = ''
        i = 0
        for node in lists[0]:
            if (i == numPrint):
                break
            word += str(node.word) + '\n'
            synonym += str(lists[1][i]) + '\n'
            i+=1
        embed.add_field(name='Word', value = word, inline = True)
        embed.add_field(name='Synonym', value = synonym, inline = True)
        return embed
    
    # accepts a string and the context of the bot
    # returns synonyms for the string
    def synonyms(self, userMessages, numPrint, ctx):
        mostUsedWords = self.getMostUsedWords(userMessages, ctx)
        mostUsedList = mostUsedWords.toList()
        numPrint = int(numPrint)
        i = 0
        syns = list()
        for node in mostUsedList:
            syns.append(self.getSynonym(str(node.word), ctx))
        return (mostUsedList, syns)

    def getSynonym(self, word, ctx, numSynonyms = 5):
        synset = wordnet.synsets(word)
        try:
            for syn in synset:
                for lemma in syn.lemmas():
                    if (word != lemma.name()):
                        return(lemma.name())
            #syns.append(synset[0].lemmas()[].name())
        except:
            return("none")

    def getMostUsedWords(self, userMessages, ctx):
        mostUsedWords = self.createRBT(userMessages, ctx, 'NOUN', 'VERB', 'ADV', 'ADJ', 'CONJ', 'ADP', 'DET', 'PRT', 'PRON', 'X')
        return mostUsedWords
        
    def getWordCount():
        pass
        
    def getWordsCount():
        pass
        
    def getNouns(self, userMessages, ctx):
        nouns = self.createRBT(userMessages, ctx, "NOUN")
        return nouns
    
    def getVerbs(self, userMessages, ctx):
        verbs = self.createRBT(userMessages, ctx, 'VERB')
        return verbs
        
    def getAdverbs(self, userMessages, ctx):
        adjectives = self.createRBT(userMessages, ctx, 'ADV')
        return adjectives
        
    def getConjunctions(self, userMessages, ctx):
        conjunctions = self.createRBT(userMessages, ctx, "CONJ")
        return conjunctions
    
    def getAdpositions(self, userMessages, ctx):
        adpositions = self.createRBT(userMessages, ctx, "ADP")
        return adpositions
        
    def getArticles(self, userMessages, ctx):
        articles = self.createRBT(userMessages, ctx, "DET")
        return articles
        
    def getNumerals(self, userMessages, ctx):
        numerals = self.createRBT(userMessages, ctx, "NUM")
        return numerals
    
    def getParticles(self, userMessages, ctx):
        particles = self.createRBT(userMessages, ctx, "PRT")
        return particles
        
    def getPronouns(self, userMessages, ctx):
        pronouns = self.createRBT(userMessages, ctx, 'PRON')
        return pronouns

    def getAdjectives(self, userMessages, ctx):
        adjectives = self.createRBT(userMessages, ctx, 'ADJ')
        return adjectives
            
    def getOthers(self, userMessages, ctx):
        others = self.createRBT(userMessages, ctx, "X")
        return others


    def createGrammar(self, ctx):
        rules=list()
        ruleset = set(rule for tree in nltk.corpus.treebank.parsed_sents()[:10] 
           for rule in tree.productions())
        for rule in ruleset:
            print(type(rule))
        S = nltk.Nonterminal('S')
        grammar = nltk.induce_pcfg(S, ruleset)
        #grammar = CFG.fromstring(demo_grammar)
        for sentence in generate(grammar, n=10):
             return(' '.join(sentence))