# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 23:21:05 2020

@author: Anobhama
"""

#current time in vid

import cv2
import datetime

capture = cv2.VideoCapture(0)
while (capture.isOpened()):
    ret,frame = capture.read()
    if ret == True:
        date = str(datetime.datetime.now())
        cv2.putText(frame,date,(474,63),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
        cv2.imshow("frame",frame)
        #cv2.waitKey(0) keeps running
        if cv2.waitKey(0):
            break
    else:
        break
capture.release()
cv2.destroyAllWindows()