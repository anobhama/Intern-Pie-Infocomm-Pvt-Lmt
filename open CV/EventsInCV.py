# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 23:29:43 2020

@author: Anobhama
"""
#prints the events present in the open CV
import cv2

events = [ i for i in dir(cv2) if 'EVENT' in i]
print(events)