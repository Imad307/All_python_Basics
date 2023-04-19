# In Python, the built-in range() function can be used to create a sequence of integers. 
# This sequence can be iterated over through a loop. A range is specified in the following format:
# range(start, end, step)
# let's check if there is any float number which is greater than 10.3
'''my_list=[2.5, 16.42, 10.77, 8.3, 34.21]
filter_list=[]
for i in range(0 , len(my_list)):
    if my_list[i]>=10:
        filter_list.append(my_list[i])
    else:
        print(my_list[i], " is less than 10")

print(filter_list)   
print(my_list) '''

my_list=[2.5, 16.42, 10.77, 8.3, 34.21]

for i in my_list:
    if i >=10.77:
        print (i)
    else:
        print(i, " less than 10")


