from collections import namedtuple
import os

CWD = os.path.dirname(os.path.realpath(__file__))

with open(CWD+"/inventory.txt", "r") as inventory_file:
    inventory_txt = inventory_file.read()
    
Inventory = namedtuple("Inventory", ['station', 'latitude', 'longitude',
     'element', 'start', 'end'])

inventory = [Inventory(x[0:11], float(x[12:20]), float(x[21:30]), x[31:35],
     int(x[36:40]), int(x[41:45])) for x in inventory_txt.split("\n") if x.startswith("US")]

for line in inventory[:5]:
    print(line)