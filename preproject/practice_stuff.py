########### creting button ###########
from tkinter import *

root = Tk()


def myClick():
    myLabel = Label(root, text="The quote is calculated")
    myLabel.pack()


# myButton = Button(root, text="calculate", state=DISABLED, padx=50, pady=20, command=myClick())
myButton = Button(root, text="calculate", padx=50, pady=20, command=myClick, fg="white", bg="#0459f5")
myButton.pack()

root.mainloop()

########### creting button ###########
