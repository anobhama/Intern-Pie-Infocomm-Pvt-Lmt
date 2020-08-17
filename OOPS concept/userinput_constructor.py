# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 00:02:03 2020

@author: Anobhama
"""
class maths:
    def __init__(self,x,y):  #parameters used
        self.x=x
        self.y=y
    def add(self,x,y):
        return x+y
    def sub(self, x,y):
        return x-y
#user input
x=int(input("Enter the 1st element: "))
y=int(input("Enter the 2nd element: "))
#obj creation
m1=maths(x,y)
#accessing the methods
m2=m1.add(x,y)
print("The sum is ",m2)
print("The difference is ",m1.sub(x,y))
