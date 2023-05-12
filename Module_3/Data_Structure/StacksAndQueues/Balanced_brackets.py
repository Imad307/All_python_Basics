from stacks import MyStack

def balance(exp):
    stack = MyStack()
    closed = [')','}',']']
    for char in exp:
        if char in closed:
            if stack.Is_Empty():
                return False
            if char is ')' and stack.peek() is not '(':
                return False
            if char is '}' and stack.peek() is not '{':
                return False
            if char is ']' and stack.peek() is not '[':
                return False
        else:
            stack.push(char)
    if stack.Is_Empty() is False:
        return False
    return True

