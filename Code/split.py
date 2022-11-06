import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('test.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
pytesseract
##############################################
##### Image to String   ######
##############################################
# print(pytesseract.image_to_string(img))

#############################################
#### Detecting Characters  ######
#############################################
hImg, wImg,_ = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    print(b)
    b = b.split(' ')
    print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
cv2.rectangle(img, (224,hImg- 503), (365,hImg- 525), (50, 50, 255), -1)
cv2.imshow('img', img)
cv2.waitKey(0)

# b ['R', '224', '503', '238', '525', '0'], ['5', '353', '503', '365', '525', '0']