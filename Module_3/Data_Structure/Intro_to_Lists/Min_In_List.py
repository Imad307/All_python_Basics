
# Method 1: Sort in ascending order and print the first value (Olog(n))
#Method 2 : iterate over the list. There are two methods of this method as well. 
# 1. Min_Num= Max positive integer and then checked  and 2nd one is asssign Min_Num = list[0] and then compared accross the list.
import sys
def findMinimum(lst):
    
    Min_Num = sys.maxsize # Assigning it the maximum possible number of int
    for i in range(len(lst)):
        if Min_Num> lst[i]:
            Min_Num = lst[i]
        else:
            continue
    return Min_Num

list_1 = [9,2,3,6]
print(findMinimum(list_1))
