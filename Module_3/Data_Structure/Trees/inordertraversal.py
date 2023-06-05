'''
In the case of inorder traversal, er traverse from left root right
'''

def inordertraversal(root):
    if root is None:
        return None
    stack =[]
    result = root

    while stack or result:
        while result:
            stack.append(result)
            result = result.leftchild
        result = stack.pop()
        print(result.value, end=" ")
        result = result.rightchild

def inorder(node):
    if node is None:
        return
    inorder(node.leftchild)
    print(node.value)
    inorder(node.rightchild)

        