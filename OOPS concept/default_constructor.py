# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 23:44:22 2020

@author: Anobhama
"""
#default constructor
class Number:
    #constructor
    def __init__(self):
        print("default constructor")
        self.num=100   #initializing instance variable
    def read_number(self):
        print(self.num)
#creating object 1
n1=Number()

#creating obj 2 
n2=Number()
#calling the method of the class
n2.read_number()
