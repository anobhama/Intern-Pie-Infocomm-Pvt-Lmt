# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:16:23 2020

@author: Anobhama
"""
#map
#with and without lambda function
def update(n):
    return n*2
num=[]
n=int(input("Enter the number of elements in the list: "))
for i in range(n):
    i=int(input("Enter the elements: "))
    num.append(i)
even_no = list(filter(lambda x: x%2 ==0,num)) #lambda function
print("The even list is ",even_no)    
final= list(map(update,even_no)) #no lambda function
print("The final list is ",final)
