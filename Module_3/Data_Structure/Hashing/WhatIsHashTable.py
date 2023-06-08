'''
Until now, overall time complexity for most of data structures in Insertion, deltion and searching has been O(logn) or O(nlogn) which is pretty good but for large number
of data that is still not that effient as it will still limit the efficiency of the Algorithm. 
Ideal Data Stuructue is that has O(1) time complexity for all 3 operations. that is hshing comes into play.

Hashing is a process used to store data using unique key. This means hashing use key-value pairs for storing it's data. A coolection of such pairs called Dictionary.
By using this, every object or value can be looked easily. So, we can use this for search operation that will give us O(1)  constant time. 

Concept of Hashing gave birth to many data structues but most prominent one is Hash Tables.

Hash tables:
If one's algorithm prioritizes search operations then hash tables is best data structure for it.
In python, hash tables are generally implemented using lists as they provide element searching in o(1) time complexity.
In Python, we have several built in data typres such as set or dict which can provide hash table functionality.

performance of hash tables depends on 3 fundamental factors:
1. Hash Fuction
2. Size of Hash table
3. Collision Handling Method


'''