# NearestNeighboy.py

from Truck import Truck

class NearestNeighbor:
    def __init__(self, trucks):
        self.trucks = trucks

    def deliver_packages(self):
        for truck in self.trucks:
            while (truck.is_empty() == False):
                