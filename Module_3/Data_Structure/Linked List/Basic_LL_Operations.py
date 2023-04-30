'''
The primary operations which are generally a part of the LinkedList class are listed below:

get_head() - returns the head of the list
insert_at_tail(data) - inserts an element at the end of the linked list
insert_at_head(data) - inserts an element at the start/head of the linked list
delete(data) - deletes an element with your specified value from the linked list
delete_at_head() - deletes the first element of the list
search(data) - searches for an element with the specified value in the linked list
is_empty() - returns true if the linked list is empty
'''

# get_head(): it's time complexity is O(1) as we are just checking the head
# is_empty() : it's time complexity is O(1) as we are just checking the head if it is None or Not

class Node:
    def __init__(self, data):
        self.data = data
        self.next_ele = None

class LinkedList:
    def __init__(self):
        self.head_node = None
    def get_head(self):
        return self.head_node
    def is_empty(self):
        if self.head_node is None:
            return True
        else:
            False

lst = LinkedList()
print(lst.is_empty())

  