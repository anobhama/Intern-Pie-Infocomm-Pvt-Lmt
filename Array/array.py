# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 23:41:31 2020

@author: Anobhama
"""
from array import *

arr=array('i',[1,2,3,4,5,6])

#printing the array
#method 1
print(arr)

#method 2
for i in arr:
    print(i)
print("\n")
    
#method 3
for i in range(len(arr)):
    print(arr[i])
print("\n")
    
#method 4
for i in range(6):
    print(arr[i],end=" ")
print("\n")

#address and size
print("address and size of array",arr.buffer_info())

#typecode
print("data type",arr.typecode)

#copying
arr1=array(arr.typecode,(i for i in arr))
print("The new copied array is ",arr1)
print("\n")

#can change the new array performing new operators
arr2=array(arr1.typecode,(i+i for i in arr1))
print("The new altered array is ",arr2)
print("\n")

#user input array elements
arr3=array('i',[])
n=int(input("Enter the length of the array : "))
for i in range(0,n):
    inp=int(input("Enter the array element: "))
    arr3.append(inp)
print(arr3)
    
#searching 
#method 1
num=int(input("Enter the array element to be searched: "))
j=0
for i in arr3:
    if i == num:
        print(j)
    j +=1

#method 2 using in build function
num1=int(input("Enter the array element to be searched: "))
print(arr3.index(num1))

