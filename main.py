from picamzero import Camera
from time import sleep
from datetime import datetime
from exif import Image
import os

def get_time(image_path):
    #Lê a hora exata dos Metadados da imagem
    with open(image_path, 'rb') as image_file:
        img = Image(image_file)
        time_str = img.get("datetime_original")
        time_obj = datetime.strptime(time_str, '%Y:%m:%d %H:%M:%S')
    return time_obj

def get_time_difference(image_1, image_2):
    """Calcula a diferença em segundos entre duas fotos"""
    time_1 = get_time(image_1)
    time_2 = get_time(image_2)
    difference = time_2 - time_1
    return difference.total_seconds()

diferenca_t = []

# --- EXECUÇÃO PRINCIPAL ---
if __name__ == "__main__":
    cam = Camera()
    foto1 = "foto_inicio.jpg"  
    print("--- INICIANDO CAPTURA ---")
    print(f"A tirar {foto1}...")
    cam.take_photo(foto1)
    
    # As 9 fotos
    for i in range (1,10):
        
        
        
        # 2. Definir nomes dos ficheiros
        
        foto2 = "foto_fim.jpg"
        
       
        
        
        
        # 4. Esperar (Simular o movimento da ISS)
        print("A aguardar 5 segundos...")
        sleep(5)
        
        # 5. Tirar a segunda foto
        print(f"A tirar {foto2}...")
        cam.take_photo(foto2)
        
        print("--- FOTOS CAPTURADAS ---")
        
        # 6. Calcular e Mostrar o Tempo
        # (Isto confirma que conseguimos ler os dados EXIF corretamente)
        try:
            tempo_passado = get_time_difference(foto1, foto2)
            print(f"Sucesso! Passaram {tempo_passado} segundos entre as fotos.")
            print("Estamos prontos para calcular a velocidade na próxima sessão!")
        except Exception as e:
            print(f"Erro ao ler tempo: {e}")
         
        # Renovação
        foto1 = foto2     
        diferenca_t.append(tempo_passado)   

print (diferenca_t)