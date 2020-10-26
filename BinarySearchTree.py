import nltk
from Node import *

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    # Only inserts values to the right side of BST, testing purposes
    def insert(self, node):
        if(self.root is None):
            self.root = node
        else:
            self.insertNode(self.root, node)
    
    # helper function for insert
    # allows us to track the current node without needing to have one as an argument in insert
    def insertNode(self, cur, node):
        if(cur.right is None):
            cur.right = node
        else:
            cur = cur.right
            self.insertNode(cur, node)
    
    # currently prints all right values of a BST
    def printBST(self):
        count = 0
        self.printHelper(self.root, count)
    
    # helper function, allows calling of printBST without the root       
    def printHelper(self, cur, count):
        if(cur is None):
            return
        count += 1
        print(f'{count}. {cur.word}')
        return self.printHelper(cur.right, count)
