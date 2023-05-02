'''
1. Brute Force: Nested loops:We can solve this problem by using nested loops since we also have to check the duplicate item within the list as well and
also we have to check if there is duplicate item in the second list with respect to first to list. l = m+n time: O(l^2) 
2. using Dictionary to keep track of duplicates: we will first traverse through first list also removing duplicates and then 
                                           we will traverse through second list by skipping the duplicates and adding them to 
                                           the first list as it is already unique. We will follow same procedure for intersection 
                                           except we will only add those elements into new list which are present in both lists.

'''


from LinkedList import LinkedList
from Node import Node
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Length of the list => list.length()
# Remove duplicates => list.remove_duplicates()
# Node class  {int data ; Node next_element;}

# Returns a list containing the union of list1 and list2


def union(list1, list2):
    # Write your code here
    my_dict = {}
    index = 1
    list1_p = list1.get_head()
    list2_p = list2.get_head()
    while (list1_p):
        
        if list1_p.data not in my_dict:
            my_dict[list1_p.data] = index
        elif list1_p.data in my_dict:
            temp_d = list1_p
            temp_p.next_element = temp_d.next_element
            temp_d = None
        temp_p = list1_p
        list1_p  = list1_p.next_element
        index+=1
    start = list1.get_head()
    while start:
        start = start.next_element
    while (list2_p):
        if list2_p.data not in my_dict:
            my_dict[list2_p.data] = index
            new_node = Node(list2_p.data)
            start.next_element = new_node
        elif list2_p.data in my_dict:
            temp_d = list2_p
            temp_p.next_element = temp_d.next_element
            temp_d = None
        temp_p = list2_p
        list2_p  = list2_p.next_element
    return start
    

# Returns a list containing the intersection of list1 and list2


def intersection(list1, list2):
    intersection = LinkedList()
    # Write your code here
    my_dict = {}
    index = 1
    list1_p = list1.get_head()
    list2_p = list2.get_head()
    while (list1_p):
        
        if list1_p.data not in my_dict:
            my_dict[list1_p.data] = index
        elif list1_p.data in my_dict:
            temp_d = list1_p
            temp_p.next_element = temp_d.next_element
            temp_d = None
        temp_p = list1_p
        list1_p  = list1_p.next_element
        index+=1
    while(list2_p):
        if list2_p in my_dict:
            intersection.insert_at_head(list2_p)
        list2_p = list2_p.next_element
        index+=1
    return intersection
