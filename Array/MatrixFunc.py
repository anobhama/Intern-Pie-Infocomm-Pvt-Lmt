# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 10:51:09 2020

@author: Anobhama
"""
#finding everything using matrix function
from numpy import *
arr1=matrix('1 2 3;4 5 6;7 8 9')
print("array",arr1)
print("diagnol elements",diagonal(arr1))
print("min ele",arr1.min())
print("max ele",arr1.max())
