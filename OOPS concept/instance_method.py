# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 23:38:41 2020

@author: Anobhama
"""
#instance method
#average of marks
class Student:
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
s1=Student(60,60,60,60,60)
print("the average is ",s1.avg())
print("the sum for 500 is ",s1.add())

#getting user input
eng=int(input("Enter the English marks: "))
tam=int(input("Enter the Tamil marks: "))
sci=int(input("Enter the Science marks: "))
mat=int(input("Enter the Maths marks: "))
soc=int(input("Enter the Social marks: "))

s2=Student(eng,tam,sci,mat,soc)
print("The average of marks is ",s2.avg())
print("the sum for 500 is ",s2.add())

        
        
        