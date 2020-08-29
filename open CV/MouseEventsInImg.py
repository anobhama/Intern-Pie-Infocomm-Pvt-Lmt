# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 23:52:16 2020

@author: Anobhama
"""

#right and left button events by giving a image
import cv2

def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,' ',y)
        font=cv2.FONT_HERSHEY_SIMPLEX
        strXY=str(x)+' '+str(y)
        cv2.putText(img,strXY,(x,y),font,1,(255,255,0),2)
        cv2.imshow('image',img)
    if event==cv2.EVENT_RBUTTONDOWN:
        blue=img[x,y,0]
        green=img[x,y,0]
        red=img[x,y,0]
        font=cv2.FONT_HERSHEY_SIMPLEX
        strBGR=str(blue)+','+str(green)+','+str(red)
        cv2.putText(img,strXY,(x,y),font,1,(255,255,0),2)
        cv2.imshow('image',img)
img1 = cv2.imread("butterfly.jpg")
img=cv2.resize(img1,(500,500),interpolation = cv2.INTER_AREA)
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()      
