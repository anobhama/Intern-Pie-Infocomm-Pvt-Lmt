# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 01:41:12 2020

@author: Anobhama
"""

#displaying image in black and white
import cv2

img = cv2.imread('cat.jpg',0)
#0 indictes its a black and white img

cv2.imshow("Image",img)

cv2.waitKey(0) 

cv2.destroyAllWindows() 

"""
0 -> black and white
-1 -> rgb colour
1 -> original  colour

"""
