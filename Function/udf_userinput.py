# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 19:30:33 2020

@author: Anobhama
"""
#input from the user

def add(a,b):
    print("Sum is",a+b)

def sub(a,b):
    return a-b
def mul_div(a,b):
    x=a*b
    y=a/b
    z=a//b
    return x,y,z

n1=int(input("Enter the 1st number: "))
n2=int(input("Enter the 2nd number: "))

add(n1,n2)
print("Difference is ",sub(n1,n2))

r1,r2,r3=mul_div(n1,n2)
print("Multiplication is ",r1,"Division is",r2,"quotient is",r3)

