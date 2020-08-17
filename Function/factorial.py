# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 19:56:13 2020

@author: Anobhama
"""
#factorial of a number
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    print(f)
n=int(input("Enter the number: "))
fact(n)