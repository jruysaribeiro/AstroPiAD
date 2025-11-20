import sys
from astro_pi_orbit import ISS

iss = ISS()

print(iss.coordinates())
print(iss.coordinates().latitude.degrees)

