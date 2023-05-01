class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None

class linkedlist:
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
    
    def del_by_value(self, value):
        temp = self.head_node
        tempd = None

        while temp.data is not None:
            if temp.data is value:
                tempd.next_element = temp.next_element
                temp = None
                return True
            tempd = temp
            temp = temp.next_element
        return False
    

