# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 00:17:09 2020

@author: Anobhama
"""
#method overloadin

class Addition:
    def add(self, n1=None, n2=None, n3=None):
        sum=0
        if n1!=None and n2!=None and n3!=None:
            sum = n1 + n2 + n3
        elif n1!=None and n2!=None:
            sum = n1 + n2
        else:
            sum = n1
        return sum
a1= Addition()
print("The added value is ",a1.add(10)) #one argument
print("The added value is ",a1.add(10,20)) #two argument
print("The added value is ",a1.add(10,20,30)) #three argument

#user input
n1 = int(input("Enter the 1st number : "))
n2 = int(input("Enter the 2nd number : "))
n3 = int(input("Enter the 3rd number : "))

a2 = Addition()
print("The added value is ",a1.add(n1)) #one argument
print("The added value is ",a1.add(n1,n2)) #two argument
print("The added value is ",a1.add(n1,n2,n3)) #three argument
