
import math
import ficheiros_file_utils 
from math import sin, cos, asin, sqrt

raio = 6371
lat1 = 38.744
long1 = -9.160
alt1 = 0
t1 = 0

lat2 = 41.162
long2 = -8.622
alt2 = 0
t2 = 30

alt = float(((alt1 + alt2) / 2) + raio)
delta_t = float(t2 - t1)


havlat =  float((sin(math.radians((lat2 - lat1)/ 2)))**2)
havlong = float((sin(math.radians((long2 - long1)/ 2)))**2)
sqrt1 = float(sqrt(havlat + cos(math.radians((lat1))) * cos(math.radians(lat2)) * havlong))


d = 2 * alt * asin(math.radians(sqrt1))
vel = float(d / delta_t)
print(sin(90))
print("A distância entre estas coordenadas é: ", d)
print("O delta_t entre estas coordenadas é: ", delta_t)
print("A velocidade entre estas coordenadas é: ", vel)