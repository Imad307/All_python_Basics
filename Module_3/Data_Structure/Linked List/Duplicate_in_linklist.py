'''
There are different method to solve this problem 
1. Brute Force: In this method, we pick one value traverse the whole list to find it's equal vaules and remove them 
                then we pick the next element in the list. it takes O(n(n-1)(n-2)....) time which is equivalent to O(n^2)

2. using dictionary: In this method, we use the dictionary to keep track of the values that we have included before in dictionary 
                     if that value comes in front of us next time as well we remove it there and then. 
                     This Method takes some exta space of dictionary but it solves the problem in O(n)Time.Which is quite efficient


'''

# Second Method 
from LinkedList import LinkedList
from Node import Node
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Length of the list => list.length()
# Node class  { int data ; Node next_element;}


def remove_duplicates(lst):
    # Write - Your - Code
    temp = lst.get_head()
    index = 1
    my_dict = {}
    while temp:
        if temp.data not in my_dict:
            my_dict[temp.data] = index
        elif temp.data  in my_dict:
            temp_d = temp
            temp_p.next_element = temp_d.next_element
            temp_d = None
        temp_p = temp
        temp= temp.next_element
        index+=1
    return lst
