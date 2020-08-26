# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 01:41:36 2020

@author: Anobhama
"""
#Digital Clock using Tkinter

from  tkinter import *
import time 

#to get the present time
def timeToKnow():
	current_time=time.strftime("%H:%M:%S") 
	ShowTime.config(text=current_time)
	ShowTime.after(200,timeToKnow)


window =Tk()
window.title("My Digital Clock")
window.geometry("500x250")
window.configure(bg='yellow')
#display of time
ShowTime=Label(window,font=("times",50,"bold"),bg="orange")
ShowTime.grid(row=2,column=2,pady=25,padx=100)
#calling the function to get the present time
timeToKnow()

#header 
clock=Label(window,text="DIGITAL CLOCK",font="times 24 bold",bg="yellow")
clock.grid(row=0,column=2)

#caption below the time running
caption=Label(window,text="hours   minutes   seconds   ",font="times 15 bold",bg="yellow")
caption.grid(row=3,column=2)

window.mainloop()