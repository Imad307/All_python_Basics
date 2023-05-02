'''
Doubly Link List: The difference between SLL and DLL is that in DLL each node contain pointers for both next_element and 
previous node. Which makes it bi-directional 


DLLs have a few advantages over SLLs, but these perks do not come without a cost:

Doubly linked lists can be traversed in both directions, which makes them more compatible with complex algorithms.

Nodes in doubly linked lists require extra memory to store the previous_element pointer.

Deletion is more efficient in doubly linked lists as we do not need to keep track of the previous node. 
We already have a backwards pointer for it.


'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None    # Pointer to next node
        self.previous_element = None # Pointer to previous node
    
# Tail Pointer in Linked Lists
'''
The head node is essential for any linked list, but what if we also kept account of the tail of the list? 
Now, you are aware of both ends of a linked list.
In a singly linked list, insert_at_tail now works in O(1). 
We can simply set the new node as the next_element of the previous end node and update the tail_node.

However, the tail really shines in doubly linked lists.

Apart from tail operations, insertion and deletion become twice as fast because we can traverse the list from both sides.
'''
class LinkedList:
    def __init__(self) -> None:
        self.head_node = None    # Pointer for head node
        self.tail_node = None    # Pointer to tail node
