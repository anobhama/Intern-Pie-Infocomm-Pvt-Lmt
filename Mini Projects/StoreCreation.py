# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 20:09:06 2020

@author: Anobhama
"""

from tkinter import *

def getValue():
    print("form submitted")
    print(f"{name_value.get(),phone_value.get(),email_value.get(),gender_value.get(),payment_value.get(),foodServiceValue.get()}")
    with open("records.txt","a") as f:
        f.write(f"{name_value.get(),phone_value.get(),email_value.get(),gender_value.get(),payment_value.get(),foodServiceValue.get()}\n")
    
window = Tk()
window.geometry('500x300')

#heading 
Label(window,text="Welcome to my store",font="ariel",pady=15).grid(row=0,column=3)

#text for the form
name = Label(window, text="Name")
phone = Label(window, text="Phone")
email = Label(window, text="Email")
gender = Label(window, text="Gender")
payment = Label(window, text="Payment")

#packing text 
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
email.grid(row=3,column=2)
gender.grid(row=4,column=2)
payment.grid(row=5,column=2)

#Tkinter variables for storing entries
name_value = StringVar()
phone_value = StringVar()
email_value = StringVar()
gender_value = StringVar()
payment_value = StringVar()
foodServiceValue = IntVar() 

#entry values for form elements
name_entry = Entry(window,textvariable=name_value)
phone_entry = Entry(window, textvariable=phone_value)
email_entry = Entry(window, textvariable=email_value)
gender_entry = Entry(window, textvariable=gender_value)
payment_entry = Entry(window, textvariable=payment_value)

#packing the entries
name_entry.grid(row=1,column=3) 
phone_entry.grid(row=2,column=3) 
email_entry.grid(row=3,column=3) 
gender_entry.grid(row=4,column=3) 
payment_entry.grid(row=5,column=3) 

#check box
foodService = Checkbutton(text="want to pre book",variable= foodServiceValue)
foodService.grid(row=6, column=3)

#button
Button(text="submit",command= getValue).grid(row=7,column=3)

window.mainloop()


