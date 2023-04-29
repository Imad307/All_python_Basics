#Challenge 9: Rearrange Positive & Negative Values

def rearrange(lst):
    positive_temp_list = []
    negative_temp_list = []
    for i in range(len(lst)):
        if (lst[i]<0):
            negative_temp_list.append(lst[i])
        elif lst[i]>=0:
            positive_temp_list.append(lst[i])
        
    return(negative_temp_list + positive_temp_list)

list_1 = [10,-1,20,4,5,-9,-6]
print (rearrange(list_1))

# It can also be done without using space of other lists if we rearrange in the same list.
