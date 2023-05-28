# Binary Tree
'''
A binary tree is a tree in which each node has 0 to 2 children nodes. 
'''
# Types of Binary Tree
'''
Complete Binary Tree: 
    A type of binary tree in which at levels each node has 2 nodes except perhaps the last level, But from left to right side.
Full Binary Trees: 
    A type of binary tree in which all the nodes has either 2 children of 0, no node has 1 child. 
    Tot. No. of nodes in Full Binary tree is: 2h+1 < total number of nodes<=(2^(h+1))-1
Perfect Binary Tree:
    A type of binary tree in which all the nodes has 2 nodes except for the leaf nodes. 
    Tot. No. of nodes in Perfect Binary tree : (2^(h+1)) -1
    Tot. Number of leaf nodes: 2^h or (n+1)/2

Some other tree types:
Complete binary tree
Skewwed Binary tree 
Binary search tree
AVL tree
'''
# Skewed Binary Tree
'''
A type of binary tree in which either all the left most nodes or right most nodes are present in a binary tree. We should avoid these binary tree at all costs
as they make worst scenarios for all the complex problems. 
Types of Skewed Binary tree:
Left-Skewed Binary tree
Right-Skewed Bibary tree
'''
# What makes a tree balanced
'''
A binary tree is height balanced if for each node in the tree the difference between height of right subtree and left subtree is at most 1. 
|Height(leftsubtree) - Height(rightsubtree)|<=1
'''
