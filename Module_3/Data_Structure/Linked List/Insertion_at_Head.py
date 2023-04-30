class Node:
    def __init__(self, data):
        self.data = data
        self.next_ele = None

class LinkedList:
    def __init__(self):
        self.head_node = None
    
    def insertion_at_head(self, data):
        # creating a new  object node having the data
        temp_node = Node(data)
        # New node pointing to same node as Head
        temp_node.next_ele = self.head_node
        self.head_node = temp_node
        return self.head_node
    def is_empty(self):
        if self.head_node is None:
            return True
        else:
            return False
    
    def print_list(self):
        if(self.is_empty()):
            print("List is Empty: ")
            return False
        temp = self.head_node
        while temp.next_ele is not None:
            print(temp.data, end= "->")
            temp = temp.next_ele
        print(temp.data, "-> None")
        return True


lst = LinkedList()
lst.print_list()

print("Inserting values in Linked LIst")
for i in range(10):
    lst.insertion_at_head(i)
lst.print_list()
