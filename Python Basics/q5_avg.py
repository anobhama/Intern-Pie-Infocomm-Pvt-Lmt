# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 00:04:03 2020

@author: Anobhama
"""
#(Q5)WAP to print the average of four numbers.
a=[]
avg=0
print("Enter only 4 elements")
for i in range(1,5): 
    elem=int(input("Enter element: "))
    a.append(elem)
avg=sum(a)/4
print("Average of elements ",round(avg,2))