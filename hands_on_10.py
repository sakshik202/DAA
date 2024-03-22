import sys

# Structure for doubly linked list node
class ListNode:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.prev = None
        self.next = None

# Structure for hash table
class HashTable:
    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.array = [None] * capacity

def create_node(key, data):
    return ListNode(key, data)

def create_hash_table(capacity):
    return HashTable(capacity)

# Multiplication method
def hash(key, capacity):
    A = 0.6180339887  # Multiplicative constant (golden ratio)
    val = key * A
    val -= int(val)
    return int(capacity * val)

# Function to insert a key-value pair into the hash table
def insert(hash_table, key, data):
    index = hash(key, hash_table.capacity)
    new_node = create_node(key, data)
    
    current = hash_table.array[index]
    if current is None:
        hash_table.array[index] = new_node
        hash_table.size += 1
        return
    
    while current.next is not None:
        current = current.next
    
    current.next = new_node
    new_node.prev = current
    hash_table.size += 1


def erase(hash_table, key):
    index = hash(key, hash_table.capacity)
    current = hash_table.array[index]
    
    while current is not None:
        if current.key == key:
            if current.prev is not None:
                current.prev.next = current.next
            else:
                hash_table.array[index] = current.next
            
            if current.next is not None:
                current.next.prev = current.prev
            
            del current
            hash_table.size -= 1
            return
        current = current.next


def search(hash_table, key):
    index = hash(key, hash_table.capacity)
    current = hash_table.array[index]
    
    while current is not None:
        if current.key == key:
            return current.data
        current = current.next
    
    return -1  # Key not found


def clear(hash_table):
    if hash_table is None:
        return
    
    for i in range(hash_table.capacity):
        current = hash_table.array[i]
        while current is not None:
            temp = current
            current = current.next
            del temp
        
        hash_table.array[i] = None
    
    del hash_table

def main():
    hash_table = create_hash_table(8)  # Initial capacity of 8
    
   
    insert(hash_table, 10, 100)
    insert(hash_table, 20, 200)
    insert(hash_table, 30, 300)
    insert(hash_table, 15, 150)
    
   
    print("Value for key 10:", search(hash_table, 10))
    print("Value for key 20:", search(hash_table, 20))
    print("Value for key 30:", search(hash_table, 30))
    print("Value for key 15:", search(hash_table, 15))
    
   
    erase(hash_table, 20)
    
    # Check if removed successfully
    print("Value for key 20 after removal:", search(hash_table, 20))
    
    # Free memory allocated for the hash table
    clear(hash_table)

if __name__ == "__main__":
    main()

