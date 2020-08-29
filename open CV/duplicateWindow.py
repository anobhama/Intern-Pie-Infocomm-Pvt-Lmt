# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 23:53:26 2020

@author: Anobhama
"""
#setting a new window 
import numpy as np
import cv2

def click_event(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x,y,0]
        green = img[x,y,0]
        red = img[x,y,0]
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        MyImg = np.zeros((512,512,3),np.uint8)
        MyImg[:] = [blue,green,red]
        cv2.imshow("Image",MyImg)
#img = np.zeros((512,512,3),np.uint8)
img = cv2.imread("cat.jpg")
cv2.imshow("image",img)
cv2.setMouseCallback("image",click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()