# Vincent Moreno #012508726
# main.py

from DistanceTable import DistanceTable
from PackageLoader import PackageLoader
from HashTable import HashTable
from RestrictionType import RestrictionType
from Truck import Truck

#load distances and addresses from csv file
distance_table = DistanceTable()
distance_table.load_distances("./data/distance_table.csv")
distance_table.load_addresses("./data/address_table.csv")

#load all packages from csv file
package_table = HashTable()
package_loader = PackageLoader(package_table)
package_loader.load_packages("./data/package_table.csv")

#instantiage three trucks
truck1 = Truck(1, 480, distance_table.addresses[0], distance_table, package_table)
truck2 = Truck(2, 480, distance_table.addresses[0], distance_table, package_table)
truck3 = Truck(3, 480, distance_table.addresses[0], distance_table, package_table)

#load all packages into three trucks 
package_loader.load_trucks([truck1, truck2, truck3])

#truck 1 completes all deliveries
truck1.set_packages_en_route(truck1.priority_packages)
truck1.set_packages_en_route(truck1.packages)
truck1.deliver_priority_packages()
truck1.deliver_non_priority_packages()
truck1.travel_to(distance_table.addresses[0])

#truck 2 delivers all packages with deadline and returns to hub
truck2.set_packages_en_route(truck2.priority_packages)
truck2.deliver_priority_packages()
truck2.travel_to(distance_table.addresses[0])

#driver from truck 2 waits for delayed packages 
# before going on delivery with truck 3
truck3.current_time = truck2.current_time
truck3.current_time += 15
truck3.set_packages_en_route(truck3.priority_packages)
truck3.set_packages_en_route(truck3.packages)
truck3.deliver_priority_packages()
truck3.deliver_non_priority_packages()

#driver from truck 1 hops onto truck 2 to complete its non priority packages
truck2.current_time = truck1.current_time
truck2.set_packages_en_route(truck2.packages)
truck2.deliver_non_priority_packages()

#all miles have been delivered
total_miles = truck1.total_mileage + truck2.total_mileage + truck3.total_mileage

def valid_time(time):
    try:
        time = time.strip().lower()

        time_part, period = time.split()
        hour, minute = time_part.split(":")

        hour = int(hour)
        minute = int(minute)

        if period not in ("am", "pm"):
            return False

        if hour < 1 or hour > 12:
            return False

        if minute < 0 or minute > 59:
            return False

        return True

    except ValueError:
        print("Invalid Time")
        return False
    

def main_menu():
    while True:
        print("\nWGUPS ROUTING PROGRAM")
        print("---------------------")
        print("1. View Package")
        print("2. View All Packages")
        print("3. View Mileage")
        print("4. Exit")

        choice = input("\nEnter selection: ")

        match choice:
            case "1":
                view_package_menu()

            case "2":
                view_all_packages_menu()

            case "3":
                view_mileage()

            case "4":
                print("Exiting program.")
                break

            case _:
                print("Invalid selection. Please enter a value between 1 - 4.")


def view_package_at_time(package_id, time):
    if not valid_time(time):
        return
    
    display_package(package_id, time)

def view_package_history(package_id):
    display_package(package_id, None)

def view_package_menu():
    while True:
        package_id = input("\nEnter package number (1 - 40): ")

        if package_id.isdigit():
            package_id = int(package_id)

            if 1 <= package_id <= 40:
                break

        print("Package number must be a valid value between 1 - 40.")

    print("\n1. View package at a specific time")
    print("2. View entire package history")

    while True:
        choice = input("\nEnter selection: ")

        match choice:
            case "1":
                time = input("Enter time (example: 9:30 AM): ")

                view_package_at_time(package_id, time)

                break

            case "2":
                view_package_history(package_id)

                break

            case _:
                print("Invalid selection. Please enter 1 or 2.")


def display_package(package_id, time):
    if time is not None:
        print(f"Package Status at {time}")

    package = package_table.get(package_id)

    print("----------------------------------------")
    print(f"Package #{package.id}")
    print(f"Truck:       #{package.assigned_to_truck}")

    # Display entire package history
    if time is None:
        print(f"Address:     {package.address}")
        print(f"City:        {package.city}")
        print(f"ZIP:         {package.zip}")
        print(f"Weight:      {package.weight}")

        if package.deadline is None:
            print("Deadline:    EOD")
        else:
            print(f"Deadline:    {truck1.min_to_hr(package.deadline)}")

        print()

        if package.restriction_type == RestrictionType.DELAYED_UNTIL:
            print(f"Delayed Until: {truck1.min_to_hr(package.restriction_data)}")

        print(f"Departed:      {truck1.min_to_hr(package.departure_time)}")
        print(f"Delivered:     {truck1.min_to_hr(package.delivery_time)}")
        print("----------------------------------------")
        return

    # Convert requested clock time to minutes since midnight
    time = package_loader.hr_to_min(time)

    # Package #9 had the wrong address until 10:20 AM
    if package.id == 9 and time < 620:
        print("Address:     300 State St")
        print("City:        Salt Lake City")
        print("ZIP:         84103")
    else:
        print(f"Address:     {package.address}")
        print(f"City:        {package.city}")
        print(f"ZIP:         {package.zip}")

    print(f"Weight:      {package.weight}")

    if package.deadline is None:
        print("Deadline:    EOD")
    else:
        print(f"Deadline:    {truck1.min_to_hr(package.deadline)}")

    print()

    # Package is still delayed
    if (
        package.restriction_type == RestrictionType.DELAYED_UNTIL
        and time < package.restriction_data
    ):
        print("Status:      DELAYED")
        print(f"Available:   {truck1.min_to_hr(package.restriction_data)}")

    # Package has not left the hub yet
    elif time < package.departure_time:
        print("Status:      AT HUB")

    # Package has left the hub but has not been delivered
    elif time < package.delivery_time:
        print("Status:      EN ROUTE")
        print(f"Departed:    {truck1.min_to_hr(package.departure_time)}")

    # Package has already been delivered
    else:
        print("Status:      DELIVERED")
        print(f"Delivered:   {truck1.min_to_hr(package.delivery_time)}")

    print("----------------------------------------")


#display all packages at a specific time
def view_all_packages_at_time(time):
    if not valid_time(time): return

    for i in range(1, 41):
        display_package(i, time)
        print()

#display all the history of all packages
def view_all_package_history():
    for i in range(1, 41):
        display_package(i, None)
        print()

def view_all_packages_menu():
    print("\n1. View all packages at a specific time")
    print("2. View entire delivery history")

    while True:
        choice = input("\nEnter selection: ")

        match choice:
            case "1":
                time = input("Enter time (example: 9:30 AM): ")
                view_all_packages_at_time(time)

                break

            case "2":
                view_all_package_history()

                break

            case _:
                print("Invalid selection. Please enter 1 or 2.")


def view_mileage():
    print(f"Truck #1 total mileage: {truck1.total_mileage:.1f} miles")
    print(f"Truck #2 total mileage: {truck2.total_mileage:.1f} miles")
    print(f"Truck #3 total mileage: {truck3.total_mileage:.1f} miles")
    print(f"Total Mileage: {total_miles:.1f} miles")



main_menu()
