'''
Trees consists of vertices(nodes) and edges that connects them. Unlike the liner DS, they are similar to graphs but they do not have cyles in them. They are acyclic.

Basic Properties: 
Root Node: A node with no parent node. (From where a tree statrs)
child node: A node which is linked to upper node
Parent node: A node which has some child nodes
Sibling Nodes: Nodes that have same parent node.
Ancestor Nodes: Nodes from that node to the root node(Parent nodes, grandparents nodes etc)


Some other Terminologies and formulas: 
Sub-tree: From a particular non-leaf node, a collection of nodes, essentially a tree. 
Degree of a node: Total number of children of node.
Length of a path: Number of edges in the path
Depth of a node n: length of path from a node n to the root node. Depth of a root node is Zero (0)
Level of a node: Depth of a node + 1
Height of a node n: Height of its root node.

Some Tree Types:
Binary tree 
Binary search tree
AVL Tree
Red-Black tree 
2-3 Trees
'''
# What makes a tree balanced
'''
A binary tree is height balanced if for each node in the tree the difference between height of right subtree and left subtree is at most 1. 
|Height(leftsubtree) - Height(rightsubtree)|<=1
'''
