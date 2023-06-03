# Find minimum in a BST
# iterative approach
def findminimum(root):
    if root is None:
        return None
    while root:
        node = root
        root = root.leftchild
    return node.value
# recursive

def finmin(node):
    if node is None:
        return None
    elif node.leftchild is None:
        return node.value
    else:
        finmin(node.leftchild)
