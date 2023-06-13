

def issubset(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    if s1.intersection(s2) == s2:
        return True
    return False

def issub(list1, list2):
    s1 = set(list1)
    for ele in list2:
        if ele not in s1:
            return False
    return True
