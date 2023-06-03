'''
In preorder traversal, we traverse the tree with (root  left right) approach. 
That means we first access the root nodes then left child node and then right right child node.

'''

class Node:
    def __init__(self, value):
        self.value = value
        self.leftchild = None
        self.rightchild = None
    def insert(self, data):
        if self is None:
            self = Node(data)
            return
        current = self
        while(current):
            parent = current
            if data < current.value:
                current = current.leftchild
            else:
                current = current.rightchild
        if data< parent.value:
            parent.leftchild = Node(data)
        else:
            parent.rightchild = Node(data)
    def search(self, Value):
        if self is None:
            return False
        node = self
        while(node):
            if Value< node:
                node = node.leftchild
            else:
                node = node.rightchild
        return node
    def copy(self, node2):
        self.value = node2.value
        if node2.lefthild:
            self.leftchild = node2.leftchild
        else:
            self.rightchild = node2.rightchild
        

    def delete(self, data):
        if self is None: # if tree is empty Case#1
            return False
        # If tree is not empty, we have to search for the data to be deleted
        replacenode = self
        while ( replacenode and replacenode.value != data):
            former = replacenode
            if data < replacenode:
                replacenode = replacenode.leftchild
            else:
                replacenode = replacenode.rightchild
        if replacenode is None and replacenode.value != data: # if data not found case #2
            return False
        elif replacenode.leftchild is None and replacenode.rightchild is None: # Case 3: if it is leaf node
            if data< former.value:
                former.leftchild = None
            else:
                former.rightchild = None
            return True
    

        elif replacenode.leftchild and replacenode.rightchild is None: # case4:  if it has only one child....only left child
            if former is None:
                 self.copy(self.leftchild)
                 self.leftchild = None
            elif data < former.value:
                former.leftchild = replacenode.leftchild
            else:
                former.rightchild = replacenode.leftchild
        elif replacenode.rightchild and replacenode.leftchild is None: # if it has only right child
            if former is None:
                self.copy(self.rightchild)
                self.rightchild = None
            elif data > former.value:
                former.rightchild = replacenode.rightchild
            else:
                former.leftchild = replacenode.rightchild
        else: # Node has two children
            replacenodeparent = replacenode
            replacenode2 = replacenode.rightchild
            while replacenode.leftchild:
                replacenodeparent = replacenode2
                replacenode2 = replacenode2.leftchild
            replacenode.value = replacenode2.value
            if replacenode2.rightchild:
                if replacenodeparent.value > replacenode2.value:
                    replacenodeparent.leftchild = replacenode2.rightchild 
                elif replacenodeparent.value < replacenode2.value:
                    replacenodeparent.rightchild = replacenode2.rightchild 
                else:
                    if replacenode2.value < replacenodeparent.value:
                        replacenodeparent.leftchild = None
                    else:
                        replacenodeparent.rightchild = None
def preordertraversal(root):
    if root is None:
        return 
    stack  = []
    stack.append(root)
    while stack:
        node = stack.pop()
        print(node.value, end=" ")
        if node.rightchild:
            stack.append(node.rightchild)
        if node.leftchild:
            stack.append(node.leftchild)


def preorder(root):
    if root is None:
        return
    print(root.value, end=" ")
    preorder(root.leftchild)
    preorder(root.rightchild)
    
    


