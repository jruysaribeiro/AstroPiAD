# --- SESSÃO 5: PREPARAÇÃO E CÁLCULO DE VELOCIDADE ---
from picamzero import Camera
from time import sleep
from datetime import datetime
from exif import Image
import cv2  # Biblioteca de Visão Computacional (OpenCV)
import math # Biblioteca de Matemática

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

def convert_to_cv(image_1, image_2):
    """Converte as imagens para um formato que o OpenCV entende"""
    img1_cv = cv2.imread(image_1, 0)
    img2_cv = cv2.imread(image_2, 0)
    return img1_cv, img2_cv

def calculate_features(img1, img2, feature_number=1000):
    """Procura pontos de interesse (cantos, bordas) nas imagens"""
    orb = cv2.ORB_create(nfeatures=feature_number)
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)
    return kp1, kp2, des1, des2

def calculate_matches(des1, des2):
    """Encontra os mesmos pontos nas duas imagens"""
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    # Ordena para ter os melhores pontos primeiro
    matches = sorted(matches, key=lambda x: x.distance)
    return matches

def find_matching_coordinates(kp1, kp2, matches):
    """Extrai as coordenadas X e Y dos pontos encontrados"""
    coordinates_1 = []
    coordinates_2 = []
    for match in matches:
        image_1_idx = match.queryIdx
        image_2_idx = match.trainIdx
        (x1, y1) = kp1[image_1_idx].pt
        (x2, y2) = kp2[image_2_idx].pt
        coordinates_1.append((x1, y1))
        coordinates_2.append((x2, y2))
    return coordinates_1, coordinates_2

def calculate_mean_distance(coordinates_1, coordinates_2):
    """Calcula a distância média em PIXEIS que os pontos se moveram"""
    all_distances = 0
    merged_coordinates = list(zip(coordinates_1, coordinates_2))
    
    for coordinate in merged_coordinates:
        x_difference = coordinate[0][0] - coordinate[1][0]
        y_difference = coordinate[0][1] - coordinate[1][1]
        
        # Usa Teorema de Pitágoras para achar a distância
        distance = math.hypot(x_difference, y_difference)
        all_distances = all_distances + distance
        
    return all_distances / len(merged_coordinates)

def calculate_speed_in_kmps(feature_distance, GSD, time_difference):
    """Usa o GSD para converter pixeis em km e calcula a velocidade"""
    # Converter a distância de pixeis para centímetros
    distance_in_cm = feature_distance * GSD
    
    # Converter centímetros para quilómetros (dividir por 100.000)
    distance_in_km = distance_in_cm / 100000
    
    # Calcular velocidade: Velocidade = Distância / Tempo
    speed = distance_in_km / time_difference
    
    return speed

# --- EXECUÇÃO PRINCIPAL ---
if __name__ == "__main__":
    
    # 1. Configurar Câmara
    cam = Camera()
    
    # 2. Definir nomes dos ficheiros e GSD
    foto1 = "foto_inicio.jpg"
    foto2 = "foto_fim.jpg"
    
    # GSD (Ground Sampling Distance) para a altitude da ISS (~12648 cm/pixel)
    # Este valor diz-nos que 1 pixel na foto = 126 metros no chão
    GSD = 12648
    
    print("--- INICIANDO CAPTURA ---")
    
    # 3. Tirar a primeira foto
    print(f"A tirar {foto1}...")
    cam.take_photo(foto1)
    
    # 4. Esperar (Simular o movimento da ISS)
    print("A aguardar 5 segundos...")
    sleep(5)
    
    # 5. Tirar a segunda foto
    print(f"A tirar {foto2}...")
    cam.take_photo(foto2)
    
    print("--- FOTOS CAPTURADAS. A CALCULAR VELOCIDADE... ---")
    
    try:
        # A. Calcular o tempo que passou
        tempo_passado = get_time_difference(foto1, foto2)
        print(f"Tempo decorrido: {tempo_passado} segundos")
        
        # B. Processar as imagens com OpenCV
        img1_cv, img2_cv = convert_to_cv(foto1, foto2)
        kp1, kp2, des1, des2 = calculate_features(img1_cv, img2_cv)
        matches = calculate_matches(des1, des2)
        coordinates_1, coordinates_2 = find_matching_coordinates(kp1, kp2, matches)
        
        # C. Calcular a distância em pixeis
        distancia_media_pixeis = calculate_mean_distance(coordinates_1, coordinates_2)
        print(f"Movimento detetado: {distancia_media_pixeis:.2f} pixeis")
        
        # D. Calcular a velocidade final em km/s
        velocidade = calculate_speed_in_kmps(distancia_media_pixeis, GSD, tempo_passado)
        
        print(f"Velocidade calculada: {velocidade:.4f} km/s")
        
        # E. Escrever o resultado no ficheiro obrigatório (result.txt)
        # Formata para ter 4 casas decimais
        resultado_formatado = f"{velocidade:.4f}"
        
        with open("result.txt", "w") as f:
            f.write(resultado_formatado)
            
        print("Sucesso! Ficheiro 'result.txt' criado.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")