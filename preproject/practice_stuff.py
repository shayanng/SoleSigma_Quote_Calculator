########### creting button ###########
from tkinter import *

root = Tk()

e = Entry(root, width=60, bg="white", borderwidth=3)
e.pack()
e.insert(0, "Type Client's Budget")


def myClick():
    myLabel = Label(root, text="The client Budget is " + e.get())
    myLabel.pack()


# myButton = Button(root, text="calculate", state=DISABLED, padx=50, pady=20, command=myClick())
myButton = Button(root, text="calculate", padx=50, pady=20, command=myClick, fg="white", bg="#0459f5")
myButton.pack()

root.mainloop()

########### Input Box ###########
