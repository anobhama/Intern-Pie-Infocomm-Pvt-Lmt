# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 01:04:56 2020

@author: Anobhama
"""
"""
(Q10)
WAP to enter five subjects marks and calculate average and print them as follows:-
OUTPUT:-
REPORT
**********
(1)	Maths	=
(2)	English	=
(3)	Hindi	=
(4)	Computer	=
(5) G.K.	= Average	=
**********
"""
M= int(input("Enter your Maths Mark: "))
E= int(input("Enter your English Mark: "))
H= int(input("Enter your Hindi Mark: "))
C= int(input("Enter your Computer Mark: "))
GK= int(input("Enter your G.K Mark: "))
avg=0
avg=(M+E+H+C+GK)/5
print("\n")
print("REPORT")
def pat(n):
    return '*'*n
print(pat(15))
print("(1) Maths = ",M)
print("(2) English = ",E)
print("(3) Hindi = ",H)
print("(4) Computer = ",C)
print("(5) G.K. = ",GK)
print("Average = ",avg)
print(pat(15))
 