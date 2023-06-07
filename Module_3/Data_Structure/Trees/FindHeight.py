'''
1. Height of a tree can be found recursively 
2. Height of a tree can also be calculated using the level order traversal of the tree. And with each level we increment in a variable of height. 

'''
import queue
def findheight(root):
    if root is None:
        return 0
    left_height = findheight(root.leftchild)
    right_height = findheight(root.rightchild)
    return 1 + max(left_height , right_height )

def findHeight(root):
    if root is None:
        return None
    Height = 0
    queue = []
    queue.enqueue(root)
    while queue:
        for _ in range(len(queue)):
            node = queue.dequeue
            if root.leftchild:
                queue.enqueue(root.leftchild)
            if root.rightchild:
                queue.enqueue(root.rightchild)
        Height+=1
    return Height
        
