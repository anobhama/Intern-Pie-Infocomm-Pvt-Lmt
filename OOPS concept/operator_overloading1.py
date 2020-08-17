# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 00:01:34 2020

@author: Anobhama
"""
#operator overloadin method 2
class Number:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
    def __add__(self,other):
        n1 = self.n1 + other.n1
        n2 = self.n2 + other.n2
        n3 = Number(n1,n2)
        return n3

#user input
a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number : "))

num1 = Number(a,b)  
num2 = Number(a, b)  

#num1 = Number(10,5)
#num2 = Number(15,10)

nuum3 = num1 + num2
print(nuum3.n1)
print(nuum3.n2)

print(num1.n1)
print(num1.n2)
print(num2.n1)
print(num1.n2)