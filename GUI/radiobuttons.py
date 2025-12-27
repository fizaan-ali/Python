# radiobutton => similar to checkbox but you can only select one from the group
from tkinter import *

def order():
    if(x.get() == 0):
        print("You ordered Apple")
    elif(x.get() == 1):
        print("You ordered Banana")
    else:
        print("You ordered Mango")

food = ['Apple', 'Banana', 'Mango']


window = Tk()
x = IntVar()

apple = PhotoImage(file="C:\\Users\\Fizaan\\Desktop\\GUI\\apple.png")
banana = PhotoImage(file="C:\\Users\\Fizaan\\Desktop\\GUI\\banana.png")
mango = PhotoImage(file="mango.png")

foodImages = [apple, banana, mango]
 
for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],  # adds text to radiobuttons
                              variable=x, # groups radiobuttons together if they share the same variable
                              value=index, # assigns each radiobutton a different value
                              padx=25, # adds padding on x-axis
                              pady=5,
                              font=('Impact', 50, 'italic'),
                              image=foodImages[index], # adds image to respective radiobuttons
                              compound='left', # adds image left to text
                            #   indicatoron=0, # eliminates circle indicator
                            #   width=375, # set's width of radiobuttons 
                              command=order, # set command of radiobutton to function
                              )
    # radiobutton.config() 
    radiobutton.pack(anchor=W)  # W for west # where to place our radiobutotns
window.mainloop()