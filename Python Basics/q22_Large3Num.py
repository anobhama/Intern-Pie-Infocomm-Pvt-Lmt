# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 16:08:45 2020

@author: Anobhama
"""
#(Q22)WAP to print the largest number among three numbers.
n1=int(input("Enter the 1st element: "))
n2=int(input("Enter the 2nd element: "))
n3=int(input("Enter the 3rd element: "))
if n1>=n2:
    if n1>=n3:
        print("The largest number is ",n1 ,"among",n1,",",n2,",",n3)
else:
    if n2>n3:
        print("The largest number is ",n2,"among",n1,",",n2,",",n3)
    else:
        print("The largest number is ",n3,"among",n1,",",n2,",",n3)
        