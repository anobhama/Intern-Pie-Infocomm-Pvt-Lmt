# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 10:42:31 2020

@author: Anobhama
"""
#aliasing
from numpy import *
arr1=array([1,2,3,4,45,56])
print("array before aliasing or changing the value")
print(arr1)
arr2=arr1
arr1[4]=50
print("array1",arr1)
print("array2",arr2)
print(id(arr1))
print(id(arr2))
