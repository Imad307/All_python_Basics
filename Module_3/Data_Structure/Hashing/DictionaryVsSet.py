'''
Before solving any challenge regarding hashtables, it is necessary to look at the implementations of dict and set and see how they are different. Both are implemented
in Python. It is also a misconception that these two structures are the same but infact they are very different from each other. 

Dict:
 dict or dictionary is a mapping type object which maps hashable values to arbitrary objects. It stores element in a key-value pairs. 
 It provides basic functionality of hashing along with some other helper functions that helps in the process of insertion, deletion and search. 
 Some key features are given below:
  A dict stores key-value pairs to map a key to the value.
  dict cannot contaion duplicate keys, however it can have duplicate values.
  dict does not store elements in any order or form like with repect to keys or values. 
  dict uses hash function for its implementaion. it takes the key and maps it into range of hash table using hash function
  On average, time complexity is O(1). It will go up to O(n) in the worst case scenario. 

Set:
 Set is a container in python which has no duplictes. It consists of elements in no specific order. it is also built in same way as dict. -i-e- using the hashtable, 
 but it is still quite different from dict. 
 Some key features are listed below:
  set is a container that implements the set interface, and this interface only store values, not a key-value pair. The value of its element is its key at the same time.
  set does not allow storing duplicate values as a set can only contain unique elements. 
  On average, complexity of basic operation is O(1). It will go up to O(n) in the worst case. 
  
'''