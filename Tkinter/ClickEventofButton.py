# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 01:40:39 2020

@author: Anobhama
"""
#calling a function to do the event after a button is clicked

from tkinter import *

#event to take place after button click
def click():
    print("U have clicked me !!! ")
window = Tk()
window.geometry('200x200') 

button = Button(window,text="click me",command= click)
button.pack()

window.mainloop()

