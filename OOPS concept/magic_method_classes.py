# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 20:21:26 2020

@author: Anobhama
"""
#magic method using classes
class number:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
    def __add__(self):
        return self.n1+ self.n2 
    def __sub__(self):
        return self.n1 - self.n2
    def __mul__(self):
        return self.n1 * self.n2
    def __divmod__(self):
        return self.n1 / self.n2
    def __gt__(self):
         if self.n1 > self.n2:
             return "{} is greater than {}".format(self.n1,self.n2)
         else:
             return "{} is greater than {}".format(self.n2,self.n1)
    def __lt__(self):
         if self.n1 < self.n2:
             return "{} is less than {}".format(self.n1,self.n2)
         else:
             return "{} is less than {}".format(self.n2,self.n1)
    def __le__(self):
         if self.n1 < self.n2:
             return "{} is less than {}".format(self.n1,self.n2)
         elif self.n1 == self.n2:
             return "{} is equal to {}".format(self.n1,self.n2)
         else:
             return "{} is less than {}".format(self.n2,self.n1)
    def __ge__(self):
         if self.n1 >= self.n2:
             return "{} is greater than {}".format(self.n1,self.n2)
         elif self.n1 == self.n2:
             return "{} is equal to {}".format(self.n1,self.n2)
         else:
             return "{} is greater than {}".format(self.n2,self.n1)
#user input
n1=int(input("Enter the 1st number "))
n2=int(input("Enter the 2nd number "))

num=number(n1,n2)
print("The added number is ", num.__add__())
print("The substracted number is ", num.__sub__())
print("The nultiplied number is ", num.__mul__())
print("The divided number is ", num.__divmod__())
print(num.__gt__())
print(num.__lt__())
print(num.__le__())
print(num.__ge__())
