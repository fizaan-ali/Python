from tkinter import * 
# grid => geometry manager that organizes in a table like structure

def button():
    firstname = firstnameEntry
    print("First name: ", firstname)

window = Tk() 

# replace pack with grid -> specify rows and cols
firstnameLabel = Label(window, text="First name: ").grid(row=0, column=0)
firstnameEntry = Entry(window).grid(row=0, column=1)

lastnameLabel = Label(window, text="Last name: ").grid(row=1, column=0)
lastnameEntry = Entry(window).grid(row=1, column=1)

emailnameLabel = Label(window, text="Email: ").grid(row=2, column=0)
emailnameEntry = Entry(window).grid(row=2, column=1)

submitbutton = Button(window, text="Submit", command=button, bg="red").grid(row=5, column=1, columnspan=2) # columnspan -> takes space of two cols

window.mainloop()