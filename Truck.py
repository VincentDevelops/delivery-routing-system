# Truck.py

from DeliveryStatus import DeliveryStatus

# Represents one delivery truck and tracks packages, time, location, and mileage
class Truck:
    def __init__(self, truck_number, time, location, distance_table, package_table):
        
        self.__number = truck_number
        self.__start_time = time
        self.__speed = 18 # mph
        self.__distance_table = distance_table
        self.__package_table = package_table

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

    # Moves truck to a new location and updates time and mileage
    def travel_to(self, location):
        distance = self.__distance_table.get_distance_between(self.location, location)
        self.update_time(distance)
        self.total_mileage += distance
        self.location = location

    # Marks current package as delivered and records delivery time
    def deliver_package(self):
        self.current_delivery.status = DeliveryStatus.DELIVERED
        self.current_delivery.delivery_time = self.current_time

    def deliver_packages(self):
        self.nearest_neighbor_delivery(self.priority_packages)
        self.nearest_neighbor_delivery(self.packages)

    def deliver_priority_packages(self):
        self.nearest_neighbor_delivery(self.priority_packages)
    
    def deliver_non_priority_packages(self):
        self.nearest_neighbor_delivery(self.packages)

    # Delivers packages using the nearest neighbor algorithm
    def nearest_neighbor_delivery(self, packages):
        while (len(packages) != 0):
            # Updates package 9 address once the corrected address becomes available
            if self.current_time >= 620:
                pkg = self.__package_table.get(9)
                if pkg.address != "410 S State St":
                    pkg.address = "410 S State St"
                    pkg.city = "Salt Lake City"
                    pkg.zip = "84111"
                    pkg.full_address = "410 S State St (84111)"

            # Finds the package with the shortest distance from the truck's current location
            closest_package = min(
                packages,
                key=lambda package: self.__distance_table.get_distance_between(
                    self.location,
                    package.full_address
                )
            )

            self.current_delivery = closest_package
            self.travel_to(self.current_delivery.full_address)
            self.deliver_package()    
            packages.remove(self.current_delivery)


    # Updates truck time based on distance traveled at 18 mph
    def update_time(self, distance):
        travel_time = (distance / self.speed) * 60 # in minutes
        self.current_time += travel_time 
    
    # Converts minutes since midnight into a readable clock time
    def min_to_hr(self, minutes):
        hour = int(minutes // 60)
        minute = int(minutes % 60)

        period = "AM" if hour < 12 else "PM"

        hour = hour % 12

        if hour == 0:
            hour = 12

        return f"{hour}:{minute:02d} {period}"
    
    # Marks loaded packages as en route and records their departure time
    def set_packages_en_route(self, packages):
        for package in packages:
            package.status = DeliveryStatus.EN_ROUTE
            package.departure_time = self.current_time