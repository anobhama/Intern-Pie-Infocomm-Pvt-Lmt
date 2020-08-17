# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:22:39 2020

@author: Anobhama
"""
#reduce using lambda and normal function
from functools import *
def add(x,y):
    return x+y
num=[]
n=int(input("Enter the number of elements in the list: "))
for i in range(n):
    i=int(input("Enter the elements: "))
    num.append(i)
even_no = list(filter(lambda x: x%2 ==0,num)) #lambda function
print("The even list is ",even_no) 
update= list(map(lambda x: x+5,even_no))
print("Updated list is ",update)
sum=reduce(add,update) #normal function
print("Sum is",sum)

s=reduce(lambda x,y: x+y,update)  #lambda function
print("sum using lambda function is ",s)