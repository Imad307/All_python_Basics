from Node import Node

class LinkedList:
    def __init__(self):
        self.head_node = None
    def get_head(self):
        return self.head_node
    def is_empty(self):
        if self.head_node is None:
            print("List is Empty ")
            return True
        else:
            return False
    def insert_at_k(self, data, k, lst):
        count = 0
        new_node = Node(data)
        if lst.get_head() is None:
            print("List is empty, we cannot add node at the given value. So, Added to first index")
            self.head_node = new_node
            return self.head_node
        temp = lst.get_head()
        while count<k-1:
            temp = temp.next_element
            count+=1
        new_node.next_element = temp.next_element
        temp.next_element = new_node
        return
    def print_list(self):
        temp_node = self.head_node
        if temp_node is None:
            print("List is Empty")
        while temp_node.next_element is not None:
            print(temp_node.data, end="->")
            temp_node = temp_node.next_element
        print(temp_node.data, "->None")
        return
    
lst = LinkedList()
print(lst.insert_at_k(5,1,lst))

        

