import math_utils
from astro_pi_orbit import ISS

import time
iss = ISS()

coord1={
    "coord":iss.coordinates(),
    "time":time.localtime()
}
time.sleep(30) 
coord2={
    "coord":iss.coordinates(),
    "time":time.ctime()
}

lat1=coord1["coord"].latitude.degrees
long1=coord1["coord"].longitude.degrees
alt1=coord1["coord"].elevation.m
time1=coord1["time"]

lat2=coord2["coord"].latitude.degrees
long2=coord2["coord"].longitude.degrees
alt2=coord2["coord"].elevation.m
time2=coord2["time"]

print(alt1,lat1,long1,time1)
print(alt2,lat2,long2,time2)
