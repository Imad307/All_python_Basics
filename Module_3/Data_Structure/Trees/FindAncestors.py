'''
We can find the ancestors by searching the tree and recording the tree where er are traversing then treeturning the list. 
'''

def FindAncestors(root,k):
    if root is not None:
        return None
    current = root
    ancestors = []
    while current is not None:
        if k > current.value:
            ancestors.append(current.value)
            current = current.rightchild
        elif k < current.value:
            ancestors.append(current.value)
            current = current.leftchild
        else:
            return ancestors[::-1]
        return []
    