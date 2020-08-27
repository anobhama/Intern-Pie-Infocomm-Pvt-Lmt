# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 01:53:41 2020

@author: Anobhama
"""
#video capture
import cv2

capture = cv2.VideoCapture(0)
while(True):
    ret,frame = capture.read()
    cv2.imshow("video",frame)
    if cv2.waitKey(0) or 0xFF == ord('q'): 
        break
capture.release()
cv2.destroyAllWindows()