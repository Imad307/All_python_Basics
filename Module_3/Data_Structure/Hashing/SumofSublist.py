

def sumofsublist(my_list):
    total_sum = 0
    dictionary = dict()

    for ele in my_list:
        total_sum +=ele

        if ele == 0 or total_sum == 0 or dictionary.get(total_sum) is not None:
            return True
        dictionary[total_sum] = ele
    return False
my_list = [6,4,-7,3,12,9]
print(sumofsublist(my_list))
