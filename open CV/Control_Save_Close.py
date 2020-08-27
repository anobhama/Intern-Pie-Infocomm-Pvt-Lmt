# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 01:48:37 2020

@author: Anobhama
"""

#controls for exit and save img
import cv2

img = cv2.imread('cat.jpg',0) #will be viewed as black and white
cv2.imshow("Image",img)
key = cv2.waitKey(0)
if key == 27: #ascii value fro esc
    cv2.destroyAllWindows()
elif key == ord('s'):#save the image by clicking s in keyboard
    cv2.imwrite("cat_copy.jpg",img)
    cv2.destroyAllWindows()
    