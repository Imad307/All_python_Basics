'''
Max heaps follows max heap property which means that the key at parent node is always greater than the child nodes. heaps can be implemented using lists, nodes 
or tree classes. Although, they are implemented using lists or arrays as this is  more space effient approach. To build a heap start from empty one and succevely 
insert() all elements. 

Insertion in Max-Heap:
Create a new child at te end of heap.
Place new key at that node. 
Then, restore the heap property by swapping parent and child values if parent key is smaller than the child key. This is called 'Percolating up'
Continue to percolate up until heap property is restored. 


Remove Maximum in max-heap:
remove the root node. 
move the key of last child node to the last level root.
Now compare the values with it's children and if the key value is smaller than either of children swap values. This is called 'max heapifying'
continue to max heapify until heap property is restored. 
'''
# Max-Heap Implementation:

class Maxheap:
    def __init__(self):
        pass

    def insert(self, value):
        pass
    def getmax(self):
        pass
    def removemax(self):
        pass
    def __percolateup(self, index):
        pass
    def __maxheapify(self, index):
        pass

heap = Maxheap()
