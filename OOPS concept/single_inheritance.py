# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 00:16:23 2020

@author: Anobhama
"""
#single inheritance
#single parent and child class

class rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breath=b
    def arearect(self):
        area = self.length * self.breath
        print("The area of rectange is ",area)
class square(rectangle):
    def __init__(self,l,b):
        super().__init__(l,b)
    def areasquare(self):
        area= self.length * self.length
        print("The area of square is ",area)

a=square(10,5)
a.areasquare()
a.arearect()

#user input
length= int(input("Enter the length : "))
breath = int(input("Enter the breath : "))
shape=square(length,breath)
#shape.arearect()
#shape.areasquare()
print("if you wanna find the area of ")
print("(1) Rectange Press 1")
print("(2) Square Press 2")
print("(3) Both Press 3")
n=int(input("Enter your choice: "))
if n == 1:
    shape.arearect()
elif n == 2:
    shape.areasquare()
else:
    shape.arearect()
    shape.areasquare()
    
        