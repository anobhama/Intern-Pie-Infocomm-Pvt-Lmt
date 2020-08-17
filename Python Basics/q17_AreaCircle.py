# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 01:49:17 2020

@author: Anobhama
"""
#(Q17)WAP to calculate the area of a circle.
def findArea(r): 
    PI = 3.142
    return PI * (r*r)
r=float(input("Enter the radius of the circle : "))
print("The area of circel is ",findArea(r))