# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 01:45:36 2020

@author: Anobhama
"""


#displaying image in original colour format
import cv2

img = cv2.imread('cat.jpg',1)

cv2.imshow("Image",img)

cv2.waitKey(0) 

cv2.destroyAllWindows() 