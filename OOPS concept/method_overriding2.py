# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 00:31:20 2020

@author: Anobhama
"""
#method overriding
class Animal:
    def __init__(self):
        print("Animal : ")
    def info(self):
        print("Human is animal")
    def char(self):
        print("No own food preparation ")

class HomoSapiens(Animal):
    def __init__(self):
        super().__init__() #inheriting the parent class constructor
    def info(self):
        print("I am a human ")
    def walk(self):
        print("Walks in two legs")
    
h = HomoSapiens()
h.info()  #overloaded in child class
h.char()
h.walk()
        