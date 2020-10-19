# node class for BST
# holds the word itself, word count, part of speech
import nltk

class Node:
    def __init__(self, word):
        self.left = None
        self.right = None
        self.word = word
        self.count = 0
        
    def getWord(self):
        return self.word
    
    def getCount(self):
        return self.count
