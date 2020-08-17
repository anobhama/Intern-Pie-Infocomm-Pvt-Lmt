# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 00:30:53 2020

@author: Anobhama
"""

#(Q25)WAP to input a number between 1 to 7 and print daysname.
n=int(input("Enter the number between 1 and 7 : "))
if n==1:
    print("Monday")
elif n==2:
    print("Tuesday")
elif n==3:
    print("Wednesday")
elif n==4:
    print("Thursday")
elif n == 5:
    print("Friday")
elif n == 6:
    print("Saturday")
elif n ==7:
    print("Sunday")
else:
    print("invalid entry")