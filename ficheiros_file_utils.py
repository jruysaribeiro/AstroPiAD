import math_utils
from astro_pi_orbit import ISS

import time
iss = ISS()

coord1=(iss.coordinates())
time.sleep(30) 
coord2=(iss.coordinates())


lat1=coord1.latitude.degrees
long1=coord1.longitude.degrees
alt1=coord1.elevation.m

lat2=coord2.latitude.degrees
long2=coord2.longitude.degrees
alt2=coord2.elevation.m
    
print(alt1,lat1,long1)
print(alt2,lat2,long2)



