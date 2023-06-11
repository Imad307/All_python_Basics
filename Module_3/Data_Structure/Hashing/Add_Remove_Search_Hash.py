class HashEntry:
    def __init__(self, key, data):
        self.key = key
        self.value = data
        self.next = None
    def __str__(self):
        return str(entry.key) + ", " + entry.value
class HashTable:
    def __init__(self):
        self.slots = 10
        self.size = 0
        self.bucket = [None] * self.slots
        self.threshold = 0.6
    def get_size(self):
        return self.size
    def is_empty(self):
        return self.get_size() == 0
    def get_index(self, key):
        hash_code = hash(key)
        index = hash_code % self.slots
        return index
    def resize(self):  # Resize the list to avaoid the collision.
        new_slots = self.slots*2
        new_bucket = [None] * new_slots
        # rehash all the items into new slots
        for items in self.bucket:
            head = items
            while head is not None:
                new_index = hash(head.key) % new_slots
                if new_bucket[new_index] is None:
                    new_bucket[new_index] = HashEntry(head.key, head.value)
                else:
                    node = new_bucket[new_index]
                    while node is not None:
                        if node.key is head.key:
                            node.value = head.value 
                            node = None
                        elif node.next is None:
                            node.next = HashEntry(head.key, head.value)
                            node = None
                        else:
                            node = node.next

                head = head.next
        self.bucket = new_bucket
        self.slots = new_slots
    def insert(self, key, value): # Insert the value using the key 
        # Find the nodes with the given key
        b_index = self.get_index(key)
        if self.bucket[b_index] is None:
            self.bucket[b_index] = HashEntry(key, value)
            print(key, "-", value, "Inserted at index: ", b_index)
            self.size+=1
        else:
            head = self.bucket[b_index]
            while head is not None:
                if head.key == key:
                    head.value = value
                    break
                elif head.next is None:
                    head.next = HashEntry(key, value)
                    print(key, "-", value, "Inserted at index: ", b_index)
                    self.size+=1
                    break
                head = head.next
        load_factor =  float(self.size)/ float(self.slots)
        if load_factor>= self.threshold:
            self.resize()
    def search(self, key):
        b_index = self.get_index(key)
        head = self.bucket[b_index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None
    def delete(self, key): # Remove a value based on key
        b_index = self.get_index(key)
        head = self.bucket[b_index]
        if head.key == key:
            self.bucket[b_index] = head.next
            print(key, "-", head.value, "Deleted")
            self.size-=1
            return
        prev = None
        while head is not None:
            if head.key == key:
                prev.next = head.next
                print(key, "-", head.value, "Deleted")
                self.size-=1
                return
            prev = head
            head = head.next

        print("Key not found")
        return
    
         

entry = HashEntry()