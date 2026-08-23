# LinkedList.py

class LinkedList:
    # Node stores one package and a reference to the next node
    class Node:
        def __init__(self, package=None):
            self.package = package
            self.next = None

    def __init__(self):
        self.head = None

    # Adds a package to the end of the linked list
    def append(self, package):
        if (self.head == None):
            self.head = self.Node(package)
            return
        
        new_node = self.Node(package)
        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def remove(self, package_id):
        if (self.head == None):
            return

        # If the matching package is the head, move head to the next node
        if (self.head.package.id == package_id):
            self.head = self.head.next
            return 
        
        current = self.head

        # Search for the matching package and bypass its node when found
        while (current.next is not None):
            if current.next.package.id == package_id:
                current.next = current.next.next
                return
        
            current = current.next

    # Traverses the list and returns the package with the matching ID
    def get(self, package_id):
        if (self.head == None):
            return None

        current = self.head

        while (current is not None):
            if (current.package.id == package_id):
                return current.package

            current = current.next
        
        return None
        



    
