# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 10:44:51 2020

@author: Anobhama
"""
#shallow copy
from numpy import *
arr1=array([1,2,3,4,45,56])
print("array before shallow copy")
print(arr1)
arr2=arr1.view()
arr1[4]=50
print("array1",arr1)
print("array2",arr2)
print(id(arr1))
print(id(arr2))
