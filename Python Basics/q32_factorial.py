# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 01:05:06 2020

@author: Anobhama
"""
#(Q32) WAP to input a number and print factorial of a number.
num=int(input("Enter the number : "))
fact=1
if num < 0:
    print("No factorial for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num + 1):
        fact=fact * i
    print("The factorial of {} is {}".format(i,fact))
    