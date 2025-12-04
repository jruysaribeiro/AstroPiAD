from picamzero import Camera
from time import sleep
from datetime import datetime
from exif import Image

cam = Camera()
def get_time(image_path):
    with open(image_path, 'rb') as image_file:
        img = Image(image_file)
        time_str = img.get("datetime_original")
        time_obj = datetime.strptime(time_str, '%Y:%m:%d %H:%M:%S')
    return time_obj

def get_time_difference(image_1, image_2):
    time_1 = get_time(image_1)
    time_2 = get_time(image_2)
    difference = time_2 - time_1
    return difference.total_seconds()

def photos():
    fotos = cam.capture_sequence('sequencia.jpg', num_images = 9, interval = 5)
    return fotos

stempo = 0
num_fotos = 9
sequencia = photos()
for i in range(1,num_fotos-1):
    foto1 = f'sequencia-{i}.jpg'
    foto2 = f'sequencia-{i+1}.jpg'
    tempo = get_time_difference(foto1,foto2)
    stempo += tempo
print(round(stempo/num_fotos,3))
