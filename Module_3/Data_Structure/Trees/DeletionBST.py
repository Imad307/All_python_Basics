'''
There could be 4 scenarios for deletion in a binary search tree. 

1. Deleting in an empty tree:
   if a tree is empty then return None or False. This is the edge case for error handling

2. Deleting a node with no children, i.e., a leaf node.
   When the node to be deleted is a leaf node in a Binary Search Tree, we simply remove that leaf node. We do this by making the parent node’s left or right child 
   (whichever one the leaf node was) None. 
   
3. Deleting a node which has one child only
i. Deleting a node which has a right child only
ii.Deleting a node which has a left child only
   We search for the node, once the node is found we check if and how many children it has. If it has only one child, we check the parent node to see 
   if the current node is the left or right child and then replace its child node with the current node

4. Deleting a node with two children
   From the given node to be deleted, find either the node with the smallest value in the right sub-tree or the node with the largest value in the left sub-tree. 
   Suppose you want to find the smallest value in the right sub-tree; you do this by moving on to every node’s left child until the last left child is reached.
   Replace the node to be deleted with the node found (the smallest node in the right sub-tree or the largest node in the left sub-tree).
   Finally, delete the node found (the smallest in the right sub-tree).
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.rightchild = None
        self.leftchild = None
    def insert(self, value):
        if value < self.value:
            if self.leftchild:
                self.leftchild.insert(value)
            else:
                self.leftchild = Node(value)
                return
        elif value > self.value:
            if self.rightchild:
                self.rightchild.insert(value)
            else:
                self.leftchild = Node(value)
                return
    def search(self, value):
        if value < self.value:
            if self.leftchild:
                return self.leftchild.search(value)
            else:
                return False
        elif value > self.value:
            if self.rightchild:
                return self.rightchild.search(value)
            else:
                return False
    def delete(self, Value):
        if self is None:
            return False
        
        if Value < self.value: # Finding value in Left subtree
            if self.leftchild:
                self.leftchild = self.leftchild.delete(Value)
            else:
                print(str(Value), "Value not found in left subtree")
                return None
        elif Value > self.value:  # Finding Value in Right Subtree
            if self.rightchild:
                self.rightchild = self.rightchild.delete(Value)
            else:
                print (str(Value), "Value not found in Right subtree")
                return None
        else: # Value Found
            if self.leftchild is None and self.rightchild is None: # Deleting leaf nodes
                self = None
                return None
            elif self.leftchild is None: # Deleting right node (POV: Only right child exists)
                temp = self.rightchild
                self = None
                return temp
            elif self.rightchild is None:# Deleting left node (POV: Only left child exists)
                temp = self.leftchild
                self = None
                return temp
            else:
                #First get the inorder successor
                current = self.rightchild
                while(current.leftchild is not None):
                    current = current.lefttchild
                self.value = current.Value
                self.rightchild = self.rightchild.delete(current.Value)

                
        
