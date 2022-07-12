import Package

# Truck class with attributes of truck
class Truckinfo:  #O(1)
    def __init__(self, tkname, location, deladdy, speed, timepassed, onboard, totalmile, starttime):
        self.tkname = tkname
        self.location = location
        self.nextdel = deladdy
        self.speed = speed
        self.timepassed = timepassed
        self.onboard = onboard
        self.total_mile = totalmile
        self.start = starttime



    # Time complexity: O(1)
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.tkname,  self.location, self.nextdel, self.speed,
                                                   self.timepassed, self.onboard, self.total_mile, self.start)

    #  O(1)
    # changes status of package
    # adds package to onboard "loads"
    def load(self, packnum):
        pa = Package.myHash.get(packnum)
        pa.status = "At the hub on the truck"
        self.onboard.append(pa)

