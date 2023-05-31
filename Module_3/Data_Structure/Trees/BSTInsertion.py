#BST Insertion
'''
Start from the root node.
Check value to to be inserted is greater than the root/current node's value
If yes, then repeat the steps above for the right subtree, if not, then repeat for the left subtree
Repeat untill you find a node that has no right/left child to move into. Insert the given value there and update the parent node accordingly.

'''
# BST insertion can done using:
# 1. Iteratively    2. Rercursively

# using iterative approach
class Node:
    def __init__(self, value):
        self.value = value
        self.leftchild = None
        self.rightchild = None
    def insert(self,value):
        current = self
        parent = None
        while current:
            parent = current
            if value <= current.value:
                current = current.leftchild
            elif value > current.value:
                current = current.rightchild
        if value < parent.value:
            parent.leftchild = Node(value)
        else:
            parent.rightchild = Node(value)
class BinarySearchTree:
    def __init__(self,value):
        self.root = Node(value)
    def insert(self,value):
        if self.root:
            return self.root.insert(value)
        else:
            self.root = Node(value)
            return True
BST = BinarySearchTree(50)
BST.insert(70)
BST.insert(13)
print(BST.root.leftchild.value)

# using Recursive Approach

class Nod:
    def __init__(self,value):
        self.value = value
        self.leftchild = None
        self.rightchild = None
    def insert(self, value):
        if value < self.value:
            if self.leftchild:
                self.leftchild.insert(value)
            else:
                self.leftchild = Nod(value)
                return 
        if value > self.value:
            if self.rightchild:
                self.rightchild.insert(value)
            else:
                self.rightchild = Nod(value)
                return
class BSTree:
    def __init__(self,value): 
        self.root = Nod(value)
    def insert(self,value):
        if self.root:
            return self.root.insert(value)
        else:
            self.root = Nod(value)
            return
bst = BSTree(11)
bst.insert(19)
bst.insert(8)
bst.insert(9)
print(bst.root.leftchild.rightchild.value)

