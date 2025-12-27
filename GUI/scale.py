from tkinter import * 
def submit():
    print("The temperature is", scale.get(), "degrees celcius")
window = Tk()

scale = Scale(window,
              from_=100, # range starting value
              to=0, # ending value
              length=400, # length
              orient=VERTICAL, # orientation of scale # HORIZONTAL, VERTICAL
              font=('Consolas', 13),
              tickinterval=10, # marks interval at specific intervals
            #   showvalue=0, # hides current value during sliding
              resolution=5, # increment of slider
              troughcolor='red',
              fg='green',
              bg='black',
              ) 
scale.set(90) # sets default value of scale by default is zero! 
scale.pack()

button = Button(window, text='Submit', command=submit)
button.pack()

window.mainloop()