
# we used tuples as if we used list elements to add to set, it would give an error of unhashable type list. As it is a list of lists(pairs). 
def find_symmetric(list1):
    set_pairs = set()
    res = []
    for elements in list1:
        simple_pair = tuple(elements)
        elements.reverse()
        reversed_pair = tuple(elements)
        if reversed_pair in set_pairs:
            res.append(list(simple_pair))
            res.append(list(reversed_pair))
        else:
            set_pairs.add(simple_pair)
    return res


arr = [[1, 2], [4, 6], [4, 3], [6, 4], [5, 9], [3, 4], [9, 5]]
symmetric = find_symmetric(arr)
print(symmetric)
