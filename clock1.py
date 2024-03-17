from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("clock")

def time():
    string = strftime('%I:%M:%S %P')
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=("ds-digital", 80), background = "black", foreground = "cyan")
label.pack(anchor='center')
print(time)

mainloop()