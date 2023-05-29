# Binary search Tree
'''
A binary search tree is type of binary tree in which all nodes of tree has key-value pairs.
For All nodes in BST, the values of keys in left subtree of node is less than the value of node themselves. All keys in the right subtree have greter values than node.
This is reffered as the BST Rule.
NodeValue(Leftsubtree) <= NodeValue(Current) < NodeValue(RightSubtree)
'''

# Implementing a Binary Search tree
'''
To implement BST, first we need a Node class
A node class should have a value, a left child, a right child, a prent 
'''
class Node:
    def __init__(self,val): # Constructor to intialize the value of the node
        self.val = val
        self.leftchild = None  
        self.rightchild = None
        self.parent = None
# Binary serach tree class
class BinarySearchTree:
    def __init__(self, val): # intializes a root node
        self.root = Node(val)
BST = BinarySearchTree(6)
print(BST.root.val)