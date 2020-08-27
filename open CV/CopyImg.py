# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 01:46:55 2020

@author: Anobhama
"""
#creating a copy of the original img
import cv2

img = cv2.imread('cat.jpg',0) #will be viewed as black and white

cv2.imshow("Image",img)

cv2.waitKey(0) 

cv2.destroyAllWindows() 

cv2.imwrite("catBlackWhite.jpg",img)