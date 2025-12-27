from tkinter import * 
from tkinter import messagebox 
# message box => 
def click():
    # messagebox.showinfo(title="INFO", message="You are Fizaan",)
    # while True: # keeps showing the box 
    # messagebox.showwarning(title="WARNING", message="You are being watched",)
    # messagebox.showerror(title="ERROR", message="Your PC has been taken down!",)
    # if messagebox.askokcancel(title="Yep", message="Do you wish to continue"):
    #     print("You did a thing")
    # else:
    #     print("You didn't do a thing")
    # if messagebox.askyesno(title="Yo!", message="Do you like me"): # returns boolean value true or false
    #     print("Me too")
    # else:
    #     print("Me too")
    # answer = messagebox.askquestion(title="Question", message="Do you like python") # returns string yes / no 
    # if answer == "yes":
    #     print("Really!!")
    # elif answer=="no":
    #     print("Great")
    print(messagebox.askyesnocancel(title="yes no cancel", message="What do you want?",icon='warning')) # yes, no, cancel => True, False, None

    # also change icon using icon=''
window = Tk()
window.title("Message Box")

button = Button(window, command=click, text="Click me")
button.pack()

window.mainloop()
