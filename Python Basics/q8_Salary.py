# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 00:31:32 2020

@author: Anobhama
"""
"""
(Q8)
WAP enter salary of a person and find HRA,DA,PF. HRA = 20% of salary.
DA		= 15% of salary. PF	= 10% of salary.

OUTPUT:-
Salary	=
HRA	=
DA	=
PF	=
Net Salary = 
Salary in hand = 
"""
sal=int(input("Enter the salary: "))
print("Salary = ",sal)
HRA=(20/100)*sal
print("HRA = ", HRA)
DA=(15/100)*sal
print("DA = ",DA )
PF=(10/100)*sal
print("PF = ", PF)
print("Net Salary = ", sal+HRA+DA+PF )
print("Salary in hand = ", (sal+HRA+DA)-PF )