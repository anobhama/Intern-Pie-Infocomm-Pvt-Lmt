# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 23:13:35 2020

@author: Anobhama
"""

#creating blank frame using numpy

import numpy as np
import cv2

img = np.zeros([500,500,3],np.uint8) #blank frame created
img = cv2.line(img,(0,0),(255,255),(145,78,22),5) #line in a blank frame
img = cv2.line(img,(500,0),(255,255),(145,78,22),5)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()