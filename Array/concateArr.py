# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 10:40:52 2020

@author: Anobhama
"""
#to concatenate 2 array

from numpy import *
arr1=array([1,2,3,4,5,6,7,8,9,10])
print("array1 ",arr1)
arr2=array([11,22,33,44,55])
print("array2 ",arr2)
print("concatenated array: ",concatenate([arr1,arr2]))
