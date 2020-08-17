# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 23:49:20 2020

@author: Anobhama
"""
#duck typing
class Animal:
    def char(self):
        print("Animal category")
class HomoSapiens:
    def char(self):
        print("I am a human")
class Reptiles:
    def char(self,other):
        other.char()
#accessing animal class    
a1=Animal()
r1= Reptiles()
r1.char(a1)

#accessing homosapiens class 
h1=HomoSapiens()
r2 = Reptiles()
r1.char(h1)

