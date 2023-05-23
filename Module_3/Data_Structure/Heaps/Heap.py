'''
Heaps are advanced data structures that are useful in applications such as sorting and implementing a priority queue. they are regular binary trees with some special
properties:
1. They are complete binary trees. 
2. They have heap order property
   Min. Heap 
   Max. Heap

Primarily, Heaps are used to get the smallest or largest element. This is because, time complexity for grtting them is O(1). 
Heaps are used to design priority queues. Some of famous algorithms which are implemented using heaps are prim's algorithm,Djiktra's Algorthm,and famous HeapSort Algorithm


Heaps Representaion in Lists:
Heaps can be implemented using arrays or lists in python, The node values are stored in a such a way that all the parent nodes ocuur in the first half of the list
(index<=floor((n-1)/2), where n is the last index and leaves exist in the rest. 

So, the last parent node in the list is floor((n-1)/2). Also, left child of the node at kth index is 2k+1 and right child will be at 2k+2.
To put it simply, index of each node is how much you would count if you started from 0 at the root and went left to right level wise in the tree.
Last Parent Node: floor((n-1)/2)
Left Child:       2k+1
Right Child:      2k+2

Some Misconceptions:
Heaps are sometimes called binary heaps but they are infact binary trees. Also, Heap  data structure is not same as heap memory. Furthermore, it is commonly beleived that
elements of heap are sorted. They are not all sorted, the only key condition is that a Heap follows this: Largest or smallest elements is always placed at the top
(parent node) depending on what type of heap we using (Min/Max).

'''