# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 00:06:02 2020

@author: Anobhama
"""
#image display for other forms of img excpt png

from tkinter import *
from PIL import Image,ImageTk

window = Tk()
window.geometry('500x200')
window.title("Image Display")

#jpeg and other forms
image= Image.open("TomAndJerry1.jpg")
img = ImageTk.PhotoImage(image)
photo=Label(image=img)
photo.pack()

window.mainloop()

