# PackageLoader.py

import csv

from DeliveryStatus import DeliveryStatus
from RestrictionType import RestrictionType
from Package import Package

class PackageLoader:
    def __init__(self, hash_table):
        self.package_table = hash_table
        self.package_ids = []

    def load_packages(self, file_path):
        with open(file_path, "r") as file:
            csvreader = csv.reader(file)

            for row in csvreader:
                package = self.create_package(row)
                self.package_table.insert(package)
                self.package_ids.append(package.id)


    def create_package(self, row):
        package_id = int(row[0])
        package = Package(package_id)

        package.address = row[1]
        package.city = row[2]
        package.zip = row[4]
        package.weight = row[6]
        package.full_address = f"{row[1]} ({row[4]})"

        if (row[5] != "EOD"):
            package.deadline = self.hr_to_min(row[5])

        if row[7] != "":
            self.parse_note(package, row[7])

        if (package.restriction_type == RestrictionType.DELAYED_UNTIL):
            package.status = DeliveryStatus.DELAYED
        else:
            package.status = DeliveryStatus.AT_HUB


        return package


    def parse_note(self, package, notes):
        package.note = notes.split(":")

        match package.note[0]:
            case "401":
                package.restriction_type = RestrictionType.REQUIRED_TRUCK
            case "402":
                package.restriction_type = RestrictionType.DELIVER_WITH
            case "403":
                package.restriction_type = RestrictionType.DELAYED_UNTIL
            case "404":
                package.restriction_type = RestrictionType.WRONG_ADDRESS

        if "," in package.note[1]:
            package.restriction_data = package.note[1].split(",")
            for value in range(len(package.restriction_data)):
                package.restriction_data[value] = int(package.restriction_data[value])
        else:
            package.restriction_data = int(package.note[1])
            

    def hr_to_min(self, time):
        time = time.strip().lower()

        time_part, period = time.split()
        hour, minute = time_part.split(":")

        hour = int(hour)
        minute = int(minute)

        if period == "pm" and hour != 12:
            hour += 12
        elif period == "am" and hour == 12:
            hour = 0

        return (hour * 60) + minute        

    def load_trucks(self, trucks):
        truck1 = None
        truck2 = None
        truck3 = None

        for truck in trucks:
            if truck.number == 1:
                truck1 = truck
            elif truck.number == 2:
                truck2 = truck
            elif truck.number == 3:
                truck3 = truck

        # Manual package assignments
        truck1_ids = [
            1, 4, 7, 13, 14, 15, 16, 19,
            20, 21, 29, 31, 34, 39, 40
        ]

        truck2_ids = [
            2, 3, 5, 8, 18,
            30, 33, 36, 37, 38
        ]

        truck3_ids = [
            6, 9, 10, 11, 12, 17, 22, 23,
            24, 25, 26, 27, 28, 32, 35
        ]

        # Load Truck 1
        for package_id in truck1_ids:
            package = self.package_table.get(package_id)

            if package.deadline is not None:
                truck1.priority_packages.append(package)
            else:
                truck1.packages.append(package)

        # Load Truck 2
        for package_id in truck2_ids:
            package = self.package_table.get(package_id)

            if package.deadline is not None:
                truck2.priority_packages.append(package)
            else:
                truck2.packages.append(package)

        # Load Truck 3
        for package_id in truck3_ids:
            package = self.package_table.get(package_id)

            if package.deadline is not None:
                truck3.priority_packages.append(package)
            else:
                truck3.packages.append(package)



