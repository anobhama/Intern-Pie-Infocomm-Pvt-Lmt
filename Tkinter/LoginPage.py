# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 01:28:00 2020

@author: Anobhama
"""
#login page fields

from tkinter import *
window = Tk()
window.geometry('200x200') 

#fields 
name = Label(window,text="Name")
email = Label(window,text="Email")
password = Label(window,text="Password")
button = Button(window, text="submit",fg="red",bg="white")

#input from user field
enter_name = Entry(window)
enter_email = Entry(window)
enter_password = Entry(window,show="*") #hiding it as it is a password

#inserting them into window by grid()
name.grid(row=0)
email.grid(row=1)
password.grid(row=2)

enter_name.grid(row=0,column=1)
enter_email.grid(row=1,column=1)
enter_password.grid(row=2,column=1)

button.grid(row=4,column=1)

window.mainloop()




