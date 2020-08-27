# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 02:19:03 2020

@author: Anobhama
"""

#drawing a circle in the image
import cv2

img = cv2.imread('cat.jpg',1)
img = cv2.circle(img,(500,63),63,(0,0,255),4)
img= cv2.putText(img,"cat",(474,63),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
cv2.imshow("Image",img)
cv2.waitKey(0) 
cv2.destroyAllWindows() 