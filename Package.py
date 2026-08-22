# Package.py

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
        self.delivery_time = None
        self.full_address = None
        self.assigned_to_truck = None

    @property
    def id(self):
        return self.__id