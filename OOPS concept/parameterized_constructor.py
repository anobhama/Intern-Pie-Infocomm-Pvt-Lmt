# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 23:57:02 2020

@author: Anobhama
"""
#parameterized constructor
class maths:
    def __init__(self,x,y):  #parameters used
        self.x=x
        self.y=y
    def add(self,x,y):
        return x+y
    def sub(self, x,y):
        return x-y

#obj creation
m1=maths(10,5) #passing paramters
print("The sum is ",m1.add(10,5))

m2=m1.sub(10,5)
print("The difference is ",m2)