# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 01:52:46 2020

@author: Anobhama
"""
#menu bar (dropdown)

from tkinter import *

#action 
def Name():
    print("My name is Anobhama V")
def Dprt():
    print("My department is IT ")
def Rno():
    print("My roll number is 170801008")
def quit():
    window.destroy()
    
window = Tk()
window.geometry('200x500')

menu = Menu(window) #menu is an inbuild func to create menu bar
window.config(menu=menu) #adding menu to window
subMenu = Menu(menu) #drop down for menu

menu.add_cascade(label="details", menu=subMenu) #scroll to drop down

#adding elements to submenu
subMenu.add_command(label="Name",command=Name)
subMenu.add_command(label="Department", command=Dprt)
subMenu.add_command(label="roll number", command=Rno)
subMenu.add_command(label="Exit", command=quit) #quit the prog

window.mainloop()

