from collections import namedtuple
import os

CWD = os.path.dirname(os.path.realpath(__file__))

with open(CWD+"/inventory.txt", "r") as inventory_file:
    inventory_txt = inventory_file.read()
    
Inventory = namedtuple("Inventory", ['station', 'latitude', 'longitude',
     'element', 'start', 'end'])

inventory = [Inventory(x[0:11], float(x[12:20]), float(x[21:30]), x[31:35],
     int(x[36:40]), int(x[41:45])) for x in inventory_txt.split("\n") if x.startswith("US")]

inventory_temps = [x for x in inventory if x.element in ['TMIN', 'TMAX']
                   and x.end >= 2015 and x.start < 1920]

latitude, longitude = 41.882, -87.629

inventory_temps.sort(key=lambda x: abs(latitude-x.latitude) + abs(longitude- x.longitude))


with open(CWD+"/stations.txt", "r") as stations_file:
    stations_txt = stations_file.read()
    
station_id = 'USC00110338'
# parse stations
Station = namedtuple("Station", ['station_id', 'latitude', 'longitude',
     'elevation', 'state', 'name', 'start', 'end'])

for line in inventory[:5]:
    print(line)