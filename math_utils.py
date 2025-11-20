import math 
from math import sin, cos, asin, sqrt

lat1 = -12.5799
long1 = -7.5351
alt1 = 420642.2

lat2 = -6.7368
long2 = -3.2431
alt2 = 418926.6

alt = float(alt1 + alt2) / 2
havlat =  float((sin((lat2 - lat1)/ 2))**2)
havlong = float((sin((long2 - long1)/ 2))**2)
sqrt = float(sqrt(havlat + cos(lat1) * cos(lat2) * havlong))
d = 2 * alt * asin(sqrt)

print("A distância entre estas coordenadas é: ", d)