# Sorting:
'''
Sorting is any process of arranging items systematically. In Computer Science, algorithms put elements of a list in a certain order. Most frequently used orders are numarically and lexicograghical.
Efficient sorting is important for optimizing the efficiency of other algorithms, which require sorted input or the sort of a given input as part of their process. 
'''
# Selection Sort Algorithm
'''
This algorithm works by repeatedly finding the minimum in the list and placing it at the beginning. This way, algorithm maintains two lists:
1. Sublist of already-sorted elements, which is filled from left to right.
2. Sublist of the remaining unsorted elements that needs to be sorted.

In Other words, this algorithm works by iterating over list and swapping each element with minimum(or maximum) element found in insorted list with that in the sorted list. 
Below is the code for Selection Sort Algorithm:
'''
def swap(i,min_index, lst):
    temp = lst[i]
    lst[i] = lst[min_index]
    lst[min_index] = temp

def selection_sort(lst):

    for i in range(len(lst)):
        minimum_num = i
        for j in range(i+1, len(lst)):
            if lst[minimum_num] > lst[j]:
                minimum_num = j
        #lst[i] , lst[minimum_num] = lst[minimum_num] , lst[i]
        swap(i, minimum_num, lst)
    return lst

print("Selection Sort", selection_sort([64, 25, 12, 22, 11]))
# Time Complexity for this Sorting Algorithm is O(n^2) as we have to traverse the list n(n-1)(n-2)...1 times

# Bubble Sort Algorithm:
'''
This is another sorting algorithm also known as 'Sinking Sort'. It works by comparing the adjacent elements and swapping them if they are in the wrong order. This is repeated until list is sorted.
Think of it this way, a bubble passses over the list, takes the max/min element with it to and move it to the right side.
Below is the code for Bubble Sort: It has  a Time Complexity of O(n^2)
'''
def Bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(0, len(lst)-i-1):
            if lst[j] > lst[j+1]:
                swap(j,j+1, lst)
    return lst

lst = [3,2,1,5,4]
print("Bubble Sort: ", Bubble_sort(lst))

#Insertion Sort Algorithm
'''
Insertion sort algorithm works the same way as we would naturally sort the in real life. It itrates over the given list, figures out what the correct position is of every element, insert it there.
Below is the Code: Time Complexity is O(n^2)
'''
def Insertion_sort(lst):

    for i in range(1, len(lst)):
        key = lst[i]
        j = i -1
        while j>=0 and key < lst[j]:
            lst[j+1] = lst[j]
            j-=1
        lst[j+1] = key
    return lst
lst = [64,99,15,22,11,1,0]
print("Insertion Sort: ", Insertion_sort(lst))
# Note: The Complexity actually n^2 only when the input list reverse sorted. So, the best case complexity (when the list is sorted) is Omega(n)

# Space Complexity: Note that all algorithms are in-place, hence the space complexity is O(1) 

