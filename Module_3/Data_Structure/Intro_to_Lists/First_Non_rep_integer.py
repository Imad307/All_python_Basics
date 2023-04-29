
def Non_Rep_integer(lst):
    check_list = [0 for i in range(1000)]
    for i in range(len(lst)): 
        check_list.insert(lst[i], check_list[i]+1 )
    for i in range(len(check_list)):
        if check_list[i] == 1:
            return i

list_1 = [2,3,2,6,6] 

    
# This is not a corrct implementation as something is missing because, it gives min non repeating integer but we need first non repeating integer.

#print(Non_Rep_integer(list_1))

# Brute Force: we would iterate over the list for n(n-1)(n-2)... untill we find a value otherwise return none
# this would be applied using nested loops 

def First_Non(lst_1):
    for i in range(len(lst_1)):
        j=0
        while (j<len(lst_1)):
            if (i!=j and lst_1[i] == lst_1[j]):
                break
            j+=1
        if(j ==len(lst_1)):
            return lst_1[i]
    return None

print(First_Non(list_1))
