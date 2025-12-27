from tkinter import * 
from tkinter import filedialog
def openFile():
    filepath = filedialog.askopenfilename( # returns string of the file path
                                          initialdir="C:\\Users\\Fizaan\\Desktop\\GUI", # initial directory which should open
                                          title="Open file okay?",   # title of file opening window
                                          filetypes=(("text files", "*.txt"),("Python files", "*.py"),("all files", "*.*")), # specify the files 
                                          ) 
    # print(filepath)
    file = open(filepath, 'r')
    print(file.read())
    file.close()
window = Tk()
button = Button(window, text="Open", command=openFile)
button.pack()
window.mainloop()