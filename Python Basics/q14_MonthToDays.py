# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 01:35:19 2020

@author: Anobhama
"""
#(Q14)WAP to enter days and convert it into months and days.
days=int(input("Enter the number of days: "))
m=days//30
d=days%30
print("{} months and {} days".format(m,d))

