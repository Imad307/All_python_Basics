
# Kth largest in the list
'''test_list = [40,35,82,14,22,66,53]
print(test_list)
test_list.sort()
print(test_list)
k = 2
if k>len(test_list):
    print("error")
else:
    print(test_list[len(test_list)-k])'''

# Count High Lows
#num_list = [20,9,51,81,50,42,77]
num_list = []
def count_low_high(num_list):
    if(len(num_list)==0):
        return None
    high_list = len([n for n in num_list if n>50 or n%3==0])
    low_list = len([n for n in num_list if n<=50 and n%3!=0])
    return [low_list, high_list]

print(count_low_high(num_list))