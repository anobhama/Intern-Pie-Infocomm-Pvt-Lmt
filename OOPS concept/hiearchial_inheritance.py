# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 01:05:30 2020

@author: Anobhama
"""
#hiearchial inheritance
#single parent class many child classes
class figure:
    def __init__(self,length,breath,height):
        self.length = length
        self.breath = breath
        self.height = height
        
class rectangle(figure):
    def __init__(self,length,breath,height):
        super().__init__(length,breath,height)
        
    def arearect(self):
        area = self.length * self.breath
        print("The area of rectange is ",area)

class square(figure):
    def __init__(self,length,breath,height):
        super().__init__(length,breath,height)
    def areasquare(self):
        area= self.length * self.length
        print("The area of square is ",area)
        
class triange(figure):
    def __init__(self,length,breath,height):
        super().__init__(length,breath,height)
    def areatri(self):
        area=(1/2)* self.breath * self.height
        print("The area of triangle is ",area)

r=rectangle(10,3,0)
r.arearect()

s=square(20,0,0)
s.areasquare()

t=triange(0,30,60)
t.areatri()



    
