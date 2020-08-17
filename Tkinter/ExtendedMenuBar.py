# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 02:07:01 2020

@author: Anobhama
"""
#menu bar with two fields each having drop down

from tkinter import *
from tkinter import filedialog

#action 
def Name():
    print("My name is Anobhama V")
def Dprt():
    print("My department is IT ")
def Rno():
    print("My roll number is 170801008")
def quit():
    window.destroy()
def Browrse():
    filename = filedialog.askopenfilename(filetypes=(("file","*.py"),("all files","*.*")))
    pathlabel.config(text=filename)
def Resize():
    window.geometry('100x300')
def Default():
    window.geometry('200x500')    
window = Tk()
window.geometry('200x500')

#first element
menu = Menu(window) #menu is an inbuild func to create menu bar
window.config(menu=menu) #adding menu to window
subMenu = Menu(menu) #drop down for menu


menu.add_cascade(label="details", menu=subMenu) #scroll to drop down

#adding elements to submenu
subMenu.add_command(label="Name",command=Name)
subMenu.add_command(label="Department", command=Dprt)
subMenu.add_command(label="roll number", command=Rno)
subMenu.add_command(label="Exit", command=quit) #quit the prog

#second element
editMenu = Menu(menu) #menu is an inbuild func to createedit  menu bar

menu.add_cascade(label="edit", menu=editMenu)

editMenu.add_command(label="Open",command=Browrse)
editMenu.add_command(label="Resize", command=Resize)
editMenu.add_command(label="Default", command=Default)
editMenu.add_command(label="Exit", command=quit) #quit the prog

#giving path to browse the contents and files in lap
pathlabel = Label(window)
pathlabel.pack()

window.mainloop()