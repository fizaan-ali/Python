from tkinter import *
from tkinter import colorchooser # why are we adding it because it's a submodule
def click():
    color = colorchooser.askcolor()
    # print(color)
    # colorHex = color[1]
    # print(colorHex)
    # button.config(bg=colorHex)
    # window.config(bg=color[1])
    window.config(bg=colorchooser.askcolor()[1])
window = Tk()
window.geometry("420x420")
button = Button(window, text="click",command=click)
button.pack()
window.mainloop()