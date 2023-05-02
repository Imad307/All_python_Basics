from Node import Node
from LinkedList import LinkedList
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Node class attributes: {data, next_element}


def length(lst):
    # Write - Your - Code
    lengt = 0
    temp = lst.get_head()
    while temp is not None:
        lengt +=1
        temp = temp.next_element
    return lengt