# first graphical user interface (GUI)

from tkinter import *

# widgets -> GUI elements: buttons, textboxes, labels, images
# windows -> serves as a container to hold or contain these widgets

window = Tk() # instantiate an instance of a window

window.geometry("1000x500") # width and height of our windows respectively!

window.title("Fizaan's first GUI program!") # default is 'tk'

icon = PhotoImage(file='logo.png') # to use photo in icon we first have to covert to photo image

window.iconphoto(True, icon) # now it changes the icon to our photo

window.config(background="#b0b31b") # you can write color name or also hex value 

window.mainloop() # display our window , also listen for events!

