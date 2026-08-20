# HashTable.py

from LinkedList import LinkedList


#Hash Map implementation
class HashTable:

    def __init__(self):
        self.buckets = []
        self.__hash_size = 20 # lower number to demonstrate chaining 
        self.__size = 0

        for i in range(self.__hash_size):
            self.buckets.append(LinkedList())

    def insert(self, package):
        bucket = self.hash_function(package.id)
        self.buckets[bucket].append(package)
        self.__size += 1

    def remove(self, package_id):
        bucket = self.hash_function(package_id)
        self.buckets[bucket].remove(package_id)
        self.__size -= 1
    
    def get(self, package_id):
        bucket = self.hash_function(package_id)
        return self.buckets[bucket].get(package_id)

    def hash_function(self, package_id):
        return package_id % self.__hash_size
    