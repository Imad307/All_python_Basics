from Node import Node
class LinkedList:
    def __init__(self):
        self.head_node = None
    def get_head(self):
        return self.head_node
    def is_empty(self):
        if self.head_node is None:
            print("List is Empty")
            return True
        else:
            return False
    def print_list(self):
        if (self.is_empty):
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print (temp.data , end="->")
            temp = temp.next_element
        print(temp.data, "->None")
        return True
    