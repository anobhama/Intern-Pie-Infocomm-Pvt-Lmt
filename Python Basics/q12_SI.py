# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 01:22:28 2020

@author: Anobhama
"""
#(Q12)WAP to enter principal, rate, and time in years and find the simple interest.
p=int(input("Enter the principal: "))
n=int(input("Enter the number of years: "))
r=int(input("Enter the rate of interest: "))
SI=0
SI=p*n*r/100 
print("The Simple Interest is ",SI)
