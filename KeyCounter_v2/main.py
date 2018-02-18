from tkinter import *
from tkinter import ttk
import keyboard

root = Tk()
root.title("KeyCounter")


########## the 'counter'

count = StringVar()
count.set(0)

def setcount(relative=0, reset=False):
    if not reset:
        count.set(int(count.get())+relative)
    else:
        count.set(0)


########## The graphical stuff

mainframe = ttk.Frame(root, padding=(3,3,12,12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)

mainframe.grid_rowconfigure(0, weight=1)
mainframe.grid_rowconfigure(1, weight=1)


ttk.Button(mainframe, text="-",command=lambda : setcount(-1)).grid(column=0, row=1, sticky=(E,W))
ttk.Button(mainframe, text="+",command=lambda : setcount(1)).grid(column=1, row=1, sticky=(E,W))
ttk.Button(mainframe, text="reset", command=lambda : setcount(reset=True)).grid(column=2, row=1, sticky=(E,W))

ttk.Label(mainframe, textvariable=count, font=("Courier", 44)).grid(column=1, row=0, sticky=S)


########## Hotkeys

keyboard.add_hotkey('plus', lambda: setcount(relative=1))
keyboard.add_hotkey('minus', lambda: setcount(relative=-1))
keyboard.add_hotkey('zero', lambda: setcount(reset=True))


root.mainloop()