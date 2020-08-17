# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 10:44:26 2020

@author: Anobhama
"""
#multiple inheritance
#many base classes in a single child classes
class room:
    def __init__(self,length,breath):
        self.length = length
        self.breath = breath
    def arearect(self):
        area = self.length * self.breath
        return area
        
class cost:
    def costpermeter(self):
        c=100 
        return c
        

class paintingcost(room,cost):
    def __init__(self,length,breath):
        super().__init__(length,breath)
    def paintcost(self):
        room.arearect(self)
        print("The painting cost is",self.arearect() * self.costpermeter())
    
p = paintingcost(100,3)
p.paintcost()

#user input
l=int(input("Enter the length of the room: "))
b=int(input("Enter the height of the room: "))
p1 = paintingcost(l,b)
p1.paintcost()