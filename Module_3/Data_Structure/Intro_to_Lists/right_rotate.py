

list_1 = [1,2,3,4,5,6,7,8,9,10]
def right_rotate(lst,k):
    if k> len(lst):
         k = k % len(list_1) # If k exceeds the length of list
         print("K exceeds the length of list but now rounded off to: ", k)
    a =k
    k1=0

    while(k1 <k):
        temp = lst[k1]
        lst[k1] = lst[-a]
        lst[-a] = temp
        k1+=1
        a-=1
    return(lst)


print(right_rotate(list_1,41))


 

