# Truck.py

class Truck:
    def __init__(self, truck_number, time, location, distance_table):
        
        self.__number = truck_number
        self.__start_time = time
        self.__speed = 18 # mph
        self.__distance_table = distance_table
        self.__capacity = 16 # max amount of packages per truck

        self.packages = []
        self.priority_packages = []
        self.current_delivery = None

        self.current_time = self.__start_time        
        self.location = location
        self.total_mileage = 0

    @property
    def number(self):
        return self.__number

    @property
    def speed(self):
        return self.__speed
    
    @property
    def start_time(self):
        return self.__start_time

    def is_empty(self):
        return len(self.packages) == 0 and len(self.priority_packages) == 0

    def travel_to(self, location):
        distance = self.__distance_table.get_distance_between(self.location, location)
        self.update_time(distance)
        self.total_mileage += distance
        self.location = location
        print(f"Traveled to {self.location}")
        print(f"Current Time: {self.current_time}")

    def deliver_package(self):
        print(f"Truck: {self.number}")
        print(f"Package: {self.current_delivery.id}")
        print(f"Delivery Time: {self.current_time}")

    # deliver packages using the nearest neighbor algorithm
    def deliver_packages(self):
        while (len(self.priority_packages) != 0):
            lowest_distance = 10000
            self.current_delivery = self.priority_packages
            closest_package = min(
                self.priority_packages,
                key=lambda package: self.__distance_table.get_distance_between(
                    self.location,
                    package.full_address
                )
            )

            self.current_delivery = closest_package
            self.travel_to(self.current_delivery.full_address)
            self.deliver_package()    
            self.priority_packages.remove(self.current_delivery)

        while (len(self.packages) != 0):
            ...

    def nearest_neighbor_delivery(self, packages):
        while (len(self.priority_packages) != 0):
            lowest_distance = 10000
            self.current_delivery = self.priority_packages
            closest_package = min(
                self.priority_packages,
                key=lambda package: self.__distance_table.get_distance_between(
                    self.location,
                    package.full_address
                )
            )

            self.current_delivery = closest_package
            self.travel_to(self.current_delivery.full_address)
            self.deliver_package()    
            self.priority_packages.remove(self.current_delivery)
            return

    def update_time(self, distance):
        travel_time = (distance / self.speed) * 60 # in minutes
        self.current_time += travel_time 
    
    