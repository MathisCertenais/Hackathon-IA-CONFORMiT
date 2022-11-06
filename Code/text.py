# Script v0 conversion texte en String et localisation des caracteres https://www.topcoder.com/thrive/articles/python-for-character-recognition-tesseract

import pytesseract
import cv2
img = cv2.imread('../P&ID/png/SIMPLE-3-1.png')
cv2.imshow('Initial image', img)
# pytesseract error on Windows, Set the tesseract path in the script before calling
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
if img is None:
    print('Wrong path')
else:
    #img = cv2.resize(img, (600, 360))
    hImg, wImg, _ = img.shape
    # Convertir l'image en String
    print(pytesseract.image_to_string(img))
    # Récupérer la position de chaque lettre des textes de l'image
    boxes = pytesseract.image_to_boxes(img)
    # Stockage des caractères et ses coordonnées
    # Filtrage car symbole confondu avec caractere

    # Dissimuler texte avec carré blanc (prendre coord premier et dernier caractere, puis generer le carré)
    for b in boxes.splitlines():
        b = b.split(' ')
        if b[0]=="O" or b[0]=="—" or b[0]==">" or b[0]=="P" or b[0]=="x" or b[0]=="t" or b[0]=="~" :
            print("yes")
        # Ignorer si le caractere est if b[0]!="~" : and b[0]!="‘" and b[0]!="O" and b[0]!="e" and b[0]!="p" and b[0]!="C"
        else:
            # Créer un carré blanc sur chaque caractère, en prenant les coordonnées
            x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
            cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (255, 255, 255), -1)

cv2.imshow('Result', img)
cv2.waitKey(0)