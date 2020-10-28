import nltk
from Node import *

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    # Only inserts values to the right side of BST, testing purposes
    def insert(self, node):
        if(self.root is None):
            self.root = node
            node.color = 1
        else:
            self.insertNode(self.root, node)
            self.recolor(node)
            self.rotate(node)
    
    # if nodes uncle is black or doesnt exist (black) and nodes parent is red and node is not a root
    # finds unbalanced node (if grandparent is missing a child)
    # rotates one of 4 ways
    def rotate(self, cur):
        if(not cur or not cur.parent or not cur.parent.parent):
            return
        if(cur.parent.color == 0 and self.root is not cur):
            if(cur.parent.parent.left and cur.parent.parent.left is not cur.parent):
                if(cur.parent.parent.left.color == 1):
                    print(f'Needs rotation')
            elif(cur.parent.parent.right and cur.parent.parent.right is not cur.parent):
                if(cur.parent.parent.right.color == 1):
                    print(f'Needs rotation')
            elif(not cur.parent.parent.right or not cur.parent.parent.left):
                print(f'Needs rotation')
    
    # right rotation    
    def leftRotation(self, cur):
        pass
                
    # left rotation
    def leftRotation(self, cur):
        pass
    
    # if nodes uncle is red and nodes parent is red and node is not a root
    # changes parent and uncle to black
    # grandparent to red
    def recolor(self, cur):
        if(not cur or not cur.parent or not cur.parent.parent):
            return
        if(cur.parent.color == 0 and self.root is not cur):
            if(cur.parent.parent.left and cur.parent.parent.left is not cur.parent):
                if(cur.parent.parent.left.color == 0):
                    cur.parent.color = 1
                    cur.parent.parent.left.color = 1
                    cur.parent.parent.color = 0
                    self.recolor(cur.parent.parent)
            elif(cur.parent.parent.right and cur.parent.parent.right is not cur.parent):
                if(cur.parent.parent.right.color == 0):
                    cur.parent.color = 1
                    cur.parent.parent.right.color = 1
                    cur.parent.parent.color = 0
                    self.recolor(cur.parent.parent)
            if(self.root.color == 0):
                self.root.color = 1
           
    # helper function for insert
    # allows us to track the current node without needing to have one as an argument in insert
    # cur is the parent / current node
    def insertNode(self, cur, node):
        if(node.word == cur.word):
            cur.count += 1
        # if new node <= cur node
        # if cur.left exists recursively call insert
        # else insert the node at cur.left
        elif(node.word <=  cur.word):
            if(cur.left):
                self.insertNode(cur.left, node)
            else: 
                cur.left = node
                node.parent = cur
        # if new node <= cur node
        # if cur.right exists recursively call insert
        # else insert the node at cur.right        
        elif(node.word > cur.word):
            if(cur.right):
                self.insertNode(cur.right, node)
            else: 
                cur.right = node
                node.parent = cur
        if(node is self.root):
            node.color = 1
   
    # inorder print of bst
    def printBST(self):
        count = 0
        self.printHelper(self.root, count)
    
    # helper function, allows calling of printBST without the root / cur node as an argument      
    def printHelper(self, cur, count):
        if(cur):
            count+=1
            self.printHelper(cur.right, count)
            print(f'{count}. color: {cur.color} value: {cur.word}')
            self.printHelper(cur.left, count)

bst = BinarySearchTree()
bst.insert(Node(15))
bst.insert(Node(20))
bst.insert(Node(10))
bst.insert(Node(25))
bst.insert(Node(5))
bst.insert(Node(3))
#bst.insert(Node(0))
#bst.insert(Node(12))
#bst.insert(Node(18))
#bst.insert(Node(3))
#bst.insert(Node(6))
#bst.insert(Node(19))
bst.printBST()