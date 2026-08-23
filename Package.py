# Package.py

# Represents a single delivery package and stores all data
# needed for routing, restrictions, status, and delivery history
class Package:
    def __init__(self, id):
        self.__id = id
        self.address = None
        self.city = None
        self.zip = None
        self.weight = None
        self.deadline = None
        self.status = None
        self.note = None
        self.restriction_type = None
        self.restriction_data = None
        self.departure_time = None
        self.delivery_time = None
        self.full_address = None
        self.assigned_to_truck = None

    # Package ID is read-only after creation
    @property
    def id(self):
        return self.__id