# LinkedList.py

class LinkedList:
    class Node:
        def __init__(self, package=None):
            self.package = package
            self.next = None

    def __init__(self):
        self.head = None

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

        # If the package is at the head
        if (self.head.package.id == package_id):
            self.head = self.head.next
            return 
        
        current = self.head

        while (current.next is not None):
            if current.next.package.id == package_id:
                current.next = current.next.next
                return
        
            current = current.next

    def get(self, package_id):
        if (self.head == None):
            return None

        current = self.head

        while (current is not None):
            if (current.package.id == package_id):
                return current.package

            current = current.next
        
        return None
        



    
