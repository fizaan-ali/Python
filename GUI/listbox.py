# listbox = A listing of selectable text items within it's own container
from tkinter import * 
def submit():
    # print("You have ordered:", listbox.get(listbox.curselection()))
    food = []
    for index in listbox.curselection(): # gives us index and values of current selection
        food.insert(index, listbox.get(index))
    print("You have ordered:")
    for index in food:
        print(index)


def add():
    listbox.insert(listbox.size(), entrybox.get()) # adds an element at index 
    listbox.config(height=listbox.size()) # adjust height after addition


def delete():
    # listbox.delete(listbox.curselection()) # deletes current selection
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    
    listbox.config(height=listbox.size()) # adjust height after dleletion
window = Tk()
window.title("Listbox")

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia",20,'italic'),
                  width=12,
                  selectmode=MULTIPLE,
                  )
listbox.insert(1, "Pizza") 
listbox.insert(2, "Burger") 
listbox.insert(3, "Fries") 
listbox.insert(4, "Potatoes") 
listbox.insert(5, "Mango") 

listbox.config(height=listbox.size())
listbox.pack()

entrybox = Entry(window)
entrybox.pack()

addbutton = Button(window, text="Add", command=add)
addbutton.pack()

deletebutton = Button(window, text="Delete", command=delete)
deletebutton.pack()

submitbutton = Button(window,
                      text="Submit",
                      command=submit,
                      )
submitbutton.pack()
window.mainloop()