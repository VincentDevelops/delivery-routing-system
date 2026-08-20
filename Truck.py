# Truck.py

class Truck:
    def __init__(self, truck_number, time, location):
        self.__number = truck_number
        self.__start_time = time
        self.__speed = 18 #mph
        self.packages = []
        self.current_time = self.__start_time        
        self.location = location
    
    def is_empty(self):
        return len(self.packages) == 0

    
    