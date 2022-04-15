from tkinter import *
from tkinter.ttk import *
import time

master = Tk()
master.geometry("500x500")
master.title("SmartFit")

count = 60

def countDown():
    while (count > 0):
        count -= 1
        time.sleep(1)

def openPushUp():
    newWindow = Toplevel(master)
    newWindow.title = 'SmartFit: PushUps'
    newWindow.geometry = ("500x500")
    pushUpLabel = Label(newWindow, text = 'Push Up Exercise - 15 Reps')
    pushUpLabel.pack(pady = '10')
    

def openMeditation():
    newWindow = Toplevel(master)
    newWindow.title('SmartFit: Meditiation')
    meditationLabel = Label(newWindow, text = 'Meditation Exercise - 1:00')
    meditationLabel.pack(pady = 10)

welcomeLabel = Label(master, text = "Welcome to SmartFit")
welcomeLabel.pack(pady = 10)

pushUpLabel = Label(master, text = 'Push Up Exercise')
pushUpLabel.pack(pady = 20)

pushUpButton = Button(master, text = 'Start', command = openPushUp)

pushUpButton.pack(pady = 10)


mediLabel = Label(master, text ='Meditation Exercise')
mediLabel.pack(pady = '10')

MediButton = Button(master, text='Start', command = openMeditation)
MediButton.pack(pady = '20')

mainloop()
