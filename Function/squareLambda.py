# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:04:43 2020

@author: Anobhama
"""
#normal function
def square(n):
    return n*n
n=int(input("Enter the number: "))
print("the square of the number is ",square(n))


#lambda function
n=int(input("Enter the number: "))
res=lambda n: n*n 
print(res(n))