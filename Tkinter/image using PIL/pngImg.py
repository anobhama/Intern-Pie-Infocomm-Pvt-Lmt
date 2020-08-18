# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 23:00:48 2020

@author: Anobhama
"""
#image display for png pics

from tkinter import *
window = Tk()
window.geometry('1000x1000')
window.title("Image Display")

#png image
photo=PhotoImage(file="TomAndJerry.png")
imgLabel= Label(image=photo)
imgLabel.pack()

window.mainloop()