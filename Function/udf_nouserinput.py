# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 19:21:41 2020

@author: Anobhama
"""
#types of user defined functions
#no argument no return type
def greet():
    print("welcome")
greet()

#no argument with return type
def welcome():
    return "how are you"
print(welcome())

#with arguments no return type
def add(a,b):
    print("Sum is",a+b)
add(2,3)

#with arguments with return type
#single return value
def sub(x,y):
    return x-y
print("Difference is",sub(10,4))

#mutliple return value
def add_sub(x,y):
    a=x+y
    b=x-y
    return a,b
print(add_sub(10,5))
res1,res2=add_sub(20,19)
print("added list",res1,"subtracted list",res2)
