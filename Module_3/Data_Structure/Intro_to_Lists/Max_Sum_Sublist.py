# Challenge 11: Maximum Sum Sublist
'''import sys
def Max_Sum_Sub(lst):
    full_max = -(sys.maxsize)
    for i in range(len(lst)):
        max_sum = -(sys.maxsize)
        max_sum_sum = -(sys.maxsize)
        previous_sum_sum = max_sum_sum
        for j in range(len(lst)):
            previous_sum = max_sum
            if i == j:
                max_sum=max(max_sum, lst[i])
            else:
                max_sum = max_sum + lst[j]
            
            max_sum_sum = max(previous_sum, max_sum, max_sum_sum)
        
        full_max= max(previous_sum_sum, max_sum_sum, full_max)
    
    return(full_max)'''


list_1 = [-4,2,-5,1,2,3,6,-5]
#print(Max_Sum_Sub(list_1))


def kadane(arr):
    max_sum_so_far = 0
    max_sum_ending_here = 0

    for i in range(len(arr)):
        max_sum_ending_here = max(arr[i], max_sum_ending_here + arr[i])
        max_sum_so_far = max(max_sum_so_far, max_sum_ending_here)
        print("For i = ", i)
        print("Max Sum Ending Here: ", max_sum_ending_here)
        print("Max Sum So Far:",max_sum_so_far)
        

    return max_sum_so_far

print(kadane(list_1))
#print(max(-4,-4))


def Maximum_Sum_Sublist(lst):
    max_sum_for_now = 0
    maax_sum_total = 0
    for i in range(len(lst)):
        max_sum_for_now = max(lst[i], max_sum_for_now + lst[i])
        maax_sum_total = max(maax_sum_total,max_sum_for_now)
    return maax_sum_total

lis = [-4, 2, -5, 1, 2, 3, 6, -5, 1]
print(Maximum_Sum_Sublist(lis))

