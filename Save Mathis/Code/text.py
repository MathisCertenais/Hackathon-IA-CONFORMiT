# Script v0 conversion texte en String et localisation des caracteres https://www.topcoder.com/thrive/articles/python-for-character-recognition-tesseract
import arrow
import pytesseract
import cv2
img = cv2.imread('../P&ID/png/SIMPLE-14-1.png')
cv2.imshow('Initial image', img)
# pytesseract error on Windows, Set the tesseract path in the script before calling
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Mauvais chemin d'image
if img is None:
    print('Wrong path')
else:
    #img = cv2.resize(img, (600, 360))
    hImg, wImg, _ = img.shape
    # Convertir l'image en String
    text = pytesseract.image_to_string(img)
    text_splitted = text.splitlines()
    # Filtrage en enlevant les strings vide de la liste
    text_splitted = list(filter(None, text_splitted))
    text_splitted_new = []
    for i in range(0,len(text_splitted)):

        text_splitted_new.append(text_splitted[i].replace(" ", ""))
    # text_splitted_line_and_enter = text.split("\n\n") # Pas fiable lorsque le texte est trop petit
    text_splitted_localisation = text_splitted # avec les 2 pt extremes du mot, et creation rectangle
    # Récupérer la position de chaque lettre des textes de l'image
    boxes = pytesseract.image_to_boxes(img)

    # Récupérer coordonnée rectangle de chaque mot
    list = []
    # Parcours de chaque element de la liste
    for i in range(0,len(text_splitted_new)):
        # Récupération de la taille de chaque element
        list.append(len(text_splitted_new[i]))
        #print("premier elem ",i," :",text_splitted[i][0])
        #print("dernier elem ",text_splitted[i][-1])

    # Stock les premieres et dernieres lettres de chaque element
    list_coord = []
    # Stock les premieres et dernieres pos. x1 des lettres de chaque element
    list_coord_x1 = []
    # Stock les premieres et dernieres pos. x2 des lettres de chaque element
    list_coord_x2 = []
    # Stock les premieres et dernieres pos. y des lettres de chaque element
    list_coord_y1 = []
    # Stock les premieres et dernieres pos. y2 des lettres de chaque element
    list_coord_y2 = []

    compteur = 0
    # Parcours de la liste des tailles de chaque element
    i=0
    # Dissimuler texte avec carré blanc (prendre coord premier et dernier caractere, puis generer le carré)
    for b in boxes.splitlines() :
        b = b.split(' ')
        print(b)

        # Filtrage
        if  b[0]=="~" or b=="P" or b=="x" or b=="t" or b=="—" or b==">":
            pass

        elif compteur==0:
            # Récupération de la coordonnée x1 (x du premier caractere)
            list_coord.append(b[0])
            list_coord_x1.append(b[1])
            list_coord_y1.append(b[2])
            list_coord_x2.append(b[3])
            list_coord_y2.append(b[4])

            compteur+=1

        # Récupération de la coordonnée x1 et y2
        elif compteur%(list[i]-1)==0:

            list_coord.append(b[0])
            list_coord_x1.append(b[1])
            list_coord_y1.append(b[2])
            list_coord_x2.append(b[3])
            list_coord_y2.append(b[4])

            i+=1
            if i==len(list):
                break
            compteur=0
            # Récupération de la coordonnée y2 (y du second caractere)


        else:
            compteur+=1


        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        # Récupération de la coordonnée x1 (x du premier caractere), y2 (y du second caractere)

        if b[0]=="~" or b=="P" or b=="x" or b=="t" or b=="—" or b==">": #or b[0]==">" Filtrage pour ne pas delete valve ..
            pass
        # Ignorer si le caractere est if b[0]!="~" : and b[0]!="‘" and b[0]!="O" and b[0]!="e" and b[0]!="p" and b[0]!="C"
        else:
            # Créer un carré blanc sur chaque caractère, en prenant les coordonnées
            cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (255, 255, 255), -1)


# Tableau qui recupere les coordonnées du rectangle
tab_final_coord = []
compteur2 = 0
# Comparer tous les 2 elements et garder le plus petit x1 et le plus grand x2
for i in range (0, len(list_coord_x1)-1,2):
    if(i%2==0):
        tab_final_coord.append(text_splitted_new[compteur2])
        compteur2+=1;
    x1 = list_coord_x1[i]
    if x1 > list_coord_x1[i+1]:
        x1 = list_coord_x1[i+1]

    x2 = list_coord_x2[i]
    if x2 < list_coord_x2[i+1]:
        x2 = list_coord_x2[i+1]

    y1 = list_coord_y1[i]
    if y1 > list_coord_y1[i+1]:
        y1 = list_coord_y1[i+1]

    y2 = list_coord_y2[i]
    if y2 < list_coord_y2[i+1]:
        y2 = list_coord_y2[i+1]

    tab_final_coord.append(x1)
    tab_final_coord.append(y1)
    tab_final_coord.append(x2)
    tab_final_coord.append(y2)


cv2.imshow('Result', img)
cv2.waitKey(0)

exec(open('arrow.py').read())