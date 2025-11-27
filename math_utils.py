
import math
import ficheiros_file_utils 
from math import sin, cos, asin, sqrt

raio = 6371
lat1 = ficheiros_file_utils.lat1
long1 = ficheiros_file_utils.long1
alt1 = ficheiros_file_utils.alt1
t1 = 0

lat2 = ficheiros_file_utils.lat2
long2 = ficheiros_file_utils.long2
alt2 = ficheiros_file_utils.alt2
t2 = 30

alt = float(((alt1 + alt2) / 2) + raio)
delta_t = float(t2 - t1)


havlat =  float((sin(math.radians((lat2 - lat1)/ 2)))**2)
havlong = float((sin(math.radians((long2 - long1)/ 2)))**2)
sqrt1 = float(sqrt(havlat + cos(math.radians((lat1))) * cos(math.radians(lat2)) * havlong))


d = 2 * alt * asin(sqrt1)
vel = float(d / delta_t)
print(sin(90))
print("A distância entre estas coordenadas é: ", d)
print("O delta_t entre estas coordenadas é: ", delta_t)
print("A velocidade entre estas coordenadas é: ", vel)