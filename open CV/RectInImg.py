# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 02:17:18 2020

@author: Anobhama
"""

#drawing a rectange in the image and filled
import cv2

img = cv2.imread('cat.jpg',1)
img = cv2.rectangle(img,(600,0),(200,50),(0,0,255),-1) #x axis,y axis,colour(B,G,R),thickness,-1 indicates fill
cv2.imshow("Image",img)
cv2.waitKey(0) 
cv2.destroyAllWindows() 