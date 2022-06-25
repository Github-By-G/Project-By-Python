from tkinter import*
from tkinter.ttk import*

from time import strftime

x= Tk()
x.title("clock")

def time():
    string = strftime ( "%H:%M:%S %p ")
    label.config (text=string)
    label.after (1000, time)
    
label=Label(x, font=("ds-digital",80,"bold"),background="deepskyblue3",foreground="black")
label.pack(anchor='center')
time()

mainloop()