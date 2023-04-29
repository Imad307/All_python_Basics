import sys
def secondmax(lst):
    first_max = max(lst[0], lst[1])
    sec_max  =  min(lst[0], lst[1])
    print(first_max)
    print(sec_max)
    for index in range(len(lst)):
        if first_max<lst[index] and first_max>sec_max:
            first_max = lst[index]
        elif(sec_max<lst[index] and sec_max<first_max):
            sec_max = lst[index]
    return sec_max

list_1 =[9,2,3,6]
print(secondmax(list_1))

# O(n)