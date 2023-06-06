
import requests
# get readme.txt file
r = requests.get('https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt') 
readme = r.text

print(readme)

r = requests.get('https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-inventory.txt')
inventory_txt = r.text
r = requests.get('https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt')
stations_txt = r.text
with open("inventory.txt", "w") as inventory_file:
    inventory_file.write(inventory_txt)
with open("stations.txt", "w") as stations_file:
    stations_file.write(stations_txt)