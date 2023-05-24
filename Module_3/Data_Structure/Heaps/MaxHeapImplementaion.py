class MaxHeap:
    def __init__(self):
        self.heap = []
    def insert(self, value):
        self.heap.append(value)
        self.__percolateup(len(self.heap)-1)

    def getmax(self):
        if self.heap:
            return self.heap[0]
        return None
    
    def removemax(self):
        if len(self.heap) > 1:
            max = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.__maxheapify(0)
            return max
        elif(len(self.heap) == 1):
            max = self.heap[0]
            del self.heap[0]
            return max
        
    def __percolateup(self, index):
        parent = (index-1)//2
        if index<=0:
            return
        elif self.heap[parent] < self.heap[index]:
            temp = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = temp
            self.__percolateup( parent)

    def __maxheapify(self, index):
        left = index *2 +1
        right = index*2 +2
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap)> right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest!=index:
            temp = self.heap[largest]
            self.heap[largest] = self.heap[index]
            self.heap[index] = temp
            self.__maxheapify(largest)
    def buildheap(self, arr):
        self.heap = arr
        for i in range(len(self.heap)-1, -1, -1):
            self.__maxheapify(i)


heap = MaxHeap()
for i in range(0,101, 10 ):
    heap.insert(i)

print(heap.getmax())
print(heap.removemax())
print(heap.insert(1000))
print(heap.getmax())
