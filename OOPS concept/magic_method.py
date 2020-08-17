# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 00:38:27 2020

@author: Anobhama
"""
#magic methods

n1 = float(input("Enter the 1st number : "))
n2 = float(input("Enter the 2nd number : "))

print("The added number is ", float.__add__(n1,n2))
print("The substracted number is ", abs(float.__sub__(n1,n2)))
print("The nultiplied number is ", float.__mul__(n1,n2))
print("The divided number is ", float.__divmod__(n1,n2))
print("Is 1st number greater than 2nd number? ",float.__gt__(n1,n2))
print("Is 1st number less than 2nd number? ",float.__lt__(n1,n2))
print("Is 1st number less than or equal to 2nd number? ",float.__le__(n1,n2))
print("Is 1st number greater than or equal to 2nd number? ",float.__ge__(n1,n2))

