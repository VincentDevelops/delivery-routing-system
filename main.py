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

truck1 = Truck(1, 480, distance_table.addresses[0], distance_table, package_table)
truck2 = Truck(2, 480, distance_table.addresses[0], distance_table, package_table)
truck3 = Truck(3, 480, distance_table.addresses[0], distance_table, package_table)

package_loader.load_trucks([truck1, truck2, truck3])

#truck 1 completes all deliveries
truck1.set_packages_en_route(truck1.priority_packages)
truck1.set_packages_en_route(truck1.packages)
truck1.deliver_priority_packages()
truck1.deliver_non_priority_packages()
truck1.travel_to(distance_table.addresses[0])
print(f"TRUCK 1 HAS COMPLETED ALL DELIVERIES AT {truck1.min_to_hr(truck1.current_time)} WITH A TOTAL OF {truck1.total_mileage:.1f} MILES")
print()
print()


#truck 2 delivers all packages with deadline and returns to hub
truck2.set_packages_en_route(truck2.priority_packages)
truck2.deliver_priority_packages()
truck2.travel_to(distance_table.addresses[0])
print()
print()

#driver from truck 2 takes a 15 minute break and hops onto truck 3 to complete its packages, and returns to hub
truck3.current_time = truck2.current_time
truck3.current_time += 15
truck3.set_packages_en_route(truck3.priority_packages)
truck3.set_packages_en_route(truck3.packages)
truck3.deliver_priority_packages()
truck3.deliver_non_priority_packages()
print(f"TRUCK 3 HAS COMPLETED ALL DELIVERIES AT {truck3.min_to_hr(truck3.current_time)} WITH A TOTAL OF {truck3.total_mileage} MILES")
print()
print()


#driver from truck 1 hops onto truck 2 to complete its non priority packages
truck2.current_time = truck1.current_time
truck2.set_packages_en_route(truck2.packages)
truck2.deliver_non_priority_packages()
truck2.travel_to(distance_table.addresses[0])
print(f"TRUCK 2 HAS COMPLETED ALL DELIVERIES AT {truck2.min_to_hr(truck2.current_time)} WITH A TOTAL OF {truck2.total_mileage} MILES")
print()
print()

total_miles = truck1.total_mileage + truck2.total_mileage + truck3.total_mileage
print(f"ALL DELIVERIES COMPLETED IN {total_miles} MILES ")