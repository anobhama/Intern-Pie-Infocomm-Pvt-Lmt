# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 02:14:10 2020

@author: Anobhama
"""

#drawing a arrow in the image
import cv2

img = cv2.imread('cat.jpg',1)
img = cv2.arrowedLine(img,(600,0),(150,50),(255,0,0),5) #x axis,y axis,colour(B,G,R),thickness
cv2.imshow("Image",img)
cv2.waitKey(0) 
cv2.destroyAllWindows() 