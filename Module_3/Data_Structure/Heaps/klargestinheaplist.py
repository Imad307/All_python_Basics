from MaxHeapImplementaion import MaxHeap
def klargestinlist(lst, k):
    heap = MaxHeap()
    heap.buildheap(lst)
    klargest = [heap.removemax() for i in range(k)]
    return klargest
