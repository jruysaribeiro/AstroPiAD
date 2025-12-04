
from picamzero import Camera
from time import sleep
from datetime import datetime
from exif import Image

cam = Camera()
print("A tirar fotos...")
cam.capture_sequence("sequencia.jpg", num_images=5, interval=5)
def obter_hora_da_foto(nome_ficheiro):
    # Abre a imagem e lê a data original
    with open(nome_ficheiro, 'rb') as imagem:
        img = Image(imagem)
        # O campo 'datetime_original' tem a hora
        hora_str = img.get("datetime_original")
        return hora_str

data1=obter_hora_da_foto("sequencia-1.jpg")
data2=obter_hora_da_foto("sequencia-2.jpg")
data3=obter_hora_da_foto("sequencia-3.jpg")
data4=obter_hora_da_foto("sequencia-4.jpg")
data5=obter_hora_da_foto("sequencia-5.jpg")
print("Fotos tiradas!")


for i in range (0,5):
    ppp=f'data{i+1}'
    print (ppp)

minuto1=float(str(data1)[14:16])
seg1=float(str(data1)[17:])
minuto2=float(str(data2)[14:16])
seg2=float(str(data2)[17:])


intervalo=(minuto2-minuto1)*60+(seg2-seg1)
print(intervalo)

#def get_time_difference(time_1,time_2):
    #difference = time_2 - time_1
    #return difference.total_seconds()

#print(get_time_difference(data1, data2))
