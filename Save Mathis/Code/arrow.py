
import cv2
import numpy as np
 
# Read the main image
img_rgb = cv2.imread('image.png')
cv2.imshow('Initial image', img_rgb)

# Convert it to grayscale
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
 
# Read the template
template = cv2.imread('arrow.png', 0)
template_up = cv2.imread('arrow2.png', 0)
template_down = cv2.imread('arrow3.png', 0)


# Effacer les fleches direction droite
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (255, 255, 255), -1)

# Effacer les fleches direction haute
w, h = template_up.shape[::-1]
res = cv2.matchTemplate(img_gray, template_up, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (255, 255, 255), -1)

# Effacer les fleches direction bas
w, h = template_down.shape[::-1]
res = cv2.matchTemplate(img_gray, template_down, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (255, 255, 255), -1)
cv2.imshow('Detected', img_rgb)
cv2.waitKey(0)