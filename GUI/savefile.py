from tkinter import * 
from tkinter import filedialog
def save():
    # asksaveasfilename() -> returns the saved file location!
    file = filedialog.asksaveasfile(defaultextension='.txt',  # returns an opened file object
                                    filetypes=[("text files",".txt"),("Python files",".py"),("all files", ".*")], # allowed file types
                                    initialdir='C:\\Users\\Fizaan\\Desktop\\GUI') 
     
    if file is None: # exception handle if no file to select
        return 

    fileText = text.get("1.0", END) 
    # fileText = input("Enter text to store: ") # also you can write from terminal as you wish
    file.write(fileText)
    file.close()

window = Tk()
button = Button(window, text="Save", command=save)
button.pack()
text = Text(window)
text.pack()
window.mainloop()