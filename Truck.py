# Truck.py

from DeliveryStatus import DeliveryStatus

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
        print(f"Truck {self.number} leaving {self.location} at {self.min_to_hr(self.current_time)}")

        distance = self.__distance_table.get_distance_between(self.location, location)
        self.update_time(distance)
        self.total_mileage += distance
        self.location = location

        print(f"Truck {self.number} arrived at {self.location} at {self.min_to_hr(self.current_time)}")

    def deliver_package(self):
        print(f"Truck {self.number} delivered Package #{self.current_delivery.id} at {self.min_to_hr(self.current_time)}")
        self.current_delivery.status = DeliveryStatus.DELIVERED

    def deliver_packages(self):
        self.nearest_neighbor_delivery(self.priority_packages)
        self.nearest_neighbor_delivery(self.packages)
        print()


    def deliver_priority_packages(self):
        self.nearest_neighbor_delivery(self.priority_packages)
    
    def deliver_non_priority_packages(self):
        self.nearest_neighbor_delivery(self.packages)

    def nearest_neighbor_delivery(self, packages):
        while (len(packages) != 0):
            closest_package = min(
                packages,
                key=lambda package: self.__distance_table.get_distance_between(
                    self.location,
                    package.full_address
                )
            )

            self.current_delivery = closest_package
            self.current_delivery.status = DeliveryStatus.EN_ROUTE
            self.travel_to(self.current_delivery.full_address)
            self.deliver_package()    
            packages.remove(self.current_delivery)
            print()


    def update_time(self, distance):
        travel_time = (distance / self.speed) * 60 # in minutes
        self.current_time += travel_time 
    
    def min_to_hr(self, minutes):
        hour = int(minutes // 60)
        minute = int(minutes % 60)

        period = "AM" if hour < 12 else "PM"

        hour = hour % 12

        if hour == 0:
            hour = 12

        return f"{hour}:{minute:02d} {period}"