'''
there are two method to solve this, first is to use two variables as indeces at the extreme. An Effecient technique
second is, when we split the list and use indeces to add/remove data from stacks. This is not efficient 
'''
# First Method: effecient method
class Twostacks:
    def __init__(self, size):
        self.size = size
        self.stack_list = [0] * size
        self.top1 = -1
        self.top2 = self.size

    def push1(self, value):
        if self.top1<self.top2-1:
            self.top1+=1
            self.stack_list[self.top1] = value
        else:
            print("Stack Overflow")
            return
    def push2(self, value):
        if self.top1<self.top2-1:
            self.top2-=1
            self.stack_list[self.top2] = value
        else:
            print("Stack Overflow")
            return
    def pop1(self):
        if self.top1>=0:
            val = self.stack_list[self.top1]
            self.top1-=1
            return val
        else:
            print("Stack Underflow")
            return
    def pop2(self):
        if self.top2<self.size:
            val = self.stack_list[self.top2]
            self.top2+=1
            return val
        else:
            print("Stack Underflow")
            return

# Second Method:
class TwoStacks:
    # Initialize the two stacks here
    def __init__(self, size):
        self.stack_list = [None] *size
        self.stack1_size = 0
        self.stack2_size = 0
        self.index1 =0 
        self.index2 =0

    # Insert Value in First Stack
    def push1(self, value):
        i = 1
         
        if (self.stack_list[((len(self.stack_list)//2)-i)] != None):
            i+=1
        self.index1 = (len(self.stack_list)//2)-i
        if self.index1 >=0 or self.index1<(len(self.stack_list)/2):
            self.stack_list.insert(self.index1, value)
            self.stack1_size+=1
        else: 
            print("Stack Overflow")
        

    # Insert Value in Second Stack
    def push2(self, value):
        i = 0
        if (self.stack_list[(((len(self.stack_list))//2)+ i)] != None):
            i+=1
        self.index2 = ((len(self.stack_list))//2) + i
        if self.index2>=5 or self.index2<10:
            self.stack_list.insert(self.index2,value)
            self.stack2_size +=1
        else: 
            print("Stack Overflow")
        

    # Return and remove top Value from First Stack
    def pop1(self):
        self.stack1_size -=1
        return (self.stack_list[self.self.index1].pop())

    # Return and remove top Value from Second Stack
    def pop2(self):
        self.stack2_size -=1
        return (self.stack_list.pop(self.index2))
    
