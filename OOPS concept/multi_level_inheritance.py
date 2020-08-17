# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 00:41:05 2020

@author: Anobhama
"""
#multi level inheritance
#parent class with child class but child class again bevomes the parent class
class rectangle:
    def __init__(self,l,b,h):
        self.length = l
        self.breath = b
        self.height = h
    def arearect(self):
        area = self.length * self.breath
        print("The area of rectange is ",area)
class square(rectangle):
    def __init__(self,l,b,h):
        super().__init__(l,b,h)
    def areasquare(self):
        area= self.length * self.length
        print("The area of square is ",area)
class triangle(square):
    def __init__(self,l,b,h):
        super().__init__(l, b,h)
    def areatri(self):
        area=(1/2)* self.breath* self.height
        print("The area of triangle is ",area)

shape1=triangle(100,50,50)
shape1.arearect()
shape1.areasquare()
shape1.areatri()

print("if you wanna find the area of ")
print("(1) Rectange Press 1")
print("(2) Square Press 2")
print("(3) Triangle Press 3")
print("(4) all press 4")
#user input
length= int(input("Enter the length : "))
breath = int(input("Enter the breath : "))
print(" if u choose (3) or (4) enter the value or else ignore it by putting 0")
height = int(input("Enter the height of triangle : "))
shape=triangle(length,breath,height)
#shape.arearect()
#shape.areasquare()

n=int(input("Enter your choice: "))
if n == 1:
    shape.arearect()
elif n == 2:
    shape.areasquare()
elif n == 3:
    shape.areatri()
else:
    shape.arearect()
    shape.areasquare()
    shape.areatri()
    