

# 1st Method
def is_disjoint(list1, list2):
    s1 = set(list1)
    for ele in list2:
        if ele not in s1:
            continue
        else:
            return False
    return True


# 2nd Method:

def disjoint(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    s3 = set()
    if s1.intersection(s2) == s3:
        return True
    return False
    