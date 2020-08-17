# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 00:34:54 2020

@author: Anobhama
"""
#(Q26)WAP to find whether a year is leap year or not.
year=int(input("Enter the year: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
