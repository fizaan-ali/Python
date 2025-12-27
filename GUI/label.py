from tkinter import * 
# label -> an area widget that holds text and/or an image within a window

window = Tk()

photo = PhotoImage(file='C:\\Users\\Fizaan\\Desktop\\Python\\logo.png')                         

label = Label(window,text="Fizaan Ali", 
                    font=('Georgia', 40, 'bold'), # font name, size, style
                    fg="#64c7cc",  # font color
                    bg="black", # label background color
                    relief=RAISED, # border
                    bd=10, # border size
                    padx=20, # padding(spacing) in x
                    pady=20, # padding in y
                    image=photo,  # add photo
                    compound='top') # it places our photo bottom to text # top, left, right, bottom
label.pack() # pack puts the widget on screen
# label.place(x=0, y=0) # we can also specify our label position using x and y in place()

window.mainloop()