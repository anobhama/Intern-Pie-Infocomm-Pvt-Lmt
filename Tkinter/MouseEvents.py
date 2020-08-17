# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 01:47:20 2020

@author: Anobhama
"""
#mouse events 

from tkinter import *

#event actions
def left(event):
    print("U left clicked me !!!")
def middle(event):
    print("U middle clicked me !!!")
def right(event):
    print("U right clicked me !!!")

window = Tk()
window.geometry('200x200')

button = Button(window,text="click me")
button.bind("<Button-1>",left)
button.bind("<Button-2>",middle)
button.bind("<Button-3>",right)

button.pack()

window.mainloop()
 