# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:09:50 2020

@author: Anobhama
"""
#filter function
#without lambda function
def even(n):
    return n%2 ==0
num=[]
n=int(input("Enter the number of elements in the list: "))
for i in range(n):
    i=int(input("Enter the elements: "))
    num.append(i)
even_num=list(filter(even,num))
print("The filtered list is ",even_num)


#with lambda function

num=[]
n=int(input("Enter the number of elements in the list: "))
for i in range(n):
    i=int(input("Enter the elements: "))
    num.append(i)
even_num=list(filter(lambda x: x%2==0,num))
print("The filtered list is ",even_num)