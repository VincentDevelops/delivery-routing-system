# Truck.py

class Truck:
    def __init__(self, truck_number, time, location, distance_table):
        
        self.__number = truck_number
        self.__start_time = time
        self.__speed = 18 #mph
        self.__distance_table = distance_table

        self.packages = []
        self.priority_packages = []
        self.current_delivery = None

        self.current_time = self.__start_time        
        self.location = location

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
        return len(self.packages) == 0

    def travel_to(self, location):
        distance = self.__distance_table.get_distance_between(self.location, location)
        self.update_time(distance)
        self.location = location

    def deliver_package():
        ...
    
    def update_time(self, distance):
        travel_time = (distance / self.speed) * 60 # in minutes
        self.current_time += travel_time 



# load trucks
#  - go through packages


    
    