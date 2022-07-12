import csv
import Hashtable

#Package class and attributes of the package class.
class Package:  #O(1)
    def __init__(self, package_id, delivery_address, city, state, zipcode, deadline, weight, note, delt,
                 delivery_status, start):
        self.package_id = package_id
        self.delivery_address = delivery_address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.note = note
        self.delt = delt
        self.delivery_status = delivery_status
        self.start = start

    # Time complexity: O(1)
    def __str__(self):  # overwite print function, so it prints reference
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s,  %s, %s" % (
        self.package_id, self.delivery_address, self.city, self.state,
        self.zipcode, self.deadline, self.weight, self.note, self.delt, self.delivery_status, self.start)


# Time complexity: O(N)
#  this is pulling the data from the CSV file
def loadPData(FN):
    with open(FN) as pp:
        pData = csv.reader(pp, delimiter=',')
        next(pData)
        for package in pData:
            pid = int(package[0])
            pdelivery_address = package[1]
            pcity = package[2]
            pstate = package[3]
            pzipcode = package[4]
            pdeadline = package[5]
            pweight = package[6]
            pnote = package[7]
            ptime = "00:00"
            pstatus = "At hub"
            pstart = "00:00"

            # a package object includes these things
            p = Package(pid, pdelivery_address, pcity, pstate, pzipcode, pdeadline, pweight, pnote, ptime, pstatus, pstart)

            myHash.insert(pid, p)


myHash = Hashtable.ChainingHashTable()

#loading packagaes into hash table
loadPData('Packagefiletest.csv')


# print("Packages from Hashtable:")
# Fetch data from Hash Table
# for i in range(len(myHash.map) + 1):
# print("Package: {}".format(myHash.search(i + 1)))  # 1 to 41 is sent to myHash.search()

