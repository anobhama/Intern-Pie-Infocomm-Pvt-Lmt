# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 00:25:45 2020

@author: Anobhama
"""
#method overriding
#same name , same arguments , different classes

class School:
    print("Where are you currently studying? ")
    def info(self):
        print("My school is Alphonsa MHSS")
class College(School):
    def info(self):
        print("My clg is SVCE")
        
s = College()
s.info()