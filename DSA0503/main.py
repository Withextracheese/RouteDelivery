# Keagan Farniok
# Student ID: 008473349
# 05/11/2021

import datetime
import Package
from Truck import Truckinfo
import CSVinfo


hashh = Package.myHash


# This algorithm will find the truck route.
# it finds the closest delivery address.
# Greedy algorithm which finds minimum distance
# Time complexity: O(N)^2
def closest(truck):
    curloc = truck.location
    addr = [curloc]
    distpair = {}

    # sort packages by closest next delivery
    for i in range(len(truck.onboard)):  # looking at array of packages on truck
        distpair[truck.onboard[i].package_id] = CSVinfo.get_distance(curloc, truck.onboard[i].delivery_address)
        #  above is setting the key to a value

    # O(n)^2
    # finds minimum distance
    for pair in range(len(distpair)):
        key = list(distpair.keys())  # list of all keys
        value = list(distpair.values())  # list of all values
        minval = value.index(min(value))  # returns the index of the smallest value

        closestp = Package.myHash.get(key[minval])  # ID with smallest distance
        addr.append(closestp.delivery_address)  # append to addr list

        curloc = closestp.delivery_address  # truck location is set to new address
        del distpair[key[minval]]  # the minimum value is removed because it was the address we just came from

        truck.onboard.remove(closestp)  # removing the ID of the package we "delivered"

        for i in range(len(truck.onboard)):  # again calling distance from current location
            distpair[truck.onboard[i].package_id] = CSVinfo.get_distance(curloc, truck.onboard[i].delivery_address)

    sortedloclist = []  # making a list for duplicate removal

    [sortedloclist.append(i) for i in addr if i not in sortedloclist]  # removes duplicates from addr

    sortedloclist.append("4001 South 700 East")  # Adding the hub as the last stop

    return sortedloclist  # here is the new list without duplicates


# Trucks filled with beginning values
tck1 = Truckinfo("Truck number 1", "4001 South 700 East", 0, 0.3, 0, [], '', "8:00")
tck2 = Truckinfo("Truck number 2", "4001 South 700 East", 0, 0.3, 0, [], '', "9:30")
tck3 = Truckinfo("Truck number 3", "4001 South 700 East", 0, 0.3, 0, [], '', "10:30")

hashh.get(9).address = "410 S State St"

# Packages manually loaded onto truck
truck1 = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40, 6, 25]
truck2 = [2, 3, 8, 10, 12, 18, 21, 23, 27, 28, 32, 36, 38]
truck3 = [4, 5, 7, 11, 17, 22, 24, 26, 33, 9, 35, 39]


# Time complexity: O(1)
# Combining mileage of the three trucks
def Mile():
    trktotaldis = tck2.total_mile + tck1.total_mile + tck3.total_mile
    return trktotaldis


# Simulates delivery without printing
# Time complexity O(n)^2
def delsim(truck, route):
    while len(tck1.onboard) == 0:  # Running through truck 1 packages
        for i in truck1:
            tck1.load(i)

    while len(tck2.onboard) == 0:  # Running through truck 2 packages
        for i in truck2:
            tck2.load(i)

    while len(tck3.onboard) == 0:  # Running through truck 3 packages
        for i in truck3:
            tck3.load(i)

    time_passed = datetime.datetime.strptime(truck.start, '%H:%M')  # basic time format blurb

    for i in range(len(truck.onboard)):  # starting time of truck
        truck.onboard[i].start = time_passed.time()

    miles_driven = 0  # miles started at 0
    delcargo = []

    for i in range(len(route) - 1):
        truck.nextdel = route[i + 1]  # set next delivery
        traveledmiles = CSVinfo.get_distance(truck.location, truck.nextdel)  # returns float of distance/miles
        miles_driven = miles_driven + traveledmiles  # adds miles to current miles
        time_passed = time_passed + datetime.timedelta(minutes=round(traveledmiles / truck.speed))  #  time conversion
        time_passedd = time_passed.time()

        for i, e in enumerate(truck.onboard):  # this will make a list of packages at current address
            if truck.nextdel == e.delivery_address:
                delcargo.append(e.package_id)
                package = Package.myHash.get(e.package_id)
                package.status = "delivered"  # will update status to delivered
                package.delt = time_passedd
        if delcargo:
            truck.location = truck.nextdel  # will catch packages will same address

        else:
            truck.location = truck.nextdel
            truck.total_mile = miles_driven
        delcargo.clear()  # will clear the list


# simulate delivery while printing
# Time complexity O(n)^2
def delsim2(truck, route):
    while len(tck1.onboard) == 0:  # Running through truck 1 packages
        for i in truck1:
            tck1.load(i)

    while len(tck2.onboard) == 0:  # Running through truck 2 packages
        for i in truck2:
            tck2.load(i)

    while len(tck3.onboard) == 0:  # Running through truck 3 packages
        for i in truck3:
            tck3.load(i)

    miles_driven = 0  # setting miles to 0
    time_passed = datetime.datetime.strptime(truck.start, '%H:%M')  #time conversion
    delcargo = []  # temporary list for storage

    for i in range(len(truck.onboard)):  # Assigning time
        truck.onboard[i].start = time_passed.time()

    for i in range(len(route) - 1):
        truck.nextdel = route[i + 1]  # set next delivery
        traveledmiles = CSVinfo.get_distance(truck.location, truck.nextdel)  # returns float of distance/miles
        miles_driven = miles_driven + traveledmiles  # adds miles to current miles
        time_passed = time_passed + datetime.timedelta(minutes=round(traveledmiles / truck.speed))  # time conversion
        time_passedd = time_passed.time()

        for i, e in enumerate(truck.onboard):  # this will make a list of packages at current address
            if truck.nextdel == e.delivery_address:
                delcargo.append(e.package_id)
                package = Package.myHash.get(e.package_id)
                package.status = "delivered"  # will update status to delivered
                package.delt = time_passedd

        if delcargo:
            truck.location = truck.nextdel  #setting next truck to next delivery
            # printing the truck, package, location, time, and miles traveled so far below
            print(truck.tkname + " delivered package number " + str(delcargo) + " to " + truck.location + " at " + str(
                time_passedd) + ". Distance traveled = " + "{:0.2f}".format(miles_driven) + " miles")

        else:
            truck.location = truck.nextdel
            # printing the truck and total mileage for the day below
            print(truck.tkname + " returned to the Hub with total distance" + " {:0.2f}".format(
                miles_driven) + " miles at " + str(time_passedd))
            truck.total_mile = miles_driven
        delcargo.clear()


# simulate delivery while not printing
# Time complexity O(1)
def delsim3():
    delsim(tck1, closest(tck1))  # this runs through the delivery sim for each truck without printing
    delsim(tck2, closest(tck2))
    delsim(tck3, closest(tck3))

#  below is main class
# the first part in green is what will show on the screen for the user
class Main:
    print("\n")
    print("\n")
    print("Welcome to WGUPS")

    prompt = input("""
        You have a few different options:
        1. Get information for all of the packages and trucks at a specific time
        2. Show full package details including time delivered for all packages at end of day        
        3. Quit program
        Enter 1,2, or 3 here:
    \n\n\n""")

    [tck1.load(i) for i in truck1]  #loading the packages onto the trucks
    [tck2.load(i) for i in truck2]
    [tck3.load(i) for i in truck3]

    if prompt == '1':  # if the user presses one
        delsim3()
        format = '%H:%M'
        timeentered = input('Enter a time as HH:MM: ')  # then they need to enter a time
        timepicked = datetime.datetime.strptime(timeentered, format).time()  # convert from string to timedate format
        addcor = datetime.datetime.strptime("10:20", format).time()
        for p in range(1, 41):  # this is set at 40 packages and needs modification for more packages
            delstart = Package.myHash.get(p).start  # get delivery start time from hash table
            deltime = Package.myHash.get(p).delt  # get delivery time from hash table
            #  code below sets status for different times user may enter
            if timepicked < addcor:  # if user picks a time before 10:20 address will show 300 state st
                hashh.get(9).address = "300 State St"

            if timepicked < delstart:
                Package.myHash.get(p).status = "on the truck at hub"  # this shows when the truck is at the hub

            elif (timepicked >= delstart) and (timepicked < deltime):  # this is after the truck left but before delivery
                Package.myHash.get(p).status = "on the way"

            elif timepicked >= deltime:
                Package.myHash.get(p).status = "delivered at " + str(deltime)  # this is when it was delivered
            # below prints out all package information
            print("Package: " + str(hashh.get(p).package_id) + " must arrive by: " + hashh.get(p).deadline +
                  " Being delivered to: " + hashh.get(p).delivery_address + " " + hashh.get(p).city + " " +
                  hashh.get(p).zipcode + " Weight: " + hashh.get(p).weight + " kilo(s) Current location: " +
                  hashh.get(p).status + " Other special instructions: " + hashh.get(p).note)

    elif prompt == '2': # the user enters a 2
        delsim3()
        # below is running delivery simulation and printing all details for the 3 trucks
        delsim2(tck1, closest(tck1))
        print("\n")
        print("\n")
        delsim2(tck2, closest(tck2))
        print("\n")
        print("\n")
        delsim2(tck3, closest(tck3))
        print("\n")
        print("\n")
        print("Total Distance Traveled by All Trucks: " + str(Mile()) + " miles")  # shows total mileage of all three trucks

    elif prompt == '3':
        print("Thanks. Have a good day.")  # if the user presses 3 the program ends
        exit()
