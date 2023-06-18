def find_pair(my_list):
    # Write your code here
    sublist_sum = []
    all_dict = dict()
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            added = my_list[i] + my_list[j]
            if added not in all_dict:
                all_dict[added] = [my_list[i], my_list[j]]
            else:
                prev_pair = all_dict.get(added)
                second_pair = [my_list[i], my_list[j]]
                sublist_sum.append(prev_pair)
                sublist_sum.append(second_pair)
                return sublist_sum
    return sublist_sum








