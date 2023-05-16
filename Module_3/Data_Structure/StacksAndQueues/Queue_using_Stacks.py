from stacks import MyStack
# Implement Queue using stacks: Two Stacks will be used to implement the queue
class newqueue:
    def __init__(self):
        self.main_stack = MyStack()
        self.spare_stack = MyStack()
    
    def enqueue(self, data):
        self.main_stack.push(data)
    def dequeue(self):
        if self.main_stack.Is_Empty():
            return None
        while self.main_stack.Is_Empty() is False:
            self.spare_stack.push(self.main_stack.pop())
        val = self.spare_stack.pop()
        while(self.spare_stack.Is_Empty is False):
            self.main_stack.push(self.spare_stack.pop())
        return val
# Second Solution Could be recursive and using only one stack instead of two stacks 
class que:
    def __init__(self):
        self.same_stack = MyStack()
    def enqueue(self, value):
        self.same_stack.push(value)
    def dequeue(self):
        if self.same_stack.Is_Empty():
            return None
        elif len(self.same_stack) ==1:
            self.same_stack.pop()
        else:
            popped = self.same_stack.pop()
            item = self.dequeue()
            self.same_stack.push(popped)
            return item
        
