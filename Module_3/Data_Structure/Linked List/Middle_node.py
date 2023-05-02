class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None
        self.previous_element = None


class LinkedList(Node):
    def __init__(self):
        self.head_node = None
        self.tail_node = None
    def get_head(self):
        if self.head_node is not None:
            return self.head_node
        return None
    def get_tail(self):
        if self.tail_node is not None:
            return self.tail_node
        return None 
    def is_empty(self):
        if (self.head_node or self.tail_node):
            print("List is Empty")
            return True
        return False
    def insert_at_head(self,data):
        temp_node = Node(data)
        temp_node.next_element = self.head_node
        self.head_node = temp_node
        return self.head_node
    def insert_at_tail(self, value):
        temp_node = Node(value)
        t_node = self.tail_node
        temp_node.next_element = None
        temp_node.previous_element = self.tail_node
        t_node.next_element = temp_node
    def print_list(self):
        if(self.is_empty()):
            print("list is empty")
            return False
        p_node = self.head_node
        
        while p_node:
            print(p_node.data, end="->")
            p_node = p_node.next_element
        print(end="->None")
        return True
    def length(self):
        temp = self.get_head()
        length = 0
        while temp:
            length+=1
            temp = temp.next_element
        return length
    # This is two pointer technique for finding the middle of linked list
    def mid_node(self):
        temp_h= self.get_head()
        if (self.is_empty()):
            return None
        if temp_h.next_element is None:
            return temp_h.data
        mid_node = temp_h
        while temp_h.next_element:
            mid_node = mid_node.next_element
            temp_h = temp_h.next_element
            if temp_h:
                temp_h = temp_h.next_element
        if mid_node:
            return mid_node.data
        return -1
    
        
        