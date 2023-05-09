from stacks import MyStack

# Brute Force
# It has o(n^2) time complexity
def next_greatest(lst):
    result = []
    for i in range(len(lst)):
        next_greater = -1
        for j in range(i+1, len(lst)):
            if lst[j]>lst[i]:
                next_greater = lst[j]
                break
        result.append(next_greater)
    return result

# Using Stacks
# It has O(n) time complexity
def next_great(lst):
    stack = MyStack()
    res = [-1] * len(lst)
    for i in range(len(lst)-1, -1, -1):
        while stack.Is_Empty() is False and stack.peek() <= lst[i]:
            stack.pop()
        if stack.Is_Empty() is False:
            res[i] = stack.peek()
        stack.push(lst[i])
    return res

if __name__ == "__main__":
    print(next_great([4,6,3,2,8,1,9,9,9]))

