# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 01:35:43 2020

@author: Anobhama
"""
#displaying the image 

import cv2

img = cv2.imread('cat.jpg')
cv2.imshow("Image",img)

cv2.waitKey(0) #0 means we have to click the close button to close the image

cv2.destroyAllWindows() 