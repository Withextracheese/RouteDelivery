import csv

with open('distancenumonly.csv') as distances:
    distanceData = list(csv.reader(distances, delimiter=','))

    # Time complexity: O(N)
    # Get info from address CSV
with open("addressNAMEADDRESS.csv", newline='') as f:
    addressonly = []
    businessonly = []
    csv_reader = csv.reader(f)
    next(csv_reader)
    for row in csv_reader:
        addressonly.append(row[1])
        businessonly.append(row[0])

    # Time complexity O(1)
    def address_lookup(addindex):
        index = (addressonly.index(addindex))
        return index

    # returns current distance
    # Time complexity: O(1)
    def get_distance(column_loc, row_dest):
        column_loc = address_lookup(column_loc)
        row_dest = address_lookup(row_dest)
        distance = distanceData[column_loc][row_dest]  # [column] [row]
        return float(distance)

