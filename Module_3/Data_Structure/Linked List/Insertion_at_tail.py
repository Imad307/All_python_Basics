from LinkedList import LinkedList
from Node import Node


def insert_at_tail(lst,value):
    new_node = Node(value)

    if lst.get_head() is None:
        lst.head_node =  new_node
        return
    temp = lst.get_head()
    while temp.next_element is not None:
        temp = temp.next_element
    temp.next_element = new_node
    new_node.next_element = None
    return


lst = LinkedList()
lst.print_list()

