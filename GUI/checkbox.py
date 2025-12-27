from tkinter import *

def display():
    if (x.get() == 1):
        print("You agreed!")
    else:
        print("You didn't agreed!")
window = Tk()
x = IntVar() # by default it returns 0 / 1 # also StringVar() 
photo = PhotoImage(file='download.png')

check_button = Checkbutton(window,
                           text="I agree",
                           variable=x,
                           onvalue=1, # value that is going to stored in x if checkbox is on
                           offvalue=0, # value that is going to stored in x if checkbox is off
                           command=display,
                           font=("Comic Sans", 20, 'bold'),
                           fg="red",
                           bg="black",
                           activeforeground="yellow",
                           activebackground="#00FF00",
                           padx=25,
                           pady=10,
                           image=photo,
                           compound='top', # left, right, top, bottom relative to text
                           ) 
check_button.pack()
window.mainloop()

# make sure to change the variable datatype IntVar(), StringVar(), BooleanVar(),
# according to the values that is going to be returned in onvalue and offvalue
