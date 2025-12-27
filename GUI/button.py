# button -> you click it then it does stuff
from tkinter import *

count = 0

def click():
    global count
    count += 1
    print("You clicked the button",count,"times!")



window = Tk() 

photo = PhotoImage(file="download.png")

button = Button(window,
                text="Click Here", # text in button
                command=click, # function to perfrom after clicking
                font=("Georgia", 40, "bold"), # font specifications name, size, type
                fg="red", # foreground / font color
                bg="black", # background color
                activeforeground="green", # color of text after pressing or holding the button
                activebackground="grey", # color of background after pressing or holding the button
                state=ACTIVE, #  DISABLED prevents from clicking the button! by default ACTIVE
                image=photo, # insert photoimage
                compound="top", # top, bottom, left, right
                ) 

button.pack()

window.mainloop()
