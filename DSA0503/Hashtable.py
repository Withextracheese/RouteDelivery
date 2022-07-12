# Hash table class and helper functions to manipulate the hashtable.
class ChainingHashTable:
    def __init__(self, initial_capacity=10):

        self.map = []
        for i in range(initial_capacity):
            self.map.append([])

    # Time complexity: O(1)
    def gethash(self, key):
        bucket = int(key) % len(self.map)
        return bucket

    # Look through hash table for key and if found return it
    # Time complexity: O(N)^2
    def insert(self, key, item):  # does both insert and update

        bucket = hash(key) % len(self.map)
        bucket_list = self.map[bucket]

        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Time complexity: O(N)
    def get(self, key):
        key_hash = self.gethash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    # Searches for an item with matching key
    # Time complexity: O(N)
    def search(self, key):

        bucket = hash(key) % len(self.map)
        bucket_list = self.map[bucket]
        # print(bucket_list)

        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                return kv[1]  # value
        return None

    # Removes an item
    # Time complexity: O(N)
    def remove(self, key):

        bucket = hash(key) % len(self.map)
        bucket_list = self.map[bucket]

        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])



