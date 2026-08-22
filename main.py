# Vincent Moreno #012508726
# main.py

from DistanceTable import DistanceTable
from PackageLoader import PackageLoader
from HashTable import HashTable

table = DistanceTable()

table.load_distances("./data/distance_table.csv")
table.load_addresses("./data/address_table.csv")



package_table = HashTable()
package_loader = PackageLoader(package_table)

package_loader.load_packages("./data/package_table.csv")

town1 = package_loader.package_ids[0]
town2 = package_loader.package_ids[4]
print(town1)
print(town2)

town1 = package_table.get(town1).full_address
town2 = package_table.get(town2).full_address


print(table.get_distance_between(town1, town2))

print()