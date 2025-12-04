from picamzero import Camera
from time import sleep
from datetime import datetime
from exif import Image
import os

# 1. Iniciar a câmara
cam = Camera()

# 3. Tirar uma sequência (Várias fotos seguidas)
# Tira 10 fotos com intervalo de 5 segundos
cam.capture_sequence("sequencia.jpg", num_images=9, interval=5)

# 4. Calcular a diferença de tempo entre cada foto

def get_time(image_path):
    """Lê a hora exata dos metadados da imagem"""
    with open(image_path, 'rb') as image_file:
        img = Image(image_file)
        time_str = img.get("datetime_original")
        # Converte texto para objeto de tempo
        time_obj = datetime.strptime(time_str, '%Y:%m:%d %H:%M:%S')
        return time_obj

index = 0

for index in range(0,8):
    difference = get_time(f'sequencia-{index + 2}.jpg') - get_time(f'sequencia-{index + 1}.jpg')
    difference = difference.total_seconds()
    print(f"Diferença entre foto {index + 1} e foto {index + 2}: {difference} segundos")
    index += 1


