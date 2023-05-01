from Node import Node
from LinkedList import LinkedList
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Node class  {int data ; Node next_element;}

# Searches a value in the given list.


def search(lst, value):
    # Write your code here
    temp = lst.get_head()
    if lst.is_empty():
        print("List is Empty")
        return False
    while temp.next_element is not None:
        if temp.data == value:
            return True
        
        temp = temp.next_element
    return False
    
# recursive Solution
def search(node, value):

    # Base case
    if(not node):
        return False  # value not found

    # check if the node's data matches our value
    if(node.data is value):
        return True  # value found

    # Recursive call to next node in the list
    return search(node.next_element, value)


lst = LinkedList()
lst.insert_at_head(4)
lst.insert_at_head(10)
lst.insert_at_head(40)
lst.insert_at_head(5)
lst.print_list()
print(search(lst.get_head(), 4))
    
        
        
