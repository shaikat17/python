from tkinter import *
from tkinter.ttk import *
from time import *

root = Tk()
root.title("TKinter Digital Clock")

def time():
	string = strftime("%I:\n%M:\n%S:\n%p")
	label.config(text=string)
	label.after(1000,time)
	
label = Label(root,font=("Arial",125),background="green",foreground="white")
label.pack(anchor = "center")

time()

mainloop()
