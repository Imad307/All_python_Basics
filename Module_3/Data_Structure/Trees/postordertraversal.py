'''
In Post order traversal of tree we access with left right root. 
'''

def postordertraveral(root):
    if root is None:
        return
    stack = []
    result = []
    stack.append(root)

    while stack:
        node = stack.pop()
        result.append(node)
        if node.leftchild:
            stack.append(node.leftchild)
        if node.rightchild:
            stack.append(node.rightchild)
    while result:
        poping = result.pop()
        print(poping.value , end=" ")

def postorder(root):
    if root is None:
        return
    postorder(root.leftchild)
    postorder(root.rightchild)
    print(root.value)
    
    