# Set Theory Operations
'''
In mathematics, there are 3 types of operations On sets.
1. Union
2. Intersection 
3. difference
Python, Allows all these operations as well.
'''
# Since sets are unordered data structure, content order of output does not matter
set1 = {1,2,34,6,7}
set2 = {6,7,59,90,8}
# Union
'''
Union is collections of all the unique elements present in both the sets.
It is executed using pipe '|' function or union() method.
'''
print(set1 | set2)
print(set1.union(set2))
print(set2.union(set1))

#Intersection
'''
Intersection is set of all the unique elements in both the sets which are common among them.
Intersection between two sets can be achieved using '&' operator or intersection() method.
'''
print(set1 & set2)
print(set1.intersection(set2))
print(set2.intersection(set1))

#Difference 
'''
Difference is set of all the unique elements which is present in first set but not in the second set. 
It is achieve by using '-' operator between two sets or difference() method.
'''
print(set1 - set2)
print(set1.difference(set2))
print(set2 - set1)
print(set2.difference(set1))