# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 02:08:12 2020

@author: Anobhama
"""
#drawing a line in the image
import cv2

img = cv2.imread('cat.jpg',1)
img = cv2.line(img,(600,0),(100,200),(0,255,0),5) #x axis,y axis,colour(B,G,R),thickness
cv2.imshow("Image",img)
cv2.waitKey(0) 
cv2.destroyAllWindows() 