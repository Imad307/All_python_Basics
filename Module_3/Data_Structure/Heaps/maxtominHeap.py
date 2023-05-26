'''def convertmax(maxheap):
    for i in range(len(maxheap)//2, -1,-1):
        maxheap = minheap(maxheap, i)
    return maxheap

def minheap(heap, ind):
    left = 2*ind +1
    right = 2*ind +2
    smallest = ind
    if len(heap) > left and heap[smallest] > heap[left]:
        smallest = left
    if len(heap) > right and heap[smallest] > heap[right]:
        smallest = right
    if smallest !=ind:
        temp = heap[smallest]
        heap[smallest] = heap[ind]
        heap[ind] = temp
        minheap(heap,smallest)
    return heap'''


heaped = []
def cmaxmin(maxheap):
    for i in range(len(maxheap)):
        insert(maxheap[i])
    return heaped

def insert(value):
    heaped.append(value)
    percolateup(len(heaped)-1)

def percolateup(inde):
    parent = (inde-1)//2
    if inde<=0:
        return
    elif heaped[parent] > heaped[inde]:
        temp = heaped[parent]
        heaped[parent] = heaped[inde]
        heaped[inde] = temp
        percolateup(parent)

maxHeap = [9,4,7,1,-2,6,5]
print(cmaxmin(maxHeap))
