import pytesseract
import cv2
img = cv2.imread('test2.png')

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.resize(img, (600, 360))
# Convertir l'image en String
print(pytesseract.image_to_string(img))
# Récupérer la position de chaque lettre des textes de l'image
print(pytesseract.image_to_boxes(img))
cv2.imshow('Result', img)
cv2.waitKey(0)
