from exif import Image
from datetime import datetime
import cv2
import math

# --- FUNÇÕES DE VISÃO COMPUTACIONAL (A "CAIXA NEGRA") ---
# (Não precisam de mexer aqui! Estas funções fazem a magia.)

def convert_to_cv(image_1, image_2):
    img1_cv = cv2.imread(image_1, 0)
    img2_cv = cv2.imread(image_2, 0)
    return img1_cv, img2_cv

def calculate_features(img1, img2, feature_number=1000):
    orb = cv2.ORB_create(nfeatures=feature_number)
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)
    return kp1, kp2, des1, des2

def calculate_matches(des1, des2):
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)
    return matches

def find_matching_coordinates(kp1, kp2, matches):
    coords1 = []
    coords2 = []
    for match in matches:
        img1_idx = match.queryIdx
        img2_idx = match.trainIdx
        (x1, y1) = kp1[img1_idx].pt
        (x2, y2) = kp2[img2_idx].pt
        coords1.append((x1, y1))
        coords2.append((x2, y2))
    return coords1, coords2