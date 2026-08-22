# Package.py

# delivery address
# delivery deadline
# delivery city
# delivery zip code
# package weight
# delivery status (i.e., delayed, at the hub, en route, or delivered), including the delivery time


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

    @property
    def id(self):
        return self.__id