from collections import namedtuple
import os, requests

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

for line in inventory[:5]:
    print(line)

with open(CWD+"/stations.txt", "r") as stations_file:
    stations_txt = stations_file.read()
    
station_id = inventory_temps[0].station
# parse stations
Station = namedtuple("Station", ['station_id', 'latitude', 'longitude',
     'elevation', 'state', 'name', 'start', 'end'])
stations = [(x[0:11], float(x[12:20]), float(x[21:30]), float(x[31:37]), x[38:40].strip(), x[41:71].strip())
            for x in stations_txt.split("\n") if x.startswith(station_id)]
station = Station(*stations[0] + (inventory_temps[0].start,
     inventory_temps[0].end))
print(station)

r = requests.get('https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/all/{}.dly'.format(station.station_id))
weather = r.text
# save into a text file, so we won't need to fetch again
with open(CWD+'/weather_{}.txt'.format(station.station_id), "w") as weather_file:
    weather_file.write(weather)
