# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 09:16:49 2017

@author: cavasinf
"""

import cv2

img_gray = cv2.imread("women.jpg",0)
img_bgr = cv2.imread("women.jpg",1)

#display the matrix shapes
print("Niveaux de Gris = "+ str(img_gray.shape))
print("Image RGB = "+ str(img_bgr.shape))

#display the loaded images
cv2.imshow("Images avec effet de niveuax de gris", img_gray)
cv2.imshow("Image d'origine en RGB", img_bgr)

cv2.waitKey(0)