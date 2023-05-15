"""
1. Use a second temp_stack.
2. Pop value from mainStack.
3. If the value is greater or equal to the top of temp_stack,
  then push the value in temp_stack
  else pop all values from temp_stack
      and push them in mainStack
      and in the end push value in temp_stack
4.repeat from step 2 till mainStack is not empty.
5. When mainStack will be empty,
    temp_stack will have sorted values in descending order.
6. Now transfer values from temp_stack to mainStack
    to make values sorted in ascending order.
"""

from stacks import MyStack

def sort_stack(stack):
    temp_stack = MyStack()
    while not stack.is_empty():
        value = stack.pop()
        # if value is not none and larger, push it at the top of temp_stack
        if temp_stack.peek() is not None and value >= temp_stack.peek():
            temp_stack.push(value)
        else:
            while not temp_stack.is_empty() and value < temp_stack.peek():
                stack.push(temp_stack.pop())
            # place value as the smallest element in temp_stack
            temp_stack.push(value)
    # Transfer from temp_stack => stack
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())
    return stack

if __name__ == "__main__" :
    # Creating and populating the stack
    stack = MyStack()
    stack.push(2)
    stack.push(97)
    stack.push(4)
    stack.push(42)
    stack.push(12)
    stack.push(60)
    stack.push(23)
    # Sorting the stack
    stack = sort_stack(stack)
    # Printing the sorted stack
    print("Stack after sorting")
    print([stack.pop() for i in range(stack.size())])