class LinkedList:
    def __init__(self):
        self.head = None

    # print contents of linked list
    def __str__(self):
        currStr = ""
        curr = self.head
        while curr is not None:
            currStr += f'{str(curr.value)} -> '
            curr = curr.next
        return currStr

    # find and return node with given value
    def find_value(self, value):
        curr = self.head
        while curr is not None:
            if curr.value == value:
                return curr
            curr = curr.next
        return None

    # find and return node with given key
    def find_key(self, key):
        curr = self.head
        while curr is not None:
            if curr.key == key:
                return curr
            curr = curr.next
        return None

    # deletes node w/ given key and returns its node
    def delete(self, key):
        curr = self.head
        prev = None

        # special case if we need to delete the head
        if curr.key == key:
            self.head = curr.next
            curr.next = None
            return curr

        while curr is not None:
            if curr.key == key:
                prev.next = curr.next
                curr.next = None
                return curr
            else:
                prev = curr
                curr = curr.next

        return None

    # insert given node at head of list
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    # overwrite node or insert node at head
    def insert_at_head_or_overwrite(self, node):
        existingNode = self.find_key(node.key)

        if existingNode is not None:
            existingNode.value = node.value
            return False
        else:
            self.insert_at_head(node)
            return True

    # Return True/False if head is None
    def is_head_not_none(self):
        if self.head is not None:
            return True
        else:
            return False

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.num_elements = 0
        self.table = self.create_new_hash_table(self.capacity)

    def create_new_hash_table(self, capacity):
        new_table = []
        for i in range(capacity):
            new_table.append(LinkedList())
        return new_table

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        count = 0
        for ll in self.table:
            count += ll.is_head_not_none()
        return count / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.

        Source: https://github.com/sup/pyhash/blob/master/pyhash/pyhash.py
        """

        #Constants
        FNV_prime = 1099511628211
        offset_basis = 14695981039346656037
        seed = 0

        #FNV-1a Hash Function
        hash = offset_basis + seed
        for char in key:
            hash = hash * FNV_prime
            hash = hash ^ ord(char)
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity


    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # self.table[self.hash_index(key)] = value

        ll = self.table[self.hash_index(key)]

        if ll is not None:
            did_add_new_node = ll.insert_at_head_or_overwrite(
                HashTableEntry(key, value))
            if did_add_new_node:
                self.num_elements += 1
        else:
            ll.insert_at_head(HashTableEntry(key, value))
            self.num_elements += 1

        if self.get_load_factor() > 0.7:
            self.resize(self.get_num_slots() * 2)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # if self.table[self.hash_index(key)] == None:
        #     return 'Value in hash table at specified key is already equal to None'
        # self.table[self.hash_index(key)] = None

        ll = self.table[self.hash_index(key)]

        if ll is not None:
            did_delete_node = ll.delete(key)
            if did_delete_node is not None:
                self.num_elements -= 1
        else:
            print(f"the key '{key}' is not found in the hash table")


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # if self.table[self.hash_index(key)] == None:
        #     return
        # return self.table[self.hash_index(key)]

        entry = self.table[self.hash_index(key)].find_key(key)

        if entry is None:
            return None
        else:
            return entry.value


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """

        store_old_table = self.table
        self.capacity = new_capacity
        self.table = self.create_new_hash_table(new_capacity)

        for ll in store_old_table:
            if ll.is_head_not_none:
                curr_node = ll.head
                while curr_node is not None:
                    hash_index = self.hash_index(curr_node.key)
                    key = curr_node.key
                    value = curr_node.value

                    if self.table[hash_index] is not None:
                        did_add_new_node = self.table[hash_index].insert_at_head_or_overwrite(
                            HashTableEntry(key, value))
                        if did_add_new_node:
                            self.num_elements += 1
                    else:
                        self.table[hash_index].insert_at_head(
                            HashTableEntry(key, value))
                        self.num_elements += 1

                    curr_node = curr_node.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))
