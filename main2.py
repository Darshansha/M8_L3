from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

def msg():
    messagebox.askquestion("Question Box", "Press Yes or No")

button = Button(root, text="Get asked question", command=msg)
button.place(x=40, y=80)

root.mainloop()