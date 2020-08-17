# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 23:58:37 2020

@author: Anobhama
"""

#operator overloading method 1
a=10
b=15
print(int.__add__(a,b))

#user input
a=int(input("Enter the 1st element : "))
b=int(input("Enter the 2nd element : "))
print("The added number is ",int.__add__(a,b)) #magic method