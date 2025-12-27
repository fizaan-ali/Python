# frame -> a rectangular container to group and hold widgets!
from tkinter import * 
window = Tk()

frame = Frame(window, bg="light yellow", bd=5, relief= RAISED)
frame.pack(side=BOTTOM) 
# frame.place(x=0,y=0)  

Button(frame,text="W",font=("Georgia",25),width=3).pack(side=TOP)
Button(frame,text="A",font=("Georgia",25),width=3).pack(side=LEFT)
Button(frame,text="S",font=("Georgia",25),width=3).pack(side=LEFT)
Button(frame,text="D",font=("Georgia",25),width=3).pack(side=LEFT)

window.mainloop()