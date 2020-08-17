# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 00:14:25 2020

@author: Anobhama
"""
#numpy in array
from numpy import *
arr=array([1,2,3,4,5])
print(arr)

#explicitly mentioning the data type
arr1=array([6,7,8,9,10],float)
print(arr1)

#diff ways of creating numpy array
#array()
arr2=([12,23,34,45,56,67])
print(arr2)

#linspace() 
arr3=linspace(1,12,10) #(start ele,end ele,size of array)
print(arr3)

#arange()
arr4=arange(1,12,3) #(start ele,end ele,differenec of initial with next)
print(arr4)

#logspace() log involved
arr5=logspace(1,40,5)
print(arr5)

#zeros() 
#by default will be float
arr6=zeros(5)
print(arr6)
arr6=zeros(5,int) #making it int type
print(arr6)

#ones()
#by default will be float
arr7=ones(5)
print(arr7)
arr7=ones(5,int) #making it int
print(arr7)