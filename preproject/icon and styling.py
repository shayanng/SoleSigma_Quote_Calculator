from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Sole Sigma Quote Calculator")
root.iconbitmap("../graphics/Solesigma Favecon (1).ico")

my_image = ImageTk.PhotoImage(Image.open("../graphics/Solesigma Favecon (1).png"))
my_label = Label(image=my_image)
my_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()
