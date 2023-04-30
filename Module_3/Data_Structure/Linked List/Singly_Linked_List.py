'''
the two classes needed to implement a singly linked list:

Node Class
LinkedList Class

1. Node Class
The Node class has two components:

Data
Pointer
Data is the value you want to store in the node. Think of it as the value at a specific index in a list. The data type can range from string or integer to a user-defined class.

The pointer refers us to the next node in the list. It is essential for connectivity.

Note that ‘pointer’ is a Node type variable.
'''
class Node:
    def __init__(self,data, ):
        self.data = data          # Data Field
        self.next_element = None  # pointer to next node
'''
2. LinkedList Class:
Linked List itself is a collection of node objects which we defined above. To keep track of list we need a pointer to first node. 
This is where principle of head node comes in. Head Node Doesn't contain any data but simply points to the head of list. 

This means that, to perform any operation on linked list we have to traverse through it starting from it's head node.
'''
class LinkedList:
    def __init__(self):
        self.head_node = None


# Linked Lists Vs. Lists
'''
The main difference between lists and linked lists is in the way elements are inserted and deleted. 
As for linked lists, insertion and deletion at the head happen in a constant amount of time, 
whereas at tail, it takes O(n) time. In the case of lists, it takes O(n) time to insert or delete a value. 
This is because of the different memory layouts of both the data structures. Lists are arranged contiguously in the memory, 
while nodes of a linked list may be dispersed in the memory. This memory layout also affects access operation; 
contiguous layout of lists allows us to index the list; thus, access operation in the list is O(1), 
whereas, for a linked list, we need to perform a traversal thus, it becomes O(n).

Note:* Insertion at tail for arrays like data structures is in O(n), but in python, 
the append method for lists is able to do it in O(1).

Note:** Deletion at tail for arrays like data structures is in O(n), but in python, 
the pop method for lists is able to do it in O(1).

'''
    