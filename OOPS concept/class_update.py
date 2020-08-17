# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 23:27:03 2020

@author: Anobhama
"""
#class with some functions
class Student:
    def __init__(self):
        self.name="Anobhama V"
        self.age = 20
    def update(self):
        self.age=21
    def compare(self,other):
        if self.age == other.age:
            print("same age")
        else:
            print("different age")
s1=Student()
s2=Student()
s1.compare(s2)
#updating the age
s1.update()
s1.compare(s2)


    