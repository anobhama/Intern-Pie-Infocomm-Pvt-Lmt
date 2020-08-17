# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 00:41:32 2020

@author: Anobhama
"""
#(Q28)WAP to check whether a person is eligible for voting or not.
num=int(input("Enter your age: "))
if num >= 18:
    print("This person aged {} is eligible to vote".format(num))
else:
    print("This person aged {} is not eligible to vote".format(num))
