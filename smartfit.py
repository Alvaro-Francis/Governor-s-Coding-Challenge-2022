from tkinter import *
from tkinter.ttk import *

master = Tk()
master.geometry("500x500")
master.title("SmartFit")

def openWindow():
    newWindow = Toplevel(master)
    newWindow.title("SmartFit")
    newWindow.geometry("500x500")
    pushup = Label(newWindow, text = "This is SmartFit")
    pushup.pack(pady = 10)

label = Label(master, text = "Welcome to SmartFit")
label.pack(pady = 10)

btn = Button(master, text = 'Tap Me', command = openWindow)

btn.pack(pady = 10)

mainloop()