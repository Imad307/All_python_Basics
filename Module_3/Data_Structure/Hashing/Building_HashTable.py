'''
We know that, hash table are implemented using lists in python. The implementation itself is quite simple. we will use the chaining strategy along with resize opration to
avoid collision in the table. 
All elements with same hash key will be stored in a linked list at that index. In data structures, these lists are called buckets. The size of hash tables is as n*m where
n is the number of keys it can hold and m is the number of slots each bucket contains. Each slot holds a pair of key/value.

# implementation:

we will start build a simple HashEntry class, As discussed earlier, A typical hash entry consists of 3 data members: The key, the value and the reference to new entry. 
Below is the code for HashEntry.
'''
class HashEntry:
    def __init__(self, key, data):
        self.key = key
        self.value = data
        self.next = None
    def __str__(self):
        return str(entry.key) + ", " + entry.value
entry = HashEntry(5, "Imad in Educative")
print(entry)

'''
Now, we will create a HashTable class which is a collection of HashEntry objects. We will also keep track of total number of slots in the Hash Table and current size 
of the hash table. these 2 variables will come in handy when we would be resizing the table.
Here is code:
'''
class HashTable:
    def __init__(self):
        self.slots = 10 # Size of the hashtable 
        # Current entries in the table 
        # Used while resizing the table when half of the table gets filled 
        self.size = 0
        # List of HashEntry Objects (by default all None)
        self.bucket = [None] * self.slots
    # Helper Functions
    def get_size(self):
        return self.size
    def is_empty(self):
        return self.get_size() == 0

ht = HashTable()
print(ht.is_empty())

'''
The last thing we need is a hash function where a hash function maps values to a slot in the hash table. We tried out some different approaches in previous lessons. 
For our implementation, we will simple take the modular of the key with the total size of hash table(slots).
Here is the code:

'''
def get_index(self, key):
    hash_code = hash(key) # Hash is a built in function in python
    index = hash_code % self.slots 
    return index
'''Our Hash Table is ready. As Always, the next step is to implement the operations of search, insertion and deletion one by one.'''

