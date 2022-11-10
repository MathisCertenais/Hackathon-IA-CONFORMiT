# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 14:59:51 2022

@author: aboug
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import skimage.io, skimage.color


from skimage.feature import hog
from skimage import data, exposure
from skimage import feature
import random


def substract(img1,img2):
   for i in range(0, img1.shape[0]):
    for j in range(0, img1.shape[1]):
        color_1 = img1[i][j][2]
        color_2 = img2[i][j][2]
        if (color_1 == color_2):
            img[i][j] = 255
        pass
    pass

def convert(img, target_type_min, target_type_max, target_type):
    imin = img.min()
    imax = img.max()

    a = (target_type_max - target_type_min) / (imax - imin)
    b = target_type_max - a * imax
    new_img = (a * img + b).astype(target_type)
    return new_img

horizontal_mask = np.array([-1, 0, 1])
vertical_mask = np.array([[-1],
                             [0],
                             [1]])
img = cv2.imread('SIMPLE-7-1.png')

################ MORPHOLOGIE #################
#morphologie

kernel = np.ones((1, 120), np.uint8)
kernel2 = np.ones((10,1), np.uint8)
kernel3 = np.ones((1,10), np.uint8)
kernel4 = np.ones((1,5), np.uint8)

(thresh, img_b) = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)


#dilatation
#Cimg_dilation = cv2.dilate(img_b, kernel, iterations=1)
#substract(img_b, img_dilation)
#img_dilation2 = cv2.dilate(img_b, kernel2, iterations=1)
#substract(img_b, img_dilation2)
#img_dilation3 = cv2.dilate(img_b, kernel3, iterations=1)
#substract(img_b, img_dilation3)
#img_dilation4 = cv2.dilate(img_b, kernel4, iterations=1)
#substract(img_b, img_dilation4)


cv2.imshow('input',img)

cv2.waitKey(0)

################ patch valve #################
patch = cv2.imread('bb.png',0)


patch_resize = cv2.resize(patch, (230,230))
cv2.imshow('input',patch_resize)

cv2.waitKey(0)


im = plt.imread('a.png',0)


####################################
fd, hog_image = hog(patch_resize, orientations=8, pixels_per_cell=(200, 200),
                    cells_per_block=(1, 1), visualize=True)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)

ax1.axis('off')
ax1.imshow(patch_resize, cmap=plt.cm.gray)
ax1.set_title('Input image')

# Rescale histogram for better display
hog_image_valve = exposure.rescale_intensity(hog_image, in_range=(0, 10))

ax2.axis('off')
ax2.imshow(hog_image_valve, cmap=plt.cm.gray)
ax2.set_title('Histogram of Oriented Gradients')
plt.show()

x = np.arange(0,8,1)
plt.bar(x,fd)
plt.show()

###################################################

################ DETECTION ###################
ss = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()
ss.setBaseImage(img)
ss.switchToSelectiveSearchQuality()
rects = ss.process()

Sauvegarde = []
good_pos = []
val_mean = 10000000
for i in range(0, len(rects), 100):
    # clone the original image so we can draw on it
    output = img.copy()
    # loop over the current subset of region proposals
    for (x, y, w, h) in rects[i:i + 100]:
        # draw the region proposal bounding box on the image
        #color = [random.randint(0, 255) for j in range(0, 3)]
        #cv2.rectangle(output, (x, y), (x + w, y + h), color, 2)
        
        cropped_image = output[int(y):int(y+h),int(x):int(x+w)]
        local_im = cv2.resize(cropped_image, (230,230))
       
        fd_l, hog_image = hog(local_im, orientations=8, pixels_per_cell=(200, 200),
                    cells_per_block=(1, 1), visualize=True)
        
        
        ##### affichage ####
        #fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)

        #ax1.axis('off')
        #ax1.imshow(local_im, cmap=plt.cm.gray)
        #ax1.set_title('Input image')

        # Rescale histogram for better display
        #hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))

        #ax2.axis('off')
        #ax2.imshow(hog_image, cmap=plt.cm.gray)
        #ax2.set_title('Histogram of Oriented Gradients')
        #plt.show()
        #x = np.arange(0,8,1)
        #plt.bar(x,fd)
        #plt.show()
        
        # Rescale histogram for better display
        
        #### detection et affiliation ###
        tab = np.subtract(fd,fd_l)
        
        local_m = np.mean(tab,axis=0)
        if(local_m < val_mean and local_m>0.0005):
            val_mean = local_m
            print(val_mean)
            good_pos = [x,y]
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)

            ax1.axis('off')
            ax1.imshow(local_im, cmap=plt.cm.gray)
            ax1.set_title('Input image')

            #↨ Rescale histogram for better display
            hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))

            ax2.axis('off')
            ax2.imshow(hog_image, cmap=plt.cm.gray)
            ax2.set_title('Histogram of Oriented Gradients')
            plt.show()
       
#img = cv2.circle(img, (good_pos[0],good_pos[1]),5,(0,0,255),3)
img = cv2.rectangle(img, (good_pos[0],good_pos[1]), (good_pos[0] + 200,good_pos[1]+700),(255,255,255), thickness= -1)


### système de sauvegarde ###
#Sauvegarde.append([good_pos[0],good_pos[1]])
# Displaying the image
cv2.imshow('resultat détection', output)
cv2.waitKey(0)



patch = cv2.imread('valve2.png',0)


patch_resize = cv2.resize(patch, (230,230))
cv2.imshow('input',patch_resize)




####################################
fd, hog_image = hog(patch_resize, orientations=8, pixels_per_cell=(200, 200),
                    cells_per_block=(1, 1), visualize=True)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)

ax1.axis('off')
ax1.imshow(patch_resize, cmap=plt.cm.gray)
ax1.set_title('Input image')

# Rescale histogram for better display
hog_image_valve = exposure.rescale_intensity(hog_image, in_range=(0, 10))

ax2.axis('off')
ax2.imshow(hog_image_valve, cmap=plt.cm.gray)
ax2.set_title('Histogram of Oriented Gradients')
plt.show()

x = np.arange(0,8,1)
plt.bar(x,fd)
plt.show()

###################################################

################ DETECTION ###################
ss = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()
ss.setBaseImage(img)
ss.switchToSelectiveSearchQuality()
rects = ss.process()

Sauvegarde = []
good_pos = []
val_mean = 10000000
for i in range(0, len(rects), 100):
    # clone the original image so we can draw on it
    output = img.copy()
    # loop over the current subset of region proposals
    for (x, y, w, h) in rects[i:i + 100]:
        # draw the region proposal bounding box on the image
        #color = [random.randint(0, 255) for j in range(0, 3)]
        #cv2.rectangle(output, (x, y), (x + w, y + h), color, 2)
        
        cropped_image = output[int(y):int(y+h),int(x):int(x+w)]
        local_im = cv2.resize(cropped_image, (230,230))
       
        fd_l, hog_image = hog(local_im, orientations=8, pixels_per_cell=(200, 200),
                    cells_per_block=(1, 1), visualize=True)
        
        
        ##### affichage ####
        #fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)

        #ax1.axis('off')
        #ax1.imshow(local_im, cmap=plt.cm.gray)
        #ax1.set_title('Input image')

        # Rescale histogram for better display
        #hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))

        #ax2.axis('off')
        #ax2.imshow(hog_image, cmap=plt.cm.gray)
        #ax2.set_title('Histogram of Oriented Gradients')
        #plt.show()
        #x = np.arange(0,8,1)
        #plt.bar(x,fd)
        #plt.show()
        
        # Rescale histogram for better display
        
        #### detection et affiliation ###
        tab = np.subtract(fd,fd_l)
        
        local_m = np.mean(tab,axis=0)
        if(local_m < val_mean and local_m>0.0005):
            val_mean = local_m
            print(val_mean)
            good_pos = [x,y]
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)

            ax1.axis('off')
            ax1.imshow(local_im, cmap=plt.cm.gray)
            ax1.set_title('Input image')

            #↨ Rescale histogram for better display
            hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))

            ax2.axis('off')
            ax2.imshow(hog_image, cmap=plt.cm.gray)
            ax2.set_title('Histogram of Oriented Gradients')
            plt.show()
       
#img = cv2.circle(img, (good_pos[0],good_pos[1]),5,(0,0,255),3)
img = cv2.rectangle(img, (good_pos[0],good_pos[1]), (good_pos[0] + 200,good_pos[1]+200),(255,255,255), thickness= -1)


### système de sauvegarde ###
Sauvegarde.append([good_pos[0],good_pos[1]])
# Displaying the image
cv2.imshow('resultat détection', img)
cv2.waitKey(0)


patch = cv2.imread('POMPE.png',0)


patch_resize = cv2.resize(patch, (230,230))
cv2.imshow('input',patch_resize)




####################################
fd, hog_image = hog(patch_resize, orientations=8, pixels_per_cell=(200, 200),
                    cells_per_block=(1, 1), visualize=True)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)

ax1.axis('off')
ax1.imshow(patch_resize, cmap=plt.cm.gray)
ax1.set_title('Input image')

# Rescale histogram for better display
hog_image_valve = exposure.rescale_intensity(hog_image, in_range=(0, 10))

ax2.axis('off')
ax2.imshow(hog_image_valve, cmap=plt.cm.gray)
ax2.set_title('Histogram of Oriented Gradients')
plt.show()

x = np.arange(0,8,1)
plt.bar(x,fd)
plt.show()

###################################################

################ DETECTION ###################
ss = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()
ss.setBaseImage(img)
ss.switchToSelectiveSearchQuality()
rects = ss.process()

Sauvegarde = []
good_pos = []
val_mean = 10000000
for i in range(0, len(rects), 100):
    # clone the original image so we can draw on it
    output = img.copy()
    # loop over the current subset of region proposals
    for (x, y, w, h) in rects[i:i + 100]:
        # draw the region proposal bounding box on the image
        #color = [random.randint(0, 255) for j in range(0, 3)]
        #cv2.rectangle(output, (x, y), (x + w, y + h), color, 2)
        
        cropped_image = output[int(y):int(y+h),int(x):int(x+w)]
        local_im = cv2.resize(cropped_image, (230,230))
       
        fd_l, hog_image = hog(local_im, orientations=8, pixels_per_cell=(200, 200),
                    cells_per_block=(1, 1), visualize=True)
        
        
        ##### affichage ####
        #fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)

        #ax1.axis('off')
        #ax1.imshow(local_im, cmap=plt.cm.gray)
        #ax1.set_title('Input image')

        # Rescale histogram for better display
        #hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))

        #ax2.axis('off')
        #ax2.imshow(hog_image, cmap=plt.cm.gray)
        #ax2.set_title('Histogram of Oriented Gradients')
        #plt.show()
        #x = np.arange(0,8,1)
        #plt.bar(x,fd)
        #plt.show()
        
        # Rescale histogram for better display
        
        #### detection et affiliation ###
        tab = np.subtract(fd,fd_l)
        
        local_m = np.mean(tab,axis=0)
        if(local_m < val_mean and local_m>0.0005):
            val_mean = local_m
            print(val_mean)
            good_pos = [x,y]
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)

            ax1.axis('off')
            ax1.imshow(local_im, cmap=plt.cm.gray)
            ax1.set_title('Input image')

            #↨ Rescale histogram for better display
            hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))

            ax2.axis('off')
            ax2.imshow(hog_image, cmap=plt.cm.gray)
            ax2.set_title('Histogram of Oriented Gradients')
            plt.show()
       
#img = cv2.circle(img, (good_pos[0],good_pos[1]),5,(0,0,255),3)
img = cv2.rectangle(img, (good_pos[0],good_pos[1]), (good_pos[0] + 100,good_pos[1]+100),(255,255,255), thickness= -1)


### système de sauvegarde ###
Sauvegarde.append([good_pos[0],good_pos[1]])
# Displaying the image
cv2.imshow('resultat détection', img)
cv2.waitKey(0)

