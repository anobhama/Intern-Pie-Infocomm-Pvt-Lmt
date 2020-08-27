# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 02:06:17 2020

@author: Anobhama
"""
#video capture in black and white
import cv2

capture = cv2.VideoCapture(0)
while(True):
    ret,frame = capture.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("video",gray)
    if cv2.waitKey(0) or 0xFF == ord('q'): 
        break
capture.release()
cv2.destroyAllWindows()