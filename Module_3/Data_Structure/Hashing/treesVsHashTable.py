'''
Both data structures can be used for the same job but their performance would vary based on their programs. Let's take a look what factors we should keep in mind when 
deciding about the appropriate data structure. 

Basic Operations:
   On average, hash tables can perform insertion, deletion and search in contanst time whereas trees usually work in O(log n). However, in the worst case scenario
   hash tables comes down to O(n) but trees like AVL tree would still have worst case scenario of O(log n). 
Hash Function:
   An efficient hash table requires a smart hash function that would distribute the keys over all the space that is available to us. A tree is simpler to implement in
   regard as it acesses extra space only when it is needed and no hash function is required to optimize its structure. 

Order of Data:
   if our application needs data that needs to be in a specific format or sequence, trees would prove more useful because a BST or an AVL tree maintains order. 
   Hash tables are smarter choice if data is required in random sequence. 
'''