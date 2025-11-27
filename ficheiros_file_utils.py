import math_utils
from astro_pi_orbit import ISS
import time
import datetime


iss = ISS()

coord1={
    "coord":iss.coordinates(),
    "time":datetime.datetime.now()
}
time.sleep(3) 
coord2={
    "coord":iss.coordinates(),
    "time":datetime.datetime.now()
}

lat1=coord1["coord"].latitude.degrees
long1=coord1["coord"].longitude.degrees
alt1=coord1["coord"].elevation.km
time1=coord1["time"]

lat2=coord2["coord"].latitude.degrees
long2=coord2["coord"].longitude.degrees
alt2=coord2["coord"].elevation.km
time2=coord2["time"]


#print(alt1,lat1,long1,time1)
#print(alt2,lat2,long2,time2)

#print("o tempo é vindo de ficheiros util : ", time1)

#print(alt1,lat1,long1,time1)
#print(alt2,lat2,long2,time2)



HoraStr=str(time1)[12:14]
#MinStr=time1[15:17]
#SegStr=time[17:]
#Hora=float(HoraStr)
#Minuto=float(MinStr)
#Seg=float(SegStr)
#Tempo=Hora*3600+Minuto*60+Seg

print(len(str(time1)[12:14]))
print(str(datetime.datetime.now())[12:14])