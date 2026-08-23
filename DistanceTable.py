# DistanceTable

import csv


# Stores all delivery addresses and the distances between them
class DistanceTable:
    def __init__(self):
        self.size = 27

        # matrix of all distances between each address 
        self.matrix = [[None for _ in range(self.size)] for _ in range(self.size)] 

        # list of all addresses
        self.addresses = []

    # Returns the distance between two addresses.
    # The distance table is triangular, so if one direction is blank,
    # the reverse direction is checked.    
    def get_distance_between(self, address1, address2):
        address1_index = self.get_index(address1)
        address2_index = self.get_index(address2)

        distance =  self.matrix[address1_index][address2_index]

        if distance is None:
            distance = self.matrix[address2_index][address1_index]

        return distance

    # Returns the index of an address in the address list.    
    def get_index(self, address):
        return self.addresses.index(address)
    
    # Loads the triangular distance table from the provided CSV file.    
    def load_distances(self, file_path):
        with open(file_path, 'r') as file:
            csvreader = csv.reader(file)

            i = 0
            for row in csvreader:
                for j in range(27):
                    distance = row[j].strip()

                    if distance == "":
                        distance = None
                    else:
                        distance = float(distance)

                    self.matrix[i][j] = distance

                i += 1

    # Loads delivery addresses from the provided CSV file.    
    def load_addresses(self, file_path):
        with open(file_path, 'r') as file:
            csvreader = csv.reader(file)

            for row in csvreader:
                address = row[0]
                address = address.strip("'[]")
                self.addresses.append(address)

