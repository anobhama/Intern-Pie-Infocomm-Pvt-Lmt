# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 01:38:39 2020

@author: Anobhama
"""

#closing the image - auto close
import cv2

img = cv2.imread('cat.jpg')
cv2.imshow("Image",img)

# except 0 , other numbers means it will automatically close after the entered time is exhausted
cv2.waitKey(3000) #secs

cv2.destroyAllWindows() 