# HashTable.py

from LinkedList import LinkedList


# Hash table implementation using separate chaining with LinkedList buckets
class HashTable:

    def __init__(self):
        self.buckets = []
        self.__hash_size = 20 # lower number to demonstrate chaining 
        self.__size = 0

        # Each bucket contains a linked list so multiple packages can share a bucket
        for i in range(self.__hash_size):
            self.buckets.append(LinkedList())

    # Hashes the package ID and inserts the package into the corresponding bucket
    def insert(self, package):
        bucket = self.hash_function(package.id)
        self.buckets[bucket].append(package)
        self.__size += 1

    def remove(self, package_id):
        bucket = self.hash_function(package_id)
        self.buckets[bucket].remove(package_id)
        self.__size -= 1
    
    # Uses the package ID to locate the correct bucket and search its linked list
    def get(self, package_id):
        bucket = self.hash_function(package_id)
        return self.buckets[bucket].get(package_id)

    # Division hashing: package ID modulo table size determines the bucket index
    def hash_function(self, package_id):
        return package_id % self.__hash_size
    