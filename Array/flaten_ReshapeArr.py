# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 10:48:40 2020

@author: Anobhama
"""
#flathen and reshape function
from numpy import *
arr1=array([[1,2,3,4,9,0],[5,6,7,8,1,2]])
print("original array",arr1)
arr2=arr1.flatten()
print("flattened array",arr2)
arr3=arr2.reshape(3,4)
print("reshaped array",arr3)
arr4=arr2.reshape(3,2,2)
print("reshaped array",arr4)
