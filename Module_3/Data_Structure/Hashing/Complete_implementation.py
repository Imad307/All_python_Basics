class HashEntry:
    def __init__(self, key, data):
        self.key = key
        self.value = data
        self.next = None    

class HashTable:
    def __init__(self):
        self.slots = 10
        self.size = 0
        self.bucket = [None] * self.slots
        self.threshold = 0.6
    def get_size(self):
        return self.size
    def is_empty(self):
        return self.get_size() ==0
    def get_index(self, key):
        hash_code = hash(key)
        index = hash_code % self.slots
        return index
    def resize(self):
        new_slots = 2*self.slots
        new_bucket = [None] * new_slots
        for item in self.bucket:
            head = item
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
                            node =  node.next
                head = head.next
        self.bucket= new_bucket
        self.slots = new_slots
    def insert(self, key, value):
        b_index = self.get_index(key)
        if self.bucket[b_index] is None:
            self.bucket[b_index] = HashEntry(key, value)
            self.size+=1
        else:
            head = self.bucket[b_index]
            while head is not None:
                if head.key ==key:
                    head.value = value
                    break
                elif head.next is None:
                    head.next = HashEntry(key, value)
                    self.size+=1
                    break
                head = head.next

        load_factor = float(self.size)/ float(self.slots)
        if load_factor>=self.threshold:
            self.resize()
    def search(self, key):
        b_index = self.get_index(key)
        head = self.bucket[b_index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        print("Key not found")
        return None
    def delete(self, key):
        b_index = self.get_index(key)
        head = self.bucket[b_index]
        if head.key == key:
            self.bucket[b_index] = head.next
            self.size-=1
            return self
        
        prev = None

        while head is not None:
            if head.key == key:
                prev.next =  head.next
                self.size-=1
                return
            prev = head
            head = head.next
        return


table = HashTable()
print(table.is_empty())
table.insert("this", 1)
table.insert("is", 2)
table.insert("a", 3)
table.insert("Test", 4)
table.insert("Drive", 5)
print("Table Size: "+ str(table.get_size()))
print("The value for 'is' key is: " + str(table.search("is")))
table.delete("is")
table.delete("a")
print("Table Size: " + str(table.get_size()))


