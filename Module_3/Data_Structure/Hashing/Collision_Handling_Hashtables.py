'''
When you map large keys into small range of numbers from 0 to N, where N is the size of list, there is huge possiblilty that two keys will return same index,
This phenomenon is called Collision.

Strategies to handle Collision:
1. Linnear Probing
2. Chaining
3. Resizing the list

1. Linear Probing:
   This strategy suggests that if our hash function returns an index that is already filled, move to the next index. This increment can be based on a fixed offset value to
   an already computed index. If that index is also occupied, traverse further until a spot is found. 
   One drawback of this strategy is that if we do not pick an offset value wisely, we can end up back where we started and hence miss out on so many possible positions
   in the list. 

2. Chaining:
   In chaining, each slot of hash table holds a pointer to another data structure such as linked list or tree. Every entry at that index will be inserted into linked
   list at that index.
   Chaining allows us to have multiple key-value pairs at the same index with constant time(insert at head of linked list)
   This strategy graetly increases performance, but it is costly in terms of space.

3. Resizing the list:
   Another way to avoid collision is to resize the list. we can set a threshold and once it is crossed, we can create a new table which is twice the size of original table
   All we have to do is copy the elements from the previous table.
   Resizing the list significantly reduces the collisions, but function itself is costly. Therefore, we need to be careful about setting of thrashold. A typical convention
   is to set the threshold at 0.6, which means that when table is filled 60% then resize option needs to take place. 
   Another factor to keep in mind is the content of hash table.The stored contents might be concentrated at one region leaving rest of list empty and you will end up 
   resizing the list inappropriately.
Some other strategies to handle collision are: quadratic probing, bucket method, randon probing, key rehashing. we must use a strategy that best suits the 
hashing algorithm and size of data we plan to store. 
  
'''