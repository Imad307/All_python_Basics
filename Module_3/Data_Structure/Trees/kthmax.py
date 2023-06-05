'''
there are various methods to solve this question. 
1. Use simple inorder traversal and store values in a list because inorder traversal gives us values in an acending order. Then, we can access largest elements in lists. 
2. Here, we can go for reverse inorder traversal where instead of (left,root,right) we can go for (right,root,left). By doing this we will be getting the largest elements
   first that means in the decending order, so by using using a simple count variable which will count to k(since kth largest element). 

Note: for both of them we have to keep track of either count or list (method 1), for list we don't need nonlocal as we need for count variable in method 2
'''


def kthmax(root, k):
    result = []
    inorder(root, result)
    print(result[-k])

def inorder(root, result):
        if root is None:
            return False
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.leftchild
            node = stack.pop()
            result.append(node)
            node = node.rightchild
        return result




