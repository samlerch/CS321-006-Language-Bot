import nltk
from Node import Node
import random
class RedBlackTree:
    def __init__(self):
        self.root = None
        self.myStr = ''
    
    # Inserts a node to rbt
    def insert(self, node):
        if(self.root is None):
            self.root = node
            node.color = 1
        else:
            self.insertNode(self.root, node)
            self.balanceTree(node)
    
    # re-balances tree after insertion
    def balanceTree(self, node):
        self.recolor(node)
        self.rotate(node)
        if(node.parent and node.parent.parent):
            self.balanceTree(node.parent.parent)
        
    # rotates a node based on its current uncle 
    def rotate(self, cur):
        if(not cur or not cur.parent or not cur.parent.parent):
            return
        # checks that parent is red and cur is not a root
        if(cur.parent.color == 0 and self.root is not cur):
            # runs if curs left uncle is black and cur is the right child of parent
            if(((cur.parent.parent.left and cur.parent.parent.left is not cur.parent) or not cur.parent.parent.left) and cur is cur.parent.right):
                if(not cur.parent.parent.left or (cur.parent.parent.left.color == 1)):
                    print(f'Left Rotation needed')
                    self.leftRotate(cur)
            # runs if curs right uncle is black and cur is the left child of parent
            elif(((cur.parent.parent.right and cur.parent.parent.right is not cur.parent) or not cur.parent.parent.right) and (cur is cur.parent.left)):
                if(not cur.parent.parent.right or (cur.parent.parent.right.color == 1)):
                    print(f'Right Rotation needed')
                    self.rightRotate(cur)
            # runs if curs right uncle is black and cur is the right child of parent
            elif((cur.parent.parent.right and cur.parent.parent.right is not cur.parent) or not cur.parent.parent.right):
                if((not cur.parent.parent.right or (cur.parent.parent.right.color == 1)) and (cur is cur.parent.right)):
                    print(f'Left-Right Rotation needed')
                    self.leftRightRotate(cur)              
            # runs if left uncle is black and cur is the left child of parent
            elif((cur.parent.parent.left and cur.parent.parent.left is not cur.parent) or not cur.parent.parent.left):
                if((not cur.parent.parent.left or (cur.parent.parent.left.color == 1)) and cur is cur.parent.left):
                    print(f'Needs Right-Left rotation')
                    self.rightLeftRotate(cur)
    
    # right rotation
    # grandparent is now right child of parent
    # swap colors of parent and grand parent
    # grandparents left child is now parents right child   
    def rightRotate(self, cur):
        # swap color of parent and grandparent
        tempCol = cur.parent.color
        cur.parent.color = cur.parent.parent.color
        cur.parent.parent.color = tempCol
        
        # if great grandparent exists sets its child to cur parent
        if(cur.parent.parent.parent):
            if(cur.parent.parent.parent.right and (cur.parent.parent.parent.right is not cur.parent.parent)):     
                cur.parent.parent.parent.left = cur.parent
            elif(cur.parent.parent.parent.left and (cur.parent.parent.parent.left is not cur.parent.parent)):
                cur.parent.parent.parent.right = cur.parent
                
        # ol switcheroo
        tempNode = cur.parent.right
        cur.parent.right = cur.parent.parent
        cur.parent.parent = cur.parent.parent.parent
        cur.parent.right.parent = cur.parent
        cur.parent.right.left = tempNode
        if(cur.parent.right is self.root):
            self.root = cur.parent
        
                
    # left rotation
    def leftRotate(self, cur):
        # swap color of parent and grandparent
        tempCol = cur.parent.color
        cur.parent.color = cur.parent.parent.color
        cur.parent.parent.color = tempCol
        
        # if great grandparent exists sets its child to cur parent
        if(cur.parent.parent.parent):
           if(cur.parent.parent.parent.right and (cur.parent.parent.parent.right is not cur.parent.parent)):     
                cur.parent.parent.parent.left = cur.parent
           elif(cur.parent.parent.parent.left and (cur.parent.parent.parent.left is not cur.parent.parent)):
                cur.parent.parent.parent.right = cur.parent
        # ol switcheroo
        tempNode = cur.parent.left
        cur.parent.left = cur.parent.parent
        cur.parent.parent = cur.parent.parent.parent
        cur.parent.left.parent = cur.parent
        cur.parent.left.right = tempNode
        if(cur.parent.left is self.root):
            self.root = cur.parent
            
    # left right rotation       
    def leftRightRotate(self, cur):
        cur.parent.right = None
        cur.parent.parent.left = cur
        cur.left = cur.parent
        cur.parent = cur.parent.parent
        cur.left.parent = cur
        self.rightRotate(cur.left)
    
    # right left rotation
    def rightLeftRotate(self, cur):
        cur.parent.left = None
        cur.parent.parent.right = cur
        cur.right = cur.parent
        cur.parent = cur.parent.parent
        cur.right.parent = cur
        self.leftRotate(cur.right)
        
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
            elif(cur.parent.parent.right and cur.parent.parent.right is not cur.parent):
                if(cur.parent.parent.right.color == 0):
                    cur.parent.color = 1
                    cur.parent.parent.right.color = 1
                    cur.parent.parent.color = 0
            if(self.root.color == 0):
                self.root.color = 1
           
    # helper function for insert
    # allows us to track the current node without needing to have one as an argument in insert
    # cur is the parent / current node
    def insertNode(self, cur, node):
        if(node.word == cur.word):
            cur.count += 1
            
        elif(node.word <=  cur.word):
            if(cur.left):
                self.insertNode(cur.left, node)
            else: 
                cur.left = node
                node.parent = cur
                
        elif(node.word > cur.word):
            if(cur.right):
                self.insertNode(cur.right, node)
            else:
                cur.right = node
                node.parent = cur
                
        if(node is self.root):
            node.color = 1
   
    # inorder print of rbt
    def printRBT(self):
        count = 0
        self.printHelper(self.root, count)
    
    # helper function, allows calling of printRBT without the root / cur node as an argument      
    def printHelper(self, cur, count):
        if(cur):
            count+=1
            self.printHelper(cur.right, count)
            print(f'Level {count}. color: {cur.color} value: {cur.word}')
            self.printHelper(cur.left, count)
            
    def __str__(self):
        count = 0
        self.toString(self.root)
        temp = self.myStr
        self.myStr = ''
        return temp
    
    # converts the rbt to a readable string
    def toString(self, cur):
        if(cur):
            self.toString(cur.right)
            self.myStr += '\n' + "Word: " + str(cur.word)
            self.myStr += " | Count: " + str(cur.count)
            self.toString(cur.left)