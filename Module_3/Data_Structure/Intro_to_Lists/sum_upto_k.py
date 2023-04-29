# Find two numbers in list that add upto given number of k and return both numbers in a list.
# Brute Force: O(n^2)
list1= [1,21,3,14,5,60,7,6]
def find_sum(lst, k):
    for a in lst:
        for b in lst:
            if a+b==k:
                return [a,b]
    return False
        

print(find_sum(list1,1000))


# Moving Indices: O(nlog(n))
def find_sum(lst, k):
    # sort the list
    lst.sort()
    index1 = 0
    index2 = len(lst) - 1
    result = []
    sum = 0
    # iterate from front and back
    # move accordingly to reach the sum to be equal to k
    # returns false when the two indices meet
    while (index1 != index2):
        sum = lst[index1] + lst[index2]
        if sum < k:
            index1 += 1
        elif sum > k:
            index2 -= 1
        else:
            result.append(lst[index1])
            result.append(lst[index2])
            return result
    return False


print(find_sum([1, 2, 3, 4], 5))
print(find_sum([1, 2, 3, 4], 2))

