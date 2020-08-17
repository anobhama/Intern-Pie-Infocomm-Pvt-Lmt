# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 01:19:51 2020

@author: Anobhama
"""
#filling the buttons with labels and colours

from tkinter import *
window = Tk()
window.geometry('200x200') 

#colour labels
rlabel = Label(window,text="red colour",bg="red",fg="white")
glabel = Label(window,text="green colour",bg="green",fg="white")
blabel = Label(window,text="blue colour",bg="blue",fg="white")
plabel = Label(window,text="pink colour",bg="pink",fg="white")
#filling the colours in the full label and packing it
rlabel.pack(fill=X)
glabel.pack(fill=X,side=BOTTOM)
blabel.pack(fill=Y,side=RIGHT)
plabel.pack(fill=Y,side=LEFT)

window.mainloop()