# Vincent Moreno #012508726
# main.py

from DistanceTable import DistanceTable
from PackageLoader import PackageLoader
from HashTable import HashTable
from Truck import Truck

distance_table = DistanceTable()

distance_table.load_distances("./data/distance_table.csv")
distance_table.load_addresses("./data/address_table.csv")


package_table = HashTable()
package_loader = PackageLoader(package_table)
package_loader.load_packages("./data/package_table.csv")

truck1 = Truck(1, 480, distance_table.addresses[0], distance_table)
truck2 = Truck(2, 480, distance_table.addresses[0], distance_table)
truck3 = Truck(3, 480, distance_table.addresses[0], distance_table)

package_loader.load_trucks([truck1, truck2, truck3])

truck1.deliver_packages()