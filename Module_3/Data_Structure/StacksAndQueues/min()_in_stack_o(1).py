from stacks import MyStack
# The Concept behind is that: All the values are pushed into mainstack normally but in minstack we push the value if value is smaller than peek value,
# Else: We push peek value back again into the minstack. In this way, at the top/peek there will always be minimum value that we can acess at O(1) time Complexity.
class minStack:
    def __init__(self):
        minstack = MyStack()
        mainstack = MyStack()
    def pop(self):
        self.minstack.pop()
        return self.mainstack.pop()
    def push(self, value):
        self.mainstack.push(value)
        if self.minstack.Is_Empty() or self.minstack.peek() > value:
            self.minstack.push(value)
        else:
            self.minstack.push(self.minstack.peek())
    def min(self):
        if self.minstack.Is_Empty() is False:
            return self.minstack.peek()
        return None
    
    