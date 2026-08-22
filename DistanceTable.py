# DistanceTable

import csv

class DistanceTable:
    def __init__(self):
        self.size = 27

        # matrix of all distances between each address 
        self.matrix = [[None for _ in range(self.size)] for _ in range(self.size)] 

        # list of all addresses
        self.addresses = []

    # returns the distance between two addresses provided as strings
    def get_distance_between(self, address1, address2):
        address1_index = self.get_index(address1)
        address2_index = self.get_index(address2)

        distance =  self.matrix[address1_index][address2_index]

        if distance is None:
            distance = self.matrix[address2_index][address1_index]

        return distance

    # returns the index for addresses associated with the provided address
    def get_index(self, address):
        return self.addresses.index(address)
    
    

    # assumes csv file is in specific format
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

                    # print(f"{i}-{j}: {self.matrix[i][j]}")

                i += 1

    def load_addresses(self, file_path):
        with open(file_path, 'r') as file:
            csvreader = csv.reader(file)

            for row in csvreader:
                address = row[0]
                address = address.strip("'[]")
                self.addresses.append(address)

