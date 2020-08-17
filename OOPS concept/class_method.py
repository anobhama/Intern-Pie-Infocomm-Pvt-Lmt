# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 00:01:47 2020

@author: Anobhama
"""
#class method
class Student:
    Sch=" Student of Alphonsa Matric Higher Secondary School"
    def __init__(self,eng,tam,sci,math,soc):
        self.eng = eng
        self.tam = tam
        self.sci = sci
        self.math = math
        self.soc = soc
    def avg(self):
        return (self.eng + self.tam + self.sci + self.math + self.soc)/5
    def add(self):
        return self.eng + self.tam + self.sci + self.math + self.soc
    @classmethod   #decorator 
    def info(cls):
        return cls.Sch
    
#getting user input
eng=int(input("Enter the English marks: "))
tam=int(input("Enter the Tamil marks: "))
sci=int(input("Enter the Science marks: "))
mat=int(input("Enter the Maths marks: "))
soc=int(input("Enter the Social marks: "))

s2=Student(eng,tam,sci,mat,soc)
print(s2.info())
print("The average of marks is ",s2.avg())
print("the sum for 500 is ",s2.add())