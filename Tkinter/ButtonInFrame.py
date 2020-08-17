# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 01:02:37 2020

@author: Anobhama
"""
#frames with buttons in tkinter 

from tkinter import *
window = Tk()
topFrame = Frame(window)
topFrame.pack()
bottomFrame = Frame(window)
bottomFrame.pack(side=BOTTOM)
b1=Button(topFrame,text="button1",fg="red")
b2=Button(topFrame,text="button2",fg="blue")
b3=Button(bottomFrame,text="button3",fg="green")
b1.pack(side=LEFT)
b2.pack(side=RIGHT)
b3.pack()
window.mainloop()

