'''
Min Heap follows the min heap property which means that key at parent node is always smaller than the child nodes.

Insertion in Min-Heap:
Create a new node at the last of heap.
Insert the value in it.
Apply percolate up method until you reach the root node and heap property is satisfied.


Removing from Min-Heap:
Delete the root node.
Move the last key node value to the root node node value.
Apply percolate down method(if key is larger than it's child nodes than swap values).
Repeat untill you reach the last node.

'''

class MinHeap:
    def __init__(self):
        self.heap = []
    def getmin(self):
        if self.heap:
            return self.heap[0]
        return None
    def insert(self, value):
        self.heap.append(value)
        self.__perlocateup(len(self.heap)-1)
    def removemin(self):
        if self.heap is None:
            return None
        elif len(self.heap)==1:
            return self.heap[0]
        elif self.heap:
            min = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.__minheapify(0)
            return min
        
    def __perlocateup(self, index):
        parent = (index-1)//2
        if index <=0:
            return
        elif self.heap[parent] > self.heap[index]:
            temp = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = temp
            self.__perlocateup(parent)
    def __minheapify(self, index):
        left = 2*index +1
        right = 2*index +2
        smallest = index
        if len(self.heap) > left and self.heap[smallest]>self.heap[left]:
            smallest = left
        if len(self.heap) > right and self.heap[smallest] > self.heap[right]:
            smallest = right
        if smallest!=index:
            temp = self.heap[smallest]
            self.heap[smallest] = self.heap[index]
            self.heap[index] = temp
            self.__minheapify(smallest)
    def buildheap(self, arr):
        self.heap = arr
        for i in range(len(arr), -1, -1):
            self.__minheapify(i)


minheap = MinHeap()
for i in range(100, -101, -10):
    minheap.insert(i)

print(minheap.getmin())



