# text widget -> functions like a text area, you can enter multiple lines of text 
from tkinter import * 
def submit():
    print(text.get("1.0", END)) # from first index to end!
window = Tk()
window.title("Text Area")
text = Text(window,
            bg="light yellow",
            font=("Ink Free", 20, 'italic'),
            height=15, # no of characters wide
            width=35, # no of characters tall 
            padx=20,
            pady=20,
            fg="purple")
text.pack()
button = Button(window, text="Submit", command=submit, height=3, width=12)
button.pack()
window.mainloop()