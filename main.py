
# --- SESSÃO 5: PREPARAÇÃO PARA VELOCIDADE ---
from picamzero import Camera
from time import sleep
from datetime import datetime
from exif import Image
import os

def get_time(image_path):
    """Lê a hora exata dos metadados da imagem"""
    with open(image_path, 'rb') as image_file:
        img = Image(image_file)
        time_str = img.get("datetime_original")
        # Converte texto para objeto de tempo
        time_obj = datetime.strptime(time_str, '%Y:%m:%d %H:%M:%S')
        return time_obj

def get_time_difference(image_1, image_2):
    """Calcula a diferença em segundos entre duas fotos"""
    time_1 = get_time(image_1)
    time_2 = get_time(image_2)
    difference = time_2 - time_1
    return difference.total_seconds()

# --- EXECUÇÃO PRINCIPAL ---
if __name__ == "__main__":
    
    # 1. Configurar Câmara
    cam = Camera()
    
    # 2. Definir nomes dos ficheiros
    foto1 = "foto_inicio.jpg"
    foto2 = "foto_fim.jpg"
    
    print("--- INICIANDO CAPTURA ---")
    
    # 3. Tirar a primeira foto
    print(f"A tirar {foto1}...")
    cam.take_photo(foto1)
    
    # 4. Esperar (Simular o movimento da ISS)
    print("A aguardar 20 segundos...")
    sleep(20)
    
    # 5. Tirar a segunda foto
    print(f"A tirar {foto2}...")
    cam.take_photo(foto2)
    
    print("--- FOTOS CAPTURADAS ---")
    
    # 6. Calcular e Mostrar o Tempo
    # (Isto confirma que conseguimos ler os dados EXIF corretamente)
    try:
        tempo_passado = get_time_difference(foto1, foto2)
        print("primeira foto tirada em:", get_time(foto1))
        print("segunda foto tirada em:", get_time(foto2))
        print(f"Sucesso! Passaram {tempo_passado} segundos entre as fotos.")
        print("Estamos prontos para calcular a velocidade na próxima sessão!")
    except Exception as e:
        print(f"Erro ao ler tempo: {e}")

