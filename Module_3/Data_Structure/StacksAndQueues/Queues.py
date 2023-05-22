'''
Similar to Stacks, Queues are also linear data structure that stores data in sequential manner. The Only difference between them is 
Stacks follow LIFO(Last In First Out) structure, and Quesues follow FIFO (First In First Out) Approach. 

This means that elements are added in the rear and the deleted from front. Quesues are little bit trickier to implement as we have to
keep track of both the front and rear of the array/lists.

What Queues are used for:
1. When we want to priortize something over another.
2. A resource is shared between multiple devices. 

Essential Functions in a Queue are as follows:
Enqueue(element): To add an element in the rear of the queue
Dequeue():        Removes an element from the front of Queue
front():          Returns first element off the queue
rear():           Returns the last element in the Queue
IsEmpty():        Returns True/1 if queue is empty
size():           Returns the size of queue

Types of Queues:
Linear Queue: A simple queue according to the definition as we have discussed earlier is a linear queue.
Circular Queue: A queue whose rear end meets with the front end. 
                It is used in simulation of objects
                Event Handling(do somethiing when a particular event occurs)
Priority Queue: In the priority queue, all elements are associated with a priority and this queue is sorted as most prioritized 
                elements are in the front and least prioritized elements are at the end of the queue. these queues are mostly 
                used in the Operating systems to prioritize tasks within the enviroment
Double-Ended Queue: The Double-Ended Queue acts as queue from both ends(front and rear). It is a flexible data structure that 
                    provides enqueue and dequeue functionality as O(1). It can also act as a normal linear queue. 
                    Python has a built-in deque class that can be imported from the collections module. The class contains several 
                    useful methods such as (rotate) which can be used to rotate the list if we can remember a problem that we did
                    in Lists to right rotate a list. That can be solved really easily using deque.rotate(). 

'''
'''
Queues Implementation:
Queues can be implemented using lists, linked lists or even stacks. But most commonly lists are used to implement the queues. 
With typical arrays, however, the time complexity is O(n) when dequeuing an element from the beginning of the queue. 
This is because when an element is removed, the addresses of all the subsequent elements must be shifted by 1, 
which makes it less efficient. With linked lists and doubly linked lists, the operations become faster.

Here, we will use a doubly-linked list to implement queues.


'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next_element = None
        self.previous_element = None
class DoublyLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None
        self.length = 0
    def get_head(self):
        if self.head_node is not None:
            return self.head_node
        return None
    def IsEmpty(self):
        if self.head_node is None:
            return True
        return False
    def insert_at_tail(self, data):
        temp_node = Node(data)
        if (self.IsEmpty()):
            self.head_node = temp_node
            self.tail_node = temp_node
        else:
            self.tail_node.next_element = temp_node
            temp_node.previous_element = self.tail_node
            temp_node.next_element = None
        self.length+=1
        return temp_node.data
    def remove_at_head(self):
        if (self.head_node is None):
            return False
        remove_node = self.head_node
        if(self.length==1):
            self.head_node = None
            self.tail_node = None
        else:
            self.head_node = remove_node.next_element
            self.head_node.previous_element = None
            remove_node = None
        self.length-=1
        return remove_node.data
    def get_tail(self):
        if self.head_node is not None:
            return self.tail_node
        return None
    def print_Queue(self):
        final = ""
        if (self.IsEmpty()):
            return None
        temp = self.head_node
        final = "[" + str(temp.data) + ","
        temp = temp.next_element
        while(temp.next_element):
            final = final + str(temp.data) + ","
            temp = temp.next_element
        final = final + str(temp.data) + "]"
        return final


class MyQueue:
    def __init__(self):
        self.items = DoublyLinkedList()
    def IsEmpty(self):
        if (self.items.IsEmpty()):
            return True
        return False
    def front(self):
        return self.items.get_head()
    def rear(self):
        if self.IsEmpty():
            return None
        return self.items.get_tail()
    def size(self):
        return self.items.length
    def enqueue(self,data):
        return self.items.insert_at_tail(data)
    def dequeue(self):
        return self.items.remove_at_head()
    def print_list(self):
        return self.items.print_Queue()
     
if __name__ == "__main__":
    queue_object = MyQueue()
    print("Is Empty: ", queue_object.IsEmpty())
    print("Front: ", queue_object.front())
    print("Rear: ", queue_object.rear())
    print("size: ", queue_object.size())
    print("Enqueue Element 14: " )
    queue_object.enqueue(14)
    print("Enqueue Element 11: " )
    queue_object.enqueue(11)
    queue_object.size()
    queue_object.print_list()


while queue_object.IsEmpty():
    print("Dequeue(): ", str(queue_object.dequeue()))
print("Is Empty: ", str(queue_object.IsEmpty()))

# All of these functions except print_list are done in O(1)





