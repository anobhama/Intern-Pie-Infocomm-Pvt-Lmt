# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 19:48:45 2020

@author: Anobhama
"""
def fib(n):
    s=0
    t=1
    if n ==1:
        print(s)
    else:
        print(s)
        print(t)
        for i in range(2,n):
            temp=s+t
            s=t
            t=temp
            print(temp)
            
n=int(input("Enter the number: "))
fib(n)