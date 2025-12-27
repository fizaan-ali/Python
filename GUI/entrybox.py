from tkinter import *
# entry widget -> textbox that accepts a single line of user input
def submit():
    username = entry.get() # returns the string that have written in entry box
    print("Hello", username)
    entry.config(state=DISABLED) # after submit a username disable the entrybox
def delete():
    entry.delete(0, END) # delete from first to last character! # 2 positional arguments
def backspace():
    entry.delete(len(entry.get())-1, END)
window = Tk()

entry = Entry (window,
              font=('Georgia', 30, 'italic'),
              fg="yellow",
              bg="black",
            #   show="*", # show specific char in place of text in password typing
              )

entry.insert(0, "Fizaan") # default text in entrybox at index 0
entry.pack(side=LEFT)

submit_button = Button(window, text="Submit", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="Delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="Backspace", command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()