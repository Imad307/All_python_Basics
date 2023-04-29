#Challenge 10: Rearrange Sorted List in Max/Min Form

def max_min(lst):
    max_min_list = []
    start = 0
    length = len(lst)
    End = length-1
    while (start != length//2):
        max_min_list.append(lst[End])
        End-=1
        max_min_list.append(lst[start])
        start+=1
    if (length % 2!=0):
         max_min_list.append(lst[start])
         return(max_min_list)
    else:
        return(max_min_list)

list_1 = [-11,1,3,4,5,6,7,8]
print(max_min(list_1))
# O (n)