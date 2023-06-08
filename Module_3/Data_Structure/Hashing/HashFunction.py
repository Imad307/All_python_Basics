'''
we learned that a list can be used to implement a hash table in Python. A key is used to map a value on the list and the efficiency of a hash table depends on how a key 
is computed. At first glance, you may observe that we can directly use the indices as keys because each index is unique.

The only problem is that the key would eventually exceed the size of the list and, at every insertion, the list would need to be resized. Syntactically,
we can easily increase list size in Python, but as we learned before, the process still takes O(n) time at the back end.

In order to limit the range of the keys to the boundaries of the list, we need a function that converts a large key into a smaller key. 
This is the job of the hash function.

A hash function simply takes an item’s key and returns the corresponding index in the list for that item. Depending on your program, 
the calculation of this index can be a simple arithmetic or a very complicated encryption method.
However, it is very important to choose an efficient hashing function as it directly affects the performance of the hash table mechanism.

Let’s have a look at some of the most common hash functions used in modern programming.

1. Arithmetic Modular: 
In This Approach, we take modular of key with the list size:
   index = key MOD table_size 
Hence, the index will always stay between 0 and tableSize - 1.

'''
def hash_modular(key, size):
    return (key % size)

lst = [None] * 10 # List of size 10
key = 35
index = hash_modular(key, len(lst))
print("the index for key: " + str(key) + " is " + str(index))


'''
2. truncation:
   select a part of key instead of whole key. Once again, we can use mod function for this operation, although it does not need to be based on list size:
   key = 123456 -> index = 456
'''

def hash_trunc(key):
    return (key % 1000)  # Will always give us a key of upto 3 digits
key = 123456

index = hash_trunc(key)
print("The index for key " + str(key) + " is " + str(index))

'''
Folding:
  Divide the key in to small chunks then perform an arithmetic operation at those chunks. -i-e- Add smaller chunks together.
  key = 456789, chunk_size=2 -> index = 45+67+89
'''
def hash_fold(key, chunk_size):
    str_key = str(key)
    print("Key: " + str(key))
    hash_value = 0
    print("Chunks: ")
    for i in range(0, len(str_key), chunk_size):
        if (i+chunk_size < len(str_key)):
            print(str_key[i: i + chunk_size])
            hash_value += int(str_key[i: i + chunk_size])
        else:
            print(str_key[i: len(str_key)])
            hash_value += int(str_key[i: len(str_key)])
    return hash_value

key = 4567899
chunk_sixe = 2
print(hash_fold(key, chunk_sixe))
