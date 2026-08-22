# Vincent Moreno #012508726
# main.py

from DistanceTable import DistanceTable

table = DistanceTable()

table.load_distances("./data/distance_table.csv")
table.load_addresses("./data/address_table.csv")

print(table.get_distance_between("177 W Price Ave (84115)","195 W Oakland Ave (84115)"))