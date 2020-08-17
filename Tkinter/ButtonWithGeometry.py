# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 01:18:16 2020

@author: Anobhama
"""

#geometry with a button 

from tkinter import *
window = Tk()
window.geometry('200x200') 
button = Button(window, text = 'click me ',fg="blue") 
button.pack(side = TOP, pady = 5) 
window.mainloop()