from tkinter import * 
def create_window():
                            # Tk() => separate windows independent
    new_window = Tk()  # TopLevel() -> new window 'on top' of other windows. linked to a 'bottom' window # if bottom window closes upper will also
    old_window.destroy() # -> destroys the window 
old_window = Tk()

button = Button(old_window, text="Create new window", command=create_window).pack()
old_window.mainloop()
