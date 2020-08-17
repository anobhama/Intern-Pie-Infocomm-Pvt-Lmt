# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 00:13:04 2020

@author: Anobhama
"""
#inheritance
class A:
    def feature1(self):
        print("Feature 1")
    def feature2(self):
        print("Feature 2")
class B(A):
    def feature3(self):
        print("Feature 3")
    def feature4(self):
        print("Feature 4")
#creating obj for child class B
b=B()
#accessing all the methods of parent and child class
b.feature1()
b.feature2()
b.feature3()
b.feature4()

    