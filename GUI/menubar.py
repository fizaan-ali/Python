from tkinter import * 
from tkinter import filedialog

def openFile():
    file = filedialog.askopenfile() 
    print(file.read()) 
    print("\nFile has been opened!")

def saveFile():
    print("File has been saved!")

def copy():
    print("Your text has been copied")

def cut():
    print("Your text has been cut")

def paste():
    print("Your text has been pasted")

window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=("Georgia", 8, "italic"))

menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)

editMenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Paste", command=paste)

window.mainloop()