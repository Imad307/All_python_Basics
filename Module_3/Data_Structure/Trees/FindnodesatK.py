'''
It can be done recursively and iteratively. For both we have to use some aspect of Breadth first search
'''
import queue
# Iteratively:
def findk(root, k):
    if root is None:
        return None
    if k==0:
        return root
    my_queue = queue.Queue()
    my_queue.put(root)
    count = 0
    while my_queue and count<k:
        res = []
        level_size = len(my_queue)
        for i in range(level_size):
            node = my_queue.get()
            if node.leftchild:
                my_queue.put(node.leftchild)
                res.append(node.value)
            if node.righchild:  
                my_queue.put(node.rightchild)
                res.append(node.value)
        count+=1
    return res

# Using recursion

def findKnodes(root, k):
    res = []
    findK(root, k, res)
    return res

def findK(root, k, res):
    if root is None:
        return
    if k ==0:
        res.append(root.value)
    else:
        findK(root.leftchild , k-1 , res)
        findK(root.rightchild, k-1, res)
    
