'''
Introduction
We are all familiar with the famous Undo option which exists in almost all popular applications. 
Ever wondered how that works? Well, you store the previous states of your work (which are limited to a specific number) 
in the memory in such an order that the last one appears first. You can’t really do this with simple lists very efficiently 
for reasons we will explore in the coming chapters. So this is where the ‘Stack’ data structure comes in handy.

Stacks Follow Last In First Out(LIFO) model. That Means, the last added element is on the top and first added element is at bootom.

Stacks implementation seems simple but it is used iin complex Algorithms such as, Depth First Search Algorithm and 
The Expression Evaluation Algorithm. 

Stacks are used:
1. To backtrack to the previous task/ program. e.g- in recursive code
2. To store a partially completed task. e.g- when you are exploring two different paths in the Graph from a point while figuring
                                             out the smallest path to the target.

How Stacks Work?
There are many ways to implement the stacks:
push(element): to push an element into a stack on the top
pop():      To get an element at the top of stack and delete it as well
peek():    returns the top element in the stack
IsEmpty(): Returns true or 1 if stack is empty 
size():    To get the size of stack 

In Most Programming Languauges, Stacks are implemented using Built-in data structures. But in python, we can use a pre-built
stack class for this purposes by importing that into the program. However, by implementing stacks using built in DS we will master
the ins and outs of Data structure.

Stacks can be implemented using lists and linked lists. Each implementation has it's own advantages and disadvantages.
However, we will be using lists to implement the stacks.
A typical stack must contain following operations:
push(element), pop(), peek(), IsEmpty(), size()

'''

class MyStack:
    def __init__(self):
        self.stack_list = []
        self.stack_size = 0
    def Is_Empty(self):
        if self.stack_size == 0:
            return True
        return False
    def peek(self):
        if self.Is_Empty():
            return None
        return self.stack_list[-1]
    def size(self):
        return self.stack_size
    def push(self, value):
        self.stack_size+=1
        self.stack_list.append(value)
    def pop(self):
        if self.Is_Empty():
            return None
        self.stack_size -=1
        return self.stack_list.pop()


if __name__ == "__main__":   # This statement in Python is to ensure that script is run directly not if it is imported as a module
    # If it is imported as a module to another script we havr to call it explicityly. 
    stack_object = MyStack()
    print("Pushing Elements into stack")
    for i in range(10):
        print(i)
        stack_object.push(i)

    print("Is Empty: ", stack_object.Is_Empty())
    print("Peek Value: ", stack_object.peek())
    print("Size of stack: ", stack_object.size())
    print("Popping elements from the stack")
    for x in range(10):
        print(stack_object.pop())
    
    print("Is Empty: ", stack_object.Is_Empty())
    print("Peek Value: ", stack_object.peek())
    print("Size of stack: ", stack_object.size())
