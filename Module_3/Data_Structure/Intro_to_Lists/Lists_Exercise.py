# Challenge 2: Merge 2 Sorted lists
list1 = [-2,-1,0,7]  
list2 = [2,4,6,8,10,12]
def merge_lists(lst1, lst2):
    arr =[]
    # Write your code here
    ind1 = 0
    ind2 = 0
    print(len(lst1), len(lst2))
    if (len(lst1)>=len(lst2)):
        while ind1<len(lst1) and ind2<len(lst2):
            if(lst1[ind1]<lst2[ind2]):
                arr.append(lst1[ind1])
                ind1+=1
            elif(lst1[ind1]>lst2[ind2]):
                arr.append(lst2[ind2])
                ind2+=1
        if ind2<len(lst2):
            arr.extend(lst2[ind2:])
        
    elif(len(lst1)<len(lst2)):
        while ind1<len(lst1) and ind2<len(lst2):
            if(lst1[ind1]<lst2[ind2]):
                arr.append(lst1[ind1])
                ind1+=1
            elif(lst1[ind1]>lst2[ind2]):
                arr.append(lst2[ind2])
                ind2+=1
        if ind2<len(lst2):
            arr.extend(lst2[ind2:])
    return arr

print(merge_lists(list1,list2))

