
# Using iterative approach
class Node:
    def __init__(self, value):
        self.value = value
        self.rightchild = None
        self.leftchild = None
    def insert(self, value):
        current = self
        parent = None
        while current:
            parent = current
            if value< current.value:
                current = current.leftchild
            else:
                current = current.rightchild
        if value < parent.value:
            parent.leftchild = Node(value)
        else:
            parent.rightchild = Node(value)
    def search(self, value):
        current = self
        while current:
            if value < current.value:
                current = current.leftchild
            elif value > current.value:
                current = current.rightchild
            else:
                return True
        return False
    
class BinarySearchtree:
    def __init__(self, value):
        self.root = Node(value)
    def insert(self, value):
        if self.root:
            return self.root.insert(value)
        else:
            self.root = Node(value)
            return
    def search(self, svalue):
        if self.root:
            return self.root.search(svalue)
        else:
            return False


# Using Recursive Search Method

class Nod:
    def __init__(self, value):
        self.value = value
        self.rchild = None
        self.lchild = None
    def insert(self, ivalue):
        if ivalue < self.value:
            if self.lchild:
                self.lchild.insert(ivalue)
            else:
                self.lchild = Nod(ivalue)
                return 
        if ivalue > self.value:
            if self.rchild:
                self.rchild.insert(ivalue)
            else:
                self.rchild = Nod(ivalue)
                return
    def search (self, svalue):
        if svalue < self.value:
            if self.lchild:
                return self.lchild.search(svalue)
            else:
                return False
        elif svalue > self.value:
            if self.rchild:
                return self.rchild.search(svalue)
            else:
                return False
        else:
            return True
        return False
    

class BSTree:
    def __init__(self, value):
        self.root = Nod(value)
    def insert(self, value):
        if self.root:
            return self.root.insert(value)
        else:
            self.root = Nod(value)
            return True
    def search(self, svalue):
        if self.root:
            return self.root.search(svalue)
        else:
            return False
        


    
        

