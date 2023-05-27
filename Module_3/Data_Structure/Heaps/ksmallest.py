from Minheap import MinHeap

'''heaped = []
def ksmallestinlist(lst, k) 
'''
'''  # Write your code here
    for i in range(len(lst)):
        heaped = insert(lst[i])
    result = []
    result.append[heaped[0]]
    res = findsmall(0, result, k)
    return res

    

def findsmall(ind, result, k):
    while k<1:
        left = 2*ind + 1
        right = 2*ind+2
        smallest = ind
        if len(heaped) > left and heaped[left] < heaped[right]:
            smallest = left
        if len(heaped) > right and heaped[right] < heaped [left]:
            smallest = right
        result.append(smallest)
        k -=1
        findsmall(smallest, result, k)
    return result'''

def ksmallestinlist(lst, k):
    heap = MinHeap() # creating heap
    heap.buildheap(lst) # Building heap
    ksmallest = [heap.removemin() for i in range(k)]
    return ksmallest
