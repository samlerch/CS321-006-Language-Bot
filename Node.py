# node class for RBT
# holds the word itself, word count, part of speech
import nltk

# red is 0 black is 1
class Node:
    def __init__(self, word):
        self.left = None
        self.right = None
        self.word = word
        self.count = 1
        self.color = 0
        self.parent = None
        
    def getWord(self):
        return self.word
    
    def getCount(self):
        return self.count
