# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 10:15:54 2020

@author: Anobhama
"""
#hybrid inheritance
#combination of classes
class figure:
    def __init__(self,length,breath,height):
        self.length = length
        self.breath = breath
        self.height = height
    def info(self):
        print(" figure : Has square, rectangle and triangle")
        
class rectangle(figure):
    
    def __init__(self,length,breath,height):
        print(" rectangle: Has figure class")
        super().__init__(length,breath,height)
        
    def arearect(self):
        area = self.length * self.breath
        print("The area of rectange is ",area)

class square(rectangle):
    print(" square :Has figure and rectangle class")
    def __init__(self,length,breath,height):
        super().__init__(length,breath,height)
    def areasquare(self):
        area= self.length * self.length
        print("The area of square is ",area)
        
class triange(figure):
    def __init__(self,length,breath,height):
        
        print( " Traingle : Has figure class")
        super().__init__(length,breath,height)
    def areatri(self):
        area=(1/2)* self.breath* self.height
        print("The area of triangle is ",area)
        

shape=square(10,2,0)
shape.info()
shape.arearect()
shape.areasquare() #cant access areatri() here as no inheritance

shape1=triange(0,5,50)
shape1.info()
shape1.areatri() 
