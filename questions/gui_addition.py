# import statement for tkinter
from tkinter import *
# This is a user defined function to add two numbers
# e1.get() will return text within text box (entry widget)
# int() funcion will convert string to integer
# both int numbers from two entry widgets are added and 
# result is assigned to res variable.
# which  is set into label_text string variable 
def add_numbers():
    res=int(e1.get())+int(e2.get())
    label_text.set(res)
 
# get main window
window = Tk()
# bind the label widget to a StringVar instance,
# and set or get the label text via that variable:
label_text=StringVar();
# create 4 label widgets and place them in window using grid() 
Label(window, text="Enter First Number:").grid(row=0, sticky=W)
Label(window, text="Enter Second Number:").grid(row=1, sticky=W)
Label(window, text="Result of Addition:").grid(row=3, sticky=W)
result=Label(window, text="", textvariable=label_text).grid(row=3,column=1, sticky=W)
# create two entry widgets and place them in window
# using grid() Grid Geometry Manager
e1 = Entry(window)
e2 = Entry(window)
 
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
 
# create a button and place it in grid
# Set command = add_numbers, so that when this button is clicked
# add_numbers() function will be called.
b = Button(window, text="Calculate", command=add_numbers)
b.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)
 
# start mainloop, start GUI 
window.mainloop()
