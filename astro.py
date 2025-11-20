import sys
from astro_pi_orbit import ISS
import time

iss = ISS()

coord1 = {
    "coord": iss.coordinates(),
    "time": time.localtime()
}

time.sleep(2)
coord2 = {
    "coord": iss.coordinates(),
    "time": time.localtime()
}

print(f"Coordinate 1: {coord1['coord']} at time {time.strftime('%Y-%m-%d %H:%M:%S', coord1['time'])}")
print(f"Coordinate 2: {coord2['coord']} at time {time.strftime('%Y-%m-%d %H:%M:%S', coord2['time'])}")


print(coord1)