# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 01:26:34 2020

@author: Anobhama
"""
#(Q13)WAP to enter time in seconds and convert it in minutes and seconds.
sec=int(input("Enter the time in seconds: "))
m=sec//60
s=sec%60
print("{} minutes and {} seconds".format(m,s))
